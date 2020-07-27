## mcuxpressoide

Build scripts to create package for opensuse

### Updating spec file
The following parts of the spec file will need to be updated for a different version of mcuxpressoide
1. Version variable
2. Release variable
3. Source0

### Cleaning up prior builds
1. Delete files in BUILD directory for mcuxpressoide version
2. Delete files in BUILDROOT directory for mcuxpressoide version

### Building the package
1. clean up from any prior builds
2. rpmdev-spectool -g -R mcuxpressoide.spec
3. rpmbuild -bb mcuxpressoide.spec
4. install the package

## Segger JLINK

Build scripts to create package for opensuse

### Updating spec file
The following parts of the spec file will need to be updated for a different version of JLINK
1. Version variable
2. Release variable
3. Source0 (default is mcuxpressoide binary. the data is extracted from that installer)

### Cleaning up prior builds
1. Delete files in BUILD directory for jlink version
2. Delete files in BUILDROOT directory for jlink version

### Building the package
1. rpmdev-spectool -g -R jlink.spec
2. rpmbuild -bb jlink.spec
3. install the package

