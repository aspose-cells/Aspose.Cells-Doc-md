---
title: Druckbereich mit Python.NET festlegen
linktitle: So legen Sie den Druckbereich fest
type: docs
weight: 200
url: /de/python-net/how-to-set-print-area/
description: Erfahren Sie, wie Sie mit Aspose.Cells für Python via .NET Druckbereiche in Excel Dateien festlegen und löschen.
keywords: Python Druckbereich festlegen, Druckbereich löschen, Excel Druckeinstellungen in Python, Aspose.Cells Python Druckbereich, Limitierung des Druckbereichs in Python
---

## **Mögliche Verwendungsszenarien**

Das Festlegen eines Druckbereichs in einem Dokument hilft, den gedruckten Inhalt zu steuern. Hauptgründe sind:

1. Fokus auf bestimmte Daten: Nur relevante Abschnitte drucken
1. Verbesserte Layout: Inhalte ordentlich auf Seiten anordnen
1. Ressourcen sparen: Papier- und Tintenverbrauch reduzieren
1. Professionelle Präsentation: Gepflegtes Ergebnis sicherstellen
1. Konsistenz: Einheitliche Druckausgaben beibehalten

## **So legen Sie den Druckbereich in Excel fest**

Um einen Druckbereich programmatisch festzulegen:

1. Zugriff auf die Seiten-setup-Eigenschaften des Arbeitsblatts
1. Druckbereich mit Zellbereichsnotation definieren
Arbeitsmappe speichern

```python
# Sample image reference remains unchanged
<img src="3.png" width=60% />
```

## **So entfernen Sie den Druckbereich in Excel**

Um Druckbereichsbeschränkungen zu entfernen:

Seitenlayout-Eigenschaften aufrufen
Druckbereich auf leeren String zurücksetzen
Änderungen speichern

```python
# Sample image reference remains unchanged
<img src="4.png" width=60% />
```

## **Was passiert nach dem Entfernen des Druckbereichs**

Das Löschen des Druckbereichs führt zu:

Standardmäßiger Druck des gesamten Arbeitsblatts
Entfernung vorheriger Bereichsbeschränkungen
Einschluss aller formatierten Zellen

## **So legen Sie den Druckbereich mit Aspose.Cells fest**

Druckbereich über Seitenlayout des Arbeitsblatts festlegen:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set print area to A1:D10
worksheet.page_setup.print_area = "A1:D10"

# Save modified workbook
workbook.save("output_set_print_area.xlsx")
```

```python
# Output image reference
<img src="1.png" width=60% />
```

## **So entfernen Sie den Druckbereich mit Aspose.Cells**

Vorhandene Druckbereichsdefinition entfernen:

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("input.xlsx")

# Access first worksheet
worksheet = workbook.worksheets[0]

# Clear print area
worksheet.page_setup.print_area = ""

# Save modified workbook
workbook.save("output_clear_print_area.xlsx")
```

```python
# Output image reference
<img src="2.png" width=60% />
```

```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Set the print area - specify the range you want to print
worksheet.page_setup.print_area = "A1:D10"

# Save the workbook
workbook.save("set_print_area.pdf")
```
```python
from aspose.cells import Workbook

# Load the workbook
workbook = Workbook("input.xlsx")

# Access the desired worksheet
worksheet = workbook.worksheets[0]

# Clear the print area
worksheet.page_setup.print_area = ""

# Save the workbook
workbook.save("clear_print_area.pdf")
```
