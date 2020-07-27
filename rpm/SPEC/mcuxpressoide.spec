Summary: NXP

%define version 11.2.0
%define release 4120
%define app mcuxpressoide-%{version}_%{release}
Name: mcuxpressoide
URL: https://www.segger.com
Version: %{version}
Group: Development/Tools
Release: %{release}
License: GPL
Source0: https://freescaleesd.flexnetoperations.com/337170/917/17116917/%{app}.x86_64.deb.bin
Requires: libncurses5
Requires: libusb-1_0-devel
Requires: dfu-util
Requires: libwebkit2gtk-4_0-37

%description
MCUXpresso IDE is an Eclipse-based IDE for development of software for NXP LPC and Kinetis platforms.


%prep
ls
installer=%{app}.x86_64.deb.bin
mcuxpressoide=$(basename -- "$installer")
mcuxpressoide="${mcuxpressoide%.*}"
mcuxpressoide="${mcuxpressoide%.*}"


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

mkdir $mcuxpressoide
ar -x $mcuxpressoide.deb --output ./$mcuxpressoide
cd $mcuxpressoide
extract_control
extract_data
cd ..

cd $startdirectory


# %pre

%install
cp -R $PWD/%{app}.x86_64/data/ $RPM_BUILD_ROOT/

%files
/usr/local/%{app}
/usr/lib/libp64-0.1.so.4
/usr/share/applications/com.nxp.mcuxpressoide.desktop
/lib/udev/rules.d/56-pemicro.rules
/lib/udev/rules.d/85-mcuxpresso.rules


%post
set -e
udevadm control --reload-rules
if [ -L "/usr/local/mcuxpressoide" ]; then
  echo "Removing mcuxpressoide symbolic link..."
  rm /usr/local/mcuxpressoide
fi
ln -s /usr/local/%{app} /usr/local/mcuxpressoide


%postun
if [ "$1" -eq "0" ]; then

  rm -rf /usr/local/%{app}
  if [ -L "/usr/local/mcuxpressoide" ]; then
      echo "Removing mcuxpressoide symbolic link..."
      rm /usr/local/mcuxpressoide/
  fi
fi
