---
title: Berechnung der IFNA Funktion mit Python.NET unter Verwendung von Aspose.Cells
linktitle: Berechnung der IFNA Funktion
type: docs
weight: 40
url: /de/python-net/calculating-ifna-function-using-aspose-cells/
description: Erfahren Sie, wie Sie die IFNA Funktion in Excel Dateien mit Aspose.Cells for Python.NET berechnen. Fehler #N/A behandeln und modifizierte Tabellen effizient speichern.
keywords: Python.NET, Excel, IFNA Funktion, Aspose.Cells, Fehlerbehandlung, Tabellenberechnung
---

{{% alert color="primary" %}}

Aspose.Cells für Python.NET unterstützt die Berechnung der Excel-Funktion IFNA. Die Funktion gibt einen bestimmten Wert zurück, wenn eine Formel einen #N/A-Fehler ergibt; ansonsten liefert sie das Ergebnis der Formel.

{{% /alert %}}

## **Berechnung der IFNA-Funktion in Python.NET**

Das folgende Code-Beispiel demonstriert, wie die IFNA-Funktion mit Aspose.Cells für Python.NET berechnet wird:


## **Konsolenausgabe**
Der obige Code gibt die folgende Konsolenausgabe aus:

```
Not found
Orange
```

## **Schlüssel-Schritte-Erklärung**
1. Erstellen Sie eine neue [`Workbook`](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) Instanz
2. Zugriff auf das Arbeitsblatt und die Zellsammlung
3. Quell-Daten in Spalte A ausfüllen
4. VLOOKUP-Formeln setzen, die #N/A-Fehler erzeugen können
5. Verwenden Sie IFNA, um potenzielle Fehler zu behandeln
6. Formeln mit [`calculate_formula()`](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) berechnen
7. Ergebnisse aus Fehler-behandelten Zellen abrufen und anzeigen
8. Modifizierte Arbeitsmappe mit Berechnungsergebnissen speichern

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Add data for VLOOKUP
cells = worksheet.cells
cells.get("A1").put_value("Apple")
cells.get("A2").put_value("Orange")
cells.get("A3").put_value("Banana")

# Access cell A5 and A6
cell_a5 = worksheet.cells.get("A5")
cell_a6 = worksheet.cells.get("A6")

# Assign IFNA formula to A5 and A6
cell_a5.formula = "=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")"
cell_a6.formula = "=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")"

# Calculate the formula of workbook
workbook.calculate_formula()

# Print the values of A5 and A6
print(cell_a5.string_value)
print(cell_a6.string_value)
```
{{< app/cells/assistant language="python-net" >}}
