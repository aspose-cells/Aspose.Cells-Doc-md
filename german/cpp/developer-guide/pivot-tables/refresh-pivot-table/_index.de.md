---
title: Aktualisieren von Pivot-Tabellen in Aspose.Cells for C++
linktitle: Aktualisieren von Pivot-Tabellen
description: Erfahren Sie, wie Sie Pivot-Tabellen in Aspose.Cells for C++ mithilfe der Pivot-Aktualisierungs-API ab v26.7 aktualisieren. Dieser Artikel behandelt RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData und GetPivotTables mit praktischen Codebeispielen.
keywords: Aspose.Cells, C++, Pivot-Tabelle, Aktualisierung, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /de/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells bietet eine geschichtete Aktualisierungs-API, mit der Sie Pivot-Daten in vier verschiedenen Geltungsbereichen neu laden können – von der gesamten Arbeitsmappe bis hin zu einer einzelnen Pivot-Tabelle. Beginnend mit **Aspose.Cells for C++ v26.7** ist die legacy Methode `PivotTable.RefreshData()` als veraltet markiert und sollte durch die effizienteren, cache-bewussten APIs ersetzt werden, die in diesem Artikel beschrieben werden.
{{% /alert %}}
## Einführung
Das Aktualisieren einer Pivot-Tabelle ist selten ein einzelner Vorgang. Im Hintergrund verwaltet Aspose.Cells eine geschichtete Datenkette, die Ihre ursprünglichen Quelldaten mit den gerenderten Werten verbindet, die Sie im Arbeitsblatt sehen. Das Verständnis dieser Kette ist der Schlüssel zur Auswahl der richtigen Aktualisierungs-API für jede Situation.
Die vierstufige Datenkette ist:
1. **Datenquelle** — die ursprünglichen Arbeitsblattbereiche, Datenbankabfragen oder Konsolidierungsbereiche, in denen die Rohwerte leben.
2. **PivotCache** — der In-Memory-Snapshot der Quelldaten. Jede Pivot-Tabelle wird auf einem `PivotCache` aufgebaut; hier werden alle Daten gesammelt und aggregiert.
3. **PivotTable** — das Ansichtsobjekt, das Zeilen-, Spalten-, Wert- und Filterfelder definiert. Eine `PivotTable` liest *nur* aus ihrem `PivotCache`, niemals direkt aus der Datenquelle.
4. **Cells** — die Arbeitsblatt-`Cells`, in die die `PivotTable` ihre berechneten Werte und Stile rendert.
Ein besonders wichtiges Konzept ist der **gemeinsam genutzte Cache**. Wenn mehrere Pivot-Tabellen in einer Arbeitsmappe auf denselben Quellbereich verweisen, teilen sie sich *eine* `PivotCache`-Instanz. Auf einen einzelnen `PivotCache` können viele Pivot-Tabellen verweisen, und das Aktualisieren dieses Caches aktualisiert jede abhängige `PivotTable` auf einmal.
{{% alert color="primary" %}}
`PivotCache.SourceType` (Enum `PivotTableSourceType`) gibt an, woher die Cache-Daten stammen. Ab v26.7 unterstützt `PivotCache.Refresh()` nur die Quellentypen **`Sheet`** und **`Consolidation`** — also Daten, die in Arbeitsblattbereichen leben. Externe Quellen (Datenbanken, externe Verbindungen usw.) sind über die Cache-API noch nicht aktualisierbar.
{{% /alert %}}
Aufgrund dieser Kette gibt es in Aspose.Cells zwei grundlegende Aktualisierungspfade:
- **`PivotCache.Refresh()`** — lädt Quelle → Cache neu UND berechnet alle abhängigen `PivotTable`s in einem einzigen Vorgang neu.
- **`PivotTable.CalculateData()`** — berechnet die Anzeige einer einzelnen `PivotTable` aus bereits zwischengespeicherten Daten neu, ohne Rückkehr zur Datenquelle.
Alle Szenarien in diesem Artikel verwenden Arbeitsblatt-Zellen als Quelldaten, daher ist der Quellentyp `Sheet` und die Aktualisierungsvorgänge verhalten sich wie beschrieben.
## Erforderliche Include-Direktiven
Alle C++-Beispiele in diesem Artikel beginnen mit den folgenden Header-Includes und Namespace-Direktiven, da die Pivot-Typen im Namespace `Aspose::Cells::Pivot` leben:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`
## Alle Pivot-Tabellen in der Arbeitsmappe aktualisieren
Wenn Sie sicherstellen müssen, dass jeder Pivot-Cache und jede Pivot-Tabelle in der Arbeitsmappe die neuesten Quelldaten widerspiegelt, ist die einfachste und umfassendste API `Workbook.RefreshAll()`. Ein einziger Aufruf durchläuft die gesamte Arbeitsmappe — er aktualisiert jeden `PivotCache` aus seiner Quelle und berechnet dann jede abhängige `PivotTable` neu. Dies ist der empfohlene Ansatz für allgemeine, umfassende Dokumentaktualisierungen, bei denen die Leistung keine Rolle spielt.
Das folgende Beispiel erstellt eine Arbeitsmappe mit einem Fruit/Year/Amount-Quellbereich, erstellt eine Pivot-Tabelle, ändert einige Quellwerte und verwendet dann `RefreshAll()`, um alles in einem einzigen Aufruf auf den neuesten Stand zu bringen.
```cpp
#include "Aspose.Cells.h"



using namespace Aspose::Cells;



int main() {



    Aspose::Cells::Startup();



    Workbook wb;



    Worksheet ws = wb.GetWorksheets().Get(0);



    Cells cells = ws.GetCells();



    //Erstellen von Beispieldaten in die Tabelle.



    cells.Get(u"A1").PutValue(U16String("Fruit"));



    cells.Get(u"B1").PutValue(U16String("Year"));



    cells.Get(u"C1").PutValue(U16String("Amount"));



    cells.Get(u"A2").PutValue(U16String("grape"));



    cells.Get(u"B2").PutValue(2020);



    cells.Get(u"C2").PutValue(50);



    cells.Get(u"A3").PutValue(U16String("blueberry"));



    cells.Get(u"B3").PutValue(2020);



    cells.Get(u"C3").PutValue(60);



    cells.Get(u"A4").PutValue(U16String("kiwi"));



    cells.Get(u"B4").PutValue(2020);



    cells.Get(u"C4").PutValue(70);



    cells.Get(u"A5").PutValue(U16String("cherry"));



    cells.Get(u"B5").PutValue(2020);



    cells.Get(u"C5").PutValue(80);



    cells.Get(u"A6").PutValue(U16String("grape"));



    cells.Get(u"B6").PutValue(2021);



    cells.Get(u"C6").PutValue(90);



    cells.Get(u"A7").PutValue(U16String("blueberry"));



    cells.Get(u"B7").PutValue(2021);



    cells.Get(u"C7").PutValue(100);



    cells.Get(u"A8").PutValue(U16String("kiwi"));



    cells.Get(u"B8").PutValue(2021);



    cells.Get(u"C8").PutValue(110);



    cells.Get(u"A9").PutValue(U16String("cherry"));



    cells.Get(u"B9").PutValue(2021);



    cells.Get(u"C9").PutValue(120);



    //Eine Pivot-Tabelle hinzufügen.



    int idx = ws.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");



    PivotTable pt = ws.GetPivotTables().Get(idx);



    //Zeilen-, Spalten- und Datenfelder zur Pivot-Tabelle hinzufügen.



    pt.AddFieldToArea(PivotFieldType::Row, u"Fruit");



    pt.AddFieldToArea(PivotFieldType::Column, u"Year");



    pt.AddFieldToArea(PivotFieldType::Data, u"Amount");



    //Daten in der Quelldaten-Tabelle ändern.



    cells.Get(u"C2").PutValue(55);



    cells.Get(u"C5").PutValue(85);



    cells.Get(u"C9").PutValue(125);



    //Pivot-Tabelle aktualisieren und berechnen.






    pt.CalculateData();



    //Arbeitsmappe speichern.



    wb.Save(u"output.xlsx");



    Aspose::Cells::Cleanup();



    return 0;



}
```
## Alle Pivot-Tabellen auf einem einzelnen Arbeitsblatt aktualisieren
Manchmal müssen Sie nur die Pivot-Tabellen aktualisieren, die sich auf einem bestimmten Arbeitsblatt befinden — zum Beispiel, wenn bekannt ist, dass Pivot-Tabellen auf anderen Arbeitsblättern nicht zusammenhängen und nicht berührt werden sollten. Für diesen Fall bietet Aspose.Cells `Worksheet.RefreshPivotTables()`, das auf eine einzelne `Worksheet`-Instanz beschränkt ist.
Dies ist selektiver als `Workbook.RefreshAll()`: nur die Pivot-Tabellen auf dem Zielarbeitsblatt werden aktualisiert, während Pivot-Tabellen auf anderen Arbeitsblättern unberührt bleiben.
Das folgende Beispiel füllt die gleichen Fruit/Year/Amount-Quelldaten, fügt eine Pivot-Tabelle auf dem ersten Arbeitsblatt hinzu, ändert einige Quellwerte und aktualisiert dann nur die Pivot-Tabellen auf diesem Arbeitsblatt.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);

    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);

    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);

    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);

    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);

    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);

    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);

    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);

    worksheet.RefreshPivotTables();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## Eine einzelne Pivot-Tabelle aktualisieren
Wenn Sie eine fein abgestimmte Kontrolle über eine einzelne Pivot-Tabelle wünschen, bietet Ihnen die cache-basierte API zwei Optionen. Die Wahl zwischen ihnen hängt davon ab, was sich tatsächlich geändert hat: die zugrundeliegenden Quelldaten oder nur die Ansichts-/Layouteinstellungen der Pivot-Tabelle selbst.
### Quelldaten geändert — Verwenden Sie `PivotCache.Refresh()`
Wenn sich die zugrundeliegenden Quelldaten geändert haben, ist der richtige Einstiegspunkt `pivotTable.GetPivotCache().Refresh()`. Dieser Aufruf liest die Quelldaten erneut in den Cache ein und berechnet dann jede `PivotTable` neu, die von diesem Cache abhängt.
{{% alert color="primary" %}}
Da Pivot-Tabellen eine einzige `PivotCache`-Instanz gemeinsam nutzen, berechnet der Aufruf von `PivotCache.Refresh()` **alle** Pivot-Tabellen neu, die auf demselben Cache aufgebaut sind — nicht nur die, auf die Sie verweisen. Wenn zwei Pivot-Tabellen denselben Quellbereich gemeinsam nutzen, aktualisiert das Aktualisieren eines Caches beide.
{{% /alert %}}
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, um dieses Verhalten mit gemeinsamem Cache zu demonstrieren, ändert einige Quellwerte und aktualisiert dann über eine Cache-Referenz.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Kopfzeile: Frucht / Jahr / Betrag
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Datenzeilen
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // Fügt die erste Pivot-Tabelle "Pivot1" hinzu, verankert an Zelle E3, Quellbereich A1:C9
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Felder für Pivot1 zuweisen
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Fügt eine ZWEITE Pivot-Tabelle "Pivot2" hinzu, verankert an E15, mit demselben Quellbereich A1:C9
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Dieselben Felder für Pivot2 zuweisen
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Mehrere Betragszellenwerte in den Quelldaten ändern, um eine Datenänderung zu simulieren
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // Den gemeinsam genutzten PivotCache aktualisieren, indem die Pivot-Tabellendaten aktualisiert werden
    pivotTable1.RefreshData();

    // Die Arbeitsmappe speichern
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
### Nur Ansicht/Layout geändert — Verwenden Sie `CalculateData()`
Wenn sich die Quelldaten *nicht* geändert haben, sondern nur die Ansichts- oder Layouteinstellungen der Pivot-Tabelle geändert wurden (zum Beispiel wurde ein Feld in einen anderen Bereich verschoben oder eine Einstellung zum Aktualisieren beim Öffnen umgeschaltet), ist es nicht erforderlich, zur Datenquelle zurückzukehren. Der Cache enthält bereits die richtigen Daten; nur die gerenderte `PivotTable` muss neu berechnet werden. In diesem Fall ist `pivotTable.CalculateData()` die richtige Wahl.
Dies vermeidet den unnötigen Quellabruf und ist deutlich schneller, wenn viele Pivot-Tabellen denselben Cache gemeinsam nutzen.
Das folgende Beispiel ändert eine Nicht-Quelleigenschaft der Pivot-Tabelle und ruft dann `CalculateData()` auf, um sie aus dem vorhandenen Cache neu zu rendern.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Schreibe die Kopfzeile Fruit / Year / Amount
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // Schreibe 8 Datenzeilen (Zeilen 2-9, passend zum Quellbereich A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);

    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);

    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);

    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);

    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);

    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);

    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);

    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);

    // Füge eine Pivot-Tabelle mit dem Namen "Pivot1" an der Zielzelle E3 hinzu, deren Quelle A1:C9 ist
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Weise Felder zu: Fruit in Zeile, Year in Spalte, Amount in Daten
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Ändere eine Anzeige-/Layout-Eigenschaft – dies ist eine reine Darstellungsänderung,
    // daher ist KEIN erneutes Einlesen der Quelldaten über PivotCache.Refresh() erforderlich.
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() rendert die Anzeige DIESER Pivot-Tabelle (Daten + Stil) neu
    // aus den bereits im PivotCache vorhandenen Daten. Da sich die Quelldaten nicht geändert haben,
    // erfolgt kein Round-Trip zur Quelle – nur die zwischengespeicherten Werte werden neu
    // in die Arbeitsblattzellen berechnet.
    pivotTable.CalculateData();

    // Speichere die Arbeitsmappe auf der Festplatte
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## Alle Pivot-Tabellen abrufen, die denselben PivotCache gemeinsam nutzen
Eine Arbeitsmappe enthält oft viele Pivot-Tabellen, die alle auf einem gemeinsam genutzten Cache sitzen. Um sie aufzulisten — zum Beispiel vor einer Stapelaktualisierung oder um die Auswirkungen des gemeinsam genutzten Caches zu diagnostizieren — verwenden Sie `PivotCache.GetPivotTables()`. Diese Methode gibt die Sammlung jeder `PivotTable` zurück, die von dem angegebenen Cache abhängt.
Dies ist auch der direkteste Weg, um zu bestätigen, dass zwei Pivot-Tabellen tatsächlich dieselbe `PivotCache`-Instanz gemeinsam nutzen: Sie können Cache-Referenzen vergleichen oder einfach die von `GetPivotTables()` zurückgegebene Sammlung durchlaufen und beobachten, welche Pivot-Tabellen darin erscheinen.
Das folgende Beispiel erstellt zwei Pivot-Tabellen auf demselben Quellbereich, überprüft, dass sie dieselbe Cache-Instanz gemeinsam nutzen, und listet dann die Pivot-Tabellen des Caches auf.

## Migration von der veralteten `PivotTable.RefreshData()`
Vor Aspose.Cells for C++ v26.7 war die Standardmethode zum Aktualisieren einer Pivot-Tabelle der Aufruf von `PivotTable.RefreshData()` für jede Pivot-Tabelle einzeln. Ab v26.7 ist diese Methode als **veraltet** markiert und sollte durch die oben beschriebenen cache-bewussten APIs ersetzt werden.
Es gibt zwei Gründe, warum der pro-Tabelle-Ansatz `RefreshData()` in realen Arbeitsmappen problematisch ist:
- Er ruft die Daten jedes Mal *erneut* aus der Quelle ab, auch wenn sich die Quelle nicht geändert hat.
- Jeder Aufruf aktualisiert den gesamten gemeinsam genutzten Cache. Wenn viele Pivot-Tabellen einen Cache gemeinsam nutzen, verursacht das wiederholte Aufrufen von `RefreshData()` pro Pivot-Tabelle ein wiederholtes erneutes Abrufen desselben Caches, was sehr langsam ist.
Die empfohlenen Ersetzungen sind:
- **Aktualisieren Sie ALLE Pivot-Tabellen in der Arbeitsmappe** → verwenden Sie `workbook.RefreshAll();`
- **Aktualisieren Sie einige davon** → verwenden Sie `pivotTable.GetPivotCache().Refresh();` für einen Cache. Da der Cache gemeinsam genutzt wird, aktualisiert dieser einzelne Aufruf jede Pivot-Tabelle, die auf diesem Cache aufgebaut ist. Andere Pivot-Tabellen, die auf einem bereits aktualisierten Cache sitzen, können sicher übersprungen werden.
- **Nur die Pivot-Ansicht/das Layout hat sich geändert** → verwenden Sie `pivotTable.CalculateData();` um aus dem vorhandenen Cache neu zu rendern, ohne einen Quellrundgang.
Das folgende Beispiel demonstriert das neue effiziente Muster für Arbeitsmappen mit mehreren Pivot-Tabellen, die einen einzigen Cache gemeinsam nutzen.
```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");

    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);

    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);


    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
## Welche Aktualisierungs-API sollte ich verwenden?
Die folgende Tabelle fasst die verfügbaren Aktualisierungs-APIs zusammen und wann welche zu wählen ist.
| Ziel | Empfohlene API | Hinweise |
|------|-----------------|-------|
| Alles in der Arbeitsmappe aktualisieren | `Workbook.RefreshAll()` | Ein Aufruf; deckt alle Caches und Tabellen ab. |
| Nur Pivot-Tabellen auf einem einzelnen Blatt aktualisieren | `Worksheet.RefreshPivotTables()` | Auf ein Arbeitsblatt beschränkt. |
| Quelldaten für einen Cache geändert | `pivotTable.GetPivotCache().Refresh()` | Aktualisiert ALLE Pivot-Tabellen auf diesem gemeinsam genutzten Cache. |
| Nur Ansichts-/Layouteinstellungen geändert | `pivotTable.CalculateData()` | Überspringt unnötigen Quellrundgang. |
| Alle Pivot-Tabellen auf einem gemeinsam genutzten Cache auflisten | `pivotCache.GetPivotTables()` | Verwenden Sie dies zur Auflistung vor einer Massenaktualisierung. |
In der Praxis sind die cache-basierten APIs der veralteten pro-Tabelle `RefreshData()` vorzuziehen. Sie kennen gemeinsam genutzte Caches, vermeiden redundante Quellabrufe und ermöglichen es Ihnen, den kleinsten Geltungsbereich zu wählen, der Ihre Aktualisierungsanforderungen erfüllt.

{{< app/cells/assistant language="cpp" >}}
