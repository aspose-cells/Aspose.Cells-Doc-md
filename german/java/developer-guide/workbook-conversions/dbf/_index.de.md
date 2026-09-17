---
title: Lesen und Schreiben von DBF-Dateien
linktitle: Lesen und Schreiben von DBF-Dateien
description: Aspose.Cells ist eine Java-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Lesen und Schreiben von dBASE III- und IV-Dateien (DBF) unterstützt. Dieser Artikel erläutert, wie Sie mit Aspose.Cells Daten aus DBF-Dateien importieren und in DBF-Dateien exportieren können, einschließlich Dateiformatdetails, unterstützter Funktionen und schrittweiser Beispiele.
keywords: Aspose.Cells, Java-Bibliothek, DBF, dBASE, DBF lesen, DBF schreiben, DBF importieren, DBF exportieren, Dateiformat, .dbf
type: docs
weight: 200
url: /de/java/reading-and-writing-dbf-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet vollständige Unterstützung für das Lesen und Schreiben von DBF-Dateien (dBASE). Sie können vorhandene dBASE III- und dBASE IV-Dateien in ein Workbook-Objekt laden, die Daten mithilfe der umfangreichen Aspose.Cells-API bearbeiten und die Arbeitsmappe zur Verwendung mit älteren Datenbankanwendungen wieder im DBF-Format speichern.

## **Einführung**
DBF (DataBase File) ist ein älteres Datenbankdateiformat, das ursprünglich von dBASE in den frühen 1980er Jahren eingeführt wurde. Trotz des Alters des Formats werden DBF-Dateien in vielen Branchen immer noch häufig zur Speicherung strukturierter Daten verwendet, insbesondere in der Buchhaltung, im GIS und in anderen spezialisierten Anwendungen. Mit Aspose.Cells können Sie diese älteren Dateien nahtlos in moderne Java-Tabellenkalkulations-Workflows integrieren.
Die Bibliothek unterstützt sowohl das Lesen als auch das Schreiben von DBF-Dateien und bietet Ihnen folgende Möglichkeiten:
- Importieren von Daten aus vorhandenen DBF-Dateien in Aspose.Cells-Workbook-Objekte zur Weiterverarbeitung oder Konvertierung in andere Formate.
- Erstellen neuer DBF-Dateien von Grund auf oder durch Transformieren von Daten aus anderen Tabellenkalkulationsformaten.
- Beibehalten von Felddefinitionen, Datentypen und Datensatzstrukturen beim Übertragen von Daten in das und aus dem DBF-Format.
DBF-Dateien können auch direkt in Microsoft Excel und anderen Tabellenkalkulationsanwendungen geöffnet werden und stellen so eine praktische Brücke zwischen Altsystemen und modernen Tabellenkalkulationstools dar.

## **Unterstützte DBF-Versionen und Funktionen**
Aspose.Cells unterstützt die folgenden DBF-Formatversionen:
- **dBASE III** — Die ursprüngliche und am weitesten verbreitete Variante des DBF-Formats.
- **dBASE IV** — Eine erweiterte Version, die zusätzliche Datentypen und größere Feldgrößen unterstützt.

### Unterstützte Funktionen
Die Bibliothek bietet umfassende Unterstützung für die folgenden Vorgänge:
- Lesen von DBF-Daten in ein Workbook-Objekt, wobei alle Datensätze und Felddefinitionen erhalten bleiben.
- Zurückschreiben von Arbeitsmappendaten in das DBF-Format zum Export in dBASE-kompatible Anwendungen.
- Verarbeitung gängiger Datentypen, die in DBF-Dateien verwendet werden, einschließlich Zeichen-, numerischer, Datums- und boolescher Felder.
- Beibehalten von Felddefinitionen wie Feldname, Typ und Länge während Lese-/Schreibvorgängen.

### Einschränkungen und Überlegungen
Beachten Sie bei der Arbeit mit DBF-Dateien die folgenden Einschränkungen:
- Die maximale Anzahl von Feldern pro Datei beträgt **128**.
- Die maximale Datensatzgröße beträgt **4000 Bytes**.
- Feldnamen sind auf **10 Zeichen** begrenzt, müssen in Großbuchstaben angegeben werden und dürfen keine Leerzeichen enthalten.
- Datumswerte in DBF-Dateien werden im Format `YYYYMMDD` gespeichert.
- Die Zeichenkodierung kann je nach Quellanwendung variieren (häufig Windows-1252 oder OEM-Codepages).

## **Lesen einer DBF-Datei**
Aspose.Cells macht es einfach, Daten aus einer DBF-Datei in ein Workbook-Objekt zu laden. Die Bibliothek verwendet die Klasse `LoadOptions`, um das Quellformat anzugeben und sicherzustellen, dass die Daten während des Ladevorgangs korrekt interpretiert werden.

### Lesen einer DBF-Datei mit Aspose.Cells
Um eine DBF-Datei zu lesen, müssen Sie eine `LoadOptions`-Instanz erstellen, deren Eigenschaft `LoadFormat` auf `LoadFormat.Dbf` festlegen und sie zusammen mit dem Dateipfad an den `Workbook`-Konstruktor übergeben. Nach dem Laden sind die Daten über die `getWorksheets()`-Sammlung zugänglich, wo Sie durch Zellen iterieren, Werte extrahieren oder die Daten nach Bedarf bearbeiten können.
Das folgende Beispiel zeigt, wie Sie eine vorhandene DBF-Datei in Aspose.Cells laden, auf das erste Arbeitsblatt zugreifen und die Zellenwerte lesen.

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
Sie können DBF-Dateien direkt in Microsoft Excel öffnen, indem Sie die Datei im Dialogfeld „Öffnen" auswählen. Excel behandelt die DBF-Datei als Tabellenkalkulation und zeigt die Datensätze in einem tabellarischen Layout an. Dies ist nützlich, um die Daten nach dem Lesen oder Schreiben mit Aspose.Cells schnell zu überprüfen.

## **Schreiben einer DBF-Datei**
Das Schreiben von Daten in eine DBF-Datei folgt einem ähnlichen Muster wie das Speichern in einem anderen Tabellenkalkulationsformat mit Aspose.Cells. Sie erstellen oder laden ein Workbook, füllen das Arbeitsblatt mit Daten und rufen dann die Methode `save` auf, während Sie `SaveFormat.Dbf` als Zielformat angeben.

### Schreiben einer DBF-Datei mit Aspose.Cells
Um eine DBF-Datei zu erstellen, gehen Sie folgendermaßen vor:
1. Erstellen Sie eine neue `Workbook`-Instanz.
2. Greifen Sie auf das erste Arbeitsblatt aus der `getWorksheets()`-Sammlung zu.
3. Füllen Sie das Arbeitsblatt mit Ihren Daten, einschließlich Kopfzeilen in der ersten Zeile und Datensätzen in den nachfolgenden Zeilen.
4. Rufen Sie die Methode `Workbook.save` auf und übergeben Sie den Dateipfad und `SaveFormat.Dbf` als Parameter.
Das folgende Beispiel zeigt, wie Sie eine neue DBF-Datei von Grund auf erstellen. Es füllt ein Arbeitsblatt mit Beispieldaten, die verschiedene Datentypen (Zeichenketten, Zahlen und Datumsangaben) enthalten, um zu veranschaulichen, wie Feldtypen beim Export in das DBF-Format behandelt werden.

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

## **Überlegungen zu Datentypen und Formatierung**
Beim Übertragen von Daten zwischen Aspose.Cells und dem DBF-Format ist es wichtig zu verstehen, wie Datentypen zwischen den beiden Systemen zugeordnet werden, um die Datenintegrität sicherzustellen.

### Zelltypen zu DBF-Feldtypen
Zellwerte von Aspose.Cells werden beim Speichern automatisch in die entsprechenden DBF-Feldtypen konvertiert:
- **Zeichenketten** werden Zeichenfeldern (C) zugeordnet.
- **Numerische Werte** (Ganzzahlen und Dezimalzahlen) werden numerischen Feldern (N) zugeordnet.
- **Datumswerte** werden Datumsfeldern (D) im Format `YYYYMMDD` zugeordnet.
- **Boolesche Werte** werden logischen Feldern (L) zugeordnet.

### Kodierung
DBF-Dateien können je nach Anwendung, mit der sie erstellt wurden, unterschiedliche Zeichenkodierungen verwenden. Aspose.Cells verarbeitet die Kodierung in den meisten Fällen transparent. Wenn jedoch Anzeigeprobleme bei Zeichen auftreten, müssen Sie möglicherweise die Kodierung der Quelldatei überprüfen.

### Regeln für Feldnamen
DBF-Feldnamen müssen die folgenden Regeln einhalten:
- Maximale Länge von 10 Zeichen.
- Muss mit einem Buchstaben beginnen.
- Darf keine Leerzeichen oder Sonderzeichen enthalten.
- Wird unabhängig von der Groß-/Kleinschreibung in der Eingabe als Großbuchstaben gespeichert.

### Überprüfen der Ausgabe
Nach dem Schreiben einer DBF-Datei können Sie das Ergebnis überprüfen, indem Sie sie in Microsoft Excel oder einer beliebigen dBASE-kompatiblen Anwendung öffnen. Die Daten sollten in einem tabellarischen Layout mit den Feldnamen als Spaltenüberschriften angezeigt werden, und die Datensätze sollten gemäß den bereitgestellten Daten gefüllt sein.

## **Konvertieren zwischen DBF und anderen Formaten**
Einer der praktischsten Anwendungsfälle für das Lesen und Schreiben von DBF-Dateien mit Aspose.Cells ist die Konvertierung von Daten zwischen dem DBF-Format und modernen Tabellenkalkulationsformaten wie XLSX, XLS oder CSV. Da Aspose.Cells eine breite Palette von Formaten unterstützt, können Sie eine DBF-Datei problemlos laden und in einem anderen unterstützten Format speichern oder umgekehrt.
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="java" >}}