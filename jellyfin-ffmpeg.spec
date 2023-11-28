# Upstream ffmpeg version
%global ffmpeg_version 6.0.1
# Jellyfin patchset release
%global patchset_release 1

Name:           jellyfin-ffmpeg
Version:        %{ffmpeg_version}
Release:        %{patchset_release}.1%{?dist}
Summary:        Custom ffmpeg build with Jellyfin patchset

License:        LGPLv2+ and GPLv3+
URL:            https://github.com/jellyfin/%{name}
Source0:        https://github.com/jellyfin/%{name}/archive/refs/tags/v%{version}-%{patchset_release}.tar.gz

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
BuildRequires:  pkgconfig(libopenmpt)
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
BuildRequires:  pkgconfig(vpl)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(x264)
BuildRequires:  pkgconfig(x265)
BuildRequires:  pkgconfig(zimg)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2)

Obsoletes:      jellyfin-ffmpeg5
Conflicts:      jellyfin < 10.8.10

%description
FFmpeg is a leading multimedia framework, able to decode, encode, transcode,
mux, demux, stream, filter and play pretty much anything that humans and
machines have created. It supports the most obscure ancient formats up to the
cutting edge. No matter if they were designed by some standards committee, the
community or a corporation.

This build contains binaries built with the jellyfin-ffmpeg patchset.


%prep
%autosetup -n %{name}-%{version}-%{patchset_release} -p1

cat debian/patches/*.patch | patch -p1


%build
./configure \
    --arch=%{_target_cpu} \
    --optflags="%{build_cflags}" \
    --extra-ldflags="%{build_ldflags}" \
    --prefix=/discard \
    --bindir=%{_libexecdir}/%{name} \
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
    --enable-libopenmpt \
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
    --enable-libvpl \
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
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/ffmpeg
%{_libexecdir}/%{name}/ffprobe


%changelog
* Mon Nov 27 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0.1-1.1
- Update to 6.0.1 and patchset release 1

* Sat Nov 04 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0-8.1
- Update to patchset release 8

* Thu Nov 02 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0-7.2
- Add upstream patches for Nvidia SDK 12.1 compatibility (GH#1)

* Tue Oct 17 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0-7.1
- Update to patchset release 7

* Tue Aug 29 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0-6.1
- Update to patchset release 6

* Sun Aug 06 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0-5.1
- Update to patchset release 5

* Thu Jun 29 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0-4.1
- Update to patchset release 4

* Sun Jun 04 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0-3.1
- Update to patchset release 3

* Wed May 03 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 6.0-2.1
- Update to 6.0 and patchset release 2
- Rename package to just jellyfin-ffmpeg
- Use oneVPL instead of libmfx

* Tue Apr 18 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 5.1.3-1.1
- Update to 5.1.3 and patchset release 1
- Enable openmpt support

* Sat Mar 25 2023 Andrew Gunnerson <accounts+fedora@chiller3.com> - 5.1.2-9.1
- Update to patchset release 9

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
