Source: @(Package)
Section: misc
Priority: extra
Maintainer: @(Maintainer)
Build-Depends: debhelper (>= 9.0.0), @(', '.join(BuildDepends)), ros-groovy-laser-filters
Homepage: @(Homepage)
Standards-Version: 3.9.2

Package: @(Package)
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, @(', '.join(Depends)), ros-groovy-laser-filters
Description: @(Description)
