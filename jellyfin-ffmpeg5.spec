# Upstream ffmpeg version
%global ffmpeg_version 5.1.2
# Jellyfin patchset release
%global patchset_release 8

# Follow naming convention of other distros' jellyfin-ffmpeg packages
Name:           jellyfin-ffmpeg5
Version:        %{ffmpeg_version}
Release:        %{patchset_release}.1%{?dist}
Summary:        Custom ffmpeg build with Jellyfin patchset

License:        LGPLv2+ and GPLv3+
URL:            https://github.com/jellyfin/jellyfin-ffmpeg
Source0:        https://github.com/jellyfin/jellyfin-ffmpeg/archive/refs/tags/v%{version}-%{patchset_release}.tar.gz

ExclusiveArch:  x86_64

BuildRequires:  clang
BuildRequires:  nasm

BuildRequires:  AMF-devel
BuildRequires:  lame-devel
BuildRequires:  vulkan-loader-devel

BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(ffnvcodec)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  pkgconfig(libplacebo)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(SvtAv1Enc)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x264)
BuildRequires:  pkgconfig(x265)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2)

%description
FFmpeg is a leading multimedia framework, able to decode, encode, transcode,
mux, demux, stream, filter and play pretty much anything that humans and
machines have created. It supports the most obscure ancient formats up to the
cutting edge. No matter if they were designed by some standards committee, the
community or a corporation.

This build contains binaries built with the jellyfin-ffmpeg patchset.


%prep
%autosetup -n jellyfin-ffmpeg-%{version}-%{patchset_release}

cat debian/patches/*.patch | patch -p1


%build
./configure \
    --arch=%{_target_cpu} \
    --optflags="%{build_cflags}" \
    --extra-ldflags="%{build_ldflags}" \
    --prefix=/discard \
    --bindir=%{_libexecdir}/jellyfin-ffmpeg \
    --target-os=linux \
    --extra-version=Jellyfin \
    --disable-doc \
    --disable-ffplay \
    --disable-ptx-compression \
    --disable-stripping \
    --disable-shared \
    --disable-libxcb \
    --disable-sdl2 \
    --disable-xlib \
    --enable-lto \
    --enable-gpl \
    --enable-version3 \
    --enable-static \
    --enable-pic \
    --enable-gmp \
    --enable-gnutls \
    --enable-chromaprint \
    --enable-libfontconfig \
    --enable-libass \
    --enable-libbluray \
    --enable-libdrm \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libmp3lame \
    --enable-libopus \
    --enable-libtheora \
    --enable-libvorbis \
    --enable-libdav1d \
    --enable-libwebp \
    --enable-libvpx \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libzvbi \
    --enable-libzimg \
    --enable-libshaderc \
    --enable-libplacebo \
    --enable-vulkan \
    --enable-opencl \
    --enable-vaapi \
    --enable-amf \
    --enable-libmfx \
    --enable-ffnvcodec \
    --enable-cuda \
    --enable-cuda-llvm \
    --enable-cuvid \
    --enable-nvdec \
    --enable-nvenc \
    --enable-libfdk-aac \
    --enable-libsvtav1

%make_build


%install
%make_install

# We don't need anything but the binaries
rm -r %{buildroot}/discard


%files
%license COPYING.GPLv2 COPYING.GPLv3 COPYING.LGPLv2.1 COPYING.LGPLv3
%dir %{_libexecdir}/jellyfin-ffmpeg
%{_libexecdir}/jellyfin-ffmpeg/ffmpeg
%{_libexecdir}/jellyfin-ffmpeg/ffprobe


%changelog
* Sun Feb 19 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 5.1.2-8.1
- Update to patchset release 8

* Sat Jan 28 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 5.1.2-7.1
- Update to patchset release 7

* Sun Jan 01 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 5.1.2-6.1
- Update to patchset release 6

* Wed Dec 28 2022 Andrew Gunnerson <accounts+fedora@chiller3.com> - 5.1.2-5.1
- Update to patchset release 5
- Add --enable-libfdk-aac
- Add --enable-libsvtav1

* Mon Nov 07 2022 Andrew Gunnerson <accounts+fedora@chiller3.com> - 5.1.2-4.1
- Initial release
