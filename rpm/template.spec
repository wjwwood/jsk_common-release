Name:           ros-indigo-jsk-common
Version:        1.0.59
Release:        1%{?dist}
Summary:        ROS jsk_common package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/jsk_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-assimp-devel
Requires:       ros-indigo-bayesian-belief-networks
Requires:       ros-indigo-downward
Requires:       ros-indigo-dynamic-tf-publisher
Requires:       ros-indigo-ff
Requires:       ros-indigo-ffha
Requires:       ros-indigo-image-view2
Requires:       ros-indigo-jsk-footstep-msgs
Requires:       ros-indigo-jsk-gui-msgs
Requires:       ros-indigo-jsk-hark-msgs
Requires:       ros-indigo-jsk-network-tools
Requires:       ros-indigo-jsk-tilt-laser
Requires:       ros-indigo-jsk-tools
Requires:       ros-indigo-jsk-topic-tools
Requires:       ros-indigo-libsiftfast
Requires:       ros-indigo-mini-maxwell
Requires:       ros-indigo-multi-map-server
Requires:       ros-indigo-nlopt
Requires:       ros-indigo-opt-camera
Requires:       ros-indigo-posedetection-msgs
Requires:       ros-indigo-rospatlite
Requires:       ros-indigo-rosping
Requires:       ros-indigo-rostwitter
Requires:       ros-indigo-sklearn
Requires:       ros-indigo-speech-recognition-msgs
Requires:       ros-indigo-virtual-force-publisher
Requires:       ros-indigo-voice-text
BuildRequires:  ros-indigo-catkin

%description
Metapackage that contains commonly used toolset for jsk-ros-pkg

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Feb 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.59-1
- Autogenerated by Bloom

* Tue Feb 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.59-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.58-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.57-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.56-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.55-1
- Autogenerated by Bloom

* Tue Dec 09 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.55-0
- Autogenerated by Bloom

* Sat Nov 15 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.54-0
- Autogenerated by Bloom

* Thu Nov 06 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.53-0
- Autogenerated by Bloom

* Sun Oct 12 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.48-0
- Autogenerated by Bloom

