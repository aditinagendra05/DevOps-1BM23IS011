import docker

client = docker.from_env()

print("Building Docker image...")
client.images.build(path=".", tag="flask-apparmor")

print("Attempting to start container with AppArmor profile...")

try:
    container = client.containers.run(
        "flask-apparmor",
        name="flask-apparmor-test",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print(f"Container started: {container.short_id}")

    info = client.api.inspect_container(container.id)
    print("Configured security options:", info["HostConfig"]["SecurityOpt"])

    print("Note: configured options do not prove AppArmor enforcement.")
    container.stop()
    container.remove()
    print("Container stopped and removed.")

except docker.errors.APIError as exc:
    print("Container launch failed:")
    print(exc)
    print("This can happen because this Mac Docker environment lacks AppArmor support.")
