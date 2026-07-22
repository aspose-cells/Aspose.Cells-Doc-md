---
title: Lesen und Schreiben von DBF-Dateien
linktitle: Lesen und Schreiben von
description: Aspose.Cells ist eine Java-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Lesen und Schreiben von dBASE III- und IV-Dateien (DBF) unterstützt. Dieser Artikel erklärt, wie Sie mit Aspose.Cells Daten aus DBF-Dateien importieren und in DBF-Dateien exportieren, einschließlich Dateiformatdetails, unterstützten Funktionen und schrittweisen Beispielen.
keywords: Aspose.Cells, Java-Bibliothek, DBF, dBASE, DBF lesen, DBF schreiben, DBF importieren, DBF exportieren, Dateiformat, .dbf
type: docs
weight: 200
url: /de/java/reading-and-writing-dbf-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells bietet vollständige Unterstützung für das Lesen und Schreiben von DBF- (dBASE-) Dateien. Sie können bestehende dBASE III- und dBASE IV-Dateien in ein Workbook-Objekt laden, die Daten mithilfe der umfangreichen Aspose.Cells-API bearbeiten und die Arbeitsmappe zur Verwendung mit älteren Datenbankanwendungen wieder im DBF-Format speichern.

{{% /alert %}}

## **Einführung**

DBF (DataBase File) ist ein älteres Datenbankdateiformat, das ursprünglich Anfang der 1980er Jahre von dBASE eingeführt wurde. Trotz des Alters des Formats werden DBF-Dateien in vielen Branchen weiterhin häufig zum Speichern strukturierter Daten verwendet, insbesondere in der Buchhaltung, im GIS und in anderen spezialisierten Anwendungen. Aspose.Cells ermöglicht es Ihnen, diese älteren Dateien nahtlos in moderne Java-Tabellenkalkulations-Workflows zu integrieren.

Die Bibliothek unterstützt sowohl das Lesen als auch das Schreiben von DBF-Dateien und bietet Ihnen folgende Möglichkeiten:

- Importieren von Daten aus bestehenden DBF-Dateien in Aspose.Cells-Workbook-Objekten zur weiteren Verarbeitung oder Konvertierung in andere Formate.
- Erstellen neuer DBF-Dateien von Grund auf oder durch Umwandlung von Daten aus anderen Tabellenkalkulationsformaten.
- Beibehalten von Felddefinitionen, Datentypen und Datensatzstrukturen beim Übertragen von Daten in und aus dem DBF-Format.

DBF-Dateien können auch direkt in Microsoft Excel und anderen Tabellenkalkulationsanwendungen geöffnet werden, was sie zu einer praktischen Brücke zwischen Altsystemen und modernen Tabellenkalkulationstools macht.

## **Unterstützte DBF-Versionen und Funktionen**

Aspose.Cells unterstützt die folgenden DBF-Formatversionen:

- **dBASE III** — Die ursprüngliche und am weitesten verbreitete Variante des DBF-Formats.
- **dBASE IV** — Eine erweiterte Version, die zusätzliche Datentypen und größere Feldgrößen unterstützt.

### Unterstützte Funktionen

Die Bibliothek bietet umfassende Unterstützung für die folgenden Operationen:

- Lesen von DBF-Daten in ein Workbook-Objekt, wobei alle Datensätze und Felddefinitionen erhalten bleiben.
- Zurückschreiben von Workbook-Daten in das DBF-Format für den Export in dBASE-kompatible Anwendungen.
- Verarbeitung gängiger Datentypen, die in DBF-Dateien verwendet werden, einschließlich Zeichen-, numerische, Datums- und logische Felder.
- Beibehaltung von Felddefinitionen wie Feldname, Typ und Länge bei Lese-/Schreiboperationen.

### Einschränkungen und Überlegungen

Beachten Sie bei der Arbeit mit DBF-Dateien die folgenden Beschränkungen:

- Die maximale Anzahl von Feldern pro Datei beträgt **128**.
- Die maximale Datensatzgröße beträgt **4000 Bytes**.
- Feldnamen sind auf **10 Zeichen** begrenzt, müssen in Großbuchstaben geschrieben sein und dürfen keine Leerzeichen enthalten.
- Datumswerte in DBF-Dateien werden im Format `YYYYMMDD` gespeichert.
- Die Zeichenkodierung kann je nach Quellanwendung variieren (üblicherweise Windows-1252 oder OEM-Codepages).

## **Lesen einer DBF-Datei**

Aspose.Cells macht es einfach, Daten aus einer DBF-Datei in ein Workbook-Objekt zu laden. Die Bibliothek verwendet die `LoadOptions`-Klasse, um das Quellformat anzugeben, und stellt sicher, dass die Daten während des Ladevorgangs korrekt interpretiert werden.

### Lesen einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu lesen, müssen Sie eine `LoadOptions`-Instanz erstellen, deren `LoadFormat`-Eigenschaft auf `LoadFormat.Dbf` setzen und sie zusammen mit dem Dateipfad an den `Workbook`-Konstruktor übergeben. Nach dem Laden sind die Daten über die `getWorksheets()`-Sammlung zugänglich, wo Sie durch die Zellen iterieren, Werte extrahieren oder die Daten nach Bedarf bearbeiten können.

Das folgende Beispiel zeigt, wie eine bestehende DBF-Datei in Aspose.Cells geladen wird, wie auf das erste Arbeitsblatt zugegriffen wird und wie die Zellenwerte gelesen werden.

```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "Data/";
String filePath = new File(new File(dataDir), "example.dbf").getPath();

LoadOptions loadOptions = new LoadOptions(LoadFormat.DBF);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

StringBuilder sb = new StringBuilder();

int maxRow = cells.getMaxDataRow();
int maxCol = cells.getMaxDataColumn();

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells.get(i, j);
        String value = cell.getStringValue();
        sb.append("|").append(value);
    }
    sb.append("|").append(System.lineSeparator());
}

System.out.println(sb.toString());

String outputPath = new File(new File(dataDir), "output.xlsx").getPath();
workbook.save(outputPath, SaveFormat.XLSX);

System.out.println("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Sie können DBF-Dateien direkt in Microsoft Excel öffnen, indem Sie die Datei im Dialogfeld Öffnen auswählen. Excel behandelt die DBF-Datei als Tabellenkalkulation und zeigt ihre Datensätze in einem tabellarischen Layout an. Dies ist nützlich, um die Daten nach dem Lesen oder Schreiben mit Aspose.Cells schnell zu überprüfen.

{{% /alert %}}

## **Schreiben einer DBF-Datei**

Das Schreiben von Daten in eine DBF-Datei folgt einem ähnlichen Muster wie das Speichern in einem anderen Tabellenkalkulationsformat mit Aspose.Cells. Sie erstellen oder laden ein Workbook, füllen das Arbeitsblatt mit Daten und rufen dann die `save`-Methode auf, wobei Sie `SaveFormat.Dbf` als Zielformat angeben.

### Schreiben einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu erstellen, gehen Sie folgendermaßen vor:

1. Erstellen Sie eine neue `Workbook`-Instanz.
2. Greifen Sie auf das erste Arbeitsblatt aus der `getWorksheets()`-Sammlung zu.
3. Füllen Sie das Arbeitsblatt mit Ihren Daten, einschließlich Kopfzeilen in der ersten Zeile und Datensätzen in den nachfolgenden Zeilen.
4. Rufen Sie die `Workbook.save`-Methode auf und übergeben Sie den Dateipfad und `SaveFormat.Dbf` als Parameter.

Das folgende Beispiel zeigt, wie eine neue DBF-Datei von Grund auf erstellt wird. Es füllt ein Arbeitsblatt mit Beispieldaten, die verschiedene Datentypen enthalten (Zeichenketten, Zahlen und Datumsangaben), um zu veranschaulichen, wie Feldtypen beim Export in das DBF-Format behandelt werden.

```java
import com.aspose.cells.*;
import java.io.File;
import java.util.GregorianCalendar;

String outputDir = "C:\\Output\\";
String filePath = new File(new File(outputDir), "output.dbf").getPath();

if (!new File(outputDir).exists())
{
    new File(outputDir).mkdirs();
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();

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
cells.get(1, 4).putValue(new GregorianCalendar(2020, 2, 15).getTime());

// Datenzeile 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new GregorianCalendar(2019, 6, 22).getTime());

// Datenzeile 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new GregorianCalendar(2021, 0, 10).getTime());

// Datenzeile 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new GregorianCalendar(2018, 10, 5).getTime());

// Datenzeile 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new GregorianCalendar(2022, 4, 30).getTime());

// Spaltenbreiten für bessere Lesbarkeit festlegen
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);

workbook.save(filePath, SaveFormat.DBF);
```

{{% alert color="primary" %}}

Stellen Sie beim Schreiben von Daten in eine DBF-Datei sicher, dass Ihre Daten den Einschränkungen des Formats entsprechen. Feldnamen sollten nicht länger als 10 Zeichen sein und keine Leerzeichen enthalten. Datensätze, die insgesamt 4000 Bytes überschreiten, werden nicht korrekt gespeichert. Datumsangaben sollten gültige Datumswerte sein, die im Format YYYYMMDD dargestellt werden können.

{{% /alert %}}

## **Überlegungen zu Datentypen und Formatierung**

Beim Übertragen von Daten zwischen Aspose.Cells und dem DBF-Format ist es wichtig zu verstehen, wie Datentypen zwischen den beiden Systemen zugeordnet werden, um die Datenintegrität zu gewährleisten.

### Zelltypen zu DBF-Feldtypen

Aspose.Cells-Zellenwerte werden beim Speichern automatisch in die entsprechenden DBF-Feldtypen konvertiert:

- **Zeichenketten** werden Zeichenfeldern (C) zugeordnet.
- **Numerische Werte** (Ganzzahlen und Dezimalzahlen) werden numerischen Feldern (N) zugeordnet.
- **Datumswerte** werden Datumsfeldern (D) im Format `YYYYMMDD` zugeordnet.
- **Boolesche Werte** werden logischen Feldern (L) zugeordnet.

### Kodierung

DBF-Dateien können je nach Anwendung, die sie erstellt hat, unterschiedliche Zeichenkodierungen verwenden. Aspose.Cells verarbeitet die Kodierung in den meisten Fällen transparent. Wenn Sie jedoch Anzeigeprobleme mit Zeichen feststellen, müssen Sie möglicherweise die Kodierung der Quelldatei überprüfen.

### Regeln für Feldnamen

DBF-Feldnamen müssen die folgenden Regeln einhalten:

- Maximale Länge von 10 Zeichen.
- Muss mit einem Buchstaben beginnen.
- Darf keine Leerzeichen oder Sonderzeichen enthalten.
- Wird unabhängig von der in der Eingabe verwendeten Groß-/Kleinschreibung in Großbuchstaben gespeichert.

### Überprüfen der Ausgabe

Nach dem Schreiben einer DBF-Datei können Sie das Ergebnis überprüfen, indem Sie sie in Microsoft Excel oder einer anderen dBASE-kompatiblen Anwendung öffnen. Die Daten sollten in einem tabellarischen Layout angezeigt werden, wobei die Feldnamen als Spaltenüberschriften und die Datensätze gemäß den von Ihnen bereitgestellten Daten erscheinen.

## **Konvertieren zwischen DBF und anderen Formaten**

Einer der praktischsten Anwendungsfälle für das Lesen und Schreiben von DBF-Dateien mit Aspose.Cells ist die Konvertierung von Daten zwischen dem DBF-Format und modernen Tabellenkalkulationsformaten wie XLSX, XLS oder CSV. Da Aspose.Cells eine Vielzahl von Formaten unterstützt, können Sie eine DBF-Datei einfach laden und in einem anderen unterstützten Format erneut speichern oder umgekehrt.

Beispielsweise können Sie eine DBF-Datei lesen, Formatierungen oder Berechnungen mit der Aspose.Cells-API anwenden und das Ergebnis dann als XLSX-Datei speichern, um sie an Benutzer zu verteilen, die mit modernen Tabellenkalkulationsanwendungen arbeiten. Umgekehrt können Sie Daten aus einer XLSX- oder CSV-Datei nehmen und in das DBF-Format exportieren, um sie in Altsysteme zu integrieren.



{{< app/cells/assistant language="java" >}}