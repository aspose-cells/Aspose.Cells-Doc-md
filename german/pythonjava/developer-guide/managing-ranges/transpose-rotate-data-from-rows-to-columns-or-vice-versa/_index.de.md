---
title: Transpose Range
description: This article explains how to transpose or rotate data from rows to columns or vice versa in Excel files using Aspose.Cells for Python via Java with three different approaches.
linktitle: Bereich transponieren
url: /de/python-java/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, Python via Java-Bibliothek, Tabellenkalkulation, Bereich transponieren, Daten drehen, Transponierungsfunktion, dynamische Array-Formel, Array-Formel, Excel TRANSPOSE, Zeilen zu Spalten
type: docs
weight: 80
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for Python via Java unterstützt das Transponieren (Drehen) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Arten. Der erste Ansatz verwendet die direkte Methode `Range.transpose()` und funktioniert in jeder Excel-Version, während der zweite Ansatz `Cell.setDynamicArrayFormula()` verwendet, um eine moderne dynamische Array-Formel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch überläuft. Der dritte Ansatz verwendet `Cell.setArrayFormula()`, um eine klassische Array-Formel mit Strg+Umschalt+Eingabe (CSE) zu schreiben, die mit älteren Excel-Versionen kompatibel ist. Dieser Artikel führt durch jeden Ansatz mit schrittweisen Anweisungen und vollständigen Codebeispielen.
{{% /alert %}}

## **Einführung**
Das Transponieren eines Bereichs bedeutet, ihn so zu drehen, dass eine Zeile zu einer Spalte wird und eine Spalte zu einer Zeile, was die Daten effektiv über die Hauptdiagonale reflektiert. In Microsoft Excel führt die Tabellenkalkulationsfunktion `TRANSPOSE` diese Operation aus, und die konzeptionelle Referenz ist unter [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) dokumentiert. Dieselbe Idee kann programmatisch auf einen Zellbereich angewendet werden, was in vielen Geschäfts- und Berichtsszenarien nützlich ist.
Häufige Szenarien, in denen eine Transponierung nützlich ist, umfassen die folgenden.
- Neuorientierung von Quartals- oder Jahresverkaufsberichten, bei denen Quartale normalerweise über die Seite und Regionen über die Seite laufen, oder umgekehrt.
- Tauschen der Achsenorientierung in Dashboards oder Diagrammen, sodass eine Zeitreihe über die Seite statt quer verläuft.
- Umformen von Daten, die aus externen Systemen importiert wurden, sodass sie dem Layout entsprechen, das von nachgelagerten Analyse- oder Berichtsvorlagen erwartet wird.
Um den Rest des Artikels konkret zu gestalten, verwendet jedes Beispiel die folgende kleine Tabelle mit Umsätzen nach Region und Quartal. In der Beispielarbeitsmappe belegt diese Tabelle den Bereich **A1:D5**, wobei **A1** als obere linke Ecke leer bleibt, **B1:D1** die Regionsüberschriften enthalten und **A2:A5** die Quartalsüberschriften enthalten.
| Region            | Europe    | Asia      | North America |
|-------------------|-----------|-----------|---------------|
| Qtr 1             | 21704714  | 8774099   | 12094215      |
| Qtr 2             | 17987034  | 12214447  | 10873099      |
| Qtr 3             | 19485029  | 14356879  | 15689543      |
| Qtr 4             | 22567894  | 15763492  | 17456723      |
Der Artikel stellt dann drei verschiedene Möglichkeiten vor, diese Daten mit Aspose.Cells for Python via Java zu transponieren, die jeweils für eine andere Excel-Version und einen anderen Anwendungsfall geeignet sind.

## **Ansatz 1 — Bereich direkt transponieren (Range.transpose)**
Verwenden Sie diesen Ansatz, wenn Sie Daten transponieren möchten, ohne die Tabellenkalkulationsfunktion `TRANSPOSE` zu verwenden. Er funktioniert in **jeder Excel-Version** und hat keine Abhängigkeit von dynamischen Arrays, was ihn zur sichersten versionsübergreifend kompatiblen Option macht. Er ist ideal, wenn Sie nur die endgültige transponierte Ausgabe benötigen und die ursprüngliche `TRANSPOSE`-Formel nicht in der Arbeitsmappe behalten müssen.

### **Verwendete API**
`Range.transpose()` ist eine Instanzmethode der Klasse `com.aspose.cells.Range`. Der Aufruf dreht den Bereich direkt um, indem er Zeilen und Spalten tauscht, sodass eine Zeile zu einer Spalte wird und eine Spalte zu einer Zeile. Die Methode ändert die zugrunde liegenden Zellen direkt, ohne eine Formel zu schreiben.

### **Schritte**
1. Öffnen Sie die Quellarbeitsmappe mit `LoadOptions`, die auf das `.xlsx`-Format eingestellt sind, durch Aufruf von `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt aus der Arbeitsmappe mit `workbook.getWorksheets().get(0)` ab.
3. Greifen Sie über `worksheet.getCells()` auf die Zellensammlung des Arbeitsblatts zu.
4. Erstellen Sie den Quellbereich, der **A1:D5** abdeckt, durch Aufruf von `cells.createRange("A1:D5")`.
5. Rufen Sie `source.transpose()` auf, um den Bereich direkt zu drehen und Zeilen und Spalten zu tauschen.
6. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Nach der Transponierung enthält derselbe Ankerbereich die gedrehten Daten. Die erste Zeile lautet (leer, **Europe**, **Asia**, **North America**) und die erste Spalte lautet (leer, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**). Jede ursprüngliche Spalte mit Verkaufszahlen wird zu einer Zeile im transponierten Bereich.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, LoadOptions, LoadFormat
srcFile = "source.xlsx"
outputFile = "transposed.xlsx"
loadOptions = LoadOptions(LoadFormat.Xlsx)
workbook = Workbook(srcFile, loadOptions)
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
source = cells.createRange("A1:D5")
source.transpose()
workbook.save(outputFile)
jpype.shutdownJVM()
```

## **Ansatz 2 — Transponieren mit einer dynamischen Array-Formel (Excel 365 / 2021)**
Verwenden Sie diesen Ansatz, wenn Sie die Formel `=TRANSPOSE(A1:D5)` als Live-Formel in der Ausgabearbeitsmappe beibehalten möchten, damit sich das Ergebnis automatisch aktualisiert, wenn sich die Quelldaten ändern, und die Zieldatei in **Excel 365 / Excel 2021 oder höher** geöffnet wird, wo dynamische Arrays und der Spill-Operator unterstützt werden.

### **Verwendete API**
`Cell.setDynamicArrayFormula(String formula, FormulaParseOptions options, boolean calculateValue)` ist eine Methode auf `com.aspose.cells.Cell`, die die Formel der Zelle als **dynamische Array-Formel** festlegt. Excel wertet die Formel einmal aus und überläuft das Ergebnis automatisch in die umgebenden Zellen. Der dritte Parameter weist, wenn er auf `True` gesetzt ist, Aspose.Cells an, die resultierenden Werte auch zum Schreibzeitpunkt zu berechnen.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe mit `Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `Cells`-Sammlung zu.
3. Platzieren Sie die dynamische Array-Formel auf Zelle **A6**, direkt unterhalb des Quellbereichs, durch Aufruf von `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", None, True)`.
4. Das Argument `None` übergibt die Standard-`FormulaParseOptions`, und das dritte Argument `True` weist Aspose.Cells an, die Formel als dynamisches Array zu behandeln und sie auszuwerten, sodass die überlaufenden Werte in die Arbeitsmappe geschrieben werden.
5. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** enthält die Formel `=TRANSPOSE(A1:D5)` und Excel überläuft das Ergebnis automatisch in den Bereich **A6:D10**, einen 5-zeiligen x 4-spalten Block, der den transponierten Daten entspricht.

{{% alert color="primary" %}}
Dieser Ansatz funktioniert **nur in Excel 365 / 2021 oder höher**. Ältere Excel-Versionen überlaufen dynamische Array-Formeln nicht korrekt.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, LoadOptions, LoadFormat, FormulaParseOptions, SaveFormat
# portierter Code hier
srcFile = "source.xlsx"
outFile = "output_transpose_dynamic.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", FormulaParseOptions(), True)
workbook.save(outFile, SaveFormat.Xlsx)
jpype.shutdownJVM()
```

## **Ansatz 3 — Transponieren mit einer klassischen Array-Formel (CSE)**
Verwenden Sie diesen Ansatz, wenn Sie eine `TRANSPOSE`-Formel in der Arbeitsmappe beibehalten möchten, die Zieldatei jedoch in **älteren Excel-Versionen (vor 2021, einschließlich 2019, 2016, 2013 usw.)** geöffnet werden kann, wo das Überlaufen dynamischer Arrays nicht unterstützt wird. Die klassische CSE-Array-Formel (Strg+Umschalt+Eingabe) ist die legacy-kompatible Alternative, die alle Excel-Versionen auswerten können.

### **Verwendete API**
`Cell.setArrayFormula(String arrayFormula, int nRows, int nColumns)` ist eine Methode auf `com.aspose.cells.Cell`, die eine **klassische Array-Formel (CSE)** der Ankerzelle zuweist und die Dimensionen des resultierenden Arrays deklariert. Aspose.Cells schreibt die Multi-Cell-Array-Formel-Markierung, sodass Excel die Formel als einzelnen Array-Ausdruck auswertet, der den deklarierten Bereich füllt.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe auf die gleiche Weise wie in den vorherigen Ansätzen.
2. Rufen Sie das erste Arbeitsblatt ab und greifen Sie auf seine `Cells`-Sammlung zu.
3. Rufen Sie `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` auf. Das zweite Argument `4` ist die Anzahl der Zeilen des Zielarrays und das dritte Argument `5` ist die Anzahl der Spalten.
4. Speichern Sie die Arbeitsmappe mit `workbook.save(outputFile)`.
Zelle **A6** ist der Anker der Array-Formel und das ausgewertete Array umfasst 4 Zeilen mal 5 Spalten, beginnend bei A6, was den transponierten Dimensionen der A1:D5-Quelle entspricht. Excel schreibt eine einzelne Array-Formel-Markierung über den resultierenden Bereich, sodass ältere Excel-Versionen sie korrekt auswerten.

{{% alert color="primary" %}}
CSE-Array-Formeln sind die klassische Excel-Methode zur Auswertung eines `TRANSPOSE`-Ausdrucks, und dieser Ansatz ist universell kompatibel über alle Excel-Versionen hinweg.
{{% /alert %}}

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, LoadOptions, LoadFormat, Worksheet, Cells
# Laden Sie die Quellarbeitsmappe mit xlsx-Ladeoptionen
srcFile = "source.xlsx"
workbook = Workbook(srcFile, LoadOptions(LoadFormat.Xlsx))
# Zugriff auf das erste Arbeitsblatt und seine Zellen-Sammlung
worksheet = workbook.getWorksheets().get(0)
cells = worksheet.getCells()
# Setzen Sie die klassische CSE-Array-Formel auf Zelle A6.
# Die Formel =TRANSPOSE(A1:D5) rotiert den 5-zeiligen x 4-spaltigen Quellbereich
# in ein 4-zeiliges x 5-spaltiges Array. Das zweite Argument (4) ist die Anzahl der Zeilen
# und das dritte Argument (5) ist die Anzahl der Spalten des resultierenden Arrays.
# Aspose.Cells schreibt den CSE-Array-Formel-Marker, damit Excel es als
# eine einzelne Mehrzellen-Array-Formel auswertet, kompatibel mit älteren Excel-Versionen
# (2019, 2016, 2013 usw.), die kein dynamisches Array-Spreading unterstützen.
cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)
# Speichern Sie die Arbeitsmappe, damit der Array-Formel-Marker beibehalten wird
workbook.save("output.xlsx")
jpype.shutdownJVM()
```

## **Vergleich — Wann welcher Ansatz zu verwenden ist**
| Ansatz | API / Methode | Excel-Version | Quellformel beibehalten? | Ausgabebereich |
|----------|--------------|---------------|--------------------------|--------------|
| Ansatz 1 — Direkte Transponierung | `Range.transpose()` | Alle Excel-Versionen | Nein (nur Werte) | Gleicher Ankerbereich, 5×4 |
| Ansatz 2 — Dynamische Array-Formel | `Cell.setDynamicArrayFormula` | Excel 365 / 2021+ | Ja (überläuft dynamisch) | Vom Anker überlaufen |
| Ansatz 3 — Klassische Array-Formel (CSE) | `Cell.setArrayFormula` | Alle Excel-Versionen | Ja (Multi-Cell-Array-Formel) | Explizite Größe, 4×5 |
Verwenden Sie **Ansatz 1**, wenn Sie eine schnelle, versionsübergreifende Transformation benötigen und nur die transponierten Werte in die Datei geschrieben werden sollen. Verwenden Sie **Ansatz 2**, wenn modernes Excel garantiert ist und die Formel live bleiben und sich aktualisieren soll, wenn sich die Quelle ändert. Verwenden Sie **Ansatz 3**, wenn Sie die breiteste Kompatibilität mit einer beibehaltenen Formel über alle Excel-Versionen hinweg benötigen, einschließlich der älteren Versionen, die keine dynamischen Arrays unterstützen.

## **Verwandte Artikel**
- [SmartMarker Single Cell Array Rendering | Aspose.Cells for Python via Java](/cells/de/python-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/python-java/inserting-an-image-into-a-cell/)
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/python-java/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="python" >}}