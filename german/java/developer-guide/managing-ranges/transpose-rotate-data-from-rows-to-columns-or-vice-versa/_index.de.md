---
title: Bereich transponieren
description: Dieser Artikel erklärt, wie Sie Daten in Excel-Dateien mit Aspose.Cells for Java mithilfe von drei verschiedenen Ansätzen von Zeilen in Spalten oder umgekehrt transponieren oder drehen.
linktitle: Bereich transponieren
url: /de/java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Bereich transponieren, Daten drehen, Transponierungsfunktion, dynamische Arrayformel, Arrayformel, Excel TRANSPOSE, Zeilen zu Spalten
type: docs
weight: 80
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Java unterstützt das Transponieren (Drehen) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Arten. Der erste Ansatz verwendet die In-Place-Methode `Range.transpose()` und funktioniert mit jeder Excel-Version, während der zweite Ansatz `Cell.setDynamicArrayFormula()` verwendet, um eine moderne dynamische Arrayformel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch überläuft. Der dritte Ansatz verwendet `Cell.setArrayFormula()`, um eine klassische Arrayformel mit Strg+Umschalt+Eingabe (CSE) zu schreiben, die mit älteren Excel-Versionen kompatibel ist. Dieser Artikel führt Sie schrittweise durch jeden Ansatz und enthält vollständige Codebeispiele.
{{% /alert %}}

## **Einführung**
Das Transponieren eines Bereichs bedeutet, ihn so zu drehen, dass eine Zeile zu einer Spalte wird und eine Spalte zu einer Zeile, wobei die Daten effektiv an ihrer Hauptdiagonale gespiegelt werden. In Microsoft Excel führt die Arbeitsblattfunktion `TRANSPOSE` diese Operation aus, und die konzeptionelle Referenz ist unter [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) dokumentiert. Dieses Konzept kann programmatisch auf einen Zellbereich angewendet werden, was in vielen Geschäfts- und Berichtsszenarien nützlich ist.
- Neuorientierung von Quartals- oder Jahresumsatzberichten, in denen Quartale normalerweise über die Seite und Regionen über die Seite nach unten verlaufen, oder umgekehrt.
- Austausch der Achsenausrichtung in Dashboards oder Diagrammen, sodass eine Zeitreihe über die Seite nach unten statt quer verläuft.
- Umstrukturierung von Daten, die aus externen Systemen importiert wurden, sodass sie dem Layout entsprechen, das von nachgelagerten Analyse- oder Berichtsvorlagen erwartet wird.
Um den Rest des Artikels konkret zu gestalten, verwendet jedes Beispiel die folgende kleine Tabelle "Umsatz nach Region nach Quartal". In der Beispielarbeitsmappe belegt diese Tabelle den Bereich **A1:D5**, wobei **A1** als obere linke Ecke leer gelassen wird, **B1:D1** die Regionsheader enthält und **A2:A5** die Quartalsheader enthält.
| Region            | Europa     | Asien      | Nordamerika  |
|-------------------|------------|------------|--------------|
| Q1                | 21704714   | 8774099    | 12094215     |
| Q2                | 17987034   | 12214447   | 10873099     |
| Q3                | 19485029   | 14356879   | 15689543     |
| Q4                | 22567894   | 15763492   | 17456723     |
Der Artikel stellt dann drei verschiedene Möglichkeiten vor, diese Daten mit Aspose.Cells for Java zu transponieren, die jeweils für eine andere Excel-Version und einen anderen Anwendungsfall geeignet sind.

## **Ansatz 1 — Bereich direkt transponieren (Range.transpose)**
Verwenden Sie diesen Ansatz, wenn Sie Daten transponieren möchten, ohne die Arbeitsblattfunktion `TRANSPOSE` zu verwenden. Er funktioniert mit **jeder Excel-Version** und hat keine Abhängigkeit von dynamischen Arrays, was ihn zur sichersten versionsübergreifend kompatiblen Option macht. Er ist ideal, wenn Sie nur das endgültige transponierte Ergebnis benötigen und die ursprüngliche `TRANSPOSE`-Formel nicht in der Arbeitsmappe behalten müssen.

### **Verwendete API**
`Range.transpose()` ist eine Instanzmethode der Klasse `com.aspose.cells.Range`. Durch den Aufruf wird der Bereich direkt gedreht, indem seine Zeilen und Spalten vertauscht werden, sodass eine Zeile zu einer Spalte und eine Spalte zu einer Zeile wird. Die Methode verändert die zugrunde liegenden Zellen direkt, ohne eine Formel zu schreiben.

### **Schritte**
1. Öffnen Sie die Quellarbeitsmappe mit `LoadOptions`, das auf das Format `.xlsx` eingestellt ist, durch Aufruf von `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt aus der Arbeitsmappe mit `workbook.getWorksheets().get(0)` ab.
3. Greifen Sie über `worksheet.getCells()` auf die Zellsammlung des Arbeitsblatts zu.
4. Erstellen Sie den Quellbereich, der **A1:D5** abdeckt, durch Aufruf von `cells.createRange("A1:D5")`.
5. Rufen Sie `source.transpose()` auf, um den Bereich direkt zu drehen und Zeilen und Spalten zu vertauschen.
6. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Nach der Transponierung enthält der ursprüngliche Ankerbereich die gedrehten Daten. Die erste Zeile lautet (leer, **Europa**, **Asien**, **Nordamerika**) und die erste Spalte lautet (leer, **Q1**, **Q2**, **Q3**, **Q4**). Jede ursprüngliche Umsatzspalte wird zu einer Zeile im transponierten Bereich.

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
source.transpose();
workbook.save(outputFile);
```

## **Ansatz 2 — Transponieren mit dynamischer Arrayformel (Excel 365 / 2021)**
Verwenden Sie diesen Ansatz, wenn Sie die Formel `=TRANSPOSE(A1:D5)` als Live-Formel in der Ausgabearbeitsmappe erhalten möchten, damit sich das Ergebnis automatisch aktualisiert, wenn sich die Quelldaten ändern, und die Excel-Zieldatei in **Excel 365 / Excel 2021 oder höher** geöffnet wird, wo dynamische Arrays und der Spill-Operator unterstützt werden.

### **Verwendete API**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` ist eine Methode auf `com.aspose.cells.Cell`, die die Formel der Zelle als **dynamische Arrayformel** festlegt. Excel wertet die Formel einmal aus und überläuft das Ergebnis automatisch in die umgebenden Zellen. Der dritte Parameter weist Aspose.Cells bei Festlegung auf `true` an, die resultierenden Werte auch beim Schreiben zu berechnen.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe mit `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `Cells`-Sammlung zu.
3. Platzieren Sie die dynamische Arrayformel in Zelle **A6**, direkt unter dem Quellbereich, durch Aufruf von `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. Das Argument `null` übergibt die Standard-`FormulaParseOptions`, und das dritte Argument `true` weist Aspose.Cells an, die Formel als dynamisches Array zu behandeln und sie auszuwerten, sodass die überlaufenen Werte in die Arbeitsmappe geschrieben werden.
5. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** enthält die Formel `=TRANSPOSE(A1:D5)` und Excel überläuft das Ergebnis automatisch in den Bereich **A6:D10**, einen 5-zeiligen und 4-spalten Block, der den transponierten Daten entspricht.

{{% alert color="primary" %}}
Dieser Ansatz funktioniert **nur in Excel 365 / 2021 oder höher**. Ältere Excel-Versionen überlaufen dynamische Arrayformeln nicht korrekt.
{{% /alert %}}

```java
import com.aspose.cells.*;
String srcFile = "source.xlsx";
String outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.save(outFile, SaveFormat.XLSX);
```

## **Ansatz 3 — Transponieren mit klassischer Arrayformel (CSE)**
Verwenden Sie diesen Ansatz, wenn Sie eine `TRANSPOSE`-Formel in der Arbeitsmappe erhalten möchten, die Excel-Zieldatei jedoch möglicherweise in **älteren Excel-Versionen (vor 2021, einschließlich 2019, 2016, 2013 usw.)** geöffnet wird, in denen das Überlaufen dynamischer Arrays nicht unterstützt wird. Die klassische CSE-Arrayformel (Strg+Umschalt+Eingabe) ist die legacy-kompatible Alternative, die alle Excel-Versionen auswerten können.

### **Verwendete API**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` ist eine Methode auf `com.aspose.cells.Cell`, die der Ankerzelle eine **klassische Arrayformel (CSE)** zuweist und die Dimensionen des resultierenden Arrays festlegt. Aspose.Cells schreibt die Arrayformel-Markierung für mehrere Zellen, sodass Excel die Formel als einzelnen Arrayausdruck auswertet, der den angegebenen Bereich füllt.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe wie in den vorherigen Ansätzen beschrieben.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `Cells`-Sammlung zu.
3. Rufen Sie `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` auf. Das zweite Argument `4` ist die Anzahl der Zeilen des Zielarrays und das dritte Argument `5` ist die Anzahl der Spalten.
4. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** ist der Anker der Arrayformel und das ausgewertete Array umfasst 4 Zeilen und 5 Spalten beginnend bei A6, was den transponierten Dimensionen der Quelle A1:D5 entspricht. Excel schreibt eine einzelne Arrayformel-Markierung über den resultierenden Bereich, sodass ältere Excel-Versionen sie korrekt auswerten.

{{% alert color="primary" %}}
CSE-Arrayformeln sind die klassische Excel-Methode, um einen `TRANSPOSE`-Ausdruck auszuwerten, und dieser Ansatz ist universell über alle Excel-Versionen hinweg kompatibel.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Laden Sie die Quellarbeitsmappe mit xlsx LoadOptions
String srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.XLSX));
// Zugriff auf das erste Arbeitsblatt und seine Cells-Sammlung
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Legen Sie die klassische CSE-Array-Formel auf Zelle A6 fest.
// Die Formel =TRANSPOSE(A1:D5) dreht den 5-zeiligen x 4-spaltigen Quellbereich
// in ein 4-zeiliges x 5-spaltiges Array. Das zweite Argument (4) ist die Anzahl der Zeilen
// und das dritte Argument (5) ist die Anzahl der Spalten des resultierenden Arrays.
// Aspose.Cells schreibt den CSE-Array-Formel-Marker, damit Excel es als
// eine einzelne Mehrzellen-Array-Formel auswertet, kompatibel mit älteren Excel-Versionen
// (2019, 2016, 2013 usw.), die das dynamische Array-Spilling nicht unterstützen.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Speichern Sie die Arbeitsmappe, damit der Array-Formel-Marker beibehalten wird
workbook.save("output.xlsx");
```

## **Vergleich — Wann jeden Ansatz verwenden**
| Ansatz | API / Methode | Excel-Version | Quellformel erhalten? | Ausgabebereich |
|--------|---------------|---------------|----------------------|----------------|
| Ansatz 1 — Direkte Transponierung | `Range.transpose()` | Alle Excel-Versionen | Nein (nur Werte) | Ursprünglicher Ankerbereich, 5×4 |
| Ansatz 2 — Dynamische Arrayformel | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Ja (läuft dynamisch über) | Vom Anker überlaufen |
| Ansatz 3 — Klassische Arrayformel (CSE) | `Cell.setArrayFormula` | Alle Excel-Versionen | Ja (Multi-Cell-Arrayformel) | Explizite Größe, 4×5 |
Verwenden Sie **Ansatz 1**, wenn Sie eine schnelle, versionsübergreifende Transformation benötigen und nur die transponierten Werte in die Datei geschrieben werden sollen. Verwenden Sie **Ansatz 2**, wenn modernes Excel garantiert ist und die Formel live bleiben und sich aktualisieren soll, wenn sich die Quelle ändert. Verwenden Sie **Ansatz 3**, wenn Sie die breiteste Kompatibilität mit einer erhaltenen Formel über alle Excel-Versionen hinweg benötigen, einschließlich der älteren Versionen, die keine dynamischen Arrays unterstützen.

## **Verwandte Artikel**
- [SmartMarker Einzelzell-Array-Rendering | Aspose.Cells Java](/cells/de/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/java/inserting-an-image-into-a-cell/)
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="java" >}}