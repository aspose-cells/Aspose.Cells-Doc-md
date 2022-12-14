---
title: So installieren Sie TrueType-Schriftarten unter Linux
type: docs
weight: 20
url: /de/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

Das wahrscheinlichste Szenario ist, dass Sie Aspose.Cells verwenden, um Tabellenkalkulationen in PDF zu konvertieren. Wenn Sie dies auf einem nicht auf Windows basierenden Betriebssystem wie Linux tun, wird in diesem Thema erläutert, wie Sie sicherstellen können, dass Aspose.Cells Ihre Tabellenkalkulationen mit bester Wiedergabetreue rendert.

Um sicherzustellen, dass mit Aspose.Cells konvertierte Tabellenkalkulationen so originalgetreu wie möglich erscheinen, müssen Sie möglicherweise „Windows-Schriftarten“ oder „TrueType-Schriftarten“ auf Ihrem Linux-System installieren, da die am häufigsten verwendeten TrueType-Schriftarten nicht vorinstalliert sind Linux-Distributionen standardmäßig.

Es gibt zwei Möglichkeiten, TrueType-Schriftarten auf einem Linux-System zu erhalten:

1. Kopieren Sie Schriftdateien (.TTF und .TTC) von einem Windows-Rechner auf Ihren Linux-Rechner.
1. Installieren Sie ein Paket mit TrueType-Schriftarten, z. B. msttcorefonts.

{{% /alert %}}

## **Kopieren Sie Schriftarten von einer Windows-Maschine**

Eine einfache und schnelle Möglichkeit besteht darin, .TTF- und .TTC-Dateien aus dem Verzeichnis C:\Windows\Fonts auf einem Windows-Rechner in ein Verzeichnis auf Ihrem Linux-Rechner zu kopieren. Sie müssen diese Schriftarten in keiner Weise unter Linux installieren oder registrieren, Sie müssen lediglich den Speicherort der Schriftarten mithilfe der Methode FontConfigs.setFontFolder in Ihrer Anwendung angeben.

{{% alert color="primary" %}}

Soweit wir das beurteilen können, lizenziert Microsoft die Schriftarten für jedermann zur freien Verwendung, aber überprüfen Sie die Schriftartlizenzierung bitte selbst.

{{% /alert %}}

## **Installieren Sie ein Paket mit TrueType-Schriftarten**

Die nachstehenden Informationen führen Sie Schritt für Schritt durch die Installation der bekanntesten TrueType-Schriftarten von Microsoft auf Linux-Distributionen wie Fedora und Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Möglicherweise benötigen Sie Berechtigungen auf „Root“-Ebene, melden Sie sich daher als „Root“ an oder lassen Sie sudo konfigurieren.

{{% /alert %}}

Hier erfahren Sie, wie Sie dies mit dem Terminal tun.

1. Stellen Sie sicher, dass die folgenden RPM-Pakete installiert sind.
   1. **rpm-Build**: Wenn es nicht installiert ist, verwenden Sie den folgenden Befehl, um das Paket rpm-build zu installieren

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Wenn nicht installiert, verwenden Sie den folgenden Befehl

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. Laden Sie die neueste msttcorefonts-Spezifikationsdatei von SourceForge mit dem folgenden Befehl herunter:

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Erstellen Sie eine RPM-Datei mit der zuvor heruntergeladenen Spezifikationsdatei und dem folgenden Befehl:

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Die RPM-Datei wird gespeichert in: /root/rpmbuild/RPMS/noarch/, installieren Sie sie wie folgt,

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Starten Sie den Computer neu, damit die Änderungen wirksam werden.

Die oben bereitgestellten Anweisungen installieren das Microsoft TTFs-Paket einschließlich der folgenden Schriftfamilien:

1. Andale Mono
1. Arial Schwarz/Arial (fett, kursiv, fett kursiv)
1. Comic Sans MS (fett)
1. Kurier Neu (Fett, Kursiv, Fett Kursiv)
1. Georgien (fett, kursiv, fett kursiv)
1. Einfluss
1. Tahoma
1. Times New Roman (fett, kursiv, fett kursiv)
1. Trebuchet (fett, kursiv, fett kursiv)
1. Verdana (fett, kursiv, fett kursiv)
1. Webdings

{{% alert color="primary" %}}

 Gehen Sie unter Ubuntu zum Synaptic Package Manager. Suchen und installieren Sie die**ttf-mscorefonts-installer** Paket.

{{% /alert %}}
