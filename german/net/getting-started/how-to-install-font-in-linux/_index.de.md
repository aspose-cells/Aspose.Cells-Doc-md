---
title: Wie installiert man Schriftarten in Linux
type: docs
description: "Wie installiert man Schriftarten in Linux"
weight: 139
url: /de/net/how-to-install-font-in-linux/
---

## Übersicht

Wenn Sie Aspose.Cells in Linux verwenden, da Linux weniger Standard-Schriftarten hat, ist die in Ihrer Excel-Datei referenzierte Schriftart möglicherweise standardmäßig auf Ihrem Linux-System nicht vorhanden.
Wenn dies passiert, verwendet Aspose.Cells stattdessen eine ähnliche Schriftart, um die Zeichen anzuzeigen. Dies kann jedoch folgende Auswirkungen haben:

1. Verschiedene Schriftarten können dazu führen, dass Bilder in unterschiedlichen Layouts gerendert werden als in Excel.
2. Da sich die Schriftart geändert hat, entsprechen die ausgegebenen Zeichen möglicherweise nicht Ihren Erwartungen.

Damit Ihr Programm genauere Ergebnisse liefert, installieren Sie die benötigten Schriftarten unter Linux. Es ist wichtig sicherzustellen, dass die Schriftarten, die Sie in Excel-Dateien verwenden, in Ihrer Umgebung vorhanden sind.

## Wie installiert man Schriftarten in Linux

Es gibt zwei Möglichkeiten, Schriftarten unter Linux zu installieren, wie unten beschrieben:

### Kopieren Sie die Schriftdateien in den Linux-Systempfad

1. Legen Sie einen Ordner namens "fonts" in Ihr Programmverzeichnis, kopieren Sie die benötigten Schriftdateien in diesen Ordner.
2. Fügen Sie den folgenden Befehl zu Ihrer Linux-Dockerfile hinzu:
```
COPY fonts/ /usr/share/fonts
```
3. Nach der oben genannten Operation werden die Schriftdateien in den Linux-Systempfad kopiert. Aspose.Cells greift auf den Systempfad zu, um sie zu finden und zu verwenden. Dies ist unser empfohlener Szenario.

### Schriftart-Ordner mit Aspose.Cells API festlegen
In einigen Fällen können Sie den Linux-Systemordner nicht kontrollieren oder modifizieren, zum Beispiel auf Cloud-Servern. In diesem Fall können Sie das zweite Szenario verwenden.
1. Legen Sie einen Ordner namens "fonts" in Ihr Programmverzeichnis, kopieren Sie die benötigten Schriftdateien in diesen Ordner.
2. Rufen Sie in Ihrem Programmcode die Aspose.Cells API auf:
```
Aspose.Cells.FontConfigs.SetFontFolder("fonts", true);
```
3. Die oben genannte Operation stellt sicher, dass das Programm die Schriftart vom Projektpfad aus finden kann.

## Siehe auch

- [So führen Sie Aspose.Cells für .Net6 aus](https://docs.aspose.com/cells/net/how-to-run-aspose-cells-for-net6/)

{{< app/cells/assistant language="csharp" >}}
