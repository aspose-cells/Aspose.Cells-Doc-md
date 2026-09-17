---
title: Bereich transponieren
linktitle: Bereich transponieren
description: Dieser Artikel erklärt, wie Sie Daten in Excel-Dateien mit Aspose.Cells for .NET auf drei verschiedene Weisen transponieren oder aus Zeilen in Spalten und umgekehrt rotieren können.
keywords: Aspose.Cells, .NET-Bibliothek, Tabelle, Bereich transponieren, Daten rotieren, Transpose-Funktion, dynamische Arrayformel, Arrayformel, Excel TRANSPOSE, Zeilen in Spalten
type: docs
weight: 80
url: /de/net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for .NET unterstützt das Transponieren (Rotieren) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Weisen. Der erste Ansatz verwendet die direkte Methode `Range.Transpose()` und funktioniert in jeder Excel-Version. Der zweite verwendet `Cell.SetDynamicArrayFormula()`, um eine moderne dynamische Arrayformel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch überläuft. Der dritte Ansatz verwendet `Cell.SetArrayFormula()`, um eine klassische Arrayformel (Strg+Umschalt+Eingabe, CSE) zu schreiben, die mit älteren Excel-Versionen kompatibel ist. Dieser Artikel führt Sie schrittweise durch jeden Ansatz mit vollständigen Codebeispielen.
{{% /alert %}}

## **Einführung**
Einen Bereich zu transponieren bedeutet, ihn so zu rotieren, dass das, was eine Zeile war, zu einer Spalte wird und das, was eine Spalte war, zu einer Zeile wird, wodurch die Daten effektiv über ihre Hauptdiagonale gespiegelt werden. In Microsoft Excel führt die Arbeitsblattfunktion `TRANSPOSE` diese Operation aus, und die konzeptionelle Referenz ist unter [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) dokumentiert. Dieses Konzept kann programmatisch auf einen Zellenbereich angewendet werden, was in vielen Geschäfts- und Berichtsszenarien nützlich ist.
- Quartals- oder Jahresumsatzberichte neu ausrichten, in denen die Quartale normalerweise quer über die Seite und die Regionen die Seite hinunter verlaufen oder umgekehrt.
- Die Achsenausrichtung in Dashboards oder Diagrammen tauschen, sodass eine Zeitreihe die Seite hinunter statt quer über die Seite verläuft.
- Daten umformen, die aus externen Systemen importiert wurden, damit sie dem Layout entsprechen, das von nachgelagerten Analyse- oder Berichtsvorlagen erwartet wird.
Um den Rest des Artikels konkret zu gestalten, verwendet jedes Beispiel die folgende kleine Tabelle mit Umsätzen nach Region und Quartal. In der Beispielarbeitsmappe belegt diese Tabelle den Bereich **A1:D5**, wobei **A1** als obere linke Ecke leer bleibt, **B1:D1** die Regionsüberschriften enthalten und **A2:A5** die Quartalsüberschriften enthalten.
| Region            | Europa     | Asien      | Nordamerika |
|-------------------|------------|------------|--------------|
| Q1                | 21704714   | 8774099    | 12094215     |
| Q2                | 17987034   | 12214447   | 10873099     |
| Q3                | 19485029   | 14356879   | 15689543     |
| Q4                | 22567894   | 15763492   | 17456723     |
Der Artikel stellt dann drei verschiedene Möglichkeiten vor, diese Daten mit Aspose.Cells for .NET zu transponieren, jede geeignet für eine andere Excel-Version und einen anderen Anwendungsfall.

## **Ansatz 1 — Bereich direkt transponieren (Range.Transpose)**
Verwenden Sie diesen Ansatz, wann immer Sie Daten transponieren möchten, ohne die Arbeitsblattfunktion `TRANSPOSE` einzubeziehen. Er funktioniert in **jeder Excel-Version** und hat keine Abhängigkeit von dynamischen Arrays, was ihn zur sichersten, versionsübergreifend kompatiblen Option macht. Er ist ideal, wenn Sie nur das endgültige transponierte Ergebnis benötigen und die ursprüngliche `TRANSPOSE`-Formel nicht in der Arbeitsmappe beibehalten müssen.

### **Verwendete API**
`Range.Transpose()` ist eine Instanzmethode der Klasse `Aspose.Cells.Range`. Ihr Aufruf dreht den Bereich direkt um, indem sie seine Zeilen und Spalten vertauscht, sodass das, was eine Zeile war, zu einer Spalte wird und das, was eine Spalte war, zu einer Zeile wird. Die Methode verändert die zugrunde liegenden Zellen direkt, ohne eine Formel zu schreiben.

### **Schritte**
1. Öffnen Sie die Quellarbeitsmappe mit `LoadOptions`, eingestellt auf das Format `.xlsx`, durch den Aufruf von `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt aus der Arbeitsmappe mit `workbook.Worksheets[0]` ab.
3. Greifen Sie über `worksheet.Cells` auf die Zellensammlung des Arbeitsblatts zu.
4. Erstellen Sie den Quellbereich, der **A1:D5** abdeckt, durch den Aufruf von `cells.CreateRange("A1:D5")`.
5. Rufen Sie `source.Transpose()` auf, um den Bereich direkt zu rotieren und Zeilen und Spalten zu vertauschen.
6. Speichern Sie die Arbeitsmappe mit `workbook.Save(outputFile)`.
Nach der Transposition enthält dieser Ankerbereich die rotierten Daten. Die erste Zeile lautet (leer, **Europa**, **Asien**, **Nordamerika**) und die erste Spalte lautet (leer, **Q1**, **Q2**, **Q3**, **Q4**). Jede ursprüngliche Umsatzspalte wird zu einer Zeile im transponierten Bereich.

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outputFile = "transposed.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
var source = cells.CreateRange("A1:D5");
source.Transpose();
workbook.Save(outputFile);
```

## **Ansatz 2 — Transponieren mit dynamischer Arrayformel (Excel 365 / 2021)**
Verwenden Sie diesen Ansatz, wenn Sie die Formel `=TRANSPOSE(A1:D5)` als Live-Formel in der Ausgabearbeitsmappe beibehalten möchten, damit sich das Ergebnis automatisch aktualisiert, wenn sich die Quelldaten ändern, und die Excel-Zieldatei in **Excel 365 / Excel 2021 oder höher** geöffnet wird, in denen dynamische Arrays und der Überlaufoperator unterstützt werden.

### **Verwendete API**
`Cell.SetDynamicArrayFormula(string formula, FormulaParseOptions options, bool calculateValue)` ist eine Methode auf `Aspose.Cells.Cell`, die die Formel der Zelle als **dynamische Arrayformel** festlegt. Excel wertet die Formel einmal aus und überläuft das Ergebnis automatisch in die umgebenden Zellen. Der dritte Parameter weist Aspose.Cells, wenn er auf `true` gesetzt ist, an, die resultierenden Werte auch beim Schreiben zu berechnen.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe mit `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `Cells`-Sammlung zu.
3. Platzieren Sie die dynamische Arrayformel in Zelle **A6**, direkt unter dem Quellbereich, durch den Aufruf von `cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)`.
4. Das Argument `new FormulaParseOptions()` verwendet die Standardeinstellungen von `FormulaParseOptions`, und das dritte Argument `true` weist Aspose.Cells an, die Formel als dynamisches Array zu behandeln und sie auszuwerten, sodass die überlaufenden Werte in die Arbeitsmappe geschrieben werden.
5. Speichern Sie die Arbeitsmappe mit `workbook.Save(outputFile)`.
Zelle **A6** enthält die Formel `=TRANSPOSE(A1:D5)`, und Excel überläuft das Ergebnis automatisch in den Bereich **A6:E9**, einen 4-zeiligen mal 5-spaltigen Block, der den transponierten Daten entspricht.

{{% alert color="primary" %}}
Dieser Ansatz funktioniert **nur in Excel 365 / 2021 oder höher**. Ältere Excel-Versionen überlaufen dynamische Arrayformeln nicht korrekt.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
string srcFile = "source.xlsx";
string outFile = "output_transpose_dynamic.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
cells["A6"].SetDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true);
workbook.Save(outFile, SaveFormat.Xlsx);
```

## **Ansatz 3 — Transponieren mit klassischer Arrayformel (CSE)**
Verwenden Sie diesen Ansatz, wenn Sie eine `TRANSPOSE`-Formel in der Arbeitsmappe beibehalten möchten, die Excel-Zieldatei jedoch in **älteren Excel-Versionen (vor 2021, einschließlich 2019, 2016, 2013 usw.)** geöffnet werden kann, in denen der Überlauf dynamischer Arrays nicht unterstützt wird. Die klassische CSE-Arrayformel (Strg+Umschalt+Eingabe) ist die legacy-kompatible Alternative, die alle Excel-Versionen auswerten können.

### **Verwendete API**
`Cell.SetArrayFormula(string arrayFormula, int nRows, int nColumns)` ist eine Methode auf `Aspose.Cells.Cell`, die eine **klassische Arrayformel (CSE)** der Ankerzelle zuweist und die Dimensionen des resultierenden Arrays festlegt. Aspose.Cells schreibt die Mehrzellen-Arrayformel-Markierung, sodass Excel die Formel als einzelnen Arrayausdruck auswertet, der den angegebenen Bereich füllt.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe wie in den vorherigen Ansätzen beschrieben.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `Cells`-Sammlung zu.
3. Rufen Sie `cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` auf. Das zweite Argument `4` ist die Anzahl der Zeilen des Zielarrays und das dritte Argument `5` ist die Anzahl der Spalten.
4. Speichern Sie die Arbeitsmappe mit `workbook.Save(outputFile)`.
Zelle **A6** ist der Anker der Arrayformel und das ausgewertete Array umfasst 4 Zeilen mal 5 Spalten ab A6, was den transponierten Dimensionen des Quellbereichs A1:D5 entspricht. Excel schreibt eine einzelne Arrayformel-Markierung über den resultierenden Bereich, sodass ältere Excel-Versionen sie korrekt auswerten.

{{% alert color="primary" %}}
CSE-Arrayformeln sind die klassische Excel-Methode, um einen `TRANSPOSE`-Ausdruck auszuwerten, und dieser Ansatz ist universell über alle Excel-Versionen hinweg kompatibel.
{{% /alert %}}

```csharp
using System;
using System.IO;
using Aspose.Cells;
// Laden Sie die Quellarbeitsmappe mit xlsx LoadOptions
string srcFile = "source.xlsx";
Workbook workbook = new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx));
// Zugriff auf das erste Arbeitsblatt und dessen Cells-Auflistung
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;
// Setzen Sie die klassische CSE-Array-Formel in Zelle A6.
// Die Formel =TRANSPOSE(A1:D5) rotiert den 5-zeiligen x 4-spalten Quellbereich
// in ein 4-zeiliges x 5-spalten Array. Das zweite Argument (4) ist die Anzahl der Zeilen
// und das dritte Argument (5) ist die Anzahl der Spalten des resultierenden Arrays.
// Aspose.Cells schreibt die CSE-Array-Formel-Markierung, damit Excel sie als
// eine einzelne Mehrzellen-Array-Formel auswertet, kompatibel mit älteren Excel-Versionen
// (2019, 2016, 2013 usw.), die kein dynamisches Array-Spilling unterstützen.
cells["A6"].SetArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
// Speichern Sie die Arbeitsmappe, damit die Array-Formel-Markierung beibehalten wird
workbook.Save("output.xlsx");
```

## **Vergleich — Wann jeder Ansatz verwendet werden sollte**
| Ansatz | API / Methode | Excel-Version | Quellformel beibehalten? | Ausgabebereich |
|----------|--------------|---------------|--------------------------|--------------|
| Ansatz 1 — Direktes Transponieren | `Range.Transpose()` | Alle Excel-Versionen | Nein (nur Werte) | Ursprünglicher Ankerbereich, 5×4 |
| Ansatz 2 — Dynamische Arrayformel | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Ja (läuft dynamisch über) | Vom Anker überlaufen |
| Ansatz 3 — Klassische Arrayformel (CSE) | `Cell.SetArrayFormula` | Alle Excel-Versionen | Ja (Mehrzellen-Arrayformel) | Explizite Größe, 4×5 |
Verwenden Sie **Ansatz 1**, wenn Sie eine schnelle, versionsübergreifende Transformation benötigen und nur die transponierten Werte in die Datei geschrieben werden sollen. Verwenden Sie **Ansatz 2**, wenn modernes Excel garantiert ist und die Formel live bleiben und sich bei Änderungen der Quelle aktualisieren soll. Verwenden Sie **Ansatz 3**, wenn Sie die größte Kompatibilität mit einer beibehaltenen Formel über alle Excel-Versionen hinweg benötigen, einschließlich der älteren Versionen, die keine dynamischen Arrays unterstützen.

{{< app/cells/assistant language="csharp" >}}