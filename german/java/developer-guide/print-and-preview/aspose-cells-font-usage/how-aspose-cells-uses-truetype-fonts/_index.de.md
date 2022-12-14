---
title: Wie Aspose.Cells TrueType-Schriftarten verwendet
type: docs
weight: 10
url: /de/java/how-aspose-cells-uses-truetype-fonts/
---
{{% alert color="primary" %}}

Aspose.Cells erfordert TrueType-Schriftarten beim Rendern von Tabellenkalkulationen in Formate wie PDF, XPS und Bilder.

Wenn Aspose.Cells eine Tabellenkalkulation rendert, benötigt es Zugriff auf die TrueType-Schriftarten, die in der Tabellenkalkulation verwendet werden. Dies ist eine normale Vorgehensweise bei der PDF-, XPS- und Bildgenerierung und stellt sicher, dass das konvertierte Dokument oder Bild für jeden Betrachter identisch erscheint.

{{% /alert %}}

## **Über Schriftarten**

### **Verfügbarkeit und Substitution von Schriftarten**

Eine Tabelle kann mit verschiedenen Schriftarten wie Arial, Times New Roman, Verdana und anderen formatiert werden. Wenn Aspose.Cells eine Tabelle rendert, versucht es, die Schriftarten auszuwählen, die in der Tabelle verwendet werden. Es gibt jedoch Situationen, in denen die genaue Schriftart möglicherweise nicht verfügbar ist, sodass Aspose.Cells stattdessen eine ähnliche Schriftart ersetzen muss.

Unten ist der Prozess, den Aspose.Cells hinter den Kulissen verfolgt.

1. Aspose.Cells versucht, die Schriftarten im Dateisystem zu finden, die genau mit dem in der Tabelle verwendeten Schriftartnamen übereinstimmen.
1. Wenn Aspose.Cells keine Schriftarten mit genau demselben Namen finden kann, versucht es, die Standardschriftart zu verwenden, die unter der DefaultStyle.Font-Eigenschaft der Arbeitsmappe angegeben ist.
1. Wenn Aspose.Cells die unter der DefaultStyle.Font-Eigenschaft der Arbeitsmappe definierte Schriftart nicht finden kann, versucht es, die am besten geeigneten Schriftarten aus allen verfügbaren Schriftarten auszuwählen.
1. Wenn schließlich Aspose.Cells keine Schriftarten im Dateisystem finden kann, wird die Tabelle mit Arial gerendert.

### **Wobei Aspose.Cells nach Schriftarten sucht**

Aspose.Cells versucht, TrueType-Schriftarten automatisch im Dateisystem zu finden. Meistens können Sie sich auf das Standardverhalten von Aspose.Cell verlassen, um TrueType-Schriftarten zu finden, aber manchmal müssen Sie möglicherweise Ordner angeben, die die TrueType-Schriftarten enthalten, indem Sie die Factory-Methode FontConfigs.setFontFolder verwenden.

### **Typische schriftbezogene Probleme und Lösungen**

In dieser Tabelle sind einige der Probleme aufgeführt, die beim Rendern von Tabellenkalkulationen in PDF mit Aspose.Cells auftreten können, sowie deren Lösungen.

{{% alert color="primary" %}}

 Denken Sie beim Kopieren von Schriftarten daran, dass die meisten Schriftarten urheberrechtlich geschützt sind. Suchen Sie zunächst die Lizenz einer Schriftart und überprüfen Sie, ob sie frei auf einen anderen Computer übertragen werden kann.

{{% /alert %}}

|**Problem** |**Grund** |**Lösung** |
|:- |:- |:- |
| Das Layout und die Schriftarten im gerenderten Dokument unterscheiden sich vom Original.| Sie verwenden Aspose.Cells unter Linux oder Mac OS, wo TureType-Schriftarten standardmäßig nicht vorhanden sind, sodass Aspose.Cells keine Schriftarten auf Ihrem Computer finden kann.|Kopieren Sie TrueType-Schriftartdateien von einem Windows-Rechner oder installieren Sie ein TrueType-Schriftartpaket. Verwenden Sie die Factory-Methode FontConfigs.setFontFolder, um den Speicherort der Schriftartdateien anzugeben.|

{{% alert color="primary" %}}

Überprüfen Sie die ausführlichen Artikel auf

- [So platzieren Sie TrueType-Schriftarten unter Linux](/cells/de/java/how-to-install-truetype-fonts-on-linux/).
- [So geben Sie den Speicherort für TrueType-Schriftarten an](/cells/de/java/how-to-specify-truetype-fonts-location/).
- [So erhalten Sie Warnungen, wenn eine Schriftartersetzung auftritt](/cells/de/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
