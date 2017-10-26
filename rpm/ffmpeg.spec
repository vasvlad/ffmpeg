Name:           ffmpeg
Version:        3.2.4
Release:        1
Summary:        FFmpeg video encoding and decoding library
Group:          Productivity/Multimedia/Video/Editors and Convertors
Url:            http://ffmpeg.org/
Source:         http://ffmpeg.org/releases/%{name}-%{version}.tar.bz2
License:        LGPLv2.1+
BuildRequires:  pkgconfig(speex)
Conflicts:      libav
%ifarch i486 x86_64
BuildRequires:  yasm
%endif

%description
FFmpeg: a complete, cross-platform solution to record, convert and stream audio and video. 

%package devel
Summary:        FFmpeg development package
Requires:       %{name} = %{version}
Requires:       bzip2-devel
Conflicts:      libav-devel

%description devel
Development headers and libraries for FFmpeg - a complete, cross-platform solution to record, convert and stream audio and video. 

%package tools
Summary:        FFmpeg tools package
Requires:       %{name} = %{version}
Conflicts:      libav-tools

%description tools
Development tools for FFmpeg - a complete, cross-platform solution to record, convert and stream audio and video. 

%prep
%setup -q -n %{name}-%{version}/upstream

%build

./configure --prefix=/usr --libdir=%{_libdir} --disable-debug --enable-shared --enable-pic \
  --disable-static --disable-doc --disable-muxers --disable-demuxers --disable-protocols \
  --disable-indevs --disable-outdevs --disable-avdevice --disable-network \
  --disable-lsp --disable-hwaccels --disable-encoders --disable-decoders --disable-bsfs \
  --enable-protocol=file --enable-fft --enable-decoder=aac --enable-decoder=aac_latm \
  --enable-decoder=vorbis --enable-decoder=theora --enable-decoder=flac \
  --enable-encoder=aac --enable-demuxer=aac --enable-demuxer=avi --enable-demuxer=flac \
  --enable-demuxer=h264 --enable-demuxer=m4v --enable-demuxer=mov --enable-demuxer=ogg \
  --enable-demuxer=mpegts --enable-demuxer=mpegvideo --enable-demuxer=matroska \
  --enable-demuxer=wav --enable-decoder=h264 --enable-decoder=mpeg4 --enable-decoder=mp3 \
  --enable-demuxer=aiff --enable-demuxer=flv --enable-demuxer=mjpeg \
  --enable-decoder=pcm_u8 --enable-decoder=pcm_u32le --enable-decoder=pcm_u32be \
  --enable-decoder=pcm_u24le --enable-decoder=pcm_u24be --enable-decoder=pcm_u16le \
  --enable-decoder=pcm_u16be --enable-decoder=pcm_s8 --enable-decoder=pcm_s32le \
  --enable-decoder=pcm_s32be --enable-decoder=pcm_s24le --enable-decoder=pcm_s24be \
  --enable-decoder=pcm_s16le --enable-decoder=pcm_s16be --enable-decoder=pcm_f64le \
  --enable-decoder=pcm_f64be --enable-decoder=pcm_f32le --enable-decoder=pcm_f32be \
  --enable-demuxer=pcm_u32be --enable-demuxer=pcm_u32le --enable-demuxer=pcm_u8 \
  --enable-demuxer=pcm_alaw --enable-demuxer=pcm_f32be --enable-demuxer=pcm_f32le \
  --enable-demuxer=pcm_f64be --enable-demuxer=pcm_f64le --enable-demuxer=pcm_s16be \
  --enable-demuxer=pcm_s16le --enable-demuxer=pcm_s24be --enable-demuxer=pcm_s24le \
  --enable-demuxer=pcm_s32be --enable-demuxer=pcm_s32le --enable-demuxer=pcm_s8 \
  --enable-demuxer=pcm_u16be --enable-demuxer=pcm_u16le --enable-demuxer=pcm_u24be \
  --enable-demuxer=pcm_u24le --enable-decoder=mjpeg --enable-decoder=vp8 --enable-decoder=vp9 \
  --enable-libspeex --enable-decoder=opus


make %{?_smp_mflags}

%install
# Remove examples
%make_install
rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/ffmpeg/*.ffpreset
%{_datadir}/ffmpeg/ffprobe.xsd
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/libavcodec/*.h
%{_includedir}/libavfilter/*.h
%{_includedir}/libavformat/*.h
%{_includedir}/libavutil/*.h
%{_includedir}/libswscale/*.h
%{_includedir}/libswresample/*.h
%{_libdir}/pkgconfig/*.pc

%files tools
%defattr(-,root,root)
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
#%{_bindir}/ffserver
