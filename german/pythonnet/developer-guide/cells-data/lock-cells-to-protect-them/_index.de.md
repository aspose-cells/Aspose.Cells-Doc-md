---
title: Zellen mit Python.NET sperren, um sie zu schützen
linktitle: Zellen sperren, um sie zu schützen
type: docs
weight: 130
url: /de/python-net/how-to-lock-cells-to-protect-them/
description: Erfahren Sie, wie Sie bestimmte Zellen sperren und Arbeitsblätter in Excel Dateien mit Aspose.Cells for Python via .NET schützen.
keywords: Python Zellen sperren, Arbeitsblätter schützen, Zellenschutz in Excel mit Python, Aspose.Cells Python Tutorial
---

## **Mögliche Verwendungsszenarien**
Das Sperren von Zellen zum Schutz ist eine gängige Praxis in Tabellenkalkulationsanwendungen wie Microsoft Excel oder Google Sheets, aus mehreren wichtigen Gründen:

1. Verhindern unbeabsichtigter Änderungen: Zellen sperren, um zu verhindern, dass Benutzer versehentlich wichtige Daten oder Formeln ändern.
2. Datenintegrität aufrechterhalten: Kritische Daten bleiben konsistent und genau.
3. Kontrollierter Zugriff: Bearbeitungsberechtigungen in kollaborativen Umgebungen verwalten.
4. Formeln schützen: Kritische Berechnungen vor Änderungen sichern.
5. Geschäftsregeln durchsetzen: Einhaltung der Datenschutzanforderungen.
6. Benutzer anleiten: Klare bearbeitbare Bereiche in komplexen Tabellen bereitstellen.

## **Wie man Zellen in Excel sperrt, um sie zu schützen**
So sperren Sie Zellen in Microsoft Excel:

1. Ausgewählte Zellen sperren: Zellen auswählen oder das Sperren des gesamten Blatts überspringen.
1. Formatierungsdialog für Zellen öffnen: Rechtsklick > "Zellen formatieren" oder Strg+1.
<br>
<img src="1.png" width=60% />
1. Zellen sperren: Zur Registerkarte "Blattschutz" gehen > "Gesperrt" aktivieren > "OK" klicken.
1. Arbeitsblatt schützen: Registerkarte "Überprüfen" > "Blatt schützen" > Passwort/Berechtigungen festlegen > "OK" klicken.
<br>
<img src="2.png" width=60% />

## **So sperren Sie Zellen, um sie mit Python zu schützen**

Aspose.Cells for Python via .NET ermöglicht die programmatische Zellentzung. Folgende Schritte sind erforderlich:
1. Laden Sie die [Beispieldatei](sample.xlsx)
2. Alle Zellen entsperren (Standardmäßig ist die Sperrfunktion erst bei Schutz aktiviert)
3. Bestimmte Zellen sperren
4. Schutz des Arbeitsblatts, um Sperren durchzusetzen

```python
import aspose.cells as ac

# Load sample workbook
workbook = ac.Workbook("sample.xlsx")
worksheet = workbook.worksheets[0]

# Unlock all cells first
style = ac.Style()
style.is_locked = False
style_flag = ac.StyleFlag()
style_flag.locked = True
worksheet.cells.apply_style(style, style_flag)

# Lock specific cells
worksheet.cells["A1"].get_style().is_locked = True
worksheet.cells["B2"].get_style().is_locked = True

# Enable worksheet protection
worksheet.protect(ac.ProtectionType.ALL)

# Save protected workbook
workbook.save("output.xlsx")
```

## **Ausgabeergebnis**
Diese Implementierung sperrt die angegebenen Zellen (A1 und B2), während andere editierbar bleiben. Der Schutz des Arbeitsblatts erzwingt diese Einstellungen.

<br>
<img src="3.png" width=60% />

```python
from aspose.cells import Workbook, ProtectionType, StyleFlag

# Load the Excel file
workbook = Workbook("sample.xlsx")

# Access the first worksheet
sheet = workbook.worksheets[0]

# Unlock all cells first
unlock_style = workbook.create_style()
unlock_style.is_locked = False

style_flag = StyleFlag()
style_flag.locked = True
sheet.cells.apply_style(unlock_style, style_flag)

# Lock specific cells (A1 and B2)
lock_style = workbook.create_style()
lock_style.is_locked = True

sheet.cells.get("A1").set_style(lock_style)
sheet.cells.get("B2").set_style(lock_style)

# Protect the worksheet to enforce locking
sheet.protect(ProtectionType.ALL)

# Save the modified workbook
workbook.save("output_locked.xlsx")
```
{{< app/cells/assistant language="python-net" >}}
