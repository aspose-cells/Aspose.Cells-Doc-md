---
title: PivotTable erstellen
linktitle: PivotTable erstellen
description: Erstellen und formatieren Sie PivotTables mit Aspose.Cells for C++.
keywords: PivotTable erstellen, PivotTable einfügen, PivotTable formatieren.
type: docs
weight: 160
url: /de/cpp/create-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Was ist eine PivotTable?**
Eine PivotTable ist ein interaktiver Zusammenfassungsbericht: Sie verdichtet einen großen Block zeilenweise erfasster Rohdaten zu einer kompakten Matrix, ohne dass eine einzige Formel erforderlich ist. Sie legen fest, welche Spalten zu Zeilenbeschriftungen, welche zu Spaltenbeschriftungen und welche als Werte aggregiert werden – die PivotTable übernimmt die Gruppierung und die Berechnung:
- **Zusammenfassen** – Gesamtumsatz pro Produkt, pro Region oder pro Quart anstelle langer Formelketten.
- **Vergleichen** – Kategorien in den Zeilen und Zeiträume in den Spalten verwandeln eine flache Liste in einen Kreuzbericht, in dem Trends auf einen Blick sichtbar werden.
- **Detailebene öffnen** – Doppelklicken Sie auf einen Zusammenfassungswert, um die zugrunde liegenden Quellzeilen einzusehen.
- **Aktualisieren** – Wenn sich die Quelldaten ändern, wird der gesamte Bericht durch eine einzige Aktualisierung neu berechnet.
Typische Anwendungsfälle sind Vertriebs-Dashboards, Kostenaufschlüsselungen und Bestandsanalysen – Fragen der Form „Wie lassen sich diese Zahlen nach Kategorie und Zeit aufschlüsseln?“ In Aspose.Cells for C++ wird eine PivotTable mit der Methode [PivotTableCollection.Add()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottablecollection/add/) eines Arbeitsblatts erstellt. Nach der Erstellung können Sie die PivotTable über die Klasse [PivotTable](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/) bearbeiten.

## **PivotTable erstellen**
Der folgende Beispielcode zeigt, wie Sie eine PivotTable erstellen und mit ihr arbeiten. Bitte prüfen Sie die mit diesem Code erzeugte [Excel-Ausgabedatei](23167010.xlsx) sowie den folgenden Screenshot, der die Ausgabedatei in Microsoft Excel zeigt.
![todo:image_alt_text](create-pivot-table_1.png)

## **Beispielcode**

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main()
{
    Aspose::Cells::Startup();

    // Erstellen Sie eine neue Arbeitsmappe und rufen Sie das erste Arbeitsblatt ab
    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Schreiben Sie die Quelldaten: Umsatz pro Sportart und Quartal
    cells.Get(u"A1").PutValue(u"Sport");
    cells.Get(u"B1").PutValue(u"Quarter");
    cells.Get(u"C1").PutValue(u"Sales");
    cells.Get(u"A2").PutValue(u"Golf");
    cells.Get(u"B2").PutValue(u"Qtr3");
    cells.Get(u"C2").PutValue(1500);
    cells.Get(u"A3").PutValue(u"Golf");
    cells.Get(u"B3").PutValue(u"Qtr4");
    cells.Get(u"C3").PutValue(2000);
    cells.Get(u"A4").PutValue(u"Tennis");
    cells.Get(u"B4").PutValue(u"Qtr3");
    cells.Get(u"C4").PutValue(600);
    cells.Get(u"A5").PutValue(u"Tennis");
    cells.Get(u"B5").PutValue(u"Qtr4");
    cells.Get(u"C5").PutValue(1500);
    cells.Get(u"A6").PutValue(u"Tennis");
    cells.Get(u"B6").PutValue(u"Qtr3");
    cells.Get(u"C6").PutValue(4070);
    cells.Get(u"A7").PutValue(u"Tennis");
    cells.Get(u"B7").PutValue(u"Qtr4");
    cells.Get(u"C7").PutValue(5000);
    cells.Get(u"A8").PutValue(u"Golf");
    cells.Get(u"B8").PutValue(u"Qtr3");
    cells.Get(u"C8").PutValue(6430);

    // Fügen Sie in der Zielzelle E3 eine Pivot-Tabelle hinzu, deren Datenquelle A1:C8 ist
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"A1:C8", 2, 4);

    // Weisen Sie die Pivot-Felder zu: Sportart zu Zeilen, Quartal zu Spalten, Umsatz zu Daten
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Quarter");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");

    // Speichern Sie die Arbeitsmappe
    workbook.Save(u"pivotTable_test_out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{< app/cells/assistant language="cpp" >}}