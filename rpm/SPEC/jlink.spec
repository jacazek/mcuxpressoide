Summary: Segger jlink

%define version 6.804
%define architecture x86_64

Name: jlink
URL: https://www.segger.com
Version: %{version}
Release: 1
License: GPL
Requires: libncurses5
Requires: glibc

%description
SEGGER J-Link tools
This package provides software tools
for SEGGER J-Link debug probes.


%prep
installer=mcuxpressoide-11.2.0_4120.x86_64.deb.bin

jlink="JLink_Linux_x86_64"

extract_control () {
    mkdir control
    tar -xzf control.tar.gz -C ./control
}

extract_data () {
    mkdir data
    tar -xzf data.tar.gz -C ./data
}

startdirectory=$PWD
outputdir=$startdirectory
../SOURCES/$installer --noexec --keep --target $outputdir
cd $outputdir

mkdir $jlink
ar -x $jlink.deb --output ./$jlink
cd $jlink
extract_control
extract_data
cd ..

cd $startdirectory

%install
cp -R $PWD/JLink_Linux_x86_64/data/ $RPM_BUILD_ROOT/


%files
/opt/SEGGER/JLink
/opt/SEGGER
/usr/bin
/etc/udev/rules.d/99-jlink.rules

%pre
SYS_SYMLINK_DIR=/opt/SEGGER
echo "Removing ${SYS_SYMLINK_DIR}/JLink ..."
if [ -e ${SYS_SYMLINK_DIR}/JLink ]       # Does it exist?
then
  if  [ -h ${SYS_SYMLINK_DIR}/JLink ]    # Is it a symbolic link?
  then
    rm -f ${SYS_SYMLINK_DIR}/JLink
  elif  [ -d ${SYS_SYMLINK_DIR}/JLink ]  # Is it a real folder?
  then
    rm -f -r ${SYS_SYMLINK_DIR}/JLink
  else 
    echo "Error: please remove ${SYS_SYMLINK_DIR}/JLink"
    exit 1                               # Unexpected result
  fi
else
  echo "${SYS_SYMLINK_DIR}/JLink not found (OK)"
fi
exit 0
