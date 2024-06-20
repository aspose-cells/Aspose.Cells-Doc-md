---
title: Anwendung fortgeschrittener bedingter Formatierung
description: Wie Sie die Aspose.Cells Bibliothek in C# verwenden, um fortgeschrittene bedingte Formatierung anzuwenden. Durch Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Fortgeschrittene Bedingte Formatierung, C#, Bedingte, Formatierung
type: docs
weight: 70
url: /de/net/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 und spätere Versionen (2010/2013/2016) bieten einige fortgeschrittene Funktionen für bedingte Formatierung. Zum Beispiel können Sie Zellenschattierung, Rahmen, farbige Symbole, Pfeile, Flaggen und Schriftformatierungen anwenden, was ziemlich anspruchsvoll geworden ist.

{{% /alert %}} 
## **Fortgeschrittene bedingte Formatierung auf Microsoft Excel-Dateien anwenden**
Bedingte Formatierung kann:

- Schattierte Datenbalken hinzufügen, um die zugrunde liegenden Zahlen graphisch zu verbessern, indem ein einfacher Balkendiagramm in den Zellen eingebettet wird.
- Zellen automatisch mit Farbskalen schattieren, basierend auf ihrer Beziehung zu Werten in anderen Zellen im Bereich. Die Standardeinstellungen schattieren den niedrigsten Wert in Rot und bewegen sich zum höchsten Wert in Grün.
- Iconsets ähnlich wie Farbskalen verwenden, jedoch anstatt der Schattierung der Zellen kleine Symbole wie Pfeile und Ampeln hinzufügen.

Aspose.Cells unterstützt die bedingte Formatierung von Microsoft Excel 2007 und späteren Versionen im XLSX-Format auf Zellen zur Laufzeit vollständig. Dieses Beispiel zeigt eine Übung für fortgeschrittene bedingte Formatierungstypen, einschließlich Symbolsets, Datenbalken, Farbskalen, Zeitperioden, Top/Bottom und anderen Regeln mit verschiedenen Attributmengen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormatting-1.cs" >}}
### **Berechnen der vom Microsoft Excel für bedingte Farbskalen ausgewählten Farbe**
Aspose.Cells bietet Ihnen die Möglichkeit, die Farbe zu berechnen, die von Microsoft Excel ausgewählt wurde, wenn die bedingte Farbskalenformatierung in einer Vorlagendatei verwendet wird. Sehen Sie sich den folgenden Beispielcode an, um zu erfahren, wie die Farbe berechnet wird, die von Microsoft Excel ausgewählt wurde.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
