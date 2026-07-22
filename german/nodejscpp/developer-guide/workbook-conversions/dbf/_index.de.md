---
title: Lesen und Schreiben von DBF-Dateien
linktitle: Lesen und Schreiben von
description: Aspose.Cells for Node.js via C++ ist eine Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Lesen und Schreiben von dBASE III- und IV-Dateien (DBF) unterstützt. Dieser Artikel erklärt, wie Sie mit Aspose.Cells Daten aus DBF-Dateien importieren und in DBF-Dateien exportieren können, einschließlich Details zum Dateiformat, unterstützten Funktionen und Schritt-für-Schritt-Beispielen.
keywords: Aspose.Cells, Node.js via C++, DBF, dBASE, DBF lesen, DBF schreiben, DBF importieren, DBF exportieren, Dateiformat, .dbf
type: docs
weight: 200
url: /de/nodejs-cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells bietet vollständige Unterstützung für das Lesen und Schreiben von DBF-Dateien (dBASE). Sie können vorhandene dBASE III- und dBASE IV-Dateien in ein Workbook-Objekt laden, die Daten mithilfe der umfangreichen Aspose.Cells-API bearbeiten und die Arbeitsmappe zur Verwendung mit Legacy-Datenbankanwendungen wieder im DBF-Format speichern.

{{% /alert %}}

## **Einführung**

DBF (DataBase File) ist ein Legacy-Datenbankdateiformat, das ursprünglich Anfang der 1980er Jahre von dBASE eingeführt wurde. Trotz des Alters des Formats werden DBF-Dateien in vielen Branchen weiterhin häufig zur Speicherung strukturierter Daten verwendet, insbesondere in der Buchhaltung, GIS und anderen spezialisierten Anwendungen. Aspose.Cells ermöglicht es Ihnen, diese Legacy-Dateien nahtlos in moderne Node.js via C++-Tabellenkalkulations-Workflows zu integrieren.

Die Bibliothek unterstützt sowohl das Lesen als auch das Schreiben von DBF-Dateien und bietet Ihnen die Möglichkeit:

- Daten aus vorhandenen DBF-Dateien in Aspose.Cells-Workbook-Objekte zur weiteren Verarbeitung oder Konvertierung in andere Formate zu importieren.
- Neue DBF-Dateien von Grund auf zu erstellen oder durch Transformieren von Daten aus anderen Tabellenkalkulationsformaten zu erzeugen.
- Felddefinitionen, Datentypen und Datensatzstrukturen bei der Übertragung von Daten in und aus dem DBF-Format beizubehalten.

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
- Beibehaltung von Felddefinitionen wie Feldname, Typ und Länge während Lese-/Schreiboperationen.

### Einschränkungen und Hinweise

Beachten Sie bei der Arbeit mit DBF-Dateien die folgenden Beschränkungen:

- Die maximale Anzahl von Feldern pro Datei beträgt **128**.
- Die maximale Datensatzgröße beträgt **4000 Bytes**.
- Feldnamen sind auf **10 Zeichen** begrenzt, müssen in Großbuchstaben vorliegen und dürfen keine Leerzeichen enthalten.
- Datumswerte in DBF-Dateien werden im Format `JJJJMMTT` gespeichert.
- Die Zeichenkodierung kann je nach Quellanwendung variieren (üblicherweise Windows-1252 oder OEM-Codepages).

## **Lesen einer DBF-Datei**

Aspose.Cells macht es einfach, Daten aus einer DBF-Datei in ein Workbook-Objekt zu laden. Die Bibliothek verwendet die Klasse `LoadOptions`, um das Quellformat anzugeben und sicherzustellen, dass die Daten während des Ladevorgangs korrekt interpretiert werden.

### Lesen einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu lesen, müssen Sie eine `LoadOptions`-Instanz erstellen, ihre Eigenschaft `LoadFormat` auf `LoadFormat.Dbf` setzen und sie zusammen mit dem Dateipfad an den `Workbook`-Konstruktor übergeben. Nach dem Laden sind die Daten über die `Worksheets`-Sammlung zugänglich, wo Sie durch Zellen iterieren, Werte extrahieren oder die Daten nach Bedarf bearbeiten können.

Das folgende Beispiel zeigt, wie eine vorhandene DBF-Datei in Aspose.Cells geladen wird, wie auf das erste Arbeitsblatt zugegriffen wird und wie die Zellenwerte gelesen werden.

```javascript
let sb = "";

const maxRow = cells.getMaxDataRow();
const maxCol = cells.getMaxDataColumn();

for (let i = 0; i <= maxRow; i++)
{
    for (let j = 0; j <= maxCol; j++)
    {
        const cell = cells.get(i, j);
        const value = cell.getStringValue();
        sb += "|" + value;
    }
    sb += "|" + "\n";
}

console.log(sb);

const outputPath = path.join(dataDir, "output.xlsx");
workbook.save(outputPath, AsposeCells.SaveFormat.Xlsx);

console.log("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Sie können DBF-Dateien direkt in Microsoft Excel öffnen, indem Sie die Datei im Dialogfeld Öffnen auswählen. Excel behandelt die DBF-Datei als Tabellenkalkulation und zeigt ihre Datensätze in einem tabellarischen Layout an. Dies ist nützlich, um die Daten nach dem Lesen oder Schreiben mit Aspose.Cells schnell zu überprüfen.

{{% /alert %}}

## **Schreiben einer DBF-Datei**

Das Schreiben von Daten in eine DBF-Datei folgt einem ähnlichen Muster wie das Speichern jedes anderen Tabellenkalkulationsformats mit Aspose.Cells. Sie erstellen oder laden eine Workbook, füllen das Arbeitsblatt mit Daten und rufen dann die Methode `save` auf, wobei Sie `SaveFormat.Dbf` als Zielformat angeben.

### Schreiben einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu erstellen, gehen Sie folgendermaßen vor:

1. Erstellen Sie eine neue `Workbook`-Instanz.
2. Greifen Sie auf das erste Arbeitsblatt aus der `Worksheets`-Sammlung zu.
3. Füllen Sie das Arbeitsblatt mit Ihren Daten, einschließlich Kopfzeilen in der ersten Zeile und Datensätzen in den nachfolgenden Zeilen.
4. Rufen Sie die Methode `workbook.save` auf und übergeben Sie den Dateipfad und `SaveFormat.Dbf` als Parameter.

Das folgende Beispiel zeigt, wie eine neue DBF-Datei von Grund auf erstellt wird. Es füllt ein Arbeitsblatt mit Beispieldaten, die verschiedene Datentypen enthalten (Zeichenketten, Zahlen und Datumsangaben), um zu veranschaulichen, wie Feldtypen beim Export in das DBF-Format behandelt werden.

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");
const fs = require("fs");

const outputDir = "C:\\Output\\";
const filePath = path.join(outputDir, "output.dbf");

if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();

// Spaltenüberschriften
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");

// Datenzeile 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new Date(2020, 2, 15));

// Datenzeile 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new Date(2019, 6, 22));

// Datenzeile 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new Date(2021, 0, 10));

// Datenzeile 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new Date(2018, 10, 5));

// Datenzeile 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new Date(2022, 4, 30));

// Spaltenbreiten für bessere Lesbarkeit festlegen
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, AsposeCells.SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Stellen Sie beim Schreiben von Daten in eine DBF-Datei sicher, dass Ihre Daten den Einschränkungen des Formats entsprechen. Feldnamen sollten nicht länger als 10 Zeichen sein und keine Leerzeichen enthalten. Datensätze, die insgesamt 4000 Bytes überschreiten, werden nicht korrekt gespeichert. Datumsangaben sollten gültige Datumswerte sein, die im Format JJJJMMTT dargestellt werden können.

{{% /alert %}}

## **Überlegungen zu Datentypen und Formatierung**

Bei der Datenübertragung zwischen Aspose.Cells und dem DBF-Format ist es wichtig zu verstehen, wie Datentypen zwischen den beiden Systemen zugeordnet werden, um die Datenintegrität sicherzustellen.

### Zellentypen zu DBF-Feldtypen

Aspose.Cells-Zellenwerte werden beim Speichern automatisch in die entsprechenden DBF-Feldtypen konvertiert:

- **Zeichenketten** werden Zeichenfeldern (C) zugeordnet.
- **Numerische Werte** (Ganzzahlen und Dezimalzahlen) werden numerischen Feldern (N) zugeordnet.
- **Datumswerte** werden Datumsfeldern (D) im Format `JJJJMMTT` zugeordnet.
- **Boolesche Werte** werden logischen Feldern (L) zugeordnet.

### Kodierung

DBF-Dateien können je nach Anwendung, die sie erstellt hat, unterschiedliche Zeichenkodierungen verwenden. Aspose.Cells handhabt die Kodierung in den meisten Fällen transparent. Wenn Sie jedoch Probleme bei der Zeichendarstellung feststellen, müssen Sie möglicherweise die Kodierung der Quelldatei überprüfen.

### Regeln für Feldnamen

DBF-Feldnamen müssen die folgenden Regeln einhalten:

- Maximale Länge von 10 Zeichen.
- Müssen mit einem Buchstaben beginnen.
- Dürfen keine Leerzeichen oder Sonderzeichen enthalten.
- Werden unabhängig von der Groß-/Kleinschreibung in der Eingabe in Großbuchstaben gespeichert.

### Überprüfen der Ausgabe

Nach dem Schreiben einer DBF-Datei können Sie das Ergebnis überprüfen, indem Sie sie in Microsoft Excel oder einer anderen dBASE-kompatiblen Anwendung öffnen. Die Daten sollten in einem tabellarischen Layout mit den Feldnamen als Spaltenüberschriften erscheinen, und die Datensätze sollten entsprechend den bereitgestellten Daten gefüllt sein.

## **Konvertieren zwischen DBF und anderen Formaten**

Einer der praktischsten Anwendungsfälle für das Lesen und Schreiben von DBF-Dateien mit Aspose.Cells ist die Konvertierung von Daten zwischen dem DBF-Format und modernen Tabellenkalkulationsformaten wie XLSX, XLS oder CSV. Da Aspose.Cells eine breite Palette von Formaten unterstützt, können Sie eine DBF-Datei einfach laden und in einem anderen unterstützten Format neu speichern oder umgekehrt.

Beispielsweise können Sie eine DBF-Datei lesen, Formatierungen oder Berechnungen mit der Aspose.Cells-API anwenden und das Ergebnis dann als XLSX-Datei speichern, um es an Benutzer zu verteilen, die mit modernen Tabellenkalkulationsanwendungen arbeiten. Umgekehrt können Sie Daten aus einer XLSX- oder CSV-Datei übernehmen und in das DBF-Format exportieren, um sie in Legacy-Systeme zu integrieren.



{{< app/cells/assistant language="javascript" >}}