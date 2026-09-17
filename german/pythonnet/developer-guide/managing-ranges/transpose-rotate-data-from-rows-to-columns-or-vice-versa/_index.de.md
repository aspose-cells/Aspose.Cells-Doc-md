---
title: Bereich transponieren
linktitle: Bereich transponieren
description: Dieser Artikel erklärt, wie Daten mit Aspose.Cells for Python via .NET von Zeilen in Spalten oder umgekehrt transponiert bzw. gedreht werden können, und stellt drei verschiedene Ansätze vor.
keywords: Aspose.Cells for Python via .NET, Tabellenkalkulation, Bereich transponieren, Daten drehen, TRANSPOSE-Funktion, dynamische Arrayformel, Arrayformel, Excel TRANSPOSE, Zeilen zu Spalten
type: docs
weight: 80
url: /de/python-net/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET unterstützt das Transponieren (Drehen) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Arten. Der erste Ansatz verwendet die In-Place-Methode `range.transpose()` und funktioniert in jeder Excel-Version, während der zweite Ansatz `cell.set_dynamic_array_formula()` verwendet, um eine moderne dynamische Arrayformel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch überläuft. Der dritte Ansatz verwendet `cell.set_array_formula()`, um eine klassische CSE-Arrayformel (Strg+Umschalt+Eingabe) zu schreiben, die mit älteren Excel-Versionen kompatibel ist. Dieser Artikel führt durch jeden Ansatz mit schrittweisen Anleitungen und vollständigen Codebeispielen.
{{% /alert %}}

## **Einführung**
Einen Bereich zu transponieren bedeutet, ihn so zu drehen, dass eine Zeile zu einer Spalte wird und eine Spalte zu einer Zeile, wobei die Daten effektiv an ihrer Hauptdiagonale gespiegelt werden. In Microsoft Excel führt die Arbeitsblattfunktion `TRANSPOSE` diese Operation aus, und die konzeptionelle Referenz ist unter [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) dokumentiert. Dieses Konzept kann programmatisch auf einen Zellbereich angewendet werden, was in vielen Geschäfts- und Berichtsszenarien nützlich ist.
- Quartals- oder Jahresumsatzberichte neu ausrichten, in denen die Quartale normalerweise über die Seite und die Regionen die Seite hinunter verlaufen, oder umgekehrt.
- Die Achsenorientierung in Dashboards oder Diagrammen tauschen, sodass eine Zeitreihe die Seite hinunter statt quer verläuft.
- Daten, die aus externen Systemen importiert wurden, so umformen, dass sie dem Layout entsprechen, das von nachgelagerten Analyse- oder Berichtsvorlagen erwartet wird.
Um den Rest des Artikels konkret zu gestalten, verwendet jedes Beispiel die folgende kleine Tabelle „Umsatz nach Region nach Quartal". In der Beispielarbeitsmappe belegt diese Tabelle den Bereich **A1:D5**, wobei **A1** als obere linke Ecke leer bleibt, **B1:D1** die Regionsüberschriften enthält und **A2:A5** die Quartalsüberschriften enthält.
| Region            | Europa      | Asien       | Nordamerika  |
|-------------------|-------------|-------------|--------------|
| Q1                | 21704714    | 8774099     | 12094215     |
| Q2                | 17987034    | 12214447    | 10873099     |
| Q3                | 19485029    | 14356879    | 15689543     |
| Q4                | 22567894    | 15763492    | 17456723     |
Der Artikel stellt dann drei verschiedene Möglichkeiten vor, diese Daten mit Aspose.Cells for Python via .NET zu transponieren, jeweils abgestimmt auf eine andere Excel-Version und einen anderen Anwendungsfall.

## **Ansatz 1 — Bereich in Place transponieren (range.transpose)**
Verwenden Sie diesen Ansatz, wenn Sie Daten transponieren möchten, ohne die Arbeitsblattfunktion `TRANSPOSE` einzubeziehen. Er funktioniert in **jeder Excel-Version** und hat keine Abhängigkeit von dynamischen Arrays, was ihn zur sichersten versionsübergreifend kompatiblen Option macht. Er ist ideal, wenn Sie nur die endgültige transponierte Ausgabe benötigen und die ursprüngliche `TRANSPOSE`-Formel nicht in der Arbeitsmappe beibehalten müssen.

### **Verwendete API**
`range.transpose()` ist eine Instanzmethode der Klasse `Aspose.Cells.Range`. Der Aufruf dreht den Bereich in Place, indem er Zeilen und Spalten vertauscht, sodass eine Zeile zu einer Spalte wird und eine Spalte zu einer Zeile. Die Methode ändert die zugrunde liegenden Zellen direkt, ohne eine Formel zu schreiben.

### **Schritte**
1. Öffnen Sie die Quellarbeitsmappe mit `LoadOptions`, das auf das Format `.xlsx` eingestellt ist, durch den Aufruf `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt aus der Arbeitsmappe mit `workbook.worksheets[0]` ab.
3. Greifen Sie über `worksheet.cells` auf die Zellauflistung des Arbeitsblatts zu.
4. Erstellen Sie den Quellbereich, der **A1:D5** abdeckt, durch den Aufruf `cells.create_range("A1:D5")`.
5. Rufen Sie `source.transpose()` auf, um den Bereich in Place zu drehen und Zeilen und Spalten zu vertauschen.
6. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Nach der Transponierung enthält der ursprüngliche Ankerbereich die gedrehten Daten. Die erste Zeile lautet (leer, **Europa**, **Asien**, **Nordamerika**) und die erste Spalte lautet (leer, **Q1**, **Q2**, **Q3**, **Q4**). Jede ursprüngliche Umsatzspalte wird zu einer Zeile im transponierten Bereich.

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.XLSX))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
source = cells.create_range("A1:D5")
source.transpose()
workbook.save(outputFile)
```

## **Ansatz 2 — Transponieren mit dynamischer Arrayformel (Excel 365 / 2021)**
Verwenden Sie diesen Ansatz, wenn Sie die Formel `=TRANSPOSE(A1:D5)` als Live-Formel in der Ausgabearbeitsmappe erhalten möchten, damit sich das Ergebnis automatisch aktualisiert, wenn sich die Quelldaten ändern, und die Ziel-Excel-Datei in **Excel 365 / Excel 2021 oder neuer** geöffnet wird, wo dynamische Arrays und der Spill-Operator unterstützt werden.

### **Verwendete API**
`cell.set_dynamic_array_formula(formula, options, calculate_value)` ist eine Methode auf `Aspose.Cells.Cell`, die die Formel der Zelle als **dynamische Arrayformel** festlegt. Excel wertet die Formel einmal aus und überläuft das Ergebnis automatisch in die umgebenden Zellen. Der dritte Parameter weist, wenn er auf `True` gesetzt ist, Aspose.Cells an, die resultierenden Werte auch beim Schreiben zu berechnen.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe mit `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `cells`-Auflistung zu.
3. Platzieren Sie die dynamische Arrayformel in Zelle **A6**, direkt unter dem Quellbereich, durch den Aufruf `cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", None, True)`.
4. Das Argument `None` übergibt die Standard-`FormulaParseOptions`, und das dritte Argument `True` weist Aspose.Cells an, die Formel als dynamisches Array zu behandeln und sie auszuwerten, sodass die überlaufenden Werte in die Arbeitsmappe geschrieben werden.
5. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** enthält die Formel `=TRANSPOSE(A1:D5)`, und Excel überläuft das Ergebnis automatisch in den Bereich **A6:D10**, einen 5-zeiligen × 4-spaltigen Block, der den transponierten Daten entspricht.

{{% alert color="primary" %}}
Dieser Ansatz funktioniert **nur in Excel 365 / 2021 oder neuer**. Ältere Excel-Versionen überlaufen dynamische Arrayformeln nicht korrekt.
{{% /alert %}}

```python
import aspose.cells as ac
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
worksheet = workbook.worksheets[0]
cells = worksheet.cells
cells["A6"].set_dynamic_array_formula("=TRANSPOSE(A1:D5)", ac.FormulaParseOptions(), True)
workbook.save(outFile, ac.SaveFormat.Xlsx)
```

## **Ansatz 3 — Transponieren mit klassischer Arrayformel (CSE)**
Verwenden Sie diesen Ansatz, wenn Sie eine `TRANSPOSE`-Formel in der Arbeitsmappe erhalten möchten, die Ziel-Excel-Datei jedoch möglicherweise in **älteren Excel-Versionen (vor 2021, einschließlich 2019, 2016, 2013 usw.)** geöffnet wird, in denen das Überlaufen dynamischer Arrays nicht unterstützt wird. Die klassische CSE-Arrayformel (Strg+Umschalt+Eingabe) ist die Legacy-kompatible Alternative, die alle Excel-Versionen auswerten können.

### **Verwendete API**
`cell.set_array_formula(array_formula, n_rows, n_columns)` ist eine Methode auf `Aspose.Cells.Cell`, die der Ankerzelle eine **klassische Arrayformel (CSE)** zuweist und die Dimensionen des resultierenden Arrays deklariert. Aspose.Cells schreibt den Mehrzellen-Arrayformel-Marker, sodass Excel die Formel als einzelnen Arrayausdruck auswertet, der den deklarierten Bereich füllt.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe wie in den vorherigen Ansätzen beschrieben.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `cells`-Auflistung zu.
3. Rufen Sie `cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)` auf. Das zweite Argument `4` ist die Anzahl der Zeilen des Ziel-Arrays und das dritte Argument `5` ist die Anzahl der Spalten.
4. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** ist der Anker der Arrayformel, und das ausgewertete Array erstreckt sich über 4 Zeilen × 5 Spalten, beginnend bei A6, was den transponierten Dimensionen der Quelle A1:D5 entspricht. Excel schreibt einen einzelnen Arrayformel-Marker über den resultierenden Bereich, sodass ältere Excel-Versionen ihn korrekt auswerten.

{{% alert color="primary" %}}
CSE-Arrayformeln sind die klassische Excel-Methode, um einen `TRANSPOSE`-Ausdruck auszuwerten, und dieser Ansatz ist universell über alle Excel-Versionen hinweg kompatibel.
{{% /alert %}}

```python
import aspose.cells as ac
# Laden Sie die Quellarbeitsmappe mit xlsx-Ladeoptionen
srcFile = "source.xlsx"
workbook = ac.Workbook(srcFile, ac.LoadOptions(ac.LoadFormat.Xlsx))
# Zugriff auf das erste Arbeitsblatt und dessen Cells-Auflistung
worksheet = workbook.worksheets[0]
cells = worksheet.cells
# Setzen Sie die klassische CSE-Array-Formel in Zelle A6.
# Die Formel =TRANSPOSE(A1:D5) dreht den 5-zeiligen x 4-spalten Quellbereich
# in ein 4-zeiliges x 5-spalten Array um. Das zweite Argument (4) ist die Anzahl der Zeilen
# und das dritte Argument (5) ist die Anzahl der Spalten des resultierenden Arrays.
# Aspose.Cells schreibt die CSE-Array-Formel-Markierung, sodass Excel sie als
# eine einzelne Mehrzellen-Array-Formel auswertet, kompatibel mit älteren Excel-Versionen
# (2019, 2016, 2013 usw.), die das dynamische Array-Spilling nicht unterstützen.
cells["A6"].set_array_formula("=TRANSPOSE(A1:D5)", 4, 5)
# Speichern Sie die Arbeitsmappe, damit die Array-Formel-Markierung beibehalten wird
workbook.save("output.xlsx")
```

## **Vergleich — Wann jeden Ansatz verwenden**
| Ansatz | API / Methode | Excel-Version | Quellformel erhalten? | Ausgabebereich |
|--------|---------------|---------------|----------------------|----------------|
| Ansatz 1 — In-Place-Transponierung | `range.transpose()` | Alle Excel-Versionen | Nein (nur Werte) | Ursprünglicher Ankerbereich, 5×4 |
| Ansatz 2 — Dynamische Arrayformel | `cell.set_dynamic_array_formula` | Excel 365 / 2021+ | Ja (läuft dynamisch über) | Vom Anker aus überlaufend |
| Ansatz 3 — Klassische Arrayformel (CSE) | `cell.set_array_formula` | Alle Excel-Versionen | Ja (Mehrzellen-Arrayformel) | Explizite Größe, 4×5 |
Verwenden Sie **Ansatz 1**, wenn Sie eine schnelle, versionsübergreifende Transformation benötigen und nur die transponierten Werte in die Datei geschrieben werden sollen. Verwenden Sie **Ansatz 2**, wenn modernes Excel garantiert ist und die Formel live bleiben und sich aktualisieren soll, wenn sich die Quelle ändert. Verwenden Sie **Ansatz 3**, wenn Sie die größtmögliche Kompatibilität mit einer erhaltenen Formel über jede Excel-Version hinweg benötigen, einschließlich der älteren Versionen, die keine dynamischen Arrays unterstützen.

## **Verwandte Artikel**
- [SmartMarker Einzelzellen-Array-Rendering | Aspose.Cells for Python via .NET](/cells/de/python-net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Bild in eine Zelle einfügen](/cells/de/python-net/inserting-an-image-into-a-cell/)
- [Excel-Dateien in mehrere Dateien aufteilen](/cells/de/python-net/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python-net" >}}