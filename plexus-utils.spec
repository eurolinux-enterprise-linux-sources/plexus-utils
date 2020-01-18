# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global parent plexus
%global subname utils

Name:           plexus-utils
Version:        3.0.9
Release:        7%{?dist}
Summary:        Plexus Common Utilities
# ASL 1.1: several files in src/main/java/org/codehaus/plexus/util/ 
# xpp: src/main/java/org/codehaus/plexus/util/xml/pull directory
# ASL 2.0 and BSD:
#      src/main/java/org/codehaus/plexus/util/cli/StreamConsumer
#      src/main/java/org/codehaus/plexus/util/cli/StreamPumper
#      src/main/java/org/codehaus/plexus/util/cli/Commandline            
# Public domain: src/main/java/org/codehaus/plexus/util/TypeFormat.java
# rest is ASL 2.0
License:        ASL 1.1 and ASL 2.0 and xpp and BSD and Public Domain
Group:          Development/Libraries
URL:            http://plexus.codehaus.org/
Source0:        https://github.com/sonatype/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt

BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.6

BuildRequires:  maven-local
BuildRequires:  maven-compiler-plugin
BuildRequires:  maven-install-plugin
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-javadoc-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:          Javadoc for %{name}
Group:            Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} .

%mvn_file : %{parent}/%{subname}
%mvn_alias : "plexus:plexus-utils"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc NOTICE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc NOTICE.txt LICENSE-2.0.txt

%changelog
* Thu Aug 22 2013 Michal Srb <msrb@redhat.com> - 3.0.9-7
- Migrate away from mvn-rpmbuild (Resolves: #997480)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.0.9-6
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.0.9-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Nov 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.9-3
- Add license from one Public Domain class 

* Fri Nov 23 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0.9-2
- Fix license tag and ASL 2.0 license text

* Wed Oct 10 2012 Alexander Kurtakov <akurtako@redhat.com> 3.0.9-1
- Update to upstream 3.0.9.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Sep 7 2011 Alexander Kurtakov <akurtako@redhat.com> 3.0-1
- Update to upstream 3.0.

* Mon Feb 28 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0.6-1
- Update to 2.0.6
- Remove obsolete patches
- Use maven 3 to build

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0.5-2
- Use versionless jars/javadocs
- Use new maven plugin names
- Add compatibility depmap

* Wed May  5 2010 Mary Ellen Foster <mefoster at gmail.com> 2.0.5-1
- Update to 2.0.5

* Fri Feb 12 2010 Mary Ellen Foster <mefoster at gmail.com> 2.0.1-1
- Update to 2.0.1
- Build with maven

* Wed Aug 19 2009 Andrew Overholt <overholt@redhat.com> 1.4.5-1.2
- Update to 1.4.5 from JPackage and Deepak Bhole
- Remove gcj bits

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.2-2.2
- fix license tag
- drop repotag

* Thu Aug 23 2007 Ralph Apel <r.apel@r-apel.de> - 0:1.4.5-1jpp
- Upgrade to 1.4.5
- Now build with maven2 by default

* Wed Mar 21 2007 Ralph Apel <r.apel@r-apel.de> - 0:1.2-2jpp
- Fix build classpath
- Optionally build with maven2
- Add gcj_support option

* Mon Feb 20 2007 Deepak Bhole <dbhole@redhat.com> - 0:1.2-2jpp.1.fc7
- Fix spec per Fedora guidelines

* Fri Jun 16 2006 Ralph Apel <r.apel@r-apel.de> - 0:1.2-1jpp
- Upgrade to 1.2

* Wed Jan 04 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.0.4-2jpp
- First JPP 1.7 build

* Mon Nov 07 2005 Ralph Apel <r.apel at r-apel.de> - 0:1.0.4-1jpp
- First JPackage build
