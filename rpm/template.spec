Name:           ros-indigo-bayesian-belief-networks
Version:        1.0.59
Release:        0%{?dist}
Summary:        ROS bayesian_belief_networks package

Group:          Development/Libraries
License:        Apache License, Version 2.0
URL:            https://github.com/eBay/bayesian-belief-networks
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
BuildRequires:  git
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-mk
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-std-msgs

%description
The bayesian_belief_networks package form https://github.com/eBay/bayesian-
belief-networks, Authored by Neville Newey, Anzar Afaq, Copyright 2013 eBay
Software Foundation

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
* Tue Feb 03 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.59-0
- Autogenerated by Bloom

* Wed Jan 07 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.58-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.57-0
- Autogenerated by Bloom

* Wed Dec 17 2014 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.0.56-0
- Autogenerated by Bloom

