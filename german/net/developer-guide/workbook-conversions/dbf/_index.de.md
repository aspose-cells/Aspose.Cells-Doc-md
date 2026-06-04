---
title: Lesen und Schreiben von DBF-Dateien
description: Aspose.Cells ist eine .NET-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Lesen und Schreiben von dBASE III- und IV-Dateien (DBF) unterstützt. Dieser Artikel erläutert, wie Sie mit Aspose.Cells Daten aus DBF-Dateien importieren und in DBF-Dateien exportieren können, einschließlich Details zum Dateiformat, unterstützten Funktionen und schrittweisen Beispielen.
keywords: Aspose.Cells, .NET-Bibliothek, DBF, dBASE, DBF lesen, DBF schreiben, DBF importieren, DBF exportieren, Dateiformat, .dbf
type: docs
weight: 200
url: /de/net/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells bietet vollständige Unterstützung für das Lesen und Schreiben von DBF-Dateien (dBASE). Sie können bestehende dBASE III- und dBASE IV-Dateien in ein Workbook-Objekt laden, die Daten über die umfangreiche Aspose.Cells-API bearbeiten und die Arbeitsmappe anschließend wieder im DBF-Format speichern, um sie in Legacy-Datenbankanwendungen zu verwenden.

{{% /alert %}}

## **Einführung**

DBF (DataBase File) ist ein Legacy-Datenbankdateiformat, das ursprünglich in den frühen 1980er Jahren von dBASE eingeführt wurde. Trotz des Alters des Formats werden DBF-Dateien in vielen Branchen weiterhin häufig zur Speicherung strukturierter Daten verwendet, insbesondere in der Buchhaltung, in GIS und anderen spezialisierten Anwendungen. Aspose.Cells ermöglicht es Ihnen, diese Legacy-Dateien nahtlos in moderne .NET-Tabellenkalkulations-Workflows zu integrieren.

Die Bibliothek unterstützt sowohl das Lesen als auch das Schreiben von DBF-Dateien und bietet Ihnen folgende Möglichkeiten:

- Daten aus bestehenden DBF-Dateien in Aspose.Cells-Workbook-Objekte importieren, um sie weiter zu verarbeiten oder in andere Formate zu konvertieren.
- Neue DBF-Dateien von Grund auf erstellen oder durch Transformation von Daten aus anderen Tabellenkalkulationsformaten erzeugen.
- Felddefinitionen, Datentypen und Datensatzstrukturen bei der Übertragung von Daten in das und aus dem DBF-Format beibehalten.

DBF-Dateien können auch direkt in Microsoft Excel und anderen Tabellenkalkulationsanwendungen geöffnet werden, was sie zu einer praktischen Brücke zwischen Legacy-Systemen und modernen Tabellenkalkulationstools macht.

## **Unterstützte DBF-Versionen und Funktionen**

Aspose.Cells unterstützt die folgenden DBF-Formatversionen:

- **dBASE III** — Die ursprüngliche und am weitesten verbreitete Variante des DBF-Formats.
- **dBASE IV** — Eine erweiterte Version, die zusätzliche Datentypen und größere Feldgrößen unterstützt.

### Unterstützte Funktionen

Die Bibliothek bietet umfassende Unterstützung für die folgenden Operationen:

- Lesen von DBF-Daten in ein Workbook-Objekt, wobei alle Datensätze und Felddefinitionen erhalten bleiben.
- Zurückschreiben von Workbook-Daten in das DBF-Format für den Export in dBASE-kompatible Anwendungen.
- Verarbeitung gängiger Datentypen in DBF-Dateien, einschließlich Zeichen-, numerischer, Datums- und logischer Felder.
- Beibehaltung von Felddefinitionen wie Feldname, Typ und Länge während der Lese-/Schreiboperationen.

### Einschränkungen und Hinweise

Beachten Sie bei der Arbeit mit DBF-Dateien die folgenden Beschränkungen:

- Die maximale Anzahl von Feldern pro Datei beträgt **128**.
- Die maximale Datensatzgröße beträgt **4000 Bytes**.
- Feldnamen sind auf **10 Zeichen** begrenzt, müssen in Großbuchstaben angegeben werden und dürfen keine Leerzeichen enthalten.
- Datumswerte in DBF-Dateien werden im Format `YYYYMMDD` gespeichert.
- Die Zeichenkodierung kann je nach Quellanwendung variieren (üblicherweise Windows-1252 oder OEM-Codepages).

## **Lesen einer DBF-Datei**

Aspose.Cells macht es einfach, Daten aus einer DBF-Datei in ein Workbook-Objekt zu laden. Die Bibliothek verwendet die `LoadOptions`-Klasse, um das Quellformat anzugeben und sicherzustellen, dass die Daten während des Ladevorgangs korrekt interpretiert werden.

### Lesen einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu lesen, müssen Sie eine `LoadOptions`-Instanz erstellen, deren `LoadFormat`-Eigenschaft auf `LoadFormat.Dbf` setzen und sie zusammen mit dem Dateipfad an den `Workbook`-Konstruktor übergeben. Nach dem Laden sind die Daten über die `Worksheets`-Sammlung zugänglich, wo Sie durch Zellen iterieren, Werte extrahieren oder die Daten nach Bedarf bearbeiten können.

Das folgende Beispiel zeigt, wie eine bestehende DBF-Datei in Aspose.Cells geladen, auf das erste Arbeitsblatt zugegriffen und die Zellenwerte gelesen werden.

```csharp
using System;
using System.IO;
using System.Text;
using Aspose.Cells;

string dataDir = "Data/";
string filePath = Path.Combine(dataDir, "example.dbf");

LoadOptions loadOptions = new LoadOptions(LoadFormat.Dbf);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.Worksheets[0];

Cells cells = worksheet.Cells;

StringBuilder sb = new StringBuilder();

int maxRow = cells.MaxDataRow;
int maxCol = cells.MaxDataColumn;

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells[i, j];
        string value = cell.StringValue;
        sb.Append("|").Append(value);
    }
    sb.Append("|").AppendLine();
}

Console.WriteLine(sb.ToString());

string outputPath = Path.Combine(dataDir, "output.xlsx");
workbook.Save(outputPath, SaveFormat.Xlsx);

Console.WriteLine("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Sie können DBF-Dateien direkt in Microsoft Excel öffnen, indem Sie die Datei im Dialogfeld „Öffnen" auswählen. Excel behandelt die DBF-Datei als Tabellenkalkulation und zeigt ihre Datensätze in einer tabellarischen Ansicht an. Dies ist nützlich, um die Daten nach dem Lesen oder Schreiben mit Aspose.Cells schnell zu überprüfen.

{{% /alert %}}

## **Schreiben einer DBF-Datei**

Das Schreiben von Daten in eine DBF-Datei folgt einem ähnlichen Muster wie das Speichern in jedem anderen Tabellenkalkulationsformat mit Aspose.Cells. Sie erstellen oder laden ein Workbook, füllen das Arbeitsblatt mit Daten und rufen anschließend die `Save`-Methode auf, wobei Sie `SaveFormat.Dbf` als Zielformat angeben.

### Schreiben einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu erstellen, gehen Sie wie folgt vor:

1. Erstellen Sie eine neue `Workbook`-Instanz.
2. Greifen Sie auf das erste Arbeitsblatt aus der `Worksheets`-Sammlung zu.
3. Füllen Sie das Arbeitsblatt mit Ihren Daten, einschließlich Kopfzeilen in der ersten Zeile und Datensätzen in den nachfolgenden Zeilen.
4. Rufen Sie die Methode `Workbook.Save` auf und übergeben Sie den Dateipfad sowie `SaveFormat.Dbf` als Parameter.

Das folgende Beispiel zeigt, wie eine neue DBF-Datei von Grund auf erstellt wird. Es füllt ein Arbeitsblatt mit Beispieldaten, die verschiedene Datentypen (Zeichenketten, Zahlen und Datumswerte) enthalten, um zu veranschaulichen, wie Feldtypen beim Export in das DBF-Format behandelt werden.

```csharp
using System;
using System.IO;
using Aspose.Cells;

string outputDir = @"C:\Output\";
string filePath = Path.Combine(outputDir, "output.dbf");

if (!Directory.Exists(outputDir))
{
    Directory.CreateDirectory(outputDir);
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;

// Spaltenüberschriften
cells[0, 0].PutValue("ID");
cells[0, 1].PutValue("Name");
cells[0, 2].PutValue("Department");
cells[0, 3].PutValue("Salary");
cells[0, 4].PutValue("HireDate");

// Datenzeile 1
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));

// Datenzeile 2
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));

// Datenzeile 3
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));

// Datenzeile 4
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));

// Datenzeile 5
cells[5, 0].PutValue(105);
cells[5, 1].PutValue("Charlie Wilson");
cells[5, 2].PutValue("Operations");
cells[5, 3].PutValue(79500.80);
cells[5, 4].PutValue(new DateTime(2022, 5, 30));

// Spaltenbreiten für bessere Lesbarkeit festlegen
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);

workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Stellen Sie beim Schreiben von Daten in eine DBF-Datei sicher, dass Ihre Daten den Einschränkungen des Formats entsprechen. Feldnamen sollten nicht länger als 10 Zeichen sein und keine Leerzeichen enthalten. Datensätze, die insgesamt 4000 Bytes überschreiten, werden nicht korrekt gespeichert. Datumsangaben sollten gültige Datumswerte sein, die im Format YYYYMMDD dargestellt werden können.

{{% /alert %}}

## **Datentyp- und Formatierungsaspekte**

Beim Übertragen von Daten zwischen Aspose.Cells und dem DBF-Format ist es wichtig zu verstehen, wie Datentypen zwischen den beiden Systemen zugeordnet werden, um die Datenintegrität sicherzustellen.

### Zelltypen zu DBF-Feldtypen

Aspose.Cells-Zellenwerte werden beim Speichern automatisch in die entsprechenden DBF-Feldtypen konvertiert:

- **Zeichenketten** werden auf Zeichenfelder (C) abgebildet.
- **Numerische Werte** (Ganzzahlen und Dezimalzahlen) werden auf numerische Felder (N) abgebildet.
- **Datumswerte** werden auf Datumsfelder (D) im Format `YYYYMMDD` abgebildet.
- **Boolesche Werte** werden auf logische Felder (L) abgebildet.

### Kodierung

DBF-Dateien können je nach erstellender Anwendung unterschiedliche Zeichenkodierungen verwenden. Aspose.Cells behandelt die Kodierung in den meisten Fällen transparent. Sollten jedoch Probleme bei der Zeichenanzeige auftreten, müssen Sie möglicherweise die Kodierung der Quelldatei überprüfen.

### Regeln für Feldnamen

DBF-Feldnamen müssen die folgenden Regeln einhalten:

- Maximale Länge von 10 Zeichen.
- Muss mit einem Buchstaben beginnen.
- Darf keine Leerzeichen oder Sonderzeichen enthalten.
- Wird unabhängig von der Groß-/Kleinschreibung in der Eingabe in Großbuchstaben gespeichert.

### Überprüfen der Ausgabe

Nach dem Schreiben einer DBF-Datei können Sie das Ergebnis überprüfen, indem Sie sie in Microsoft Excel oder einer beliebigen dBASE-kompatiblen Anwendung öffnen. Die Daten sollten in einer tabellarischen Ansicht mit den Feldnamen als Spaltenüberschriften und den Datensätzen entsprechend den bereitgestellten Daten erscheinen.

## **Konvertieren zwischen DBF und anderen Formaten**

Einer der praktischsten Anwendungsfälle für das Lesen und Schreiben von DBF-Dateien mit Aspose.Cells ist die Konvertierung von Daten zwischen dem DBF-Format und modernen Tabellenkalkulationsformaten wie XLSX, XLS oder CSV. Da Aspose.Cells eine breite Palette von Formaten unterstützt, können Sie eine DBF-Datei einfach laden und in einem beliebigen anderen unterstützten Format speichern oder umgekehrt.

Sie können beispielsweise eine DBF-Datei lesen, mit der Aspose.Cells-API Formatierungen oder Berechnungen anwenden und das Ergebnis dann als XLSX-Datei speichern, um sie an Benutzer zu verteilen, die mit modernen Tabellenkalkulationsanwendungen arbeiten. Umgekehrt können Sie Daten aus einer XLSX- oder CSV-Datei übernehmen und in das DBF-Format exportieren, um sie in Legacy-Systeme zu integrieren.



{{< app/cells/assistant language="csharp" >}}