---
title: Lesen und Schreiben von DBF-Dateien
description: Aspose.Cells ist eine Python via Java-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Lesen und Schreiben von dBASE III- und IV-Dateien (DBF) unterstützt. Dieser Artikel erläutert, wie Sie mit Aspose.Cells Daten aus DBF-Dateien importieren und in DBF-Dateien exportieren können, einschließlich Details zum Dateiformat, unterstützten Funktionen und schrittweisen Beispielen.
keywords: Aspose.Cells, Python via Java-Bibliothek, DBF, dBASE, DBF lesen, DBF schreiben, DBF importieren, DBF exportieren, Dateiformat, .dbf
type: docs
weight: 200
url: /de/python-java/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells bietet vollständige Unterstützung für das Lesen und Schreiben von DBF-Dateien (dBASE). Sie können bestehende dBASE III- und dBASE IV-Dateien in ein Workbook-Objekt laden, die Daten mit der umfangreichen Aspose.Cells-API bearbeiten und die Arbeitsmappe zur Verwendung mit älteren Datenbankanwendungen wieder im DBF-Format speichern.

{{% /alert %}}

## **Einführung**

DBF (DataBase File) ist ein älteres Datenbankdateiformat, das ursprünglich Anfang der 1980er Jahre von dBASE eingeführt wurde. Trotz des Alters des Formats werden DBF-Dateien in vielen Branchen weiterhin häufig zur Speicherung strukturierter Daten verwendet, insbesondere in der Buchhaltung, in GIS und anderen spezialisierten Anwendungen. Aspose.Cells ermöglicht es Ihnen, diese älteren Dateien nahtlos in moderne Python via Java-Tabellenkalkulations-Workflows zu integrieren.

Die Bibliothek unterstützt sowohl das Lesen als auch das Schreiben von DBF-Dateien und bietet Ihnen folgende Möglichkeiten:

- Importieren von Daten aus bestehenden DBF-Dateien in Aspose.Cells-Workbook-Objekte zur weiteren Verarbeitung oder Konvertierung in andere Formate.
- Erstellen neuer DBF-Dateien von Grund auf oder durch Umwandlung von Daten aus anderen Tabellenkalkulationsformaten.
- Beibehalten von Felddefinitionen, Datentypen und Datensatzstrukturen beim Übertragen von Daten in das und aus dem DBF-Format.

DBF-Dateien können auch direkt in Microsoft Excel und anderen Tabellenkalkulationsanwendungen geöffnet werden, was sie zu einer praktischen Brücke zwischen älteren Systemen und modernen Tabellenkalkulationstools macht.

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

Beachten Sie bei der Arbeit mit DBF-Dateien die folgenden Beschränkungen:

- Die maximale Anzahl von Feldern pro Datei beträgt **128**.
- Die maximale Datensatzgröße beträgt **4000 Bytes**.
- Feldnamen sind auf **10 Zeichen** begrenzt, müssen in Großbuchstaben geschrieben sein und dürfen keine Leerzeichen enthalten.
- Datumswerte in DBF-Dateien werden im Format `YYYYMMDD` gespeichert.
- Die Zeichenkodierung kann je nach Quellanwendung variieren (üblicherweise Windows-1252 oder OEM-Codepages).

## **Lesen einer DBF-Datei**

Aspose.Cells macht es einfach, Daten aus einer DBF-Datei in ein Workbook-Objekt zu laden. Die Bibliothek verwendet die Klasse `LoadOptions`, um das Quellformat anzugeben, und stellt sicher, dass die Daten beim Ladevorgang korrekt interpretiert werden.

### Lesen einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu lesen, müssen Sie eine `LoadOptions`-Instanz erstellen, deren Eigenschaft `LoadFormat` auf `LoadFormat.DBF` setzen und sie zusammen mit dem Dateipfad an den Konstruktor `Workbook` übergeben. Nach dem Laden sind die Daten über die Sammlung `Worksheets` zugänglich, wo Sie Zellen durchlaufen, Werte extrahieren oder die Daten nach Bedarf bearbeiten können.

Das folgende Beispiel zeigt, wie eine bestehende DBF-Datei in Aspose.Cells geladen, auf das erste Arbeitsblatt zugegriffen und die Zellenwerte gelesen werden.

```python
from asposecells.api import Workbook, LoadOptions, LoadFormat, SaveFormat

dataDir = "Data/"
filePath = os.path.join(dataDir, "example.dbf")

loadOptions = LoadOptions(LoadFormat.Dbf)

workbook = Workbook(filePath, loadOptions)

worksheet = workbook.getWorksheets().get(0)

cells = worksheet.getCells()

sb = []

maxRow = cells.getMaxDataRow()
maxCol = cells.getMaxDataColumn()

for i in range(0, maxRow + 1):
    for j in range(0, maxCol + 1):
        cell = cells.get(i, j)
        value = cell.getStringValue()
        sb.append("|" + value)
    sb.append("|\n")

print("".join(sb))

outputPath = os.path.join(dataDir, "output.xlsx")
workbook.save(outputPath, SaveFormat.Xlsx)

print("DBF file loaded successfully. Converted XLSX saved at: " + outputPath)

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Sie können DBF-Dateien direkt in Microsoft Excel öffnen, indem Sie die Datei im Dialogfeld „Öffnen" auswählen. Excel behandelt die DBF-Datei als Tabellenkalkulation und zeigt die Datensätze in einer tabellarischen Darstellung an. Dies ist nützlich, um die Daten schnell zu überprüfen, nachdem sie mit Aspose.Cells gelesen oder geschrieben wurden.

{{% /alert %}}

## **Schreiben einer DBF-Datei**

Das Schreiben von Daten in eine DBF-Datei folgt einem ähnlichen Muster wie das Speichern jedes anderen Tabellenkalkulationsformats mit Aspose.Cells. Sie erstellen oder laden eine Workbook, füllen das Arbeitsblatt mit Daten und rufen dann die Methode `save` auf, wobei Sie `SaveFormat.DBF` als Zielformat angeben.

### Schreiben einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu erstellen, gehen Sie folgendermaßen vor:

1. Erstellen Sie eine neue `Workbook`-Instanz.
2. Greifen Sie auf das erste Arbeitsblatt aus der Sammlung `Worksheets` zu.
3. Füllen Sie das Arbeitsblatt mit Ihren Daten, einschließlich Kopfzeilen in der ersten Zeile und Datensätzen in den nachfolgenden Zeilen.
4. Rufen Sie die Methode `Workbook.save` auf und übergeben Sie den Dateipfad sowie `SaveFormat.DBF` als Parameter.

Das folgende Beispiel zeigt, wie eine neue DBF-Datei von Grund auf erstellt wird. Es füllt ein Arbeitsblatt mit Beispieldaten, die unterschiedliche Datentypen (Zeichenketten, Zahlen und Datumsangaben) enthalten, um zu veranschaulichen, wie Feldtypen beim Export in das DBF-Format behandelt werden.

```python
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat
from java.util import GregorianCalendar

output_dir = "C:\\Output\\"
file_path = os.path.join(output_dir, "output.dbf")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()

# Spaltenüberschriften
cells.get(0, 0).putValue("ID")
cells.get(0, 1).putValue("Name")
cells.get(0, 2).putValue("Abteilung")
cells.get(0, 3).putValue("Gehalt")
cells.get(0, 4).putValue("Einstellungsdatum")

# Datenzeile 1
cells.get(1, 0).putValue(101)
cells.get(1, 1).putValue("John Smith")
cells.get(1, 2).putValue("Ingenieurwesen")
cells.get(1, 3).putValue(75000.50)
cells.get(1, 4).putValue(GregorianCalendar(2020, 2, 15).getTime())

# Datenzeile 2
cells.get(2, 0).putValue(102)
cells.get(2, 1).putValue("Jane Doe")
cells.get(2, 2).putValue("Marketing")
cells.get(2, 3).putValue(68000.75)
cells.get(2, 4).putValue(GregorianCalendar(2019, 6, 22).getTime())

# Datenzeile 3
cells.get(3, 0).putValue(103)
cells.get(3, 1).putValue("Bob Johnson")
cells.get(3, 2).putValue("Finanzen")
cells.get(3, 3).putValue(82000.00)
cells.get(3, 4).putValue(GregorianCalendar(2021, 0, 10).getTime())

# Datenzeile 4
cells.get(4, 0).putValue(104)
cells.get(4, 1).putValue("Alice Brown")
cells.get(4, 2).putValue("Personalwesen")
cells.get(4, 3).putValue(71000.25)
cells.get(4, 4).putValue(GregorianCalendar(2018, 10, 5).getTime())

# Datenzeile 5
cells.get(5, 0).putValue(105)
cells.get(5, 1).putValue("Charlie Wilson")
cells.get(5, 2).putValue("Betrieb")
cells.get(5, 3).putValue(79500.80)
cells.get(5, 4).putValue(GregorianCalendar(2022, 4, 30).getTime())

# Spaltenbreiten für bessere Lesbarkeit festlegen
worksheet.getCells().setColumnWidth(0, 8)
worksheet.getCells().setColumnWidth(1, 20)
worksheet.getCells().setColumnWidth(2, 20)
worksheet.getCells().setColumnWidth(3, 12)
worksheet.getCells().setColumnWidth(4, 14)

workbook.save(file_path, SaveFormat.Dbf)

jpype.shutdownJVM()
```

{{% alert color="primary" %}}

Stellen Sie beim Schreiben von Daten in eine DBF-Datei sicher, dass Ihre Daten den Einschränkungen des Formats entsprechen. Feldnamen sollten nicht länger als 10 Zeichen sein und keine Leerzeichen enthalten. Datensätze, die insgesamt 4000 Bytes überschreiten, werden nicht korrekt gespeichert. Datumsangaben sollten gültige Datumswerte sein, die im Format YYYYMMDD dargestellt werden können.

{{% /alert %}}

## **Überlegungen zu Datentypen und Formatierung**

Beim Übertragen von Daten zwischen Aspose.Cells und dem DBF-Format ist es wichtig zu verstehen, wie Datentypen zwischen den beiden Systemen zugeordnet werden, um die Datenintegrität sicherzustellen.

### Zelltypen zu DBF-Feldtypen

Aspose.Cells-Zellenwerte werden beim Speichern automatisch in die entsprechenden DBF-Feldtypen konvertiert:

- **Zeichenketten** werden auf Zeichenfelder (C) abgebildet.
- **Numerische Werte** (Ganzzahlen und Dezimalzahlen) werden auf numerische Felder (N) abgebildet.
- **Datumswerte** werden auf Datumsfelder (D) im Format `YYYYMMDD` abgebildet.
- **Boolesche Werte** werden auf logische Felder (L) abgebildet.

### Kodierung

DBF-Dateien können je nach erstellender Anwendung unterschiedliche Zeichenkodierungen verwenden. Aspose.Cells behandelt die Kodierung in den meisten Fällen transparent. Wenn jedoch Probleme bei der Zeichendarstellung auftreten, müssen Sie möglicherweise die Kodierung der Quelldatei überprüfen.

### Regeln für Feldnamen

DBF-Feldnamen müssen die folgenden Regeln einhalten:

- Maximale Länge von 10 Zeichen.
- Muss mit einem Buchstaben beginnen.
- Darf keine Leerzeichen oder Sonderzeichen enthalten.
- Wird unabhängig von der in der Eingabe verwendeten Schreibweise in Großbuchstaben gespeichert.

### Überprüfen der Ausgabe

Nach dem Schreiben einer DBF-Datei können Sie das Ergebnis überprüfen, indem Sie sie in Microsoft Excel oder einer anderen dBASE-kompatiblen Anwendung öffnen. Die Daten sollten in einer tabellarischen Darstellung erscheinen, wobei die Feldnamen als Spaltenüberschriften und die Datensätze entsprechend den bereitgestellten Daten erscheinen.

## **Konvertieren zwischen DBF und anderen Formaten**

Einer der praktischsten Anwendungsfälle für das Lesen und Schreiben von DBF-Dateien mit Aspose.Cells ist die Konvertierung von Daten zwischen dem DBF-Format und modernen Tabellenkalkulationsformaten wie XLSX, XLS oder CSV. Da Aspose.Cells eine breite Palette von Formaten unterstützt, können Sie problemlos eine DBF-Datei laden und in einem anderen unterstützten Format erneut speichern oder umgekehrt.

Sie können beispielsweise eine DBF-Datei lesen, Formatierungen oder Berechnungen mit der Aspose.Cells-API anwenden und das Ergebnis dann als XLSX-Datei speichern, um es an Benutzer zu verteilen, die mit modernen Tabellenkalkulationsanwendungen arbeiten. Umgekehrt können Sie Daten aus einer XLSX- oder CSV-Datei übernehmen und in das DBF-Format exportieren, um sie in ältere Systeme zu integrieren.



{{< app/cells/assistant language="python" >}}