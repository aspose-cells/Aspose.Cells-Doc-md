---
title: Bereich transponieren
linktitle: Bereich transponieren
description: Dieser Artikel erklärt, wie Sie mit Aspose.Cells for Node.js via Java Daten in Excel-Dateien von Zeilen in Spalten oder umgekehrt transponieren oder drehen, mit drei verschiedenen Ansätzen.
keywords: Aspose.Cells, Node.js via Java Bibliothek, Tabellenkalkulation, Bereich transponieren, Daten drehen, TRANSPOSE-Funktion, dynamische Arrayformel, Arrayformel, Excel TRANSPOSE, Zeilen zu Spalten
type: docs
weight: 80
url: /de/nodejs-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via Java unterstützt das Transponieren (Drehen) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Arten. Der erste Ansatz verwendet die In-Place-Methode `Range.transpose()` und funktioniert in jeder Excel-Version, während der zweite Ansatz `Cell.setDynamicArrayFormula()` verwendet, um eine moderne dynamische Arrayformel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch überläuft. Der dritte Ansatz verwendet `Cell.setArrayFormula()`, um eine klassische Arrayformel mit Strg+Umschalt+Eingabe (CSE) zu schreiben, die mit älteren Excel-Versionen kompatibel ist. Dieser Artikel führt durch jeden Ansatz mit schrittweisen Anleitungen und vollständigen Codebeispielen.
{{% /alert %}}

## **Einführung**
Das Transponieren eines Bereichs bedeutet, ihn so zu drehen, dass eine Zeile zu einer Spalte wird und eine Spalte zu einer Zeile, wodurch die Daten effektiv über ihre Hauptdiagonale gespiegelt werden. In Microsoft Excel führt die Arbeitsblattfunktion `TRANSPOSE` diese Operation aus, und die konzeptionelle Referenz ist unter [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) dokumentiert. Dieses Konzept kann programmatisch auf einen Zellbereich angewendet werden, was in vielen Geschäfts- und Berichtsszenarien nützlich ist.
- Neuorientierung von Quartals- oder Jahresverkaufsberichten, in denen Quartale normalerweise über die Seite und Regionen die Seite hinunter laufen, oder umgekehrt.
- Vertauschen der Achsenausrichtung in Dashboards oder Diagrammen, sodass eine Zeitreihe die Seite hinunter statt über die Seite verläuft.
- Umformen von Daten, die aus externen Systemen importiert wurden, sodass sie dem Layout entsprechen, das von nachgelagerten Analyse- oder Berichtsvorlagen erwartet wird.
Um den Rest des Artikels konkret zu gestalten, verwendet jedes Beispiel die folgende kleine Tabelle mit Verkäufen nach Region nach Quartal. In der Beispielarbeitsmappe belegt diese Tabelle den Bereich **A1:D5**, wobei **A1** als obere linke Ecke leer bleibt, **B1:D1** die Regionsüberschriften enthält und **A2:A5** die Quartalsüberschriften enthält.
| Region            | Europa     | Asien      | Nordamerika |
|-------------------|------------|------------|-------------|
| Qtr 1             | 21704714   | 8774099    | 12094215    |
| Qtr 2             | 17987034   | 12214447   | 10873099    |
| Qtr 3             | 19485029   | 14356879   | 15689543    |
| Qtr 4             | 22567894   | 15763492   | 17456723    |
Der Artikel stellt dann drei verschiedene Möglichkeiten vor, diese Daten mit Aspose.Cells for Node.js via Java zu transponieren, die jeweils für eine andere Excel-Version und einen anderen Anwendungsfall geeignet sind.

## **Ansatz 1 — Bereich in-place transponieren (Range.transpose)**
Verwenden Sie diesen Ansatz, wann immer Sie Daten transponieren möchten, ohne die Arbeitsblattfunktion `TRANSPOSE` einzubeziehen. Er funktioniert in **jeder Version von Excel** und hat keine Abhängigkeit von dynamischen Arrays, was ihn zur sichersten versionsübergreifend kompatiblen Option macht. Er ist ideal, wenn Sie nur die endgültige transponierte Ausgabe benötigen und die ursprüngliche `TRANSPOSE`-Formel nicht in der Arbeitsmappe behalten müssen.

### **Verwendete API**
`Range.transpose()` ist eine Instanzmethode auf der Klasse `com.aspose.cells.Range`. Ihr Aufruf dreht den Bereich in-place, indem sie seine Zeilen und Spalten vertauscht, sodass eine Zeile zu einer Spalte und eine Spalte zu einer Zeile wird. Die Methode ändert die zugrunde liegenden Zellen direkt, ohne eine Formel zu schreiben.

### **Schritte**
1. Öffnen Sie die Quellarbeitsmappe mit `LoadOptions`, das auf das `.xlsx`-Format eingestellt ist, durch Aufruf von `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Holen Sie das erste Arbeitsblatt aus der Arbeitsmappe mit `workbook.getWorksheets().get(0)`.
3. Greifen Sie über `worksheet.getCells()` auf die Zellauflistung des Arbeitsblatts zu.
4. Erstellen Sie den Quellbereich, der **A1:D5** abdeckt, durch Aufruf von `cells.createRange("A1:D5")`.
5. Rufen Sie `source.transpose()` auf, um den Bereich in-place zu drehen und Zeilen und Spalten zu vertauschen.
6. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Nach der Transponierung enthält der anfängliche Ankerbereich die gedrehten Daten. Die erste Zeile lautet (leer, **Europa**, **Asien**, **Nordamerika**) und die erste Spalte lautet (leer, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Jede ursprüngliche Verkaufsspalte wird zu einer Zeile im transponierten Bereich.

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outputFile = "transposed.xlsx";
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, loadOptions);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
const source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Ansatz 2 — Transponieren mit dynamischer Arrayformel (Excel 365 / 2021)**
Verwenden Sie diesen Ansatz, wenn Sie die Formel `=TRANSPOSE(A1:D5)` als Live-Formel in der Ausgabearbeitsmappe erhalten möchten, damit sich das Ergebnis automatisch aktualisiert, wenn sich die Quelldaten ändern, und die Ziel-Excel-Datei in **Excel 365 / Excel 2021 oder höher** geöffnet wird, wo dynamische Arrays und der Spill-Operator unterstützt werden.

### **Verwendete API**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` ist eine Methode auf `com.aspose.cells.Cell`, die die Formel der Zelle als **dynamische Arrayformel** festlegt. Excel wertet die Formel einmal aus und überläuft das Ergebnis automatisch in die umliegenden Zellen. Der dritte Parameter weist, wenn er auf `true` gesetzt ist, Aspose.Cells an, die resultierenden Werte auch beim Schreiben zu berechnen.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe mit `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Holen Sie das erste Arbeitsblatt und greifen Sie auf seine `Cells`-Auflistung zu.
3. Platzieren Sie die dynamische Arrayformel auf Zelle **A6**, direkt unter dem Quellbereich, durch Aufruf von `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. Das Argument `null` übergibt die Standard-`FormulaParseOptions`, und das dritte Argument `true` weist Aspose.Cells an, die Formel als dynamisches Array zu behandeln und sie auszuwerten, damit die überlaufenden Werte in die Arbeitsmappe geschrieben werden.
5. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** enthält die Formel `=TRANSPOSE(A1:D5)`, und Excel überläuft das Ergebnis automatisch in den Bereich **A6:D10**, einen 5-Zeilen-mal-4-Spalten-Block, der den transponierten Daten entspricht.

{{% alert color="primary" %}}
Dieser Ansatz funktioniert **nur in Excel 365 / 2021 oder höher**. Ältere Excel-Versionen überlaufen dynamische Arrayformeln nicht korrekt.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Ansatz 3 — Transponieren mit klassischer Arrayformel (CSE)**
Verwenden Sie diesen Ansatz, wenn Sie eine `TRANSPOSE`-Formel in der Arbeitsmappe erhalten möchten, die Ziel-Excel-Datei jedoch möglicherweise in **älteren Excel-Versionen (vor 2021, einschließlich 2019, 2016, 2013 usw.)** geöffnet wird, wo das Überlaufen dynamischer Arrays nicht unterstützt wird. Die klassische CSE-Arrayformel (Strg+Umschalt+Eingabe) ist die legacy-kompatible Alternative, die alle Excel-Versionen auswerten können.

### **Verwendete API**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` ist eine Methode auf `com.aspose.cells.Cell`, die der Ankerzelle eine **klassische Arrayformel (CSE)** zuweist und die Dimensionen des resultierenden Arrays deklariert. Aspose.Cells schreibt die Mehrzellen-Arrayformel-Markierung, sodass Excel die Formel als einen einzigen Arrayausdruck auswertet, der den deklarierten Bereich füllt.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe wie in den vorherigen Ansätzen beschrieben.
2. Holen Sie das erste Arbeitsblatt und greifen Sie auf seine `Cells`-Auflistung zu.
3. Rufen Sie `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` auf. Das zweite Argument `4` ist die Anzahl der Zeilen des Zielarrays und das dritte Argument `5` ist die Anzahl der Spalten.
4. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** ist der Anker der Arrayformel, und das ausgewertete Array umfasst 4 Zeilen mal 5 Spalten, beginnend bei A6, was den transponierten Dimensionen der Quelle A1:D5 entspricht. Excel schreibt eine einzige Arrayformel-Markierung über den resultierenden Bereich, sodass ältere Excel-Versionen ihn korrekt auswerten.

{{% alert color="primary" %}}
CSE-Arrayformeln sind die klassische Excel-Methode, um einen `TRANSPOSE`-Ausdruck auszuwerten, und dieser Ansatz ist universell kompatibel über alle Excel-Versionen hinweg.
{{% /alert %}}

```python
const AsposeCells = require("aspose.cells");
// Load the source workbook with xlsx LoadOptions
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Access the first worksheet and its Cells collection
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Set the classic CSE array formula on cell A6.
// The formula =TRANSPOSE(A1:D5) rotates the 5-row x 4-column source range
// into a 4-row x 5-column array. The second argument (4) is the number of rows
// and the third argument (5) is the number of columns of the resulting array.
// Aspose.Cells writes the CSE array-formula marker so Excel evaluates it as
// a single multi-cell array formula, compatible with older Excel versions
// (2019, 2016, 2013, etc.) that do not support dynamic array spilling.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Save the workbook so the array-formula marker is persisted
workbook.save("output.xlsx");
```

## **Vergleich — Wann ist welcher Ansatz zu verwenden?**
| Ansatz | API / Methode | Excel-Version | Quellformel erhalten? | Ausgabebereich |
|----------|--------------|---------------|--------------------------|--------------|
| Ansatz 1 — In-Place-Transponierung | `Range.transpose()` | Alle Excel-Versionen | Nein (nur Werte) | Anfänglicher Ankerbereich, 5×4 |
| Ansatz 2 — Dynamische Arrayformel | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Ja (überläuft dynamisch) | Vom Anker überlaufen |
| Ansatz 3 — Klassische Arrayformel (CSE) | `Cell.setArrayFormula` | Alle Excel-Versionen | Ja (Mehrzellen-Arrayformel) | Explizite Größe, 4×5 |
Verwenden Sie **Ansatz 1**, wenn Sie eine schnelle, versionsübergreifende Transformation benötigen und nur die transponierten Werte in die Datei geschrieben werden sollen. Verwenden Sie **Ansatz 2**, wenn modernes Excel garantiert ist und die Formel live bleiben und sich aktualisieren soll, wenn sich die Quelle ändert. Verwenden Sie **Ansatz 3**, wenn Sie die breiteste Kompatibilität mit einer erhaltenen Formel über jede Excel-Version hinweg benötigen, einschließlich der älteren Versionen, die keine dynamischen Arrays unterstützen.

## **Verwandte Artikel**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Node.js via Java](/cells/de/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Inserting an Image into a Cell](/cells/de/nodejs-java/inserting-an-image-into-a-cell/)
- [Splitting Excel Files into Multiple Files](/cells/de/nodejs-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-java" >}}