---
title: Wie man ein Arbeitsblatt mit Python.NET skaliert
linktitle: So skalieren Sie ein Arbeitsblatt
type: docs
weight: 130
url: /de/python-net/how-to-scale-a-worksheet/
description: Dieser Artikel erklärt, wie man ein Arbeitsblatt mit Aspose.Cells für Python.NET skaliert.
keywords: Python Arbeitsblatt skalieren, Arbeitsblatt mit Python.NET skalieren, In Python auf Seite anpassen, Prozentuale Skalierung eines Arbeitsblatts mit Python, Aspose.Cells Python Arbeitsblattskalierung.
---

## **Mögliche Verwendungsszenarien**
Das Skalieren eines Arbeitsblatts kann aus verschiedenen Gründen nützlich sein, abhängig vom Kontext, in dem Sie arbeiten. Hier sind einige häufige Gründe für das Skalieren eines Arbeitsblatts:
1. **Auf Seite anpassen**: Damit alle Inhalte beim Drucken auf eine Seite oder eine bestimmte Anzahl von Seiten passen.
1. **Präsentation**: Um organisierte und professionell aussehende Arbeitsblätter für die Weitergabe zu erstellen.
1. **Lesbarkeit**: Um Text- und Elementgrößen für eine bessere visuelle Zugänglichkeit anzupassen.
1. **Raumverwaltung**: Um das Arbeitsblattlayout zu optimieren und unnötigen Leerraum zu minimieren.
1. **Datenvisualisierung**: Um Diagramme und Grafiken innerhalb des verfügbaren Raums richtig zu skalieren.
1. **Konsistenz**: Um ein einheitliches Erscheinungsbild in mehreren Arbeitsblättern oder Dokumenten zu gewährleisten.

## **Wie man ein Arbeitsblatt in Excel skaliert**
Das Skalieren eines Arbeitsblatts in Excel hilft, Inhalte beim Drucken auf bestimmte Seiten anzupassen. Folgen Sie diesen Schritten:

1. Öffnen Sie Ihre Tabelle in Excel
1. Navigieren Sie zu **Seitenlayout** > **Skalieren auf Seite**
1. Passen Sie **Breite** und **Höhe** an, um die Seitenzahlanforderungen zu erfüllen
1. Falls erforderlich, benutzerdefinierte Skalierungsprozentsätze einstellen
<br>
<img src="1.png" width=60% />

## **Wie man ein Arbeitsblatt mit Python.NET skaliert**
Aspose.Cells für Python.NET bietet umfassende Möglichkeiten zur Skalierung von Arbeitsblättern. Verwenden Sie diese Ansätze, um Arbeitsblätter programmatisch zu skalieren:

### **Beispiel für Seitenanpassung**
Druckeinstellungen anpassen, um Inhalte auf bestimmte Seiten anzupassen:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the worksheet to fit to 1 page wide and 1 page tall
page_setup.fit_to_pages_wide = 1
page_setup.fit_to_pages_tall = 1

# Save the modified workbook
workbook.save("output_fit_to_page.xlsx")
```
<br>
<img src="3.png" width=60% />

### **Beispiel für Skalieren auf Prozentsatz**
Benutzerdefinierten Skalierungsprozentsatz auf Arbeitsblattinhalte anwenden:
```python
from aspose.cells import Workbook

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Access the PageSetup object
page_setup = sheet.page_setup

# Set the scaling to a specific percentage (e.g., 75%)
page_setup.zoom = 75

# Save the modified workbook
workbook.save("output_scaled_percentage.xlsx")
```
<br>
<img src="2.png" width=60% />

**Wichtige API-Referenzen:**
- [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) Klasse
- [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/) Klasse
- [**PageSetup**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/) Konfiguration
{{< app/cells/assistant language="python-net" >}}
