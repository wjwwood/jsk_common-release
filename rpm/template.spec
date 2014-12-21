Name:           ros-hydro-multi-map-server
Version:        1.0.56
Release:        0%{?dist}
Summary:        ROS multi_map_server package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/map_server
Source0:        %{name}-%{version}.tar.gz

Requires:       SDL_image-devel
Requires:       ros-hydro-map-server
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-rosconsole
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-rospy
Requires:       ros-hydro-tf
Requires:       yaml-cpp-devel
BuildRequires:  PyYAML
BuildRequires:  SDL_image-devel
BuildRequires:  python-pillow
BuildRequires:  python-pillow-qt
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-jsk-tools
BuildRequires:  ros-hydro-map-server
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-rosconsole
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rosmake
BuildRequires:  ros-hydro-rospy
BuildRequires:  ros-hydro-tf
BuildRequires:  yaml-cpp-devel

%description
multi_map_server provides the

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
* Sun Dec 21 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.56-0
- Autogenerated by Bloom

* Tue Dec 09 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.55-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Mon Oct 20 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.51-0
- Autogenerated by Bloom

* Tue Oct 14 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.49-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

