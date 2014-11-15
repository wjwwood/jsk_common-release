Name:           ros-hydro-collada-urdf-jsk-patch
Version:        1.0.54
Release:        0%{?dist}
Summary:        ROS collada_urdf_jsk_patch package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/collada_urdf_jsk_patch
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       gts
Requires:       ros-hydro-angles
Requires:       ros-hydro-assimp-devel
Requires:       ros-hydro-class-loader
Requires:       ros-hydro-collada-parser
Requires:       ros-hydro-collada-urdf
Requires:       ros-hydro-geometric-shapes
Requires:       ros-hydro-kdl-parser
Requires:       ros-hydro-pluginlib
Requires:       ros-hydro-resource-retriever
Requires:       ros-hydro-roscpp
Requires:       ros-hydro-tf
Requires:       ros-hydro-urdf
Requires:       ros-hydro-urdfdom
Requires:       ros-hydro-urdfdom-headers
BuildRequires:  collada-dom-devel
BuildRequires:  git
BuildRequires:  gts
BuildRequires:  ros-hydro-angles
BuildRequires:  ros-hydro-assimp-devel
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-class-loader
BuildRequires:  ros-hydro-cmake-modules
BuildRequires:  ros-hydro-collada-parser
BuildRequires:  ros-hydro-collada-urdf
BuildRequires:  ros-hydro-geometric-shapes
BuildRequires:  ros-hydro-kdl-parser
BuildRequires:  ros-hydro-mk
BuildRequires:  ros-hydro-pluginlib
BuildRequires:  ros-hydro-resource-retriever
BuildRequires:  ros-hydro-roscpp
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-tf
BuildRequires:  ros-hydro-urdf
BuildRequires:  ros-hydro-urdfdom
BuildRequires:  ros-hydro-urdfdom-headers

%description
unaccepted patch for collada_urdf

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
* Sat Nov 15 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Mon Oct 20 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.51-0
- Autogenerated by Bloom

* Tue Oct 14 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.49-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

