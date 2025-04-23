---
title: Wie man TrueType Schriftarten auf Linux installiert
type: docs
weight: 20
url: /de/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

Das wahrscheinlichste Szenario ist, dass Sie Aspose.Cells verwenden, um Tabellenkalkulationen in PDFs zu konvertieren. Wenn Sie dies auf einem nicht auf Windows basierenden Betriebssystem wie Linux tun, erklärt dieses Thema, wie sichergestellt werden kann, dass Aspose.Cells Ihre Tabellenkalkulationen mit bestmöglicher Genauigkeit rendert.

Um sicherzustellen, dass von Aspose.Cells konvertierte Tabellenkalkulationen so nah wie möglich am Original erscheinen, müssen Sie möglicherweise "Windows-Schriften" oder "TrueType-Schriften" auf Ihrem Linux-System installieren, da die am häufigsten verwendeten TrueType-Schriften standardmäßig nicht mit Linux-Distributionen installiert sind.

Es gibt zwei Hauptmöglichkeiten, TrueType-Schriften auf einem Linux-System zu erhalten:

1. Kopieren Sie Schriftdateien (.TTF und .TTC) von einem Windows-Computer auf Ihren Linux-Computer.
1. Installieren Sie ein TrueType-Schriften-Paket, wie z.B. msttcorefonts.

{{% /alert %}}

## **Schriftarten von einem Windows-Computer kopieren**

Ein einfacher und schneller Weg ist, die .TTF- und .TTC-Dateien aus dem Verzeichnis C:\Windows\Fonts auf einem Windows-Computer in ein Verzeichnis auf Ihrem Linux-Computer zu kopieren. Sie müssen diese Schriftarten auf Linux nicht installieren oder registrieren, sondern müssen nur den Speicherort der Schriftarten in Ihrer Anwendung mit der Methode FontConfigs.setFontFolder angeben.

{{% alert color="primary" %}}

Nach unseren Informationen lizenziert Microsoft die Schriftarten für jeden zur freien Verwendung, aber bitte überprüfen Sie die Schriftartenlizenzierung selbst.

{{% /alert %}}

## **Installieren eines TrueType-Schriftartenpakets**

Die unten bereitgestellten Informationen führen Sie Schritt für Schritt durch die Installation der bekanntesten TrueType-Schriften von Microsoft auf Linux-Distributionen wie Fedora und Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

Möglicherweise benötigen Sie Root-Berechtigungen. Melden Sie sich daher als 'root' an oder konfigurieren Sie 'sudo'.

{{% /alert %}}

So geht's mit dem Terminal.

1. Stellen Sie sicher, dass Sie die folgenden RPM-Pakete installiert haben.
   1. **rpm-build**: Wenn nicht installiert, verwenden Sie folgenden Befehl, um das Paket rpm-build zu installieren.

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: Wenn nicht installiert, verwenden Sie folgenden Befehl.

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. Laden Sie die neueste msttcorefonts Spec-Datei von SourceForge mit folgendem Befehl herunter.

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Erstellen Sie eine RPM-Datei mit der zuvor heruntergeladenen Spec-Datei und folgendem Befehl.

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. Die RPM-Datei wird gespeichert in: /root/rpmbuild/RPMS/noarch/, installieren Sie sie wie folgt.

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. Starten Sie den Computer neu, um die Änderungen wirksam werden zu lassen.

Die oben bereitgestellten Anweisungen installieren das Microsoft TTFs-Paket, einschließlich der folgenden Schriftfamilien.

1. Andale Mono
1. Arial Black/Arial (Fett, Kursiv, Fett Kursiv)
1. Comic Sans MS (Fett)
1. Courier New (Fett, Kursiv, Fett Kursiv)
1. Georgia (Fett, Kursiv, Fett Kursiv)
1. Impact
1. Tahoma
1. Times New Roman (Fett, Kursiv, Fett Kursiv)
1. Trebuchet (Fett, Kursiv, Fett Kursiv)
1. Verdana (Fett, Kursiv, Fett Kursiv)
1. Webdings

{{% alert color="primary" %}}

Auf Ubuntu, gehen Sie zum Synaptic Package Manager. Finden Sie das **ttf-mscorefonts-installer** Paket und installieren Sie es.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
