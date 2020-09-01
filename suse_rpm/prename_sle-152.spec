#
# spec file for package default
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           prename_sle-152
Version:        1.0
Release:        0
Summary:        PERL RENAME
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        GPL-3.0+
# FIXME: use correct group, see "https://en.opensuse.org/openSUSE:Package_group_guidelines"
Group:          perl 
Url:            https://github.com/asteriosos/prename
Source:         %{name}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
"prename" renames the filenames supplied according to the rule specified as the first argument.

%prep

%setup -n %{name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1

install -m 755 ~/rpmbuild/SOURCES/%{name}/prename $RPM_BUILD_ROOT/usr/bin/
install -m 644 ~/rpmbuild/SOURCES/%{name}/prename.1.gz $RPM_BUILD_ROOT/usr/share/man/man1/

%postun
if [ -f /usr/bin/prename ]; then
  echo "prename still exists. Remove now."
  rm /usr/bin/prename
else
  echo "prename successfully removed."
fi
if [ -f /usr/share/man/man1/prename.1.gz ]; then
  echo "prename1.gz still exists. Remove now."
  rm /usr/share/man/man1/prename.1.gz
else
  echo "prename1.gz successfully removed."
fi

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

%files
%defattr(-,root,root)
/usr/bin/prename
/usr/share/man/man1/prename.1.gz

%changelog
* Tue Sep 01 2020  asteriosos @ github
- 1.0 r1 First release
