---
title: Aufteilen von Excel-Dateien in mehrere Dateien
description: Aspose.Cells ist eine C++-Bibliothek zur Arbeit mit Tabellenkalkulationsdateien, die das Aufteilen einer einzelnen Excel-Datei in mehrere Dateien unterstützt. Dieser Artikel beschreibt, wie Excel-Dateien aufgeteilt werden können, indem jedes Arbeitsblatt in eine separate Arbeitsmappe kopiert wird und indem bestimmte Zellbereiche in andere Arbeitsmappen kopiert werden.
keywords: Aspose.Cells, C++-Bibliothek, Tabellenkalkulation, Excel-Datei aufteilen, Arbeitsblatt kopieren, Bereich kopieren, mehrere Arbeitsmappen, als separate Dateien speichern
type: docs
weight: 195
url: /de/cpp/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Aufteilen einer einzelnen Excel-Datei in mehrere Dateien. Es gibt zwei Hauptmethoden: (1) durch Kopieren jedes Arbeitsblatts der Quellarbeitsmappe in eine neue Arbeitsmappe und Speichern jeder als separate Datei, und (2) durch Kopieren eines bestimmten Zellbereichs aus einem Arbeitsblatt in eine neue Arbeitsmappe. Beide Ansätze sind nützlich, wenn Sie Teilmengen von Daten verteilen, kleinere Berichte für verschiedene Empfänger erstellen oder Daten zur individuellen Verarbeitung isolieren müssen.

{{% /alert %}}

## **Einführung**

Es gibt viele reale Szenarien, in denen ein Entwickler eine einzelne Excel-Datei in mehrere kleinere Dateien aufteilen muss. Beispielsweise kann eine Arbeitsmappe ein Arbeitsblatt pro Abteilung enthalten, und jeder Abteilungsleiter muss nur sein eigenes Blatt erhalten. In anderen Fällen möchten Sie möglicherweise eine bestimmte Tabelle oder einen Datenblock aus einem Arbeitsblatt extrahieren und als eigenständige Datei per E-Mail versenden, ohne den Rest der Arbeitsmappe preiszugeben. Große konsolidierte Arbeitsmappen müssen möglicherweise auch in kleinere Teile aufgeteilt werden, um eine einfachere Handhabung, schnelleres Laden oder die nachgelagerte Verarbeitung durch andere Systeme zu ermöglichen.

Aspose.Cells bietet zwei flexible Ansätze für diese Aufgabe. Der erste Ansatz durchläuft jedes Arbeitsblatt in der Quellarbeitsmappe und kopiert dessen Inhalt in eine neue `Workbook`-Instanz, die jeweils als separate Datei gespeichert wird. Der zweite Ansatz konzentriert sich auf einen bestimmten Zellbereich innerhalb eines Arbeitsblatts und kopiert nur diesen Bereich in eine neue Arbeitsmappe. In beiden Fällen ist der allgemeine Ablauf derselbe: Laden der Quellarbeitsmappe mit der `Workbook`-Klasse, Zugriff auf die relevanten Daten über die `Worksheet`- und `Cells`-Objekte, Übertragen des Inhalts in eine Ziel-`Workbook` und anschließendes Speichern des Ziels auf der Festplatte.

## **Aufteilen einer Excel-Datei durch Kopieren jedes Arbeitsblatts in eine neue Arbeitsmappe**

### **Überblick über den Ansatz**

Bei diesem Ansatz wird die Quellarbeitsmappe einmal geöffnet, und dann wird für jedes `Worksheet` in der `Worksheets`-Sammlung eine neue Ziel-`Workbook` erstellt. Der Inhalt des Quellarbeitsblatts wird dann in das erste Arbeitsblatt der Zielarbeitsmappe kopiert, und die Zielarbeitsmappe wird als Datei gespeichert, deren Name vom Namen des Quellarbeitsblatts abgeleitet wird. Das Ergebnis ist eine Ausgabedatei pro Arbeitsblatt, wobei jede Ausgabedatei die Daten eines einzelnen Quellblatts enthält.

Diese Methode ist die richtige Wahl, wenn jedes Arbeitsblatt in Ihrer Quellarbeitsmappe eine logisch unabhängige Informationseinheit darstellt (z. B. eine Abteilung, Region, einen Monat oder eine Produktlinie) und Sie jede Einheit einzeln bereitstellen oder verarbeiten möchten.

### **Schritte**

Die folgenden Schritte beschreiben, wie eine Excel-Datei aufgeteilt wird, indem jedes Arbeitsblatt in eine neue Arbeitsmappe kopiert wird:

1. Öffnen Sie die Quell-Excel-Datei, indem Sie ein `Workbook`-Objekt instanziieren und den Dateipfad an seinen Konstruktor übergeben.
2. Durchlaufen Sie die `Workbook.Worksheets`-Sammlung mit einer `for`- oder `foreach`-Schleife, damit jedes `Worksheet` in der Quelldatei verarbeitet wird.
3. Erstellen Sie innerhalb der Schleife eine neue Ziel-`Workbook`-Instanz (eine leere Arbeitsmappe) für das aktuelle Arbeitsblatt.
4. Fügen Sie der Zielarbeitsmappe ein neues `Worksheet` hinzu (oder verwenden Sie das standardmäßige erste Arbeitsblatt) und weisen Sie ihm einen aussagekräftigen Namen zu, idealerweise denselben wie die `Name`-Eigenschaft des Quellarbeitsblatts.
5. Kopieren Sie den Inhalt des Quellarbeitsblatts in das Zielarbeitsblatt. Dies kann durch Iterieren der Zellen der `Cells`-Sammlung des Quellarbeitsblatts und Schreiben ihrer Werte in die entsprechenden Zellen des Zielarbeitsblatts erfolgen, oder durch Verwenden der Methode `Cells.Copy`, um einen gesamten Bereich auf einmal zu übertragen.
6. Erstellen Sie einen Ausgabedateipfad, der den Namen des Quellarbeitsblatts enthält (zum Beispiel `dataDir + worksheet.Name + ".xls"`), damit jede generierte Datei einen eindeutigen Namen hat.
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

Die erwartete Ausgabe ist eine Reihe neuer Dateien im Datenverzeichnis, eine Datei pro Arbeitsblatt aus der Quellarbeitsmappe. Jede Datei wird nach dem entsprechenden Quellblatt benannt, und die Datei enthält die Daten (und optional die Formatierung) dieses einzelnen Blattes.

## **Aufteilen einer Excel-Datei durch Kopieren eines Bereichs in eine neue Arbeitsmappe**

### **Überblick über den Ansatz**

Manchmal entsprechen die Daten, die Sie aufteilen müssen, nicht einem gesamten Arbeitsblatt, sondern einem bestimmten rechteckigen Bereich eines Arbeitsblatts, wie z. B. `A1:D10`, oder einem benannten Bereich, der eine bestimmte Tabelle darstellt. In diesen Fällen ist das Kopieren ganzer Arbeitsblätter ineffizient, und ein präziserer Ansatz ist erforderlich: Identifizieren Sie den Quellbereich, kopieren Sie nur diesen Bereich in eine neue Arbeitsmappe und speichern Sie die neue Datei.

Dieser Ansatz ist ideal, wenn Sie eine einzelne Tabelle, einen Berichtsblock oder einen Datenbereich aus einem größeren Arbeitsblatt extrahieren möchten, während Sie alle nicht zusammenhängenden Inhalte verwerfen. Er ist auch nützlich, um vom Benutzer ausgewählte Bereiche eines Blattes als eigenständige Dateien zu exportieren.

### **Schritte**

Die folgenden Schritte beschreiben, wie eine Excel-Datei aufgeteilt wird, indem ein bestimmter Bereich in eine neue Arbeitsmappe kopiert wird:

1. Öffnen Sie die Quell-Excel-Datei, indem Sie ein `Workbook`-Objekt mit dem Dateipfad instanziieren.
2. Rufen Sie das Ziel-`Worksheet` ab, das den Bereich enthält, den Sie kopieren möchten, entweder über den Index (zum Beispiel das erste Blatt) oder über den Namen aus der `Worksheets`-Sammlung.
3. Identifizieren Sie den zu kopierenden Bereich. Dies kann ein fest codierter Zellbereich wie `A1:C10` sein, oder ein benannter Bereich, der über die `Worksheet.Cells`-Sammlung abgerufen wird, oder ein Bereich, der über `Worksheet.Cells.CreateRange` erstellt wurde.
4. Erstellen Sie eine neue Ziel-`Workbook`-Instanz.
5. Greifen Sie auf das erste `Worksheet` der Zielarbeitsmappe zu (das Standardblatt).
6. Kopieren Sie den Quellbereich in das Zielarbeitsblatt, typischerweise beginnend bei Zelle `A1`. Die Methode `Cells.Copy` auf der Ziel-`Cells`-Sammlung kann verwendet werden, um einen gesamten Bereich zu kopieren, oder Sie können die Zellen des Quellbereichs durchlaufen und ihre Werte mit `PutValue` in die Zielzellen schreiben. Optional können `CopyOptions` angegeben werden, um zu steuern, was übertragen wird (nur Werte, Werte und Stile, Formeln usw.).
7. Speichern Sie die Zielarbeitsmappe unter einem neuen Dateipfad auf der Festplatte mit der Methode `Workbook.Save`.

### **Codebeispiel**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Datenverzeichnis und Dateipfade definieren
    std::string dataDir = "data/";
    std::string sourcePath = dataDir + "book1.xls";
    std::string outputPath = dataDir + "outputrange.xls";

    // Quell-Excel-Datei öffnen
    Workbook sourceWorkbook(U16String(sourcePath.c_str()));

    // Erstes Arbeitsblatt aus der Quellarbeitsmappe abrufen
    Worksheet sourceWorksheet = sourceWorkbook.GetWorksheets().Get(0);

    // Quellzellenbereich A1:C10 definieren (10 Zeilen, 3 Spalten ab Zeile 0, Spalte 0)
    Range sourceRange = sourceWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Neue Zielarbeitsmappe erstellen
    Workbook destWorkbook;

    // Auf das erste Arbeitsblatt in der Zielarbeitsmappe zugreifen
    Worksheet destWorksheet = destWorkbook.GetWorksheets().Get(0);

    // Zielbereich bei A1 mit den gleichen Abmessungen wie der Quellbereich erstellen
    Range destRange = destWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Quellbereich in den Zielbereich kopieren
    destRange.Copy(sourceRange);

    // Zielarbeitsmappe in einer neuen .xls-Datei speichern
    destWorkbook.Save(U16String(outputPath.c_str()), SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Die erwartete Ausgabe ist eine einzelne neue Datei im Datenverzeichnis, die nur die Werte (und optional die Formatierung) des angegebenen Bereichs enthält, der aus der Quellarbeitsmappe extrahiert wurde. Die Zieldatei hat keine Beziehung zu anderen Daten in der Quelldatei; sie enthält nur den extrahierten Bereich, beginnend bei Zelle `A1` ihres ersten Arbeitsblatts.

## **Verwandte Artikel**

- [Kopieren von Zeilen und Spalten](/cells/de/cpp/copying-rows-and-columns/)
- [Zusammenführen und Aufheben der Zusammenführung von Zellen](/cells/de/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}