---
title: Anwenden erweiterter bedingter Formatierungen mit C++
linktitle: Anwendung fortgeschrittener bedingter Formatierung
description: So verwenden Sie die Aspose.Cells Bibliothek in C++, um erweiterte bedingte Formatierungen anzuwenden. Durch die Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Erweiterte bedingte Formatierung, C++, Bedingung, Formatierung
type: docs
weight: 70
url: /de/cpp/apply-advanced-conditional-formatting/
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

### **Berechnen der vom Microsoft Excel für bedingte Farbskalen ausgewählten Farbe**
Aspose.Cells bietet Ihnen die Möglichkeit, die Farbe zu berechnen, die von Microsoft Excel ausgewählt wurde, wenn die bedingte Farbskalenformatierung in einer Vorlagendatei verwendet wird. Sehen Sie sich den folgenden Beispielcode an, um zu erfahren, wie die Farbe berechnet wird, die von Microsoft Excel ausgewählt wurde.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate a workbook object and open the template file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell a1 = worksheet.GetCells().Get(u"A1");

    // Get the conditional formatting resultant object
    ConditionalFormattingResult cfr1 = a1.GetConditionalFormattingResult();

    // Get the ColorScale resultant color object
    Aspose::Cells::Color c = cfr1.GetColorScaleResult();

    Aspose::Cells::Cleanup();
}
```
