Name:           ffmpeg
Version:        5.1.3
Release:        1
Summary:        FFmpeg video encoding and decoding library
Url:            http://ffmpeg.org/
Source:         %{name}-%{version}.tar.bz2
Source1:        enable_decoders
Source2:        enable_encoders
Patch0:         0001-backport-avcodec-x86-mathops-clip-constants-used-wit.patch
License:        LGPLv2+
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(zlib)
Conflicts:      libav
%ifarch %{ix86} x86_64
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
%autosetup -p1 -n %{name}-%{version}/upstream

%build

# We have an older sed that doesn't recognize the new -E switch. Use the old one
sed -i 's/sed -E/sed -r/g' ./configure

./configure --prefix=/usr --libdir=%{_libdir} --disable-debug --enable-shared --enable-pic \
  --disable-static --disable-doc --enable-muxers --enable-demuxers --enable-protocols \
  --disable-indevs --disable-outdevs --disable-bsfs --enable-network --disable-hwaccels \
  --enable-libfontconfig --enable-libfreetype --enable-libopenjpeg --enable-libopus --enable-libpulse --enable-libspeex \
  --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libwebp --disable-encoders --disable-decoders \
  --enable-encoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%{SOURCE2})" \
  --enable-decoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%{SOURCE1})" \

%make_build

%install
# Remove examples
%make_install
rm -rf $RPM_BUILD_ROOT/%{_datadir}/%{name}/examples

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING.LGPLv2.1
%dir %{_datadir}/ffmpeg
%{_datadir}/ffmpeg/*.ffpreset
%{_datadir}/ffmpeg/ffprobe.xsd
%{_libdir}/libavcodec.so.*
%{_libdir}/libavdevice.so.*
%{_libdir}/libavfilter.so.*
%{_libdir}/libavformat.so.*
%{_libdir}/libavutil.so.*
%{_libdir}/libswresample.so.*
%{_libdir}/libswscale.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libavcodec.so
%{_libdir}/libavdevice.so
%{_libdir}/libavfilter.so
%{_libdir}/libavformat.so
%{_libdir}/libavutil.so
%{_libdir}/libswresample.so
%{_libdir}/libswscale.so
%{_libdir}/pkgconfig/libavcodec.pc
%{_libdir}/pkgconfig/libavdevice.pc
%{_libdir}/pkgconfig/libavfilter.pc
%{_libdir}/pkgconfig/libavformat.pc
%{_libdir}/pkgconfig/libavutil.pc
%{_libdir}/pkgconfig/libswresample.pc
%{_libdir}/pkgconfig/libswscale.pc
%dir %{_includedir}/libavcodec
%{_includedir}/libavcodec/ac3_parser.h
%{_includedir}/libavcodec/adts_parser.h
%{_includedir}/libavcodec/avcodec.h
%{_includedir}/libavcodec/avdct.h
%{_includedir}/libavcodec/avfft.h
%{_includedir}/libavcodec/bsf.h
%{_includedir}/libavcodec/codec.h
%{_includedir}/libavcodec/codec_desc.h
%{_includedir}/libavcodec/codec_id.h
%{_includedir}/libavcodec/codec_par.h
%{_includedir}/libavcodec/d3d11va.h
%{_includedir}/libavcodec/defs.h
%{_includedir}/libavcodec/dirac.h
%{_includedir}/libavcodec/dv_profile.h
%{_includedir}/libavcodec/dxva2.h
%{_includedir}/libavcodec/jni.h
%{_includedir}/libavcodec/mediacodec.h
%{_includedir}/libavcodec/packet.h
%{_includedir}/libavcodec/qsv.h
%{_includedir}/libavcodec/vdpau.h
%{_includedir}/libavcodec/version.h
%{_includedir}/libavcodec/version_major.h
%{_includedir}/libavcodec/videotoolbox.h
%{_includedir}/libavcodec/vorbis_parser.h
%{_includedir}/libavcodec/xvmc.h
%dir %{_includedir}/libavdevice
%{_includedir}/libavdevice/avdevice.h
%{_includedir}/libavdevice/version.h
%{_includedir}/libavdevice/version_major.h
%dir %{_includedir}/libavfilter
%{_includedir}/libavfilter/avfilter.h
%{_includedir}/libavfilter/buffersink.h
%{_includedir}/libavfilter/buffersrc.h
%{_includedir}/libavfilter/version.h
%{_includedir}/libavfilter/version_major.h
%dir %{_includedir}/libavformat
%{_includedir}/libavformat/avformat.h
%{_includedir}/libavformat/avio.h
%{_includedir}/libavformat/version.h
%{_includedir}/libavformat/version_major.h
%dir %{_includedir}/libavutil
%{_includedir}/libavutil/adler32.h
%{_includedir}/libavutil/aes.h
%{_includedir}/libavutil/aes_ctr.h
%{_includedir}/libavutil/attributes.h
%{_includedir}/libavutil/audio_fifo.h
%{_includedir}/libavutil/avassert.h
%{_includedir}/libavutil/avconfig.h
%{_includedir}/libavutil/avstring.h
%{_includedir}/libavutil/avutil.h
%{_includedir}/libavutil/base64.h
%{_includedir}/libavutil/blowfish.h
%{_includedir}/libavutil/bprint.h
%{_includedir}/libavutil/bswap.h
%{_includedir}/libavutil/buffer.h
%{_includedir}/libavutil/camellia.h
%{_includedir}/libavutil/cast5.h
%{_includedir}/libavutil/channel_layout.h
%{_includedir}/libavutil/common.h
%{_includedir}/libavutil/cpu.h
%{_includedir}/libavutil/crc.h
%{_includedir}/libavutil/csp.h
%{_includedir}/libavutil/detection_bbox.h
%{_includedir}/libavutil/des.h
%{_includedir}/libavutil/dict.h
%{_includedir}/libavutil/display.h
%{_includedir}/libavutil/dovi_meta.h
%{_includedir}/libavutil/downmix_info.h
%{_includedir}/libavutil/encryption_info.h
%{_includedir}/libavutil/error.h
%{_includedir}/libavutil/eval.h
%{_includedir}/libavutil/ffversion.h
%{_includedir}/libavutil/fifo.h
%{_includedir}/libavutil/file.h
%{_includedir}/libavutil/film_grain_params.h
%{_includedir}/libavutil/frame.h
%{_includedir}/libavutil/hash.h
%{_includedir}/libavutil/hdr_dynamic_metadata.h
%{_includedir}/libavutil/hdr_dynamic_vivid_metadata.h
%{_includedir}/libavutil/hmac.h
%{_includedir}/libavutil/hwcontext.h
%{_includedir}/libavutil/hwcontext_cuda.h
%{_includedir}/libavutil/hwcontext_d3d11va.h
%{_includedir}/libavutil/hwcontext_drm.h
%{_includedir}/libavutil/hwcontext_dxva2.h
%{_includedir}/libavutil/hwcontext_mediacodec.h
%{_includedir}/libavutil/hwcontext_opencl.h
%{_includedir}/libavutil/hwcontext_qsv.h
%{_includedir}/libavutil/hwcontext_vaapi.h
%{_includedir}/libavutil/hwcontext_vdpau.h
%{_includedir}/libavutil/hwcontext_videotoolbox.h
%{_includedir}/libavutil/hwcontext_vulkan.h
%{_includedir}/libavutil/imgutils.h
%{_includedir}/libavutil/intfloat.h
%{_includedir}/libavutil/intreadwrite.h
%{_includedir}/libavutil/lfg.h
%{_includedir}/libavutil/log.h
%{_includedir}/libavutil/lzo.h
%{_includedir}/libavutil/macros.h
%{_includedir}/libavutil/mastering_display_metadata.h
%{_includedir}/libavutil/mathematics.h
%{_includedir}/libavutil/md5.h
%{_includedir}/libavutil/mem.h
%{_includedir}/libavutil/motion_vector.h
%{_includedir}/libavutil/murmur3.h
%{_includedir}/libavutil/opt.h
%{_includedir}/libavutil/parseutils.h
%{_includedir}/libavutil/pixdesc.h
%{_includedir}/libavutil/pixelutils.h
%{_includedir}/libavutil/pixfmt.h
%{_includedir}/libavutil/random_seed.h
%{_includedir}/libavutil/rational.h
%{_includedir}/libavutil/rc4.h
%{_includedir}/libavutil/replaygain.h
%{_includedir}/libavutil/ripemd.h
%{_includedir}/libavutil/samplefmt.h
%{_includedir}/libavutil/sha.h
%{_includedir}/libavutil/sha512.h
%{_includedir}/libavutil/spherical.h
%{_includedir}/libavutil/stereo3d.h
%{_includedir}/libavutil/tea.h
%{_includedir}/libavutil/threadmessage.h
%{_includedir}/libavutil/time.h
%{_includedir}/libavutil/timecode.h
%{_includedir}/libavutil/timestamp.h
%{_includedir}/libavutil/tree.h
%{_includedir}/libavutil/twofish.h
%{_includedir}/libavutil/tx.h
%{_includedir}/libavutil/uuid.h
%{_includedir}/libavutil/version.h
%{_includedir}/libavutil/video_enc_params.h
%{_includedir}/libavutil/xtea.h
%dir %{_includedir}/libswresample
%{_includedir}/libswresample/swresample.h
%{_includedir}/libswresample/version.h
%{_includedir}/libswresample/version_major.h
%dir %{_includedir}/libswscale
%{_includedir}/libswscale/swscale.h
%{_includedir}/libswscale/version.h
%{_includedir}/libswscale/version_major.h

%files tools
%defattr(-,root,root)
%{_bindir}/ffmpeg
%{_bindir}/ffprobe
