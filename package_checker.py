def show_package_versions():
    """
    Displays the installed version and latest version of all Python packages installed in the current environment.
    Uses pip to get the information about installed and latest versions of each package. If the latest version
    information is not available, displays "unknown" instead of the version number. If there was an error getting the
    latest version information, displays "unable to determine" instead of the version number.
    """
    import pkg_resources
    import subprocess
    
    for package in packages:
        # Display current version
        output = subprocess.check_output(["pip", "show", package])
        lines = output.decode().split('\n')
        for line in lines:
            if line.startswith("Version:"):
                current_version = line.split()[1]
                break
        else:
            current_version = "unknown"

        # Display latest version
        try:
            output = subprocess.check_output(["pip", "search", package])
            lines = output.decode().split('\n')
            for line in lines:
                if line.startswith(package + ' '):
                    latest_version = line.split()[1]
                    break
            else:
                latest_version = "unknown"
        except subprocess.CalledProcessError:
            latest_version = "unable to determine"

        # Display package name, current version, and latest version
        print(f"{package} (current version: {current_version}, latest version: {latest_version})")

def upgrade_all_packages():
    """
    Upgrades all Python packages installed in the current environment to their latest versions.
    Uses pip to install the latest version of each package. Asks the user to confirm before proceeding with the upgrade.
    """
    import pkg_resources
    import sys
    packages = [dist.project_name for dist in pkg_resources.working_set]

    print(f"Found {len(packages)} packages to upgrade.")
    answer = input("Are you sure you want to attempt to upgrade all packages? (y/n)")

    if answer.lower() == "y":
        for package in packages:
            !pip install --upgrade {package}
        print("All packages have been upgraded.")
    else:
        print("Upgrade cancelled by user.")
        sys.exit(0)

show_package_versions()
upgrade_all_packages()
