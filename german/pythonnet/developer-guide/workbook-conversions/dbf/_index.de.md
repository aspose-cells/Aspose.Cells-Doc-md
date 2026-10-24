---
title: Lesen und Schreiben von DBF-Dateien
description: Aspose.Cells ist eine Bibliothek für Python via .NET zum Arbeiten mit Tabellenkalkulationsdateien, die das Lesen und Schreiben von dBASE III- und IV-Dateien (DBF) unterstützt. Dieser Artikel erklärt, wie Sie Daten aus DBF-Dateien importieren und in DBF-Dateien exportieren können, einschließlich Dateiformatdetails, unterstützten Funktionen und schrittweisen Beispielen.
linktitle: Lesen und Schreiben von
url: /de/python-net/reading-and-writing-dbf-files/
keywords: Aspose.Cells, Python via .NET Bibliothek, DBF, dBASE, DBF lesen, DBF schreiben, DBF importieren, DBF exportieren, Dateiformat, .dbf
type: docs
weight: 200
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet vollständige Unterstützung für das Lesen und Schreiben von DBF-Dateien (dBASE). Sie können vorhandene dBASE III- und dBASE IV-Dateien in ein Workbook-Objekt laden, die Daten mithilfe der umfangreichen Aspose.Cells-API bearbeiten und die Arbeitsmappe zur Verwendung mit Legacy-Datenbankanwendungen wieder im DBF-Format speichern.
{{% /alert %}}

## **Einführung**
DBF (DataBase File) ist ein Legacy-Datenbankdateiformat, das ursprünglich in den frühen 1980er Jahren von dBASE eingeführt wurde. Trotz des Alters des Formats werden DBF-Dateien in vielen Branchen weiterhin häufig zur Speicherung strukturierter Daten verwendet, insbesondere in der Buchhaltung, GIS und anderen spezialisierten Anwendungen. Aspose.Cells ermöglicht es Ihnen, diese Legacy-Dateien nahtlos in moderne Python via .NET-Tabellenkalkulations-Workflows zu integrieren.
Die Bibliothek unterstützt sowohl das Lesen als auch das Schreiben von DBF-Dateien und bietet Ihnen die Möglichkeit:
- Daten aus vorhandenen DBF-Dateien in Aspose.Cells Workbook-Objekte zu importieren, um sie weiterzuverarbeiten oder in andere Formate zu konvertieren.
- Neue DBF-Dateien von Grund auf zu erstellen oder durch Transformation von Daten aus anderen Tabellenkalkulationsformaten.
- Felddefinitionen, Datentypen und Datensatzstrukturen beim Transfer von Daten in und aus dem DBF-Format beizubehalten.
DBF-Dateien können auch direkt in Microsoft Excel und anderen Tabellenkalkulationsanwendungen geöffnet werden, was sie zu einer praktischen Brücke zwischen Legacy-Systemen und modernen Tabellenkalkulationstools macht.

## **Unterstützte DBF-Versionen und Funktionen**
Aspose.Cells unterstützt die folgenden DBF-Formatversionen:
- **dBASE III** — Die ursprüngliche und am weitesten verbreitete Variante des DBF-Formats.
- **dBASE IV** — Eine erweiterte Version, die zusätzliche Datentypen und größere Feldgrößen unterstützt.

### Unterstützte Funktionen
Die Bibliothek bietet umfassende Unterstützung für die folgenden Operationen:
- Lesen von DBF-Daten in ein Workbook-Objekt, wobei alle Datensätze und Felddefinitionen erhalten bleiben.
- Zurückschreiben von Workbook-Daten in das DBF-Format zum Export in dBASE-kompatible Anwendungen.
- Behandlung gängiger Datentypen in DBF-Dateien, einschließlich Zeichen-, numerischer, Datums- und logischer Felder.
- Beibehaltung von Felddefinitionen wie Feldname, Typ und Länge während Lese-/Schreiboperationen.

### Einschränkungen und Hinweise
Beim Arbeiten mit DBF-Dateien sollten Sie die folgenden Beschränkungen beachten:
- Die maximale Anzahl von Feldern pro Datei beträgt **128**.
- Die maximale Datensatzgröße beträgt **4000 Bytes**.
- Feldnamen sind auf **10 Zeichen** begrenzt, müssen in Großbuchstaben sein und dürfen keine Leerzeichen enthalten.
- Datumswerte in DBF-Dateien werden im Format `YYYYMMDD` gespeichert.
- Die Zeichenkodierung kann je nach Quellanwendung variieren (üblicherweise Windows-1252 oder OEM-Codepages).

## **Lesen einer DBF-Datei**
Aspose.Cells macht es einfach, Daten aus einer DBF-Datei in ein Workbook-Objekt zu laden. Die Bibliothek verwendet die Klasse `LoadOptions`, um das Quellformat anzugeben, und stellt sicher, dass die Daten während des Ladevorgangs korrekt interpretiert werden.

### Lesen einer DBF-Datei mit Aspose.Cells
Um eine DBF-Datei zu lesen, müssen Sie eine `LoadOptions`-Instanz erstellen, deren Eigenschaft `load_format` auf `LoadFormat.DBF` setzen und sie zusammen mit dem Dateipfad an den `Workbook`-Konstruktor übergeben. Nach dem Laden sind die Daten über die `worksheets`-Sammlung zugänglich, wo Sie durch Zellen iterieren, Werte extrahieren oder die Daten nach Bedarf bearbeiten können.
Das folgende Beispiel zeigt, wie eine vorhandene DBF-Datei in Aspose.Cells geladen, auf das erste Arbeitsblatt zugegriffen und die Zellenwerte gelesen werden.

```python
import os
import aspose.cells as ac
data_dir = "Data/"
file_path = os.path.join(data_dir, "example.dbf")
load_options = ac.LoadOptions(ac.LoadFormat.DBF)
workbook = ac.Workbook(file_path, load_options)
worksheet = workbook.worksheets[0]
cells = worksheet.cells
lines = []
max_row = cells.max_data_row
max_col = cells.max_data_column
for i in range(max_row + 1):
    line_parts = []
    for j in range(max_col + 1):
        cell = cells.get(i, j)
        value = cell.string_value
        line_parts.append("|" + value)
    line_parts.append("|")
    lines.append("".join(line_parts))
result = "\n".join(lines) + ("\n" if lines else "")
print(result)
output_path = os.path.join(data_dir, "output.xlsx")
workbook.save(output_path, ac.SaveFormat.XLSX)
print("DBF file loaded successfully. Converted XLSX saved at: " + output_path)
```

{{% alert color="primary" %}}
Sie können DBF-Dateien direkt in Microsoft Excel öffnen, indem Sie die Datei im Dialogfeld „Öffnen" auswählen. Excel behandelt die DBF-Datei als Tabellenkalkulation und zeigt ihre Datensätze in einer tabellarischen Ansicht an. Dies ist nützlich, um die Daten nach dem Lesen oder Schreiben mit Aspose.Cells schnell zu überprüfen.
{{% /alert %}}

## **Schreiben einer DBF-Datei**
Das Schreiben von Daten in eine DBF-Datei folgt einem ähnlichen Muster wie das Speichern in einem anderen Tabellenkalkulationsformat mit Aspose.Cells. Sie erstellen oder laden ein Workbook, füllen das Arbeitsblatt mit Daten und rufen dann die Methode `save` auf, wobei Sie `SaveFormat.DBF` als Zielformat angeben.

### Schreiben einer DBF-Datei mit Aspose.Cells
Um eine DBF-Datei zu erstellen, gehen Sie folgendermaßen vor:
1. Erstellen Sie eine neue `Workbook`-Instanz.
2. Greifen Sie auf das erste Arbeitsblatt aus der `worksheets`-Sammlung zu.
3. Füllen Sie das Arbeitsblatt mit Ihren Daten, einschließlich Kopfzeilen in der ersten Zeile und Datensätzen in den folgenden Zeilen.
4. Rufen Sie die Methode `Workbook.save` auf und übergeben Sie den Dateipfad sowie `SaveFormat.DBF` als Parameter.
Das folgende Beispiel zeigt, wie eine neue DBF-Datei von Grund auf erstellt wird. Es füllt ein Arbeitsblatt mit Beispieldaten, die verschiedene Datentypen (Zeichenketten, Zahlen und Datumswerte) enthalten, um zu veranschaulichen, wie Feldtypen beim Export in das DBF-Format behandelt werden.

```python
import os
import aspose.cells as ac
from datetime import datetime
outputDir = r"C:\Output\\"
filePath = os.path.join(outputDir, "output.dbf")
if not os.path.exists(outputDir):
    os.makedirs(outputDir, exist_ok=True)
workbook = ac.Workbook()
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Spaltenüberschriften
cells.get(0, 0).put_value("ID")
cells.get(0, 1).put_value("Name")
cells.get(0, 2).put_value("Department")
cells.get(0, 3).put_value("Salary")
cells.get(0, 4).put_value("HireDate")
# Datenzeile 1
cells.get(1, 0).put_value(101)
cells.get(1, 1).put_value("John Smith")
cells.get(1, 2).put_value("Engineering")
cells.get(1, 3).put_value(75000.50)
cells.get(1, 4).put_value(datetime(2020, 3, 15))
# Datenzeile 2
cells.get(2, 0).put_value(102)
cells.get(2, 1).put_value("Jane Doe")
cells.get(2, 2).put_value("Marketing")
cells.get(2, 3).put_value(68000.75)
cells.get(2, 4).put_value(datetime(2019, 7, 22))
# Datenzeile 3
cells.get(3, 0).put_value(103)
cells.get(3, 1).put_value("Bob Johnson")
cells.get(3, 2).put_value("Finance")
cells.get(3, 3).put_value(82000.00)
cells.get(3, 4).put_value(datetime(2021, 1, 10))
# Datenzeile 4
cells.get(4, 0).put_value(104)
cells.get(4, 1).put_value("Alice Brown")
cells.get(4, 2).put_value("Human Resources")
cells.get(4, 3).put_value(71000.25)
cells.get(4, 4).put_value(datetime(2018, 11, 5))
# Datenzeile 5
cells.get(5, 0).put_value(105)
cells.get(5, 1).put_value("Charlie Wilson")
cells.get(5, 2).put_value("Operations")
cells.get(5, 3).put_value(79500.80)
cells.get(5, 4).put_value(datetime(2022, 5, 30))
# Spaltenbreiten für bessere Lesbarkeit festlegen
worksheet.cells.set_column_width(0, 8.0)
worksheet.cells.set_column_width(1, 20.0)
worksheet.cells.set_column_width(2, 20.0)
worksheet.cells.set_column_width(3, 12.0)
worksheet.cells.set_column_width(4, 14.0)
workbook.save(filePath, ac.SaveFormat.DBF)
```

{{% alert color="primary" %}}
Stellen Sie beim Schreiben von Daten in eine DBF-Datei sicher, dass Ihre Daten den Einschränkungen des Formats entsprechen. Feldnamen sollten nicht länger als 10 Zeichen sein und keine Leerzeichen enthalten. Datensätze, die insgesamt 4000 Bytes überschreiten, werden nicht korrekt gespeichert. Datumsangaben sollten gültige Datumswerte sein, die im Format YYYYMMDD dargestellt werden können.
{{% /alert %}}

## **Überlegungen zu Datentypen und Formatierung**
Beim Transfer von Daten zwischen Aspose.Cells und dem DBF-Format ist es wichtig zu verstehen, wie Datentypen zwischen den beiden Systemen zugeordnet werden, um die Datenintegrität sicherzustellen.

### Zelltypen zu DBF-Feldtypen
Aspose.Cells-Zellwerte werden beim Speichern automatisch in die entsprechenden DBF-Feldtypen konvertiert:
- **Zeichenketten** werden auf Zeichenfelder (C) abgebildet.
- **Numerische Werte** (Ganzzahlen und Dezimalzahlen) werden auf numerische Felder (N) abgebildet.
- **Datumswerte** werden auf Datumsfelder (D) im Format `YYYYMMDD` abgebildet.
- **Boolesche Werte** werden auf logische Felder (L) abgebildet.

### Kodierung
DBF-Dateien können je nach erstellender Anwendung unterschiedliche Zeichenkodierungen verwenden. Aspose.Cells behandelt die Kodierung in den meisten Fällen transparent. Wenn jedoch Probleme bei der Zeichendarstellung auftreten, müssen Sie möglicherweise die Kodierung der Quelldatei überprüfen.

### Regeln für Feldnamen
DBF-Feldnamen müssen die folgenden Regeln einhalten:
- Maximale Länge von 10 Zeichen.
- Müssen mit einem Buchstaben beginnen.
- Dürfen keine Leerzeichen oder Sonderzeichen enthalten.
- Werden unabhängig von der in der Eingabe verwendeten Groß-/Kleinschreibung in Großbuchstaben gespeichert.

### Überprüfen der Ausgabe
Nach dem Schreiben einer DBF-Datei können Sie das Ergebnis überprüfen, indem Sie sie in Microsoft Excel oder einer beliebigen dBASE-kompatiblen Anwendung öffnen. Die Daten sollten in einer tabellarischen Ansicht mit den Feldnamen als Spaltenüberschriften erscheinen, und die Datensätze sollten entsprechend den bereitgestellten Daten gefüllt sein.

## **Konvertieren zwischen DBF und anderen Formaten**
Einer der praktischsten Anwendungsfälle für das Lesen und Schreiben von DBF-Dateien mit Aspose.Cells ist die Konvertierung von Daten zwischen dem DBF-Format und modernen Tabellenkalkulationsformaten wie XLSX, XLS oder CSV. Da Aspose.Cells eine breite Palette von Formaten unterstützt, können Sie eine DBF-Datei einfach laden und in einem beliebigen anderen unterstützten Format neu speichern oder umgekehrt.
Sie können beispielsweise eine DBF-Datei lesen, mit der Aspose.Cells-API Formatierungen oder Berechnungen anwenden und das Ergebnis dann als XLSX-Datei speichern, um es an Benutzer zu verteilen, die mit modernen Tabellenkalkulationsanwendungen arbeiten. Umgekehrt können Sie Daten aus einer XLSX- oder CSV-Datei übernehmen und in das DBF-Format exportieren, um sie in Legacy-Systeme zu integrieren.

{{< app/cells/assistant language="python-net" >}}