---
title: Hur man installerar TrueType-teckensnitt på Linux
type: docs
weight: 20
url: /sv/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

Det mest troliga scenariot är att du använder Aspose.Cells för att konvertera kalkylblad till PDF. Om du gör detta på ett icke-Windows-baserat operativsystem som Linux så förklarar det här avsnittet hur du säkerställer att Aspose.Cells renderar dina kalkylblad med bästa noggrannhet.

För att se till att kalkylblad som konverterats av Aspose.Cells visas så nära originalet som möjligt kan du behöva installera "Windows fonts" eller "TrueType fonts" på ditt Linux-system eftersom de vanligaste TrueType-teckensnitten inte kommer förinstallerade med Linux-distributioner som standard.

Det finns två huvudsakliga sätt att få TrueType-teckensnitt på ett Linux-system:

1. Kopiera teckensnittsfiler (.TTF och .TTC) från en Windows-maskin till din Linux-maskin.
1. Installera ett TrueType-teckensnittspaket, till exempel msttcorefonts.

{{% /alert %}}

## **Kopiera teckensnitt från en Windows-maskin**

Ett enkelt och snabbt sätt är att kopiera .TTF- och .TTC-filer från katalogen C:\Windows\Fonts på en Windows-maskin till någon katalog på din Linux-maskin. Du behöver inte installera eller registrera dessa typsnitt på Linux på något sätt, du behöver bara ange platsen för teckensnitten med FontConfigs.setFontFolder-metoden i din applikation.

{{% alert color="primary" %}}

Så vitt vi kan säga licensierar Microsoft typsnitten så att vem som helst kan använda dem fritt, men kontrollera typsnittslicensen själv.

{{% /alert %}}

## **Installera ett TrueType-teckensnittspaket**

Nedan tillhandahållen information guidar dig steg för steg för att installera Microsoft:s mest kända TrueType-teckensnitt på Linux-distributioner som Fedora och Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Du kan kräva "root"-nivåprivilegier och logga därför in som "root" eller konfigurera sudo.

{{% /alert %}}

Så här gör du med terminalen.

1. Se till att du har följande RPM-paket installerade.
   1. **rpm-bygga**: Om det inte är installerat, använd följande kommando för att installera paketet rpm-build

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Om den inte är installerad, använd följande kommando

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. Ladda ner den senaste msttcorefonts spec-filen från SourceForge med kommandot som följer,

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Bygg en RPM-fil med den tidigare nedladdade spec-filen och följande kommando,

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. RPM-filen kommer att lagras i: /root/rpmbuild/RPMS/noarch/, installera den enligt följande,

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Starta om maskinen så att ändringarna träder i kraft.

Instruktionerna ovan kommer att installera Microsoft TTFs-paketet inklusive följande teckensnittsfamiljer:

1. Andale Mono
1. Arial Black/Arial (fet, kursiv, fet kursiv)
1. Comic Sans MS (fet)
1. Courier New (fet, kursiv, fet kursiv)
1. Georgien (fet, kursiv, fet kursiv)
1. Påverkan
1. Tahoma
1. Times New Roman (fet, kursiv, fet kursiv)
1. Trebuchet (fet, kursiv, fet kursiv)
1. Verdana (fet, kursiv, fet kursiv)
1. Webbningar

{{% alert color="primary" %}}

 På Ubuntu, gå till Synaptic Package Manager. Hitta och installera**ttf-mscorefonts-installer** paket.

{{% /alert %}}
