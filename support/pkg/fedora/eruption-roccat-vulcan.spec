%global OrigName eruption-roccat-vulcan
%global ShortName eruption

Name:    eruption-roccat-vulcan-git
Version: 0.1.16
Release: 0%{?dist}
Summary: eruption-roccat-vulcan - Linux user-mode driver for the ROCCAT Vulcan 100/12x series keyboards
URL:     https://github.com/X3n0m0rph59/eruption-roccat-vulcan
License: GPLv3+

Source0: https://github.com/X3n0m0rph59/%{OrigName}/archive/master/master.tar.gz

BuildRoot: %{_tmppath}/%{name}-build

BuildRequires: cargo
BuildRequires: systemd-devel
BuildRequires: dbus-devel
BuildRequires: hidapi-devel
BuildRequires: libevdev-devel
BuildRequires: libusbx-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: luajit-devel
BuildRequires: libX11-devel
BuildRequires: libXrandr-devel

Requires: systemd
Requires: dbus
Requires: hidapi
Requires: libevdev
Requires: luajit

Recommends: lua-socket-compat

Conflicts: eruption-roccat-vulcan

%global gittag master
%global debug_package %{nil}

%description
Linux user-mode driver for the ROCCAT Vulcan 100/12x series keyboards

%prep
# %autosetup -n %{name}-%{version}
%autosetup %{OrigName}-master

%build
cargo build --all --release --verbose

%install
%{__mkdir_p} %{buildroot}%{_mandir}/man5
%{__mkdir_p} %{buildroot}%{_mandir}/man8
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__mkdir_p} %{buildroot}%{_sysconfdir}/%{ShortName}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/dbus-1/system.d
%{__mkdir_p} %{buildroot}/usr/lib/udev/rules.d
%{__mkdir_p} %{buildroot}/usr/lib/systemd/system-sleep
%{__mkdir_p} %{buildroot}%{_unitdir}
%{__mkdir_p} %{buildroot}%{_presetdir}
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/%{ShortName}
%{__mkdir_p} %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles
%{__mkdir_p} %{buildroot}%{_libdir}/%{ShortName}/scripts
%{__mkdir_p} %{buildroot}%{_libdir}/%{ShortName}/scripts/lib
%{__mkdir_p} %{buildroot}%{_libdir}/%{ShortName}/scripts/lib/macros
%{__mkdir_p} %{buildroot}%{_libdir}/%{ShortName}/scripts/lib/themes
%{__mkdir_p} %{buildroot}%{_libdir}/%{ShortName}/scripts/examples
%{__mkdir_p} %{buildroot}%{_docdir}/%{ShortName}
%{__mkdir_p} %{buildroot}%{_datarootdir}/icons/hicolor/scalable/apps
%{__mkdir_p} %{buildroot}%{_datarootdir}/%{ShortName}/sfx
%{__mkdir_p} %{buildroot}%{_datarootdir}/%{ShortName}/i18n

cp -a %{_builddir}/%{name}-%{version}/support/man/eruption.8 %{buildroot}/%{_mandir}/man8/
cp -a %{_builddir}/%{name}-%{version}/support/man/eruption.conf.5 %{buildroot}/%{_mandir}/man5/
cp -a %{_builddir}/%{name}-%{version}/support/man/eruptionctl.1 %{buildroot}/%{_mandir}/man1/
cp -a %{_builddir}/%{name}-%{version}/support/man/eruption-netfx.1 %{buildroot}/%{_mandir}/man1/
cp -a %{_builddir}/%{name}-%{version}/support/config/eruption.conf %{buildroot}/%{_sysconfdir}/%{ShortName}/
cp -a %{_builddir}/%{name}-%{version}/support/dbus/org.eruption.control.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d/
cp -a %{_builddir}/%{name}-%{version}/support/udev/99-eruption-roccat-vulcan.rules %{buildroot}/usr/lib/udev/rules.d/
cp -a %{_builddir}/%{name}-%{version}/support/systemd/eruption.preset %{buildroot}/%{_presetdir}/50-eruption.preset
cp -a %{_builddir}/%{name}-%{version}/support/systemd/eruption.service %{buildroot}/%{_unitdir}/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/default.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/checkerboard.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/fx1.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/fx2.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/fireworks.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/gaming.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/gradient-noise.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/heatmap.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/heatmap-errors.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/matrix.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/netfx.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/batique.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/profile1.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/profile2.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/profile3.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/profile4.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/psychedelic.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/twinkle.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/rainbow.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/preset-red-yellow.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/preset-blue-red.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/rainbow-wave.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/snake.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/solid-wave.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/starcraft2.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/spectrum-analyzer.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/vu-meter.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/swirl-perlin.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/swirl-perlin-blue-red.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/swirl-perlin-rainbow.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/swirl-perlin-red-yellow.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/swirl-turbulence.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/swirl-voronoi.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/profiles/turbulence.profile %{buildroot}%{_sharedstatedir}/%{ShortName}/profiles/
cp -a %{_builddir}/%{name}-%{version}/support/sfx/typewriter1.wav %{buildroot}%{_datarootdir}/%{ShortName}/sfx/typewriter1.wav
cp -a %{_builddir}/%{name}-%{version}/support/sfx/phaser1.wav %{buildroot}%{_datarootdir}/%{ShortName}/sfx/phaser1.wav
cp -a %{_builddir}/%{name}-%{version}/support/sfx/phaser2.wav %{buildroot}%{_datarootdir}/%{ShortName}/sfx/phaser2.wav
ln -s phaser1.wav %{buildroot}%{_datarootdir}/%{ShortName}/sfx/key-down.wav
ln -s phaser2.wav %{buildroot}%{_datarootdir}/%{ShortName}/sfx/key-up.wav
cp -ra %{_builddir}/%{name}-%{version}/eruption/src/scripts %{buildroot}%{_datarootdir}/%{ShortName}/

cp -a %{_builddir}/%{name}-%{version}/support/systemd/eruption-suspend.sh %{buildroot}/usr/lib/systemd/system-sleep/eruption

install -Dp -m 0755 %{_builddir}/%{name}-%{version}/target/release/eruption %{buildroot}%{_bindir}/eruption
install -Dp -m 0755 %{_builddir}/%{name}-%{version}/target/release/eruptionctl %{buildroot}%{_bindir}/eruptionctl
install -Dp -m 0755 %{_builddir}/%{name}-%{version}/target/release/eruption-netfx %{buildroot}%{_bindir}/eruption-netfx
install -Dp -m 0755 %{_builddir}/%{name}-%{version}/target/release/eruption-debug-tool %{buildroot}%{_bindir}/eruption-debug-tool

%post
%systemd_post %{ShortName}.service

%preun
%systemd_preun %{ShortName}.service

%postun
%systemd_postun_with_restart %{ShortName}.service

%files
%doc %{_mandir}/man5/eruption.conf.5.gz
%doc %{_mandir}/man8/eruption.8.gz
%doc %{_mandir}/man1/eruptionctl.1.gz
%doc %{_mandir}/man1/eruption-netfx.1.gz
%dir %{_datarootdir}/icons/hicolor/scalable/apps/
%config(noreplace) %{_sysconfdir}/%{ShortName}/%{ShortName}.conf
%{_sysconfdir}/dbus-1/system.d/org.eruption.control.conf
/usr/lib/udev/rules.d/99-eruption-roccat-vulcan.rules
/usr/lib/systemd/system-sleep/eruption
%{_bindir}/eruption
%{_bindir}/eruptionctl
%{_bindir}/eruption-netfx
%{_bindir}/eruption-debug-tool
%{_unitdir}/eruption.service
%{_presetdir}/50-eruption.preset
%{_sharedstatedir}/%{ShortName}/profiles/default.profile
%{_sharedstatedir}/%{ShortName}/profiles/checkerboard.profile
%{_sharedstatedir}/%{ShortName}/profiles/fx1.profile
%{_sharedstatedir}/%{ShortName}/profiles/fx2.profile
%{_sharedstatedir}/%{ShortName}/profiles/fireworks.profile
%{_sharedstatedir}/%{ShortName}/profiles/gaming.profile
%{_sharedstatedir}/%{ShortName}/profiles/gradient-noise.profile
%{_sharedstatedir}/%{ShortName}/profiles/heatmap.profile
%{_sharedstatedir}/%{ShortName}/profiles/heatmap-errors.profile
%{_sharedstatedir}/%{ShortName}/profiles/matrix.profile
%{_sharedstatedir}/%{ShortName}/profiles/netfx.profile
%{_sharedstatedir}/%{ShortName}/profiles/batique.profile
%{_sharedstatedir}/%{ShortName}/profiles/profile1.profile
%{_sharedstatedir}/%{ShortName}/profiles/profile2.profile
%{_sharedstatedir}/%{ShortName}/profiles/profile3.profile
%{_sharedstatedir}/%{ShortName}/profiles/profile4.profile
%{_sharedstatedir}/%{ShortName}/profiles/psychedelic.profile
%{_sharedstatedir}/%{ShortName}/profiles/twinkle.profile
%{_sharedstatedir}/%{ShortName}/profiles/rainbow.profile
%{_sharedstatedir}/%{ShortName}/profiles/preset-red-yellow.profile
%{_sharedstatedir}/%{ShortName}/profiles/preset-blue-red.profile
%{_sharedstatedir}/%{ShortName}/profiles/rainbow-wave.profile
%{_sharedstatedir}/%{ShortName}/profiles/snake.profile
%{_sharedstatedir}/%{ShortName}/profiles/solid-wave.profile
%{_sharedstatedir}/%{ShortName}/profiles/starcraft2.profile
%{_sharedstatedir}/%{ShortName}/profiles/spectrum-analyzer.profile
%{_sharedstatedir}/%{ShortName}/profiles/vu-meter.profile
%{_sharedstatedir}/%{ShortName}/profiles/swirl-perlin.profile
%{_sharedstatedir}/%{ShortName}/profiles/swirl-perlin-blue-red.profile
%{_sharedstatedir}/%{ShortName}/profiles/swirl-perlin-rainbow.profile
%{_sharedstatedir}/%{ShortName}/profiles/swirl-perlin-red-yellow.profile
%{_sharedstatedir}/%{ShortName}/profiles/swirl-turbulence.profile
%{_sharedstatedir}/%{ShortName}/profiles/swirl-voronoi.profile
%{_sharedstatedir}/%{ShortName}/profiles/turbulence.profile
%{_datarootdir}/%{ShortName}/scripts/examples/simple.lua
%{_datarootdir}/%{ShortName}/scripts/lib/debug.lua
%{_datarootdir}/%{ShortName}/scripts/lib/queue.lua
%{_datarootdir}/%{ShortName}/scripts/lib/utilities.lua
%{_datarootdir}/%{ShortName}/scripts/lib/declarations.lua
%config %{_datarootdir}/%{ShortName}/scripts/lib/themes/default.lua
%config %{_datarootdir}/%{ShortName}/scripts/lib/themes/gaming.lua
%config %{_datarootdir}/%{ShortName}/scripts/lib/macros/modifiers.lua
%config %{_datarootdir}/%{ShortName}/scripts/lib/macros/user-macros.lua
%config %{_datarootdir}/%{ShortName}/scripts/lib/macros/user-mappings.lua
%config %{_datarootdir}/%{ShortName}/scripts/lib/macros/starcraft2.lua
%{_datarootdir}/%{ShortName}/scripts/macros.lua
%{_datarootdir}/%{ShortName}/scripts/macros.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/profiles.lua
%{_datarootdir}/%{ShortName}/scripts/profiles.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/stats.lua
%{_datarootdir}/%{ShortName}/scripts/stats.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/afterglow.lua
%{_datarootdir}/%{ShortName}/scripts/afterglow.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/afterhue.lua
%{_datarootdir}/%{ShortName}/scripts/afterhue.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/audioviz1.lua
%{_datarootdir}/%{ShortName}/scripts/audioviz1.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/audioviz2.lua
%{_datarootdir}/%{ShortName}/scripts/audioviz2.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/audioviz3.lua
%{_datarootdir}/%{ShortName}/scripts/audioviz3.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/audioviz4.lua
%{_datarootdir}/%{ShortName}/scripts/audioviz4.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/audioviz5.lua
%{_datarootdir}/%{ShortName}/scripts/audioviz5.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/billow.lua
%{_datarootdir}/%{ShortName}/scripts/billow.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/checkerboard.lua
%{_datarootdir}/%{ShortName}/scripts/checkerboard.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/organic.lua
%{_datarootdir}/%{ShortName}/scripts/organic.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/batique.lua
%{_datarootdir}/%{ShortName}/scripts/batique.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/fbm.lua
%{_datarootdir}/%{ShortName}/scripts/fbm.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/perlin.lua
%{_datarootdir}/%{ShortName}/scripts/perlin.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/phonon.lua
%{_datarootdir}/%{ShortName}/scripts/phonon.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/psychedelic.lua
%{_datarootdir}/%{ShortName}/scripts/psychedelic.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/rmf.lua
%{_datarootdir}/%{ShortName}/scripts/rmf.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/voronoi.lua
%{_datarootdir}/%{ShortName}/scripts/voronoi.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/fire.lua
%{_datarootdir}/%{ShortName}/scripts/fire.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/fireworks.lua
%{_datarootdir}/%{ShortName}/scripts/fireworks.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/gaming.lua
%{_datarootdir}/%{ShortName}/scripts/gaming.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/ghost.lua
%{_datarootdir}/%{ShortName}/scripts/ghost.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/gradient.lua
%{_datarootdir}/%{ShortName}/scripts/gradient.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/linear-gradient.lua
%{_datarootdir}/%{ShortName}/scripts/linear-gradient.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/halo.lua
%{_datarootdir}/%{ShortName}/scripts/halo.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/heartbeat.lua
%{_datarootdir}/%{ShortName}/scripts/heartbeat.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/heatmap.lua
%{_datarootdir}/%{ShortName}/scripts/heatmap.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/impact.lua
%{_datarootdir}/%{ShortName}/scripts/impact.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/multigradient.lua
%{_datarootdir}/%{ShortName}/scripts/multigradient.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/netfx.lua
%{_datarootdir}/%{ShortName}/scripts/netfx.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/osn.lua
%{_datarootdir}/%{ShortName}/scripts/osn.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/rainbow.lua
%{_datarootdir}/%{ShortName}/scripts/rainbow.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/raindrops.lua
%{_datarootdir}/%{ShortName}/scripts/raindrops.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/shockwave.lua
%{_datarootdir}/%{ShortName}/scripts/shockwave.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/solid.lua
%{_datarootdir}/%{ShortName}/scripts/solid.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/stripes.lua
%{_datarootdir}/%{ShortName}/scripts/stripes.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/swirl-perlin.lua
%{_datarootdir}/%{ShortName}/scripts/swirl-perlin.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/swirl-turbulence.lua
%{_datarootdir}/%{ShortName}/scripts/swirl-turbulence.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/swirl-voronoi.lua
%{_datarootdir}/%{ShortName}/scripts/swirl-voronoi.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/flight-perlin.lua
%{_datarootdir}/%{ShortName}/scripts/flight-perlin.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/sysmon.lua
%{_datarootdir}/%{ShortName}/scripts/sysmon.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/temperature.lua
%{_datarootdir}/%{ShortName}/scripts/temperature.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/turbulence.lua
%{_datarootdir}/%{ShortName}/scripts/turbulence.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/water.lua
%{_datarootdir}/%{ShortName}/scripts/water.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/wave.lua
%{_datarootdir}/%{ShortName}/scripts/wave.lua.manifest
%{_datarootdir}/%{ShortName}/scripts/snake.lua
%{_datarootdir}/%{ShortName}/scripts/snake.lua.manifest
%{_datarootdir}/%{ShortName}/sfx/typewriter1.wav
%{_datarootdir}/%{ShortName}/sfx/phaser1.wav
%{_datarootdir}/%{ShortName}/sfx/phaser2.wav
%{_datarootdir}/%{ShortName}/sfx/key-down.wav
%{_datarootdir}/%{ShortName}/sfx/key-up.wav

%changelog
