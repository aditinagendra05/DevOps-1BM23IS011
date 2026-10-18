

# Exercise 5: Docker Security with AppArmor and Python

## Objective
Build a Flask application in Docker, attempt to configure an AppArmor profile using the Docker Python SDK, and test restricted operations inside the container.

## Files
- `app.py`: Flask web application.
- `Dockerfile`: Docker image configuration.
- `my-apparmor-profile`: AppArmor profile definition.
- `apply_apparmor.py`: Builds the image, attempts to run a container with the profile, and inspects security options.
- `test_restricted_actions.py`: Tests reading `/etc/passwd` and executing `/bin/bash`.
- `screenshots/`: Terminal screenshots.

## Environment
- Host: macOS with Docker Desktop.
- Docker image: `flask-apparmor:latest`.
- Python virtual environment: `.venv`.
- Docker SDK for Python: 7.2.0.

## Tasks Completed

### Task 1: Flask Application
Created `app.py` with a `/` route that returns a confirmation message.

### Task 2: Docker Image
Created the Dockerfile and successfully built the `flask-apparmor` image.

### Task 3: AppArmor Profile
Created `my-apparmor-profile`. Loading and actual enforcement of this custom profile were not verified because the host environment does not expose the required AppArmor support.

### Task 4: Docker SDK
Ran `apply_apparmor.py` successfully. The container started, Docker inspection returned `apparmor=my-apparmor-profile` in its configured security options, and the test container was stopped and removed.

**Note:** The configured security option does not prove that AppArmor was enforced.

### Task 5: Restricted Action Tests
Ran `test_restricted_actions.py` successfully.

Observed results:
- Reading `/etc/passwd`: exit code `0` — access succeeded.
- Executing `/bin/bash`: exit code `0` — execution succeeded.
- Container cleanup: successful.

The two restricted operations were not blocked in this environment.

## Environment Limitation
Docker Desktop on macOS did not report AppArmor in `docker info --format '{{json .SecurityOptions}}'`. The reported security options were `seccomp` and `cgroupns`.

Therefore, these tests demonstrate Docker SDK integration and configured security options, but **do not demonstrate successful AppArmor enforcement**. To verify the intended restrictions, run the exercise in a compatible Linux environment where the custom profile can be loaded and enforced.

## Run
Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the Docker SDK if needed:

```bash
python -m pip install docker
```

Build the image:

```bash
docker build -t flask-apparmor .
```

Run the scripts:

```bash
python apply_apparmor.py
python test_restricted_actions.py
```

