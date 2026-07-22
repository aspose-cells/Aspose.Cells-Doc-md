---
title: Lesen und Schreiben von DBF-Dateien
linktitle: Lesen und Schreiben von
description: Aspose.Cells ist eine C++-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Lesen und Schreiben von dBASE III- und IV-Dateien (DBF) unterstützt. Dieser Artikel erklärt, wie Daten mit Aspose.Cells aus DBF-Dateien importiert und in diese exportiert werden, einschließlich Dateiformatdetails, unterstützter Funktionen und Schritt-für-Schritt-Beispielen.
keywords: Aspose.Cells, C++-Bibliothek, DBF, dBASE, DBF lesen, DBF schreiben, DBF importieren, DBF exportieren, Dateiformat, .dbf
type: docs
weight: 200
url: /de/cpp/reading-and-writing-dbf-files/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells bietet vollständige Unterstützung für das Lesen und Schreiben von DBF-Dateien (dBASE). Sie können bestehende dBASE III- und dBASE IV-Dateien in ein Workbook-Objekt laden, die Daten mithilfe der umfangreichen Aspose.Cells-API bearbeiten und die Arbeitsmappe zur Verwendung mit Legacy-Datenbankanwendungen wieder im DBF-Format speichern.

{{% /alert %}}

## **Einführung**

DBF (DataBase File) ist ein Legacy-Datenbankdateiformat, das ursprünglich in den frühen 1980er Jahren von dBASE eingeführt wurde. Trotz des Alters des Formats werden DBF-Dateien in vielen Branchen weiterhin häufig zur Speicherung strukturierter Daten verwendet, insbesondere im Rechnungswesen, GIS und anderen spezialisierten Anwendungen. Aspose.Cells ermöglicht Ihnen die nahtlose Integration dieser Legacy-Dateien in moderne C++-Spreadsheet-Workflows.

Die Bibliothek unterstützt sowohl das Lesen als auch das Schreiben von DBF-Dateien und bietet Ihnen folgende Möglichkeiten:

- Importieren von Daten aus bestehenden DBF-Dateien in Aspose.Cells Workbook-Objekte zur weiteren Verarbeitung oder Konvertierung in andere Formate.
- Erstellen neuer DBF-Dateien von Grund auf oder durch Transformation von Daten aus anderen Tabellenkalkulationsformaten.
- Beibehalten von Felddefinitionen, Datentypen und Datensatzstrukturen beim Übertragen von Daten in und aus dem DBF-Format.

DBF-Dateien können auch direkt in Microsoft Excel und anderen Tabellenkalkulationsanwendungen geöffnet werden, was sie zu einer praktischen Brücke zwischen Legacy-Systemen und modernen Tabellenkalkulationstools macht.

## **Unterstützte DBF-Versionen und Funktionen**

Aspose.Cells unterstützt die folgenden DBF-Formatversionen:

- **dBASE III** — Die ursprüngliche und am weitesten verbreitete Variante des DBF-Formats.
- **dBASE IV** — Eine erweiterte Version, die zusätzliche Datentypen und größere Feldgrößen unterstützt.

### Unterstützte Funktionen

Die Bibliothek bietet umfassende Unterstützung für die folgenden Operationen:

- Lesen von DBF-Daten in ein Workbook-Objekt, wobei alle Datensätze und Felddefinitionen erhalten bleiben.
- Zurückschreiben von Workbook-Daten in das DBF-Format zum Export in dBASE-kompatible Anwendungen.
- Verarbeitung gängiger Datentypen in DBF-Dateien, einschließlich Zeichen-, numerischer, Datums- und logischer Felder.
- Beibehalten von Felddefinitionen wie Feldname, Typ und Länge während Lese-/Schreiboperationen.

### Einschränkungen und Hinweise

Beachten Sie bei der Arbeit mit DBF-Dateien die folgenden Beschränkungen:

- Die maximale Anzahl von Feldern pro Datei beträgt **128**.
- Die maximale Datensatzgröße beträgt **4000 Bytes**.
- Feldnamen sind auf **10 Zeichen** begrenzt, müssen in Großbuchstaben geschrieben sein und dürfen keine Leerzeichen enthalten.
- Datumswerte in DBF-Dateien werden im Format `YYYYMMDD` gespeichert.
- Die Zeichenkodierung kann je nach Quellanwendung variieren (häufig Windows-1252 oder OEM-Codepages).

## **Lesen einer DBF-Datei**

Aspose.Cells macht es einfach, Daten aus einer DBF-Datei in ein Workbook-Objekt zu laden. Die Bibliothek verwendet die Klasse `LoadOptions`, um das Quellformat anzugeben und sicherzustellen, dass die Daten während des Ladevorgangs korrekt interpretiert werden.

### Lesen einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu lesen, müssen Sie eine `LoadOptions`-Instanz erstellen, deren Eigenschaft `LoadFormat` auf `LoadFormat.Dbf` setzen und sie zusammen mit dem Dateipfad an den `Workbook`-Konstruktor übergeben. Nach dem Laden sind die Daten über die `Worksheets`-Sammlung zugänglich, wo Sie durch Zellen iterieren, Werte extrahieren oder die Daten nach Bedarf bearbeiten können.

Das folgende Beispiel zeigt, wie eine bestehende DBF-Datei in Aspose.Cells geladen, auf das erste Arbeitsblatt zugegriffen und die Zellenwerte gelesen werden.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "Data/";
    std::string filePath = dataDir + "example.dbf";

    LoadOptions loadOptions(LoadFormat::Dbf);

    Workbook workbook(U16String(filePath.c_str()), loadOptions);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    std::string sb = "";

    int maxRow = cells.GetMaxDataRow();
    int maxCol = cells.GetMaxDataColumn();

    for (int i = 0; i <= maxRow; i++) {
        for (int j = 0; j <= maxCol; j++) {
            Cell cell = cells.Get(i, j);
            U16String value = cell.GetStringValue();
            sb += "|";
            sb += value.ToUtf8();
        }
        sb += "|";
        sb += "\n";
    }

    std::cout << sb << std::endl;

    std::string outputPath = dataDir + "output.xlsx";
    workbook.Save(U16String(outputPath.c_str()), SaveFormat::Xlsx);

    std::cout << "DBF file loaded successfully. Converted XLSX saved at: " << outputPath << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Sie können DBF-Dateien direkt in Microsoft Excel öffnen, indem Sie die Datei im Dialogfeld „Öffnen" auswählen. Excel behandelt die DBF-Datei als Tabellenblatt und zeigt ihre Datensätze in einer tabellarischen Darstellung an. Dies ist nützlich, um die Daten nach dem Lesen oder Schreiben mit Aspose.Cells schnell zu überprüfen.

{{% /alert %}}

## **Schreiben einer DBF-Datei**

Das Schreiben von Daten in eine DBF-Datei folgt einem ähnlichen Muster wie das Speichern in jedem anderen Tabellenkalkulationsformat mit Aspose.Cells. Sie erstellen oder laden ein Workbook, füllen das Arbeitsblatt mit Daten und rufen dann die Methode `Save` auf, wobei Sie `SaveFormat.Dbf` als Zielformat angeben.

### Schreiben einer DBF-Datei mit Aspose.Cells

Um eine DBF-Datei zu erstellen, gehen Sie folgendermaßen vor:

1. Erstellen Sie eine neue `Workbook`-Instanz.
2. Greifen Sie auf das erste Arbeitsblatt aus der `Worksheets`-Sammlung zu.
3. Füllen Sie das Arbeitsblatt mit Ihren Daten, einschließlich Kopfzeilen in der ersten Zeile und Datensätzen in den nachfolgenden Zeilen.
4. Rufen Sie die Methode `Workbook.Save` auf und übergeben Sie den Dateipfad und `SaveFormat.Dbf` als Parameter.

Das folgende Beispiel zeigt, wie eine neue DBF-Datei von Grund auf erstellt wird. Es füllt ein Arbeitsblatt mit Beispieldaten, die verschiedene Datentypen enthalten (Zeichenketten, Zahlen und Datumsangaben), um zu veranschaulichen, wie Feldtypen beim Export in das DBF-Format behandelt werden.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string outputDir = "C:/Output/";
    std::string filePath = outputDir + "output.dbf";

    if (!std::filesystem::exists(outputDir)) {
        std::filesystem::create_directories(outputDir);
    }

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Spaltenüberschriften
    cells.Get(0, 0).PutValue(u"ID");
    cells.Get(0, 1).PutValue(u"Name");
    cells.Get(0, 2).PutValue(u"Department");
    cells.Get(0, 3).PutValue(u"Salary");
    cells.Get(0, 4).PutValue(u"HireDate");

    // Datenzeile 1
    cells.Get(1, 0).PutValue(101);
    cells.Get(1, 1).PutValue(u"John Smith");
    cells.Get(1, 2).PutValue(u"Engineering");
    cells.Get(1, 3).PutValue(75000.50);
    Date hireDate1{2020, 3, 15, 0, 0, 0, 0};
    cells.Get(1, 4).PutValue(hireDate1);

    // Datenzeile 2
    cells.Get(2, 0).PutValue(102);
    cells.Get(2, 1).PutValue(u"Jane Doe");
    cells.Get(2, 2).PutValue(u"Marketing");
    cells.Get(2, 3).PutValue(68000.75);
    Date hireDate2{2019, 7, 22, 0, 0, 0, 0};
    cells.Get(2, 4).PutValue(hireDate2);

    // Datenzeile 3
    cells.Get(3, 0).PutValue(103);
    cells.Get(3, 1).PutValue(u"Bob Johnson");
    cells.Get(3, 2).PutValue(u"Finance");
    cells.Get(3, 3).PutValue(82000.00);
    Date hireDate3{2021, 1, 10, 0, 0, 0, 0};
    cells.Get(3, 4).PutValue(hireDate3);

    // Datenzeile 4
    cells.Get(4, 0).PutValue(104);
    cells.Get(4, 1).PutValue(u"Alice Brown");
    cells.Get(4, 2).PutValue(u"Human Resources");
    cells.Get(4, 3).PutValue(71000.25);
    Date hireDate4{2018, 11, 5, 0, 0, 0, 0};
    cells.Get(4, 4).PutValue(hireDate4);

    // Datenzeile 5
    cells.Get(5, 0).PutValue(105);
    cells.Get(5, 1).PutValue(u"Charlie Wilson");
    cells.Get(5, 2).PutValue(u"Operations");
    cells.Get(5, 3).PutValue(79500.80);
    Date hireDate5{2022, 5, 30, 0, 0, 0, 0};
    cells.Get(5, 4).PutValue(hireDate5);

    // Spaltenbreiten für bessere Lesbarkeit festlegen
    worksheet.GetCells().SetColumnWidth(0, 8);
    worksheet.GetCells().SetColumnWidth(1, 20);
    worksheet.GetCells().SetColumnWidth(2, 20);
    worksheet.GetCells().SetColumnWidth(3, 12);
    worksheet.GetCells().SetColumnWidth(4, 14);

    workbook.Save(U16String(filePath.c_str()), SaveFormat::Dbf);

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Stellen Sie beim Schreiben von Daten in eine DBF-Datei sicher, dass Ihre Daten den Einschränkungen des Formats entsprechen. Feldnamen sollten nicht länger als 10 Zeichen sein und keine Leerzeichen enthalten. Datensätze, die insgesamt 4000 Bytes überschreiten, werden nicht korrekt gespeichert. Datumsangaben sollten gültige Datumswerte sein, die im Format YYYYMMDD dargestellt werden können.

{{% /alert %}}

## **Überlegungen zu Datentypen und Formatierung**

Beim Übertragen von Daten zwischen Aspose.Cells und dem DBF-Format ist es wichtig zu verstehen, wie Datentypen zwischen den beiden Systemen zugeordnet werden, um die Datenintegrität zu gewährleisten.

### Zelltypen zu DBF-Feldtypen

Aspose.Cells-Zellwerte werden beim Speichern automatisch in die entsprechenden DBF-Feldtypen konvertiert:

- **Zeichenketten** werden auf Zeichenfelder (C) abgebildet.
- **Numerische Werte** (Ganzzahlen und Dezimalzahlen) werden auf numerische Felder (N) abgebildet.
- **Datumswerte** werden auf Datumsfelder (D) im Format `YYYYMMDD` abgebildet.
- **Boolesche Werte** werden auf logische Felder (L) abgebildet.

### Kodierung

DBF-Dateien können je nach Anwendung, die sie erstellt hat, unterschiedliche Zeichenkodierungen verwenden. Aspose.Cells verarbeitet die Kodierung in den meisten Fällen transparent, aber wenn Probleme bei der Zeichenanzeige auftreten, müssen Sie möglicherweise die Kodierung der Quelldatei überprüfen.

### Regeln für Feldnamen

DBF-Feldnamen müssen die folgenden Regeln einhalten:

- Maximale Länge von 10 Zeichen.
- Müssen mit einem Buchstaben beginnen.
- Dürfen keine Leerzeichen oder Sonderzeichen enthalten.
- Werden unabhängig von der Groß-/Kleinschreibung in der Eingabe in Großbuchstaben gespeichert.

### Überprüfen der Ausgabe

Nach dem Schreiben einer DBF-Datei können Sie das Ergebnis überprüfen, indem Sie sie in Microsoft Excel oder einer beliebigen dBASE-kompatiblen Anwendung öffnen. Die Daten sollten in einer tabellarischen Darstellung erscheinen, mit den Feldnamen als Spaltenüberschriften und den Datensätzen, die gemäß den von Ihnen bereitgestellten Daten gefüllt sind.

## **Konvertieren zwischen DBF und anderen Formaten**

Einer der praktischsten Anwendungsfälle für das Lesen und Schreiben von DBF-Dateien mit Aspose.Cells ist die Konvertierung von Daten zwischen dem DBF-Format und modernen Tabellenkalkulationsformaten wie XLSX, XLS oder CSV. Da Aspose.Cells eine breite Palette von Formaten unterstützt, können Sie eine DBF-Datei einfach laden und in einem anderen unterstützten Format neu speichern oder umgekehrt.

Sie können beispielsweise eine DBF-Datei lesen, Formatierungen oder Berechnungen mit der Aspose.Cells API anwenden und das Ergebnis dann als XLSX-Datei speichern, um es an Benutzer zu verteilen, die mit modernen Tabellenkalkulationsanwendungen arbeiten. Umgekehrt können Sie Daten aus einer XLSX- oder CSV-Datei nehmen und in das DBF-Format exportieren, um sie in Legacy-Systeme zu integrieren.



{{< app/cells/assistant language="cpp" >}}