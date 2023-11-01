# jellyfin-ffmpeg-fedora

This repo contains the packaging files needed to create RPM packages of [jellyfin-ffmpeg](https://github.com/jellyfin/jellyfin-ffmpeg) for Fedora.

I unfortunately don't personally have the bandwidth to implement and maintain everything the other upstream packages have for other distros (eg. arm64 support). If anyone else is interested in contributing these scripts upstream though, please feel free to do so.

## Building from source

The [`jellyfin-ffmpeg.spec`](./jellyfin-ffmpeg.spec) file can be built like any ordinary RPM spec. To build it inside a `mock` container:

1. Make sure the [RPMFusion repos are enabled](https://rpmfusion.org/Configuration). The steps enable both the `free` and `nonfree` repos by default, but jellyfin-ffmpeg only requires `free`.

2. Install mock and the config files for including the rpmfusion-free repos.

    ```bash
    sudo dnf install rpmdevtools mock mock-rpmfusion-free
    ```

3. Ensure the current user is in the `mock` group.

    ```bash
    sudo gpasswd -a "${USER}" mock
    ```

4. Download the sources.

    ```bash
    spectool -g jellyfin-ffmpeg.spec
    ```

5. Build an SRPM from the spec file and the sources.

    ```bash
    fedora_ver=$(source /etc/os-release && echo "${VERSION_ID}")
    mock \
        -r fedora-${fedora_ver}-x86_64-rpmfusion_free \
        --resultdir results-srpm \
        --buildsrpm \
        --sources . \
        --spec jellyfin-ffmpeg.spec
    ```

6. Build RPMs from the SRPM.

    ```bash
    mock \
        -r fedora-${fedora_ver}-x86_64-rpmfusion_free \
        --resultdir results-rpm \
        --rebuild results-srpm/*.src.rpm
    ```

## License

The license of the packaging files is the same as the software being packaged.
