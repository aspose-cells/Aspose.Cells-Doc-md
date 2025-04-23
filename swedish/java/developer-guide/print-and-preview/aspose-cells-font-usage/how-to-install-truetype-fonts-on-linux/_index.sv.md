---
title: Hur du installerar TrueType typsnitt på Linux
type: docs
weight: 20
url: /sv/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

Det mest troliga scenariot är att du använder Aspose.Cells för att konvertera kalkylblad till PDF. Om du gör detta på ett operativsystem som inte är Windows, som Linux, förklarar detta ämne hur du ser till att Aspose.Cells renderar dina kalkylblad med bästa möjliga noggrannhet.

För att säkerställa att kalkylblad konverterade av Aspose.Cells visas så lika originalet som möjligt kan du behöva installera "Windows-typsnitt" eller "TrueType-typsnitt" på ditt Linux-system eftersom de mest använda TrueType-typsnitten inte är förinstallerade med Linux-distributioner som standard.

Det finns två huvudsakliga sätt att få TrueType-typsnitt på ett Linux-system:

1. Kopiera typsnittsfiler (.TTF och .TTC) från en Windows-dator till din Linux-dator.
1. Installera ett TrueType-typsnittspaket, som msttcorefonts.

{{% /alert %}}

## **Kopiera typsnitt från en Windows-maskin**

Ett enkelt och snabbt sätt är att kopiera .TTF- och .TTC-filer från katalogen C:\Windows\Fonts på en Windows-maskin till en katalog på din Linux-maskin. Du behöver inte installera eller registrera dessa typsnitt på Linux på något sätt, du behöver bara ange platsen för typsnitten med hjälp av metoden FontConfigs.setFontFolder i din applikation.

{{% alert color="primary" %}}

Såvitt vi vet licensierar Microsoft typsnitten för alla att använda dem fritt, men kontrollera gärna typsnittens licenser själv.

{{% /alert %}}

## **Installera ett TrueType-typsnittspaket**

Nedanstående information kommer att guida dig steg för steg för att installera Microsofts mest kända TrueType-typsnitt på Linux-distributioner som Fedora och Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Du kan behöva 'root'-behörigheter, logga in som 'root' eller konfigurera sudo.

{{% /alert %}}

Så här gör du det med Terminalen.

1. Se till att du har följande RPM-paket installerade.
   1. **rpm-build**: Om det inte är installerat, använd följande kommando för att installera rpm-build-paketet.

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Om det inte är installerat, använd följande kommando

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. Ladda ner den senaste spec-filen för msttcorefonts från SourceForge med följande kommando.

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Bygg en RPM-fil med den tidigare nedladdade spec-filen och följande kommando.

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. RPM-filen kommer att sparas i: /root/rpmbuild/RPMS/noarch/, installera den med följande kommando.

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Starta om datorn för att ändringarna ska träda i kraft.

Anvisningarna ovan kommer att installera Microsoft TTF-paketet, inklusive följande typsnittsfamiljer:

1. Andale Mono
1. Arial Black/Arial (Fetstil, Kursiv, Fetstil Kursiv)
1. Comic Sans MS (Fetstil)
1. Courier New (Fetstil, Kursiv, Fetstil Kursiv)
1. Georgia (Fetstil, Kursiv, Fetstil Kursiv)
1. Impact
1. Tahoma
1. Times New Roman (Fetstil, Kursiv, Fetstil Kursiv)
1. Trebuchet (Fetstil, Kursiv, Fetstil Kursiv)
1. Verdana (Fetstil, Kursiv, Fetstil Kursiv)
1. Webdings

{{% alert color="primary" %}}

På Ubuntu, gå till Synaptic Package Manager. Hitta och installera **ttf-mscorefonts-installer**-paketet.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
