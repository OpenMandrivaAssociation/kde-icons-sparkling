%define base_name	kde-icons
%define theme_name	sparkling
%define version		0.5
%define name		%{base_name}-%{theme_name}
%define release		%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Icon themes for kde
License:	Artistic
Group:		Graphical desktop/KDE
Source:		%{theme_name}-%{version}.tar.bz2
URL:		http://kde-look.org/content/show.php?content=9245
Requires:	kdebase3-progs
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Sparkling - an Icon Theme for KDE

%prep
rm -rf %buildroot
%setup -q -n %{theme_name}-%{version}

%build

%install
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}-%{version}
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}-%{version}/16x16
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}-%{version}/32x32
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}-%{version}/48x48
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}-%{version}/64x64
install -d -m 755 %buildroot%{_iconsdir}/%{theme_name}-%{version}/128x128

# correct files.tcl wrong script encoding
perl -pi -e 's/\015$//' changes.txt
perl -pi -e 's/\015$//' License.txt
perl -pi -e 's/\015$//' index.desktop

cp -fr * %buildroot%{_iconsdir}/%{theme_name}-%{version}/
cp -f 16x16/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/16x16/apps/menuk-mdk.png
cp -f 16x16/apps/xmms_on.png %buildroot%_iconsdir/%{theme_name}-%{version}/16x16/apps/amarok.png
cp -f 16x16/apps/firebird.png %buildroot%_iconsdir/%{theme_name}-%{version}/16x16/apps/firefox.png
cp -f 16x16/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/16x16/apps/home-mdk.png
cp -f 32x32/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/32x32/apps/menuk-mdk.png
cp -f 32x32/apps/xmms_on.png %buildroot%_iconsdir/%{theme_name}-%{version}/32x32/apps/amarok.png
cp -f 32x32/apps/firebird.png %buildroot%_iconsdir/%{theme_name}-%{version}/32x32/apps/firefox.png
cp -f 32x32/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/32x32/apps/home-mdk.png
cp -f 48x48/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/48x48/apps/menuk-mdk.png
cp -f 48x48/apps/firebird.png %buildroot%_iconsdir/%{theme_name}-%{version}/48x48/apps/firefox.png
cp -f 48x48/apps/xmms_on.png %buildroot%_iconsdir/%{theme_name}-%{version}/48x48/apps/amarokk.png
cp -f 48x48/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/48x48/apps/home-mdk.png
cp -f 64x64/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/64x64/apps/menuk-mdk.png
cp -f 64x64/apps/firebird.png %buildroot%_iconsdir/%{theme_name}-%{version}/64x64/apps/firefox.png
cp -f 64x64/apps/xmms_on.png %buildroot%_iconsdir/%{theme_name}-%{version}/64x64/apps/amarokk.png
cp -f 64x64/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/64x64/apps/home-mdk.png
cp -f 128x128/apps/kmenu.png %buildroot%_iconsdir/%{theme_name}-%{version}/128x128/apps/menuk-mdk.png
cp -f 128x128/apps/xmms_on.png %buildroot%_iconsdir/%{theme_name}-%{version}/128x128/apps/amarok.png
cp -f 128x128/apps/kfm_home.png %buildroot%_iconsdir/%{theme_name}-%{version}/128x128/apps/home-mdk.png


%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc License.txt changes.txt
%{_iconsdir}/%{theme_name}-%{version}/*
