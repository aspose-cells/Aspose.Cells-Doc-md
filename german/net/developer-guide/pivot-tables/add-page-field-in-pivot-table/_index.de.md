---
title: Filterfelder zu einer Pivot-Tabelle in Aspose.Cells for .NET hinzufügen
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET Filterfelder in Pivot-Tabellen hinzufügen und konfigurieren, einschließlich Hinzufügen von Filterfeldern, Einzelauswahl-Filterung und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, .NET, Pivot-Tabelle, Filterfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/net/add-page-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
linktitle: Filterfelder hinzufügen
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Filterfeldern in Pivot-Tabellen. Sie können ein Filterfeld über eine komfortable High-Level-API oder über die Low-Level-Sammlung `PageFields` hinzufügen. Sie können den Filter im Einzelauswahlmodus steuern, ihn zurücksetzen, um alle Filterelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, damit Benutzer über die Checkbox-Benutzeroberfläche in Excel mehrere Filterelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**
Ein Filterfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Bereich anzeigt. Endbenutzer sehen es als Dropdown-Liste am oberen Rand einer in Excel gerenderten Pivot-Tabelle. Durch Auswahl eines der verfügbaren Filterelemente wird der Pivot-Bereich neu aufgebaut, sodass nur die Datensätze zusammengefasst werden, die zu diesem Filterelement gehören. Ein Pivot-Feld wird zu einem Filterfeld, wenn es als `PivotFieldType.Page` und nicht als `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data` registriert wird.

## **Hinzufügen eines Filterfelds**

### Hinzufügen eines Filterfelds mit AddFieldToArea
Das folgende Beispiel erstellt einen kleinen Datensatz mit Fruit / Year / Amount, platziert eine Pivot-Tabelle in Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Filterbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Create a new workbook
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";
// Set up the header row
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");
// Populate 9 rows of sample data: Fruit, Year, Amount
object[,] data = new object[,]
{
    { "apple", 2020, 100 },
    { "banana", 2021, 200 },
    { "apple", 2021, 150 },
    { "grape", 2020, 120 },
    { "orange", 2022, 180 },
    { "banana", 2020, 90 },
    { "grape", 2021, 130 },
    { "apple", 2022, 170 },
    { "orange", 2021, 110 }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    worksheet.Cells[i + 1, 0].PutValue(data[i, 0]);
    worksheet.Cells[i + 1, 1].PutValue(data[i, 1]);
    worksheet.Cells[i + 1, 2].PutValue(data[i, 2]);
}
// Add a pivot table anchored at cell E3
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C10", 2, 4);
// Add fields to their areas: Fruit as Row, Amount as Data, Year as Page field
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Refresh and calculate the pivot table data
pivotTable.CalculateData();
// Save the workbook
workbook.Save("pageFieldSample.xlsx");
```

### Hinzufügen eines Filterfelds mit PageFields.Add
Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.PageFields.Add` übergeben. Die Pivot-Tabelle und das Filterfeld werden genau wie im vorherigen Szenario erstellt; nur die endgültige Registrierung im Filterbereich wird durch den Low-Level-API-Aufruf ersetzt.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data). Below we obtain the Year PivotField from the
//   BaseFields collection and pass it to PageFields.Add — the
//   low-level alternative to AddFieldToArea. The result is
//   functionally identical to Scenario 1a.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
// Headers
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");
// Sample data (9 rows)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);
// Add pivot table at E3 covering A1:C10
PivotTable pivotTable = sheet.PivotTables.Add("A1:C10", 2, 4);
// Fruit -> Row, Amount -> Data (Year will go to Page below)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
// Low-level approach: grab the existing Year PivotField from BaseFields
// and register it in the Page area via PageFields.Add(PivotField).
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);
// Refresh so the new page field is reflected in the saved workbook
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Einzelauswahl-Filterung (Anzeigen eines Filterelements)**
Im standardmäßigen Einzelauswahlverhalten wird das Filterfeld als einzelnes Dropdown gerendert, und der `PivotField.CurrentPageItem`-Integer wählt aus, welches Filterelement den Pivot-Bereich steuert. Das Zuweisen eines bestimmten Index wählt dieses eine Element aus; das Zuweisen des speziellen Sentinel-Werts `0x7FFD` (Dezimal 32765) löscht den Filter, sodass alle Filterelemente gleichzeitig zusammengefasst werden. Die Einzelauswahl ist die Standardeinstellung; Sie müssen sie nicht explizit aktivieren.

### Anzeigen aller Elemente
Das Setzen von `CurrentPageItem` auf den magischen Wert `0x7FFD` entspricht dem Löschen des Filters: Der Pivot-Bereich fasst alle Filterelemente zusammen, als ob kein Filter angewendet würde.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
class Program
{
    static void Main()
    {
        // Create a new workbook
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        // Populate Fruit/Year/Amount data
        sheet.Cells["A1"].PutValue("Fruit");
        sheet.Cells["B1"].PutValue("Year");
        sheet.Cells["C1"].PutValue("Amount");
        object[,] data = new object[,]
        {
            {"Apple", 2022, 100},
            {"Apple", 2023, 150},
            {"Banana", 2022, 80},
            {"Banana", 2023, 120},
            {"Cherry", 2022, 200},
            {"Cherry", 2023, 250}
        };
        for (int r = 0; r < data.GetLength(0); r++)
        {
            for (int c = 0; c < data.GetLength(1); c++)
            {
                sheet.Cells[r + 1, c].PutValue(data[r, c]);
            }
        }
        // Create pivot table at E3
        var pivotTables = sheet.PivotTables;
        PivotTable pivotTable = pivotTables.Add("=A1:C7", 2, 4);
        // Configure pivot fields: Fruit→Row, Amount→Data, Year→Page
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
        pivotTable.CalculateData();
        // Clear the page filter so every item in the page field is visible.
        // 0x7FFD (decimal 32765) is the special sentinel value that means "all items" —
        // equivalent to selecting "(All)" in Excel's page-field dropdown.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;
        workbook.Save("output.xlsx");
    }
}
```

### Anzeigen eines bestimmten Elements
Das Setzen von `CurrentPageItem` auf einen echten Index wählt genau dieses eine Filterelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Filterfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// Create workbook
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;
// Add sample data (Fruit/Year/Amount)
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
cells["A2"].PutValue("Apple");
cells["B2"].PutValue("2020");
cells["C2"].PutValue("100");
cells["A3"].PutValue("Apple");
cells["B3"].PutValue("2021");
cells["C3"].PutValue("150");
cells["A4"].PutValue("Banana");
cells["B4"].PutValue("2020");
cells["C4"].PutValue("200");
cells["A5"].PutValue("Banana");
cells["B5"].PutValue("2021");
cells["C5"].PutValue("250");
// Add pivot table at E3
var pivotTables = sheet.PivotTables;
var pivotTable = pivotTables.Add("A1:C5", 2, 4);
// Add fields: Fruit→Row, Amount→Data, Year→Page
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// Page-field-specific operations
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = second item in sorted order (e.g. "2021")
// Refresh and calculate pivot table
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

## **Mehrfachauswahl-Filterung**
Die Mehrfachauswahl-Filterung verwandelt das Filter-Dropdown in eine Kontrollkästchenliste und ermöglicht es dem Endbenutzer, mehrere Filterelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.IsMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.IsHidden`, welche Elemente in der Kontrollkästchenliste angezeigt werden, sodass Sie entweder alle Elemente anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
// — The pivot table and page field are constructed exactly as in
//   Scenario 1a (Fruit/Year/Amount data, pivot at E3, Fruit→Row,
//   Amount→Data, Year→Page via AddFieldToArea).
//   Below we apply multi-select filtering on the page field.
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
// Sample data: Fruit | Year | Amount
cells[0, 0].PutValue("Fruit");
cells[0, 1].PutValue("Year");
cells[0, 2].PutValue("Amount");
string[,] data = new string[,]
{
    { "apple",  "2019", "100" },
    { "apple",  "2020", "150" },
    { "apple",  "2021", "200" },
    { "banana", "2019", "110" },
    { "banana", "2020", "160" },
    { "banana", "2021", "210" },
    { "grape",  "2019", "120" },
    { "grape",  "2020", "170" },
    { "grape",  "2021", "220" }
};
for (int i = 0; i < data.GetLength(0); i++)
{
    cells[i + 1, 0].PutValue(data[i, 0]);
    cells[i + 1, 1].PutValue(Convert.ToInt32(data[i, 1]));
    cells[i + 1, 2].PutValue(Convert.ToInt32(data[i, 2]));
}
Worksheet pivotSheet = workbook.Worksheets.Add("Pivot");
PivotTableCollection pivots = pivotSheet.PivotTables;
PivotTable pivotTable = pivots.Add("A1:C10", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");
// — Enable multi-select on the page field
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;
// Part A — select ALL items (make every item visible)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}
// Part B — select only specific items by source value
for (int i = 0; i < pivotItems.Count; i++)
{
    switch (pivotItems[i].GetStringValue())
    {
        case "2020":
        case "grape":
        case "blueberry":
            pivotItems[i].IsHidden = false;
            break;
        default:
            pivotItems[i].IsHidden = true;
            break;
    }
}
pivotTable.CalculateData();
workbook.Save("output.xlsx");
```

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.IsHidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`IsHidden == false`). Wenn jedes Element ausgeblendet ist, stürzt Excel entweder beim Öffnen der Datei ab oder zeigt eine leere Pivot-Tabelle an. Stellen Sie immer sicher, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollte ich verwenden?**
Die folgende Tabelle fasst zusammen, wann Sie welche API und welchen Modus verwenden sollten, damit Sie die richtige Kombination auswählen können, ohne jedes Szenario im Detail lesen zu müssen.
| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Filterfeld über Quellspaltenname hinzufügen (am häufigsten) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n/v | High-Level, einzeilig. Verwenden Sie dies, es sei denn, Sie benötigen eine `PivotField`-Referenz. |
| Filterfeld hinzufügen, wenn Sie bereits ein `PivotField`-Objekt haben | `PivotTable.PageFields.Add(PivotField)` | n/v | Verwenden Sie dies, wenn das Feldobjekt anderweitig bezogen wurde oder wiederverwendet werden muss. |
| Auf ein einzelnes Filterelement filtern (Standardmodus) | `PivotField.CurrentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste. |
| Alle Elemente anzeigen / Filter löschen | `PivotField.CurrentPageItem` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (Dezimal 32765) ist der Sentinel-Wert für "alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.IsMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor `IsHidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahlliste ausblenden / anzeigen | `PivotItem.IsHidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`IsHidden == false`). |

{{% alert color="primary" %}}
Denken Sie beim Konfigurieren der Mehrfachauswahl-Filterung immer an die Sichtbarkeitseinschränkung. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Filterfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder zeigt eine leere Pivot-Tabelle an. Erstellen Sie Ihre Whitelist auf Basis Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Rechner zuverlässig geöffnet.
{{% /alert %}}

## **Verwandte Artikel**
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells for .NET](/cells/de/net/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}