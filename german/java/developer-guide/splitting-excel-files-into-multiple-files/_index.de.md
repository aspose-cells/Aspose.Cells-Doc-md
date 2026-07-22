---
title: Aufteilen von Excel-Dateien in mehrere Dateien
linktitle: Aufteilen von Excel-Dateien
description: Aspose.Cells ist eine Java-Bibliothek für die Arbeit mit Tabellenkalkulationsdateien, die das Aufteilen einer einzelnen Excel-Datei in mehrere Dateien unterstützt. Dieser Artikel beschreibt, wie Excel-Dateien aufgeteilt werden, indem jedes Arbeitsblatt in eine separate Arbeitsmappe kopiert wird und indem bestimmte Zellbereiche in andere Arbeitsmappen kopiert werden.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Excel-Datei aufteilen, Arbeitsblatt kopieren, Bereich kopieren, mehrere Arbeitsmappen, als separate Dateien speichern
type: docs
weight: 195
url: /de/java/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt das Aufteilen einer einzelnen Excel-Datei in mehrere Dateien. Es gibt zwei primäre Methoden dafür: (1) durch Kopieren jedes Arbeitsblatts der Quellarbeitsmappe in eine neue Arbeitsmappe und Speichern jeder als separate Datei, und (2) durch Kopieren eines bestimmten Zellbereichs aus einem Arbeitsblatt in eine neue Arbeitsmappe. Beide Ansätze sind nützlich, wenn Sie Teilmengen von Daten verteilen, kleinere Berichte für verschiedene Empfänger erstellen oder Daten für die individuelle Verarbeitung isolieren müssen.

{{% /alert %}}

## **Einführung**

Es gibt viele reale Szenarien, in denen ein Entwickler eine einzelne Excel-Datei in mehrere kleinere Dateien aufteilen muss. Beispielsweise kann eine Arbeitsmappe ein Arbeitsblatt pro Abteilung enthalten, und jeder Abteilungsleiter muss nur sein eigenes Blatt erhalten. In anderen Fällen möchten Sie möglicherweise eine bestimmte Tabelle oder einen Datenblock aus einem Arbeitsblatt extrahieren und als eigenständige Datei per E-Mail versenden, ohne den Rest der Arbeitsmappe offenzulegen. Große konsolidierte Arbeitsmappen müssen möglicherweise auch in kleinere Teile aufgeteilt werden, um die Handhabung zu erleichtern, das Laden zu beschleunigen oder die nachgelagerte Verarbeitung durch andere Systeme zu ermöglichen.

Aspose.Cells bietet zwei flexible Ansätze für diese Aufgabe. Der erste Ansatz iteriert durch jedes Arbeitsblatt in der Quellarbeitsmappe und kopiert dessen Inhalt in eine brandneue `Workbook`-Instanz, wobei jede als separate Datei gespeichert wird. Der zweite Ansatz konzentriert sich auf einen bestimmten Zellbereich innerhalb eines Arbeitsblatts und kopiert nur diesen Bereich in eine neue Arbeitsmappe. In beiden Fällen ist der allgemeine Ablauf derselbe: Laden Sie die Quellarbeitsmappe mit der `Workbook`-Klasse, greifen Sie über die `Worksheet`- und `Cells`-Objekte auf die relevanten Daten zu, übertragen Sie den Inhalt in eine Ziel-`Workbook` und speichern Sie das Ziel dann auf der Festplatte.

## **Aufteilen einer Excel-Datei durch Kopieren jedes Arbeitsblatts in eine neue Arbeitsmappe**

### **Ansatzübersicht**

Bei diesem Ansatz wird die Quellarbeitsmappe einmal geöffnet, und dann wird für jedes `Worksheet` in der `Worksheets`-Sammlung eine neue Ziel-`Workbook` erstellt. Der Inhalt des Quellarbeitsblatts wird dann in das erste Arbeitsblatt der Zielarbeitsmappe kopiert, und die Zielarbeitsmappe wird als Datei gespeichert, deren Name vom Namen des Quellarbeitsblatts abgeleitet ist. Das Ergebnis ist eine Ausgabedatei pro Arbeitsblatt, wobei jede Ausgabedatei die Daten eines einzelnen Quellblatts enthält.

Diese Methode ist die richtige Wahl, wenn jedes Arbeitsblatt in Ihrer Quellarbeitsmappe eine logisch unabhängige Informationseinheit darstellt (z. B. eine Abteilung, Region, einen Monat oder eine Produktlinie) und Sie jede Einheit einzeln bereitstellen oder verarbeiten möchten.

### **Schritte**

Die folgenden Schritte beschreiben, wie eine Excel-Datei durch Kopieren jedes Arbeitsblatts in eine neue Arbeitsmappe aufgeteilt wird:

1. Öffnen Sie die Excel-Quelldatei, indem Sie ein `Workbook`-Objekt instanziieren und den Dateipfad an dessen Konstruktor übergeben.
2. Iterieren Sie durch die `Workbook.Worksheets`-Sammlung mit einer `for`- oder `foreach`-Schleife, sodass jedes `Worksheet` in der Quelldatei verarbeitet wird.
3. Erstellen Sie innerhalb der Schleife eine neue Ziel-`Workbook`-Instanz (eine leere Arbeitsmappe) für das aktuelle Arbeitsblatt.
4. Fügen Sie der Zielarbeitsmappe ein neues `Worksheet` hinzu (oder verwenden Sie das Standardarbeitsblatt) und weisen Sie ihm einen aussagekräftigen Namen zu, idealerweise denselben wie die `Name`-Eigenschaft des Quellarbeitsblatts.
5. Kopieren Sie den Inhalt des Quellarbeitsblatts in das Zielarbeitsblatt. Dies kann durchgeführt werden, indem die Zellen der `Cells`-Sammlung des Quellarbeitsblatts durchlaufen und ihre Werte in die entsprechenden Zellen des Zielarbeitsblatts geschrieben werden, oder durch Verwendung der Methode `Cells.copy`, um einen gesamten Bereich auf einmal zu übertragen.
6. Konstruieren Sie einen Ausgabedateipfad, der den Namen des Quellarbeitsblatts enthält (zum Beispiel `dataDir + worksheet.getName() + ".xls"`), damit jede generierte Datei einen eindeutigen Namen hat.
7. Rufen Sie die Methode `Workbook.save` der Zielarbeitsmappe auf, um die Datei auf die Festplatte zu schreiben.
8. Wiederholen Sie die Schritte 3 bis 7 für das nächste Arbeitsblatt, bis alle Arbeitsblätter verarbeitet wurden.

### **Codebeispiel**

```java
import com.aspose.cells.*;

String dataDir = "data/";
Workbook workbook = new Workbook(dataDir + "book1.xls");

for (int i = 0; i < workbook.getWorksheets().getCount(); i++)
{
    Worksheet sourceSheet = workbook.getWorksheets().get(i);
    String sheetName = sourceSheet.getName();
    
    Workbook destWorkbook = new Workbook();
    int destIndex = destWorkbook.getWorksheets().add();
    Worksheet destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    String destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, SaveFormat.EXCEL_97_TO_2003);
}
```

Die erwartete Ausgabe ist eine Reihe neuer Dateien im Datenverzeichnis, eine Datei pro Arbeitsblatt aus der Quellarbeitsmappe. Jede Datei wird nach dem entsprechenden Quellblatt benannt, und die Datei enthält die Daten (und optional die Formatierung) dieses einzelnen Blatts.

## **Aufteilen einer Excel-Datei durch Kopieren eines Bereichs in eine neue Arbeitsmappe**

### **Ansatzübersicht**

Manchmal entsprechen die Daten, die Sie aufteilen müssen, nicht einem gesamten Arbeitsblatt, sondern einem bestimmten rechteckigen Bereich eines Arbeitsblatts, wie z. B. `A1:D10` oder einem benannten Bereich, der eine bestimmte Tabelle darstellt. In diesen Fällen ist das Kopieren ganzer Arbeitsblätter verschwenderisch, und ein präziserer Ansatz ist erforderlich: Identifizieren Sie den Quellbereich, kopieren Sie nur diesen Bereich in eine neue Arbeitsmappe und speichern Sie die neue Datei.

Dieser Ansatz ist ideal, wenn Sie eine einzelne Tabelle, einen Berichtsblock oder einen Datenbereich aus einem größeren Arbeitsblatt extrahieren möchten, während Sie alle nicht verwandten Inhalte verwerfen. Er ist auch nützlich, um vom Benutzer ausgewählte Bereiche eines Blatts als eigenständige Dateien zu exportieren.

### **Schritte**

Die folgenden Schritte beschreiben, wie eine Excel-Datei durch Kopieren eines bestimmten Bereichs in eine neue Arbeitsmappe aufgeteilt wird:

1. Öffnen Sie die Excel-Quelldatei, indem Sie ein `Workbook`-Objekt mit dem Dateipfad instanziieren.
2. Rufen Sie das Ziel-`Worksheet` ab, das den Bereich enthält, den Sie kopieren möchten, entweder nach Index (z. B. das erste Blatt) oder nach Name aus der `Worksheets`-Sammlung.
3. Identifizieren Sie den zu kopierenden Bereich. Dies kann ein fest codierter Zellbereich wie `A1:C10` sein, ein benannter Bereich, der über die `Worksheet.Cells`-Sammlung erhalten wurde, oder ein Bereich, der über `Worksheet.Cells.createRange` erstellt wurde.
4. Erstellen Sie eine neue Ziel-`Workbook`-Instanz.
5. Greifen Sie auf das erste `Worksheet` der Zielarbeitsmappe zu (das Standardblatt).
6. Kopieren Sie den Quellbereich in das Zielarbeitsblatt, typischerweise beginnend bei Zelle `A1`. Die Methode `Cells.copy` auf der Ziel-`Cells`-Sammlung kann verwendet werden, um einen gesamten Bereich zu kopieren, oder Sie können durch die Zellen des Quellbereichs iterieren und ihre Werte mit `putValue` in die Zielzellen schreiben. Optionale `CopyOptions` können bereitgestellt werden, um zu steuern, was übertragen wird (nur Werte, Werte und Stile, Formeln usw.).
7. Speichern Sie die Zielarbeitsmappe unter einem neuen Dateipfad auf der Festplatte mit der Methode `Workbook.save`.

### **Codebeispiel**

```java
import com.aspose.cells.*;

// Definiere das Datenverzeichnis und die Dateipfade
String dataDir = "data/";
String sourcePath = dataDir + "book1.xls";
String outputPath = dataDir + "outputrange.xls";

// Öffne die Quell-Excel-Datei
Workbook sourceWorkbook = new Workbook(sourcePath);

// Hole das erste Arbeitsblatt aus der Quellarbeitsmappe
Worksheet sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Definiere den Quellzellenbereich A1:C10 (10 Zeilen, 3 Spalten beginnend bei Zeile 0, Spalte 0)
Range sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Erstelle eine neue Zielarbeitsmappe
Workbook destWorkbook = new Workbook();

// Greife auf das erste Arbeitsblatt in der Zielarbeitsmappe zu
Worksheet destWorksheet = destWorkbook.getWorksheets().get(0);

// Erstelle den Zielbereich bei A1 mit den gleichen Dimensionen wie der Quellbereich
Range destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Kopiere den Quellbereich in den Zielbereich
destRange.copy(sourceRange);

// Speichere die Zielarbeitsmappe in einer neuen .xls-Datei
destWorkbook.save(outputPath, SaveFormat.EXCEL_97_TO_2003);
```

Die erwartete Ausgabe ist eine einzelne neue Datei im Datenverzeichnis, die nur die Werte (und optional die Formatierung) des angegebenen Bereichs enthält, der aus der Quellarbeitsmappe extrahiert wurde. Die Zieldatei hat keine Beziehung zu anderen Daten in der Quelldatei; sie enthält nur den extrahierten Bereich, beginnend bei Zelle `A1` ihres ersten Arbeitsblatts.

## **Verwandte Artikel**

- [Kopieren von Zeilen und Spalten](/cells/de/java/copying-rows-and-columns/)
- [Zusammenführen und Aufheben der Zusammenführung von Zellen](/cells/de/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}