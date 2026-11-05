---
title: Bedingte Formatierung zu einer PivotTable hinzufügen
linktitle: Bedingte Formatierung zu einer PivotTable hinzufügen
description: Bedingte Formatierung zu einer PivotTable in Aspose.Cells for .NET hinzufügen – eine Regel mit ApplyTo und einem PivotConditionFormatScopeType‑Bereich an den Datenbereich anheften oder das Ziel mit AddCellArea und PivotAreas definieren und anschließend Regeln und Stile über FormatConditions.AddCondition anhängen.
keywords: Aspose.Cells, PivotTable, bedingte Formatierung, PivotConditionalFormat, ConditionalFormats, ApplyTo, PivotConditionFormatScopeType, Data, Field, Selection, AddCellArea, PivotAreas, AddPivotArea, FormatConditions, AddCondition, FormatConditionType, C#
type: docs
weight: 30
url: /de/net/add-conditional-formatting-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Die auf der übergeordneten Seite und auf der benachbarten Seite beschriebenen Stile sind statisch – ein `PivotArea`‑ oder `CellArea`‑Bereich wird einmal gemalt und behält sein Aussehen, egal welche Werte vorliegen. Bedingte Formatierung ist das regelgesteuerte Gegenstück – jeden Betrag über 200 hervorheben, die mittleren fünfzig Prozent schattieren oder die am schlechtesten bewerteten Elemente markieren – und die Hervorhebung folgt den Werten, sobald die PivotTable neu berechnet oder aktualisiert wird.  
In Aspose.Cells leben die bedingten Formatierungen für PivotTable in der `PivotTable.ConditionalFormats`‑Sammlung. Jeder Eintrag ist ein `PivotConditionalFormat`, das zwei Fragen unabhängig beantwortet:
- **Wo soll die Regel gelten?** Der Zielbereich wird entweder über `ApplyTo(int row, int column, PivotConditionFormatScopeType scope)` definiert, was dem Bereichsauswahlwerkzeug der Excel‑Benutzeroberfläche entspricht, oder über `AddCellArea(CellArea)` und die `PivotAreas`‑Sammlung, die den Bereich explizit benennen.
- **Was prüft die Regel?** Eine oder mehrere Bedingungen werden zu `FormatConditions` mit `FormatConditionCollection.AddCondition(FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` hinzugefügt, und jede Bedingung trägt ihr eigenes `Style`.

{{% alert color="primary" %}}
Rufen Sie nicht `FormatConditionCollection.Add(CellArea cellArea, FormatConditionType type, OperatorType operatorType, string formula1, string formula2)` oder `FormatConditionCollection.AddArea(CellArea)` auf dem `FormatConditions`‑Objekt eines Pivot‑bedingten Formats auf. Diese beiden Überladungen stammen aus der normalen Arbeitsblatt‑Bedingten‑Formatierungs‑API und funktionieren für PivotTable nicht – der Zellbereich wird niemals in einen Pivot‑Bereich konvertiert, sodass die Anforderung stillschweigend ignoriert wird. Definieren Sie den Bereich immer am `PivotConditionalFormat` selbst (`ApplyTo`, `AddCellArea` oder `PivotAreas`) und fügen Sie die Regel mit einer der `AddCondition`‑Überladungen hinzu.
{{% /alert %}}

## **Regel mit einem Bereich anwenden (wie in der Excel‑Benutzeroberfläche)**
Der erste Ansatz positioniert die Regel so, wie es die Excel‑Benutzeroberfläche tut. Eine Zelle der PivotTable wird durch ihre nullbasierten Arbeitsblattkoordinaten benannt, und ein `PivotConditionFormatScopeType`‑Bereich gibt Aspose.Cells an, wie weit die Regel von dieser Zelle aus reichen soll:
- `PivotConditionFormatScopeType.Data` – alle Wertzellen, die die PivotTable erzeugt, einschließlich Gesamtsummen.
- `PivotConditionFormatScopeType.Field` – die Wertzellen, die zu dem Feld gehören, das die Zelle identifiziert, ohne Gesamtsummen. Die Zelle muss eine Feldzelle sein, wie ein Zeilen‑Feld‑Label; wird eine Wertzelle übergeben, wird eine Ausnahme ausgelöst.
- `PivotConditionFormatScopeType.Selection` – nur die Wertzellen an der Kreuzung, die die Zelle auswählt, typischerweise eine einzelne Wertzelle.
Das untenstehende Beispiel erstellt eine PivotTable für Obstverkäufe, deren obere linke Ecke bei E3 liegt, verankert ein bedingtes Format in Zelle F4 (Zeile 3, Spalte 5) mit dem `Data`‑Bereich und hebt jeden Betrag über 200 fett weiß auf rot hervor. Bei den Werten Apple 220, Banana 330, Cherry 200 und der Gesamtsumme 750 malt die Regel F4, F5 und F7 – der aufgelöste Bereich ist die gesamte Datenspalte F4:F7, und nur die Zellen, deren Wert die Regel erfüllt, leuchten.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
// Pivot-Tabelle mit ihrer oberen linken Ecke bei E3
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Verankere das bedingte Format bei F4 (Zeile 3, Spalte 5) mit dem Datenbereich
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.ApplyTo(3, 5, PivotConditionFormatScopeType.Data);
// Regel - Markiere Beträge größer als 200
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.GreaterThan, "200", null);
Style style = workbook.CreateStyle();
style.Font.IsBold = true;
style.Font.Color = Color.White;
style.ForegroundColor = Color.Red;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatData.xlsx");
```

Das Anheften derselben Regel am Zeilen‑Feld‑Label E4 (Zeile 3, Spalte 4) mit dem `Field`‑Bereich löst F4:F6 aus – dieselbe Datenspalte ohne die Zeile für die Gesamtsumme –, weil der Bereich nun das Feld `Fruit` beschreibt und nicht den gesamten Werte‑Bereich. Der `Selection`‑Bereich, verankert bei F4, löst nur F4 aus.

## **Region manuell definieren**
Der zweite Ansatz verzichtet auf die Bereichs‑Auswahl und benennt den Bereich explizit am `PivotConditionalFormat`.

### **Ein Arbeitsblattrechteck mit AddCellArea**
`AddCellArea(CellArea)` speichert das übergebene Rechteck als Ziel der Regel. Die Koordinaten sind nullbasierte Arbeitsblattkoordinaten, und der Bereich ist exakt das übergebene Rechteck – keine Erweiterung zur Datenspalte und keine Logik für Gesamtsummen. Verwenden Sie dies, wenn die interessierenden Zellen ein bekannter fester Rechteck des aktuellen Pivot‑Layouts bilden.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Ziel das Rechteck F4:F6 (die Wertzellen ohne die Gesamtsumme)
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
format.AddCellArea(new CellArea { StartRow = 3, StartColumn = 5, EndRow = 5, EndColumn = 5 });
// Regel - kursiv auf hellgelb für Beträge zwischen 150 und 300
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.Between, "150", "300");
Style style = workbook.CreateStyle();
style.Font.IsItalic = true;
style.ForegroundColor = Color.LightYellow;
style.Pattern = BackgroundType.Solid;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatCellArea.xlsx");
```

### **Ein semantischer Pivot‑Bereich mit PivotAreas**
`PivotAreas` ist dasselbe semantische Bereichs‑Modell, das die benachbarte Seite für statische Stile verwendet. Erzeugen Sie ein `PivotArea`, wählen Sie ein Feld oder einen Bereich mit `Select` oder `SelectField` und fügen Sie es mit `PivotAreas.AddPivotArea(PivotArea)` hinzu. Ein semantischer Bereich bleibt seinem Feld zugeordnet, sodass das bedingte Format dem Feld folgt, wenn die PivotTable aktualisiert und das Layout verschoben wird. Die Überladung `PivotAreas.Add(PivotArea)` kompiliert zwar noch, ist jedoch als veraltet markiert – verwenden Sie lieber `AddPivotArea`.

```csharp
using System;
using System.Drawing;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;
string[] fruits = { "Apple", "Banana", "Apple", "Banana", "Cherry", "Cherry" };
int[] years = { 2024, 2024, 2025, 2025, 2024, 2025 };
int[] amounts = { 100, 150, 120, 180, 90, 110 };
cells["A1"].PutValue("Fruit");
cells["B1"].PutValue("Year");
cells["C1"].PutValue("Amount");
for (int i = 0; i < fruits.Length; i++)
{
    cells[i + 1, 0].PutValue(fruits[i]);
    cells[i + 1, 1].PutValue(years[i]);
    cells[i + 1, 2].PutValue(amounts[i]);
}
PivotTable pivotTable = sheet.PivotTables.Add("=A1:C7", 2, 4);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.CalculateData();
// Die Regel dem Datenfeld Amount als semantischen Bereich zuweisen
int index = pivotTable.ConditionalFormats.Add();
PivotConditionalFormat format = pivotTable.ConditionalFormats[index];
PivotArea area = new PivotArea(pivotTable);
area.SelectField(PivotFieldType.Data, "Amount");
format.PivotAreas.AddPivotArea(area);
// Regel – grauer Text für Beträge unter 150
int conditionIndex = format.FormatConditions.AddCondition(
    FormatConditionType.CellValue, OperatorType.LessThan, "150", null);
Style style = workbook.CreateStyle();
style.Font.Color = Color.Gray;
format.FormatConditions[conditionIndex].Style = style;
workbook.Save("PivotConditionalFormatPivotArea.xlsx");
```

## **Wo die Regeln gespeichert werden und wie sie einem Neuladen standhalten**
Jeder Aufruf von `ConditionalFormats.Add()` fügt ein `PivotConditionalFormat` zur PivotTable hinzu. Die Bedingungen, deren Formeln und Stile werden mit der Arbeitsmappe gespeichert – beim erneuten Öffnen der Datei im nachfolgenden Beispiel werden dieselbe Regel mit ihrem Typ, Operator und Formel unverändert angezeigt, und `GetCellAreas()` meldet dieselben Bereiche. Einträge, die nie eine Bedingung erhalten haben, werden beim Speichern der Arbeitsmappe verworfen, analog zu Excel, das ein bedingtes Format ohne Regel entfernt.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("PivotConditionalFormatData.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
Console.WriteLine("Conditional formats: " + pivotTable.ConditionalFormats.Count);
for (int i = 0; i < pivotTable.ConditionalFormats.Count; i++)
{
    PivotConditionalFormat format = pivotTable.ConditionalFormats[i];
    for (int j = 0; j < format.FormatConditions.Count; j++)
    {
        FormatCondition condition = format.FormatConditions[j];
        Console.WriteLine($"Format {i}: {condition.Type} {condition.Operator} formula1={condition.Formula1}");
    }
    foreach (CellArea area in format.GetCellAreas())
        Console.WriteLine($"    rows {area.StartRow + 1}-{area.EndRow + 1}, columns {area.StartColumn + 1}-{area.EndColumn + 1}");
}
// Dies gibt aus:
// Bedingte Formate: 1
// Format 0: Zellwert GrößerAls Formel1==200
//     Zeilen 4-7, Spalten 6-6        (F4:F7, der aufgelöste Datenbereich)
```

## **Verwandte Artikel**
- [Stil auf PivotTable anwenden](/cells/de/net/apply-style-to-pivot-table/)
- [Teil einer PivotTable formatieren](/cells/de/net/format-part-of-pivot-table/)
- [Top‑10 anzeigen oder filtern in PivotTable](/cells/de/net/top-10-show-or-filter-in-pivot-table/)
- [PivotTable nach Beschriftung oder Wert filtern](/cells/de/net/filter-by-label-or-value-of-pivot-table/)

{{< app/cells/assistant language="csharp" >}}