---
title: Aufteilen von Excel-Dateien in mehrere Dateien
linktitle: Aufteilen von Excel-Dateien in mehrere Dateien
description: Aspose.Cells ist eine C++-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Aufteilen einer einzelnen Excel-Datei in mehrere Dateien unterstützt. Dieser Artikel beschreibt, wie Excel-Dateien aufgeteilt werden, indem jedes Arbeitsblatt in eine separate Arbeitsmappe kopiert wird und indem bestimmte Zellbereiche in andere Arbeitsmappen kopiert werden.
keywords: Aspose.Cells, C++-Bibliothek, Tabellenkalkulation, Excel-Datei aufteilen, Arbeitsblatt kopieren, Bereich kopieren, mehrere Arbeitsmappen, als separate Dateien speichern
type: docs
weight: 195
url: /de/cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Aufteilen einer einzelnen Excel-Datei in mehrere Dateien. Es gibt zwei grundsätzliche Vorgehensweisen: (1) durch Kopieren jedes Arbeitsblatts der Quellarbeitsmappe in eine neue Arbeitsmappe und Speichern jeder einzelnen als separate Datei sowie (2) durch Kopieren eines bestimmten Zellbereichs aus einem Arbeitsblatt in eine neue Arbeitsmappe. Beide Ansätze sind nützlich, wenn Sie Teilmengen von Daten verteilen, kleinere Berichte für unterschiedliche Empfänger erstellen oder Daten zur Einzelverarbeitung isolieren müssen.

## **Einführung**
Es gibt viele reale Szenarien, in denen ein Entwickler eine einzelne Excel-Datei in mehrere kleinere Dateien zerlegen muss. Beispielsweise kann eine Arbeitsmappe ein Arbeitsblatt pro Abteilung enthalten, und jeder Abteilungsleiter muss nur sein eigenes Blatt erhalten. In anderen Fällen möchten Sie möglicherweise eine bestimmte Tabelle oder einen Datenblock aus einem Arbeitsblatt extrahieren und als eigenständige Datei per E-Mail versenden, ohne den Rest der Arbeitsmappe offenzulegen. Große konsolidierte Arbeitsmappen müssen möglicherweise auch in kleinere Teile zerlegt werden, um sie leichter handhaben zu können, schneller zu laden oder um sie von anderen Systemen weiterverarbeiten zu lassen.
Aspose.Cells bietet zwei flexible Ansätze für diese Aufgabe. Der erste Ansatz durchläuft jedes Arbeitsblatt in der Quellarbeitsmappe und kopiert dessen Inhalt in eine brandneue `Workbook`-Instanz, wobei jede als separate Datei gespeichert wird. Der zweite Ansatz konzentriert sich auf einen bestimmten Zellbereich innerhalb eines Arbeitsblatts und kopiert nur diesen Bereich in eine neue Arbeitsmappe. In beiden Fällen ist der allgemeine Ablauf gleich: Laden Sie die Quellarbeitsmappe mit der `Workbook`-Klasse, greifen Sie über die Objekte `Worksheet` und `Cells` auf die relevanten Daten zu, übertragen Sie den Inhalt in eine Ziel-`Workbook` und speichern Sie diese anschließend auf der Festplatte.

## **Aufteilen einer Excel-Datei durch Kopieren jedes Arbeitsblatts in eine neue Arbeitsmappe**

### **Überblick über den Ansatz**
Bei diesem Ansatz wird die Quellarbeitsmappe einmal geöffnet, und dann wird für jedes `Worksheet` in deren `Worksheets`-Auflistung eine neue Ziel-`Workbook` erstellt. Der Inhalt des Quellarbeitsblatts wird dann in das erste Arbeitsblatt der Zielarbeitsmappe kopiert, und die Zielarbeitsmappe wird als Datei gespeichert, deren Name aus dem Namen des Quellarbeitsblatts abgeleitet wird. Das Ergebnis ist eine Ausgabedatei pro Arbeitsblatt, wobei jede Ausgabedatei die Daten eines einzelnen Quellenblatts enthält.
Diese Methode ist die richtige Wahl, wenn jedes Arbeitsblatt in Ihrer Quellarbeitsmappe eine logisch unabhängige Informationseinheit darstellt (z. B. eine Abteilung, eine Region, einen Monat oder eine Produktlinie) und Sie jede Einheit einzeln ausliefern oder verarbeiten möchten.

### **Schritte**
Die folgenden Schritte beschreiben, wie eine Excel-Datei durch Kopieren jedes Arbeitsblatts in eine neue Arbeitsmappe aufgeteilt wird:
1. Öffnen Sie die Excel-Quelldatei, indem Sie ein `Workbook`-Objekt instanziieren und den Dateipfad an dessen Konstruktor übergeben.
2. Durchlaufen Sie die `Workbook.Worksheets`-Auflistung mit einer `for`- oder `foreach`-Schleife, sodass jedes `Worksheet` in der Quelldatei verarbeitet wird.
3. Erstellen Sie innerhalb der Schleife eine neue Ziel-`Workbook`-Instanz (eine leere Arbeitsmappe) für das aktuelle Arbeitsblatt.
5. Kopieren Sie den Inhalt des Quellarbeitsblatts in das Zielarbeitsblatt. Dies kann erfolgen, indem die Zellen der `Cells`-Auflistung des Quellarbeitsblatts durchlaufen und deren Werte in die entsprechenden Zellen des Zielarbeitsblatts geschrieben werden, oder indem die Methode `Cells.Copy` verwendet wird, um einen gesamten Bereich auf einmal zu übertragen.
6. Erstellen Sie einen Ausgabedateipfad, der den Namen des Quellarbeitsblatts enthält (z. B. `dataDir + worksheet.Name + ".xls"`), damit jede erzeugte Datei einen eindeutigen Namen hat.
7. Rufen Sie die Methode `Workbook.Save` der Zielarbeitsmappe auf, um die Datei auf die Festplatte zu schreiben.
8. Wiederholen Sie die Schritte 3 bis 7 für das nächste Arbeitsblatt, bis alle Arbeitsblätter verarbeitet wurden.

### **Codebeispiel**

```cpp
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string dataDir = "data/";
    Workbook wb(U16String((dataDir + "book1.xls").c_str()));
    int sheetCount = wb.GetWorksheets().GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet sourceSheet = wb.GetWorksheets().Get(i);
        U16String sheetName = sourceSheet.GetName();
        Workbook destWorkbook;
        int destIndex = destWorkbook.GetWorksheets().Add();
        Worksheet destSheet = destWorkbook.GetWorksheets().Get(destIndex);
        destSheet.SetName(sheetName);
        destSheet.Copy(sourceSheet);
        std::string destFile = dataDir + sheetName.ToUtf8() + ".xls";
        destWorkbook.Save(U16String(destFile.c_str()), SaveFormat::Excel97To2003);
    }
    Aspose::Cells::Cleanup();
    return 0;
}
```

Die erwartete Ausgabe ist ein Satz neuer Dateien im Datenverzeichnis, eine Datei pro Arbeitsblatt aus der Quellarbeitsmappe. Jede Datei wird nach dem entsprechenden Quellblatt benannt, und die Datei enthält die Daten (und optional die Formatierung) dieses einzelnen Blatts.

## **Aufteilen einer Excel-Datei durch Kopieren eines Bereichs in eine neue Arbeitsmappe**

### **Überblick über den Ansatz**
Manchmal entsprechen die Daten, die Sie aufteilen möchten, nicht einem gesamten Arbeitsblatt, sondern einem bestimmten rechteckigen Bereich eines Arbeitsblatts, wie z. B. `A1:D10` oder einem benannten Bereich, der eine bestimmte Tabelle darstellt. In diesen Fällen ist das Kopieren ganzer Arbeitsblätter verschwenderisch, und es ist ein präziserer Ansatz erforderlich: Identifizieren Sie den Quellbereich, kopieren Sie nur diesen Bereich in eine neue Arbeitsmappe, und speichern Sie die neue Datei.
Dieser Ansatz ist ideal, wenn Sie eine einzelne Tabelle, einen Berichtsblock oder einen Datenbereich aus einem größeren Arbeitsblatt extrahieren möchten, während Sie alle nicht verwandten Inhalte verwerfen. Er ist auch nützlich, um vom Benutzer ausgewählte Bereiche eines Blatts als eigenständige Dateien zu exportieren.

### **Schritte**
Die folgenden Schritte beschreiben, wie eine Excel-Datei durch Kopieren eines bestimmten Bereichs in eine neue Arbeitsmappe aufgeteilt wird:
1. Öffnen Sie die Excel-Quelldatei, indem Sie ein `Workbook`-Objekt mit dem Dateipfad instanziieren.
2. Rufen Sie das Ziel-`Worksheet` ab, das den Bereich enthält, den Sie kopieren möchten, entweder über den Index (z. B. das erste Blatt) oder über den Namen aus der `Worksheets`-Auflistung.
3. Identifizieren Sie den zu kopierenden Bereich. Dies kann ein fest codierter Zellbereich wie `A1:C10` sein, oder ein benannter Bereich, der über die Auflistung `Worksheet.Cells` abgerufen wird, oder ein Bereich, der über `Worksheet.Cells.CreateRange` erstellt wurde.
4. Erstellen Sie eine neue Ziel-`Workbook`-Instanz.
5. Greifen Sie auf das erste `Worksheet` der Zielarbeitsmappe zu (das Standardblatt).
6. Kopieren Sie den Quellbereich in das Zielarbeitsblatt, typischerweise beginnend bei Zelle `A1`. Die Methode `Cells.Copy` auf der `Cells`-Auflistung des Ziels kann verwendet werden, um einen gesamten Bereich zu kopieren, oder Sie können die Zellen des Quellbereichs durchlaufen und deren Werte mit `PutValue` in die Zielzellen schreiben. Optionale `CopyOptions` können angegeben werden, um zu steuern, was übertragen wird (nur Werte, Werte und Stile, Formeln usw.).
7. Speichern Sie die Zielarbeitsmappe unter einem neuen Dateipfad auf der Festplatte mit der Methode `Workbook.Save`.

### **Codebeispiel**
Die erwartete Ausgabe ist eine einzelne neue Datei im Datenverzeichnis, die nur die Werte (und optional die Formatierung) des angegebenen Bereichs enthält, der aus der Quellarbeitsmappe extrahiert wurde. Die Zieldatei hat keine Beziehung zu anderen Daten in der Quelldatei; sie enthält nur den extrahierten Bereich, beginnend bei Zelle `A1` des ersten Arbeitsblatts.
{{% /alert %}}

## Verwandte Artikel
- [Hinzufügen von Filterfeldern zu einer PivotTable in Aspose.Cells for C++](/cells/de/cpp/add-page-field-in-pivot-table/)
- [Anwenden von Stilen auf PivotTables in Aspose.Cells for C++](/cells/de/cpp/apply-style-to-pivot-table/)
- [Ändern des Seitenfeld-Layouts in einer PivotTable](/cells/de/cpp/change-page-field-layout/)
- [Konvertieren einer Sparkline in ein Bild und HTML in Aspose.Cells for C++](/cells/de/cpp/convert-sparkline-to-image-and-html/)
- [Konvertieren von Excel in das OFD-Format](/cells/de/cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="cpp" >}}