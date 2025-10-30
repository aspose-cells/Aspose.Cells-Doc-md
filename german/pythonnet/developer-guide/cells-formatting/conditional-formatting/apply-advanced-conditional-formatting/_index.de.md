---
title: Erweiterte bedingte Formatierung mit Python.NET anwenden
linktitle: Anwendung fortgeschrittener bedingter Formatierung
type: docs
weight: 70
url: /de/python-net/apply-advanced-conditional-formatting/
description: Erfahren Sie, wie Sie die erweiterten bedingten Formatierungsfunktionen von Excel wie Datenbalken, Farbskalen und Iconsets mit Aspose.Cells für Python via .NET implementieren.
keywords: Python Excel Formatierung, Bedingte Formatierung Python, Datenbalken Python, Farbskalen Python, Iconsets Python, Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 und neuere Versionen (2010/2013/2016) bieten erweiterte bedingte Formatierungsfunktionen, einschließlich Zellhinterlegung, Rahmen, farbige Symbole, Pfeile, Flags und Schriftformatierung.

{{% /alert %}} 

## **Erweiterte bedingte Formatierung in Excel-Dateien implementieren**
Aspose.Cells für Python via .NET unterstützt alle erweiterten bedingten Formatierungsfunktionen, einschließlich:

- Schattierte Datenbalken hinzufügen, um die zugrunde liegenden Zahlen graphisch zu verbessern, indem ein einfacher Balkendiagramm in den Zellen eingebettet wird.
- Zellen automatisch mit Farbskalen schattieren, basierend auf ihrer Beziehung zu Werten in anderen Zellen im Bereich. Die Standardeinstellungen schattieren den niedrigsten Wert in Rot und bewegen sich zum höchsten Wert in Grün.
- Iconsets ähnlich wie Farbskalen verwenden, jedoch anstatt der Schattierung der Zellen kleine Symbole wie Pfeile und Ampeln hinzufügen.

Aspose.Cells unterstützt die bedingte Formatierung von Microsoft Excel 2007 und späteren Versionen im XLSX-Format auf Zellen zur Laufzeit vollständig. Dieses Beispiel zeigt eine Übung für fortgeschrittene bedingte Formatierungstypen, einschließlich Symbolsets, Datenbalken, Farbskalen, Zeitperioden, Top/Bottom und anderen Regeln mit verschiedenen Attributmengen.

- [**Adding Color Scale Conditional Formattings**](/cells/de/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/de/python-net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/de/python-net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/de/python-net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/de/python-net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/de/python-net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/de/python-net/how-to-add-top10-conditional-formatting/)



### **Berechnung der Excel-Farbenauswahl für die Farbskalen-Formatierung**
Dieser Code zeigt, wie man in Excel die für die Farbskalenkriterien gewählte Farbe bestimmt:

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
{{< app/cells/assistant language="python-net" >}}
