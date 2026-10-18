import docker

client = docker.from_env()
container = None

try:
    container = client.containers.run(
        "flask-apparmor",
        name="flask-apparmor-restriction-test",
        ports={"5000/tcp": 5000},
        security_opt=["apparmor=my-apparmor-profile"],
        detach=True
    )

    print(f"Container started: {container.short_id}")

    exit_code, output = container.exec_run(
        ["cat", "/etc/passwd"]
    )
    print(f"Read /etc/passwd: Exit Code {exit_code}")
    print(output.decode(errors="replace"))

    exit_code, output = container.exec_run(
        ["/bin/bash", "-c", "echo bash-executed"]
    )
    print(f"Execute /bin/bash: Exit Code {exit_code}")
    print(output.decode(errors="replace"))

except docker.errors.APIError as exc:
    print("Container launch or execution failed:")
    print(exc)
    print("Check whether AppArmor is supported by the Docker environment.")

finally:
    if container is not None:
        try:
            container.stop()
            container.remove()
            print("Container stopped and removed.")
        except docker.errors.APIError as exc:
            print("Container cleanup issue:", exc)
