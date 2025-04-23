---
title: Wie Aspose.Cells TrueType Fonts verwendet
type: docs
weight: 10
url: /de/java/how-aspose-cells-uses-truetype-fonts/
---

{{% alert color="primary" %}}

Aspose.Cells erfordert TrueType-Schriften beim Rendern von Arbeitsmappen in Formaten wie PDF, XPS und Bildern.

Wenn Aspose.Cells eine Arbeitsmappe rendert, benötigt es Zugriff auf die im Arbeitsblatt verwendeten TrueType-Schriften. Dies ist eine normale Praxis bei der PDF-, XPS- und Bildgenerierung und stellt sicher, dass das konvertierte Dokument oder Bild für jeden Betrachter identisch erscheint.

{{% /alert %}}

## **Über Schriften**

### **Verfügbarkeit und Ersatz von Schriften**

Eine Arbeitsmappe kann mit verschiedenen Schriften formatiert sein, wie Arial, Times New Roman, Verdana und andere. Wenn Aspose.Cells eine Arbeitsmappe rendert, versucht es, die in der Arbeitsmappe verwendeten Schriften auszuwählen. Es gibt jedoch Situationen, in denen die genaue Schriftart möglicherweise nicht verfügbar ist, und Aspose.Cells muss stattdessen eine ähnliche Schriftart verwenden.

Nachfolgend wird der Prozess beschrieben, den Aspose.Cells hinter den Kulissen befolgt.

1. Aspose.Cells versucht, die Schriften im Dateisystem zu finden, die mit dem im Arbeitsblatt verwendeten exakten Schriftnamen übereinstimmen.
1. Wenn Aspose.Cells Schriften mit genau demselben Namen nicht finden kann, versucht es, die Standardschrift zu verwenden, die unter der Eigenschaft DefaultStyle.Font des Arbeitsblatts angegeben ist.
1. Wenn Aspose.Cells die unter der Eigenschaft DefaultStyle.Font des Arbeitsblatts definierte Schriftart nicht finden kann, versucht es, die am besten geeigneten Schriften aus allen verfügbaren Schriften auszuwählen.
1. Schließlich, wenn Aspose.Cells auf dem Dateisystem keine Schriften finden kann, rendert es die Tabellenkalkulation mit Arial.

### **Wo Aspose.Cells nach Schriften sucht**

Aspose.Cells versucht, TrueType-Schriften automatisch auf dem Dateisystem zu finden. In den meisten Fällen können Sie sich auf das Standardverhalten von Aspose.Cells verlassen, um TrueType-Schriften zu finden, aber manchmal müssen Sie möglicherweise Ordner angeben, die die TrueType-Schriften enthalten, indem Sie die Methode FontConfigs.setFontFolder verwenden.

### **Typische Probleme mit Schriften und Lösungen**

In dieser Tabelle werden einige Probleme aufgeführt, die beim Rendern von Tabellenkalkulationen in PDFs mit Aspose.Cells auftreten können, und ihre Lösungen.

{{% alert color="primary" %}}

Beachten Sie beim Kopieren von Schriften, dass die meisten Schriften urheberrechtlich geschützt sind. Suchen Sie zuerst die Lizenz einer Schriftart und prüfen Sie, ob sie frei auf einen anderen Computer übertragen werden kann. 

{{% /alert %}}

|**Problem** |**Grund** |**Lösung** |
| :- | :- | :- |
|Das Layout und die Schriftarten im gerenderten Dokument unterscheiden sich vom Original. |Sie verwenden Aspose.Cells auf Linux oder Mac OS, wo TrueType-Schriftarten standardmäßig nicht vorhanden sind, daher kann Aspose.Cells keine Schriften auf Ihrem Computer finden. |Kopieren Sie TrueType-Schriftdateien von einem Windows-Computer oder installieren Sie ein TrueType-Schriftarten-Paket. Verwenden Sie die Methode FontConfigs.setFontFolder, um den Speicherort der Schriftdateien anzugeben.|

{{% alert color="primary" %}}

Überprüfen Sie die ausführlichen Artikel zu

- [Verwendung von TrueType-Schriften unter Linux](/cells/de/java/how-to-install-truetype-fonts-on-linux/).
- [Angabe des Speicherorts von TrueType-Schriften](/cells/de/java/how-to-specify-truetype-fonts-location/).
- [Wie Sie Warnungen erhalten, wenn eine Schriftarten-Substitution auftritt](/cells/de/java/get-warnings-for-font-substitution-while-rendering-excel-file/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
