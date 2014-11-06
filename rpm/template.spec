Name:           ros-hydro-opt-camera
Version:        1.0.53
Release:        0%{?dist}
Summary:        ROS opt_camera package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/opt_camera
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-camera-calibration-parsers
Requires:       ros-hydro-compressed-image-transport
Requires:       ros-hydro-cv-bridge
Requires:       ros-hydro-driver-base
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-image-proc
Requires:       ros-hydro-rospack
Requires:       ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-camera-calibration-parsers
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-compressed-image-transport
BuildRequires:  ros-hydro-cv-bridge
BuildRequires:  ros-hydro-driver-base
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-image-proc
BuildRequires:  ros-hydro-roslang
BuildRequires:  ros-hydro-rospack
BuildRequires:  ros-hydro-sensor-msgs

%description
opt_camera

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Nov 06 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Mon Oct 20 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.51-0
- Autogenerated by Bloom

* Tue Oct 14 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.49-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

