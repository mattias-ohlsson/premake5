Name:           premake5
Version:        5.0.0
Release:        0.alpha14%{?dist}
Summary:        Cross-platform build configuration tool

License:        BSD
URL:            https://premake.github.io
Source0:        https://github.com/premake/premake-core/releases/download/v5.0.0-alpha14/premake-5.0.0-alpha14-src.zip

BuildRequires:  gcc
BuildRequires:  compat-lua-devel readline-devel

%description
Premake is a build configuration tool that can generate project files for:
 - GNU make
 - Code::Blocks
 - CodeLite
 - MonoDevelop
 - SharpDevelop
 - Apple XCode 
 - Microsoft Visual Studio 

%prep
%autosetup -n premake-5.0.0-alpha14

%build
cd build/gmake.unix/
%make_build verbose=true config=debug

%install
install -m 755 -Dp ./bin/*/premake5 %{buildroot}/%{_bindir}/premake5

%files
%{_bindir}/premake5
%doc README.md CHANGES.txt
%license LICENSE.txt

%changelog
* Mon Apr 13 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 5.0.0-0.alpha14
- Initial build
