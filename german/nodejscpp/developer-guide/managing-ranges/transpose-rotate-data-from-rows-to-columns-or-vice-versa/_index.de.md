---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Node.js via C++ with three different approaches.
linktitle: Bereich transponieren
url: /de/nodejs-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Node.js via C++ Bibliothek, Tabellenkalkulation, Bereich transponieren, Daten drehen, Transponierungsfunktion, dynamische Array-Formel, Array-Formel, Excel TRANSPOSE, Zeilen in Spalten
type: docs
weight: 80
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ unterstützt das Transponieren (Drehen) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Arten. Der erste Ansatz verwendet die In-Place-Methode `range.transpose()` und funktioniert in jeder Excel-Version, während der zweite Ansatz `cell.setDynamicArrayFormula()` verwendet, um eine moderne dynamische Array-Formel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch überläuft. Der dritte Ansatz verwendet `cell.setArrayFormula()`, um eine klassische CSE-Array-Formel (Strg+Umschalt+Eingabe) zu schreiben, die mit älteren Excel-Versionen kompatibel ist. Dieser Artikel führt durch jeden Ansatz mit schrittweisen Anleitungen und vollständigen Codebeispielen.
{{% /alert %}}

## **Einführung**
Einen Bereich zu transponieren bedeutet, ihn so zu drehen, dass das, was eine Zeile war, zu einer Spalte wird und das, was eine Spalte war, zu einer Zeile wird, wodurch die Daten effektiv über ihre Hauptdiagonale gespiegelt werden. In Microsoft Excel führt die Arbeitsblattfunktion `TRANSPOSE` diese Operation aus, und die konzeptionelle Referenz ist unter [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) dokumentiert. Die gleiche Idee kann programmatisch auf einen Zellbereich angewendet werden, was in vielen Geschäfts- und Berichtsszenarien nützlich ist.
Häufige Szenarien, in denen eine Transponierung nützlich ist, umfassen die folgenden.
- Neuausrichtung von Quartals- oder Jahresumsatzberichten, in denen Quartale normalerweise waagerecht über die Seite und Regionen senkrecht die Seite hinunter verlaufen, oder umgekehrt.
- Tauschen der Achsenausrichtung in Dashboards oder Diagrammen, sodass eine Zeitreihe die Seite hinunter statt quer über die Seite verläuft.
- Umformen von Daten, die aus externen Systemen importiert wurden, damit sie dem Layout entsprechen, das von nachgelagerten Analyse- oder Berichtsvorlagen erwartet wird.
Um den Rest des Artikels konkret zu gestalten, verwendet jedes Beispiel die folgende kleine Tabelle mit Umsätzen nach Region und Quartal. In der Beispielarbeitsmappe belegt diese Tabelle den Bereich **A1:D5**, wobei **A1** als obere linke Ecke leer bleibt, **B1:D1** die Regionsüberschriften enthalten und **A2:A5** die Quartalsüberschriften enthalten.
| Region            | Europa     | Asien      | Nordamerika |
|-------------------|------------|------------|-------------|
| Qtr 1             | 21704714   | 8774099    | 12094215    |
| Qtr 2             | 17987034   | 12214447   | 10873099    |
| Qtr 3             | 19485029   | 14356879   | 15689543    |
| Qtr 4             | 22567894   | 15763492   | 17456723    |
Der Artikel stellt dann drei verschiedene Möglichkeiten vor, diese Daten mit Aspose.Cells for Node.js via C++ zu transponieren, die jeweils für eine andere Excel-Version und einen anderen Anwendungsfall geeignet sind.

## **Ansatz 1 — Bereich direkt transponieren (range.transpose)**
Verwenden Sie diesen Ansatz, wann immer Sie Daten transponieren möchten, ohne die Arbeitsblattfunktion `TRANSPOSE` einzubeziehen. Er funktioniert in **jeder Excel-Version** und hat keine Abhängigkeit von dynamischen Arrays, was ihn zur sichersten versionsübergreifend kompatiblen Option macht. Er ist ideal, wenn Sie nur das endgültige transponierte Ergebnis benötigen und die ursprüngliche `TRANSPOSE`-Formel nicht in der Arbeitsmappe behalten müssen.

### **Verwendete API**
`range.transpose()` ist eine Instanzmethode der Klasse `Aspose.Cells.Range`. Durch ihren Aufruf wird der Bereich direkt umgedreht, indem seine Zeilen und Spalten vertauscht werden, sodass das, was eine Zeile war, zu einer Spalte wird und das, was eine Spalte war, zu einer Zeile wird. Die Methode ändert die zugrunde liegenden Zellen direkt, ohne eine Formel zu schreiben.

### **Schritte**
1. Öffnen Sie die Quellarbeitsmappe mit `LoadOptions`, die auf das Format `.xlsx` eingestellt sind, durch Aufruf von `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt aus der Arbeitsmappe mit `workbook.getWorksheets().get(0)` ab.
3. Greifen Sie auf die Zellauflistung des Arbeitsblatts über `worksheet.getCells()` zu.
4. Erstellen Sie den Quellbereich, der **A1:D5** abdeckt, durch Aufruf von `cells.createRange("A1:D5")`.
5. Rufen Sie `source.transpose()` auf, um den Bereich direkt zu drehen und Zeilen und Spalten zu vertauschen.
6. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Nach der Transponierung enthält derselbe Ankerbereich die gedrehten Daten. Die erste Zeile lautet (leer, **Europa**, **Asien**, **Nordamerika**) und die erste Spalte lautet (leer, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Jede ursprüngliche Umsatzspalte wird zu einer Zeile im transponierten Bereich.

```javascript
var srcFile = "source.xlsx";
var outputFile = "transposed.xlsx";
var workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
var worksheet = workbook.getWorksheets().get(0);
var cells = worksheet.getCells();
var source = cells.createRange("A1:D5");
source.transpose();
workbook.save(outputFile);
```

## **Ansatz 2 — Transponieren mit einer dynamischen Array-Formel (Excel 365 / 2021)**
Verwenden Sie diesen Ansatz, wenn Sie die Formel `=TRANSPOSE(A1:D5)` als Live-Formel in der Ausgabearbeitsmappe erhalten möchten, damit sich das Ergebnis automatisch aktualisiert, wenn sich die Quelldaten ändern, und die Ziel-Excel-Datei in **Excel 365 / Excel 2021 oder neuer** geöffnet wird, wo dynamische Arrays und der Überlaufoperator unterstützt werden.

### **Verwendete API**
`cell.setDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` ist eine Methode von `Aspose.Cells.Cell`, die die Formel der Zelle als **dynamische Array-Formel** festlegt. Excel wertet die Formel einmal aus und überläuft das Ergebnis automatisch in die umliegenden Zellen. Wenn der dritte Parameter auf `true` gesetzt ist, weist er Aspose.Cells an, die resultierenden Werte auch zum Zeitpunkt des Schreibens zu berechnen.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe mit `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `Cells`-Auflistung zu.
3. Platzieren Sie die dynamische Array-Formel in Zelle **A6**, direkt unter dem Quellbereich, durch Aufruf von `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", null, true)`.
4. Das Argument `null` übergibt die standardmäßigen `FormulaParseOptions`, und das dritte Argument `true` weist Aspose.Cells an, die Formel als dynamisches Array zu behandeln und sie auszuwerten, damit die überlaufenden Werte in die Arbeitsmappe geschrieben werden.
5. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** enthält die Formel `=TRANSPOSE(A1:D5)` und Excel überläuft das Ergebnis automatisch in den Bereich **A6:D10**, einen 5-zeiligen mal 4-spaltigen Block, der den transponierten Daten entspricht.

{{% alert color="primary" %}}
Dieser Ansatz funktioniert **nur in Excel 365 / 2021 oder neuer**. Ältere Excel-Versionen überlaufen dynamische Array-Formeln nicht korrekt.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
const srcFile = "source.xlsx";
const outFile = "output_transpose_dynamic.xlsx";
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
const workbook = new AsposeCells.Workbook(srcFile, opts);
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new AsposeCells.FormulaParseOptions(), true);
workbook.save(outFile, AsposeCells.SaveFormat.Xlsx);
```

## **Ansatz 3 — Transponieren mit einer klassischen Array-Formel (CSE)**
Verwenden Sie diesen Ansatz, wenn Sie eine `TRANSPOSE`-Formel in der Arbeitsmappe erhalten möchten, die Ziel-Excel-Datei jedoch möglicherweise in **älteren Excel-Versionen (vor 2021, einschließlich 2019, 2016, 2013 usw.)** geöffnet wird, wo das Überlaufen dynamischer Arrays nicht unterstützt wird. Die klassische CSE-Array-Formel (Strg+Umschalt+Eingabe) ist die legacy-kompatible Alternative, die alle Excel-Versionen auswerten können.

### **Verwendete API**
`cell.setArrayFormula(string arrayFormula, int nRows, int nColumns)` ist eine Methode von `Aspose.Cells.Cell`, die eine **klassische Array-Formel (CSE)** der Ankerzelle zuweist und die Dimensionen des resultierenden Arrays deklariert. Aspose.Cells schreibt die Multi-Cell-Array-Formel-Markierung, sodass Excel die Formel als einen einzelnen Array-Ausdruck auswertet, der den deklarierten Bereich füllt.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe auf die gleiche Weise wie in den vorherigen Ansätzen.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `Cells`-Auflistung zu.
3. Rufen Sie `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` auf. Das zweite Argument `4` ist die Anzahl der Zeilen des Ziel-Arrays und das dritte Argument `5` ist die Anzahl der Spalten.
4. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** ist der Anker der Array-Formel und das ausgewertete Array umfasst 4 Zeilen mal 5 Spalten, beginnend bei A6, die den transponierten Dimensionen der Quelle A1:D5 entsprechen. Excel schreibt eine einzelne Array-Formel-Markierung über den resultierenden Bereich, sodass ältere Excel-Versionen sie korrekt auswerten.

{{% alert color="primary" %}}
CSE-Array-Formeln sind die klassische Excel-Methode zur Auswertung eines `TRANSPOSE`-Ausdrucks, und dieser Ansatz ist universell über alle Excel-Versionen hinweg kompatibel.
{{% /alert %}}

```javascript
const AsposeCells = require("aspose.cells");
// Lade die Quellarbeitsmappe mit xlsx-Ladeoptionen
const srcFile = "source.xlsx";
const workbook = new AsposeCells.Workbook(srcFile, new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx));
// Greife auf das erste Arbeitsblatt und dessen Cells-Auflistung zu
const worksheet = workbook.getWorksheets().get(0);
const cells = worksheet.getCells();
// Setze die klassische CSE-Array-Formel auf Zelle A6.
// Die Formel =TRANSPOSE(A1:D5) rotiert den 5-zeiligen x 4-spaltigen Quellbereich
// in ein 4-zeiliges x 5-spaltiges Array. Das zweite Argument (4) ist die Anzahl der Zeilen
// und das dritte Argument (5) ist die Anzahl der Spalten des resultierenden Arrays.
// Aspose.Cells schreibt das CSE-Array-Formel-Marker, sodass Excel sie als
// eine einzelne Multi-Zell-Array-Formel auswertet, kompatibel mit älteren Excel-Versionen
// (2019, 2016, 2013 usw.), die kein dynamisches Array-Spreading unterstützen.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Speichere die Arbeitsmappe, damit das Array-Formel-Marker beibehalten wird
workbook.save("output.xlsx");
```

## **Vergleich — Wann jeder Ansatz zu verwenden ist**
| Ansatz | API / Methode | Excel-Version | Quellformel erhalten? | Ausgabebereich |
|----------|--------------|---------------|--------------------------|--------------|
| Ansatz 1 — Direkte Transponierung | `range.transpose()` | Alle Excel-Versionen | Nein (nur Werte) | Gleicher Ankerbereich, 5×4 |
| Ansatz 2 — Dynamische Array-Formel | `cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Ja (läuft dynamisch über) | Vom Anker überlaufen |
| Ansatz 3 — Klassische Array-Formel (CSE) | `cell.setArrayFormula` | Alle Excel-Versionen | Ja (Multi-Cell-Array-Formel) | Explizite Größe, 4×5 |
Verwenden Sie **Ansatz 1**, wenn Sie eine schnelle, versionsübergreifende Transformation benötigen und nur die transponierten Werte in die Datei geschrieben werden sollen. Verwenden Sie **Ansatz 2**, wenn modernes Excel garantiert ist und die Formel live bleiben und sich aktualisieren soll, wenn sich die Quelle ändert. Verwenden Sie **Ansatz 3**, wenn Sie die breiteste Kompatibilität mit einer erhaltenen Formel über alle Excel-Versionen hinweg benötigen, einschließlich der älteren Versionen, die keine dynamischen Arrays unterstützen.

## **Verwandte Artikel**
- [SmartMarker Single Cell Array Rendering](/cells/de/nodejs-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/nodejs-cpp/inserting-an-image-into-a-cell/)
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/nodejs-cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="nodejs-cpp" >}}