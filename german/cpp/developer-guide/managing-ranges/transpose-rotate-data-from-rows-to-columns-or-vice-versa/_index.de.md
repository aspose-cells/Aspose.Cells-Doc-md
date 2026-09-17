---
title: Bereich transponieren
description: Aspose.Cells for C++ unterstützt das Transponieren (Rotieren) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Arten. Der erste Ansatz verwendet die In-Place-Methode `Range.Transpose()` und funktioniert in jeder Excel-Version, während der zweite `Cell.SetDynamicArrayFormula()` verwendet, um eine moderne dynamische Arrayformel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch überläuft. Der dritte Ansatz verwendet `Cell.SetArrayFormula()`, um eine klassische Strg+Umschalt+Eingabe (CSE)-Arrayformel zu schreiben, die mit älteren Excel-Versionen kompatibel ist. Dieser Artikel führt durch jeden Ansatz mit schrittweisen Anleitungen und vollständigen Codebeispielen.
linktitle: Bereich transponieren
url: /de/cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
keywords: Aspose.Cells, C++-Bibliothek, Tabellenkalkulation, Bereich transponieren, Daten rotieren, TRANSPOSE-Funktion, dynamische Arrayformel, Arrayformel, Excel TRANSPOSE, Zeilen in Spalten
type: docs
weight: 80
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for C++ unterstützt das Transponieren (Rotieren) von Daten, sodass Zeilen zu Spalten und Spalten zu Zeilen werden, auf drei verschiedene Arten. Der erste Ansatz verwendet die In-Place-Methode `Range.Transpose()` und funktioniert in jeder Excel-Version, während der zweite `Cell.SetDynamicArrayFormula()` verwendet, um eine moderne dynamische Arrayformel `=TRANSPOSE(...)` zu schreiben, die in Excel 365 oder Excel 2021 automatisch überläuft. Der dritte Ansatz verwendet `Cell.SetArrayFormula()`, um eine klassische Strg+Umschalt+Eingabe (CSE)-Arrayformel zu schreiben, die mit älteren Excel-Versionen kompatibel ist. Dieser Artikel führt durch jeden Ansatz mit schrittweisen Anleitungen und vollständigen Codebeispielen.
{{% /alert %}}

## **Einführung**
Einen Bereich zu transponieren bedeutet, ihn so zu rotieren, dass das, was eine Zeile war, zu einer Spalte wird und das, was eine Spalte war, zu einer Zeile wird, wodurch die Daten effektiv über ihre Hauptdiagonale gespiegelt werden. In Microsoft Excel führt die Arbeitsblattfunktion `TRANSPOSE` diese Operation aus, und die konzeptionelle Referenz ist unter [https://support.microsoft.com/en-us/excel/functions/transpose-function](https://support.microsoft.com/en-us/excel/functions/transpose-function) dokumentiert. Dieses Konzept kann programmatisch auf einen Bereich von Zellen angewendet werden, was in vielen Geschäfts- und Berichtsszenarien nützlich ist.
- Neuorientierung von Quartals- oder Jahresverkaufsberichten, in denen Quartale normalerweise über die Seite und Regionen die Seite hinunter verlaufen, oder umgekehrt.
- Austausch der Achsenorientierung in Dashboards oder Diagrammen, sodass eine Zeitreihe die Seite hinunter statt über sie hinweg verläuft.
- Umformen von Daten, die aus externen Systemen importiert wurden, sodass sie dem Layout entsprechen, das von nachgelagerten Analyse- oder Berichtsvorlagen erwartet wird.
Um den Rest des Artikels konkret zu gestalten, verwendet jedes Beispiel die folgende kleine Verkaufs-nach-Region-nach-Quartal-Tabelle. In der Beispielarbeitsmappe belegt diese Tabelle den Bereich **A1:D5**, wobei **A1** als obere linke Ecke leer bleibt, **B1:D1** die Regionsüberschriften enthält und **A2:A5** die Quartalsüberschriften enthält.
| Region            | Europa     | Asien      | Nordamerika   |
|-------------------|------------|------------|---------------|
| Quartal 1         | 21704714   | 8774099    | 12094215      |
| Quartal 2         | 17987034   | 12214447   | 10873099      |
| Quartal 3         | 19485029   | 14356879   | 15689543      |
| Quartal 4         | 22567894   | 15763492   | 17456723      |
Der Artikel stellt anschließend drei verschiedene Möglichkeiten vor, diese Daten mit Aspose.Cells for C++ zu transponieren, die jeweils für eine andere Excel-Version und einen anderen Anwendungsfall geeignet sind.

## **Ansatz 1 — Bereich direkt transponieren (Range.Transpose)**
Verwenden Sie diesen Ansatz, wann immer Sie Daten transponieren möchten, ohne die Arbeitsblattfunktion `TRANSPOSE` zu verwenden. Er funktioniert in **jeder Excel-Version** und hat keine Abhängigkeit von dynamischen Arrays, was ihn zur sichersten versionsübergreifend kompatiblen Option macht. Er ist ideal, wenn Sie nur das endgültige transponierte Ergebnis benötigen und die ursprüngliche `TRANSPOSE`-Formel nicht in der Arbeitsmappe beibehalten müssen.

### **Verwendete API**
`Range.Transpose()` ist eine Instanzmethode der Klasse `Aspose.Cells.Range`. Der Aufruf dreht den Bereich direkt um, indem seine Zeilen und Spalten vertauscht werden, sodass das, was eine Zeile war, zu einer Spalte wird und das, was eine Spalte war, zu einer Zeile wird. Die Methode ändert die zugrunde liegenden Zellen direkt, ohne eine Formel zu schreiben.

### **Schritte**
1. Öffnen Sie die Quellarbeitsmappe mit `LoadOptions`, die auf das `.xlsx`-Format eingestellt sind, durch Erstellen einer `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt aus der Arbeitsmappe mit `workbook.GetWorksheets().Get(0)` ab.
3. Greifen Sie über `worksheet.GetCells()` auf die Zellensammlung des Arbeitsblatts zu.
4. Erstellen Sie den Quellbereich, der **A1:D5** abdeckt, durch Aufrufen von `cells.CreateRange(u"A1:D5")`.
5. Rufen Sie `source.Transpose()` auf, um den Bereich direkt zu rotieren und Zeilen und Spalten zu vertauschen.
6. Speichern Sie die Arbeitsmappe mit `workbook.Save(outputFile)`.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    U16String srcFile(u"source.xlsx");
    U16String outputFile(u"transposed.xlsx");
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(srcFile, loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Range source = cells.CreateRange(u"A1:D5");
    source.Transpose();
    workbook.Save(outputFile);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Ansatz 2 — Transponieren mit einer dynamischen Arrayformel (Excel 365 / 2021)**
Verwenden Sie diesen Ansatz, wenn Sie die Formel `=TRANSPOSE(A1:D5)` als Live-Formel in der Ausgabearbeitsmappe erhalten möchten, damit sich das Ergebnis automatisch aktualisiert, wenn sich die Quelldaten ändern, und die Ziel-Excel-Datei in **Excel 365 / Excel 2021 oder höher** geöffnet wird, wo dynamische Arrays und der Überlaufoperator unterstützt werden.

### **Verwendete API**
`Cell.SetDynamicArrayFormula(const char* formula, FormulaParseOptions options, bool calculateValue)` ist eine Methode auf `Aspose.Cells.Cell`, die die Formel der Zelle als **dynamische Arrayformel** festlegt. Excel wertet die Formel einmal aus und überläuft das Ergebnis automatisch in die umgebenden Zellen. Der dritte Parameter weist, wenn er auf `true` gesetzt ist, Aspose.Cells an, auch die resultierenden Werte zum Schreibzeitpunkt zu berechnen.

### **Schritte**
1. Laden Sie die Quellarbeitsmappe durch Erstellen einer `Workbook(srcFile, LoadOptions(LoadFormat::Xlsx))`.
2. Rufen Sie das erste Arbeitsblatt über `workbook.GetWorksheets().Get(0)` ab und greifen Sie über `worksheet.GetCells()` auf seine `Cells`-Sammlung zu.
3. Platzieren Sie die dynamische Arrayformel in Zelle **A6**, direkt unter dem Quellbereich, durch Aufrufen von `cells.Get(u"A6").SetDynamicArrayFormula(u"=TRANSPOSE(A1:D5)", nullptr, true)`.
4. Das `nullptr`-Argument übergibt die Standard-`FormulaParseOptions`, und das dritte Argument `true` weist Aspose.Cells an, die Formel als dynamisches Array zu behandeln und sie auszuwerten, sodass die überlaufenden Werte in die Arbeitsmappe geschrieben werden.
5. Speichern Sie die Arbeitsmappe mit `workbook.Save(outputFile)`.
Zelle **A6** enthält die Formel `=TRANSPOSE(A1:D5)` und Excel überläuft das Ergebnis automatisch in den Bereich **A6:D10**, einen 5-Zeilen-mal-4-Spalten-Block, der den transponierten Daten entspricht.

{{% alert color="primary" %}}
Dieser Ansatz funktioniert **nur in Excel 365 / 2021 oder höher**. Ältere Excel-Versionen überlaufen dynamische Arrayformeln nicht korrekt.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    std::string srcFile = "source.xlsx";
    std::string outFile = "output_transpose_dynamic.xlsx";
    LoadOptions loadOptions(LoadFormat::Xlsx);
    Workbook workbook(U16String(srcFile.c_str()), loadOptions);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(u"A6");
    FormulaParseOptions options;
    cell.SetDynamicArrayFormula(U16String("=TRANSPOSE(A1:D5)"), options, true);
    workbook.Save(U16String(outFile.c_str()), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Ansatz 3 — Transponieren mit einer klassischen Arrayformel (CSE)**
Verwenden Sie diesen Ansatz, wenn Sie eine `TRANSPOSE`-Formel in der Arbeitsmappe erhalten möchten, die Ziel-Excel-Datei jedoch möglicherweise in **älteren Excel-Versionen (vor 2021, einschließlich 2019, 2016, 2013 usw.)** geöffnet wird, in denen das Überlaufen dynamischer Arrays nicht unterstützt wird. Die klassische CSE-Arrayformel (Strg+Umschalt+Eingabe) ist die legacy-kompatible Alternative, die alle Excel-Versionen auswerten können.

### **Verwendete API**
`Cell.SetArrayFormula(const char* arrayFormula, int nRows, int nColumns)` ist eine Methode auf `Aspose.Cells.Cell`, die der Ankerzelle eine **klassische Arrayformel (CSE)** zuweist und die Dimensionen des resultierenden Arrays deklariert. Aspose.Cells schreibt die Mehrzellen-Arrayformel-Markierung, sodass Excel die Formel als einzelnen Arrayausdruck auswertet, der den deklarierten Bereich füllt.

### **Schritte**
2. Rufen Sie das erste Arbeitsblatt über `workbook.GetWorksheets().Get(0)` ab und greifen Sie über `worksheet.GetCells()` auf seine `Cells`-Sammlung zu.
3. Rufen Sie `cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5)` auf. Das zweite Argument `4` ist die Anzahl der Zeilen des Zielarrays und das dritte Argument `5` ist die Anzahl der Spalten.
4. Speichern Sie die Arbeitsmappe mit `workbook.Save(outputFile)`.
Zelle **A6** ist der Anker der Arrayformel, und das ausgewertete Array umfasst 4 Zeilen mal 5 Spalten ab A6, was den transponierten Dimensionen der A1:D5-Quelle entspricht. Excel schreibt eine einzelne Arrayformel-Markierung über den resultierenden Bereich, sodass ältere Excel-Versionen sie korrekt auswerten.

{{% alert color="primary" %}}
CSE-Arrayformeln sind die klassische Excel-Methode zur Auswertung eines `TRANSPOSE`-Ausdrucks, und dieser Ansatz ist universell kompatibel über alle Excel-Versionen hinweg.
{{% /alert %}}

```cpp
#include "Aspose.Cells.h"
#include <string>
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    // Lade die Quellarbeitsmappe mit xlsx-Ladeoptionen
    std::string srcFile = "source.xlsx";
    Workbook workbook(U16String(srcFile.c_str()), LoadOptions(LoadFormat::Xlsx));
    // Greife auf das erste Arbeitsblatt und dessen Zellsammlung zu
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    // Setze die klassische CSE-Array-Formel auf Zelle A6.
    // Die Formel =TRANSPOSE(A1:D5) rotiert den 5-zeiligen x 4-spalten Quellbereich
    // in ein 4-zeiliges x 5-spalten Array. Das zweite Argument (4) ist die Anzahl der Zeilen
    // und das dritte Argument (5) ist die Anzahl der Spalten des resultierenden Arrays.
    // Aspose.Cells schreibt die CSE-Array-Formel-Markierung, damit Excel sie als
    // eine einzelne Multi-Zell-Array-Formel auswertet, kompatibel mit älteren Excel-Versionen
    // (2019, 2016, 2013 usw.), die kein dynamisches Array-Spreading unterstützen.
    cells.Get(u"A6").SetArrayFormula(u"=TRANSPOSE(A1:D5)", 4, 5);
    // Speichere die Arbeitsmappe, damit die Array-Formel-Markierung beibehalten wird
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Vergleich — Wann jeder Ansatz zu verwenden ist**
| Ansatz | API / Methode | Excel-Version | Quellformel erhalten? | Ausgabebereich |
|--------|---------------|---------------|----------------------|----------------|
| Ansatz 1 — Direkte Transponierung | `Range.Transpose()` | Alle Excel-Versionen | Nein (nur Werte) | Anfänglicher Ankerbereich, 5×4 |
| Ansatz 2 — Dynamische Arrayformel | `Cell.SetDynamicArrayFormula` | Excel 365 / 2021+ | Ja (läuft dynamisch über) | Vom Anker überlaufen |
| Ansatz 3 — Klassische Arrayformel (CSE) | `Cell.SetArrayFormula` | Alle Excel-Versionen | Ja (Mehrzellen-Arrayformel) | Explizite Größe, 4×5 |
Verwenden Sie **Ansatz 1**, wenn Sie eine schnelle, versionsübergreifende Transformation benötigen und nur die transponierten Werte in die Datei geschrieben werden müssen. Verwenden Sie **Ansatz 2**, wenn modernes Excel garantiert ist und Sie möchten, dass die Formel live bleibt und sich aktualisiert, wenn sich die Quelle ändert. Verwenden Sie **Ansatz 3**, wenn Sie die größtmögliche Kompatibilität mit einer erhaltenen Formel über jede Excel-Version hinweg benötigen, einschließlich der älteren Versionen, die keine dynamischen Arrays unterstützen.

## **Verwandte Artikel**
- [SmartMarker Einzelzell-Array-Rendering | Aspose.Cells for C++](/cells/de/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/)
- [Einfügen eines Bildes in eine Zelle](/cells/de/cpp/inserting-an-image-into-a-cell/)
- [Aufteilen von Excel-Dateien in mehrere Dateien](/cells/de/cpp/splitting-excel-files-into-multiple-files/)

{{< app/cells/assistant language="" >}}