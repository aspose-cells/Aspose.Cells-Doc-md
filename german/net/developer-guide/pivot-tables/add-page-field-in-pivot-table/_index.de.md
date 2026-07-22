---
title: Seitenfelder in Pivot-Tabellen
linktitle: Seitenfelder
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET Seitenfelder in Pivot-Tabellen hinzufügen und konfigurieren, einschließlich Hinzufügen von Seitenfeldern, Einzel- und Mehrfachauswahl-Filterung.
keywords: Aspose.Cells, .NET, Pivot-Tabelle, Seitenfeld, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, Filter
type: docs
weight: 250
url: /de/net/add-page-field-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt den gesamten Lebenszyklus von Seitenfeldern in Pivot-Tabellen. Sie können ein Seitenfeld über eine übergeordnete Komfort-API oder über die niederstufige `PageFields`-Sammlung hinzufügen. Sie können den Seitenfilter im Einzelauswahlmodus steuern, ihn zurücksetzen, um alle Seitenelemente anzuzeigen, oder das Feld auf Mehrfachauswahl umschalten, damit Benutzer über die Kontrollkästchen-Oberfläche in Excel mehrere Seitenelemente gleichzeitig auswählen können.
{{% /alert %}}

## **Einführung**

Ein Seitenfeld ist ein Pivot-Feld, das steuert, *welche Teilmenge* der Quelldaten der Pivot-Körper anzeigt. Endbenutzer sehen es als Dropdown am oberen Rand einer gerenderten Pivot-Tabelle in Excel. Durch Auswahl eines der verfügbaren Seitenelemente wird der Pivot-Körper neu aufgebaut, sodass nur die Datensätze zusammengefasst werden, die zu diesem Seitenelement gehören. Ein Pivot-Feld wird zu einem Seitenfeld, wenn es als `PivotFieldType.Page` statt als `PivotFieldType.Row`, `PivotFieldType.Column` oder `PivotFieldType.Data` registriert wird.

Ein Seitenfeld kann zwei Verhaltensweisen aufweisen. Im standardmäßigen **Einzelauswahl**-Verhalten ist jeweils nur ein Seitenelement sichtbar, sodass der Pivot-Körper genau eine Teilmenge zusammenfasst. Im **Mehrfachauswahl**-Verhalten zeigt das Feld eine Kontrollkästchenliste an, und der Pivot-Körper fasst die Vereinigung aller markierten Seitenelemente zusammen. Dasselbe Quellfeld kann zwischen diesen Verhaltensweisen hin und her verschoben werden, indem eine einzelne Eigenschaft umgeschaltet wird.

Aspose.Cells for .NET stellt zwei gleichwertige Möglichkeiten bereit, ein Seitenfeld zu registrieren. Die übergeordnete API ist `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")`, die den Namen der Quellspalte übernimmt und das Feld in einem einzigen Aufruf hinzufügt. Die niederstufige API ist `PivotTable.PageFields.Add(PivotField)`, die verwendet wird, wenn Sie bereits eine `PivotField`-Referenz besitzen und dieselbe Feldinstanz zum Seitenbereich hinzufügen möchten. Beide APIs füllen am Ende dieselbe `PageFields`-Sammlung, und der Rest dieses Artikels zeigt, wie Sie zwischen ihnen wählen und wie Sie die einzelnen Filtermodi ansteuern.

## **Hinzufügen eines Seitenfelds**

Es gibt zwei Möglichkeiten, ein Pivot-Feld im Seitenbereich zu registrieren. Der übergeordnete Aufruf übernimmt den Namen der Quellspalte als Zeichenkette und ist der häufigste Weg. Der niederstufige Aufruf akzeptiert eine vorhandene `PivotField`-Instanz und ist praktisch, wenn dieselbe Feldinstanz in mehreren Pivot-Bereichen wiederverwendet werden muss. Beide Aufrufe platzieren das Feld in `PivotTable.PageFields`, woraufhin es als Dropdown für die Seite am oberen Rand der gerenderten Pivot-Tabelle erscheint.

### Hinzufügen eines Seitenfelds mit AddFieldToArea

Das folgende Beispiel erstellt einen kleinen Datensatz mit den Spalten Frucht / Jahr / Betrag, platziert eine Pivot-Tabelle in Zelle E3 mit `Fruit` im Zeilenbereich, `Amount` im Datenbereich und `Year` im Seitenbereich, aktualisiert die Pivot-Tabelle und speichert die Arbeitsmappe.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Ein neues Arbeitsbuch erstellen
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

// Die Kopfzeile einrichten
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 Zeilen Beispieldaten einfügen: Frucht, Jahr, Betrag
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

// Eine Pivot-Tabelle hinzufügen, die an Zelle E3 verankert ist
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Felder zu ihren Bereichen hinzufügen: Frucht als Zeile, Betrag als Daten, Jahr als Seitenfeld
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Pivot-Tabellendaten aktualisieren und berechnen
pivotTable.RefreshData();
pivotTable.CalculateData();

// Das Arbeitsbuch speichern
workbook.Save("pageFieldSample.xlsx");
```

### Hinzufügen eines Seitenfelds mit PageFields.Add

Wenn Sie bereits mit einer `PivotField`-Instanz arbeiten, können Sie diese direkt an `PivotTable.PageFields.Add` übergeben. Die Pivot-Tabelle und das Seitenfeld werden genau wie im vorherigen Szenario konstruiert; nur die endgültige Registrierung im Seitenbereich wird durch den niederstufigen API-Aufruf ersetzt.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
//   Szenario 1a (Frucht/Jahr/Betrag-Daten, Pivot bei E3, Frucht→Zeile,
//   Betrag→Daten) erstellt. Unten holen wir das Jahr-PivotField aus der
//   BaseFields-Sammlung und übergeben es an PageFields.Add — die
//   Low-Level-Alternative zu AddFieldToArea. Das Ergebnis ist
//   funktional identisch mit Szenario 1a.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];

// Kopfzeilen
sheet.Cells["A1"].PutValue("Fruit");
sheet.Cells["B1"].PutValue("Year");
sheet.Cells["C1"].PutValue("Amount");

// Beispieldaten (9 Zeilen)
sheet.Cells["A2"].PutValue("apple");    sheet.Cells["B2"].PutValue("2020"); sheet.Cells["C2"].PutValue(100);
sheet.Cells["A3"].PutValue("apple");    sheet.Cells["B3"].PutValue("2021"); sheet.Cells["C3"].PutValue(150);
sheet.Cells["A4"].PutValue("apple");    sheet.Cells["B4"].PutValue("2022"); sheet.Cells["C4"].PutValue(200);
sheet.Cells["A5"].PutValue("grape");    sheet.Cells["B5"].PutValue("2020"); sheet.Cells["C5"].PutValue(300);
sheet.Cells["A6"].PutValue("grape");    sheet.Cells["B6"].PutValue("2021"); sheet.Cells["C6"].PutValue(400);
sheet.Cells["A7"].PutValue("grape");    sheet.Cells["B7"].PutValue("2022"); sheet.Cells["C7"].PutValue(500);
sheet.Cells["A8"].PutValue("blueberry"); sheet.Cells["B8"].PutValue("2020"); sheet.Cells["C8"].PutValue(250);
sheet.Cells["A9"].PutValue("blueberry"); sheet.Cells["B9"].PutValue("2021"); sheet.Cells["C9"].PutValue(350);
sheet.Cells["A10"].PutValue("blueberry");sheet.Cells["B10"].PutValue("2022"); sheet.Cells["C10"].PutValue(450);

// Pivot-Tabelle bei E3 hinzufügen, die A1:C10 abdeckt
int pivotIndex = sheet.PivotTables.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Frucht -> Zeile, Betrag -> Daten (Jahr wird unten zur Seite hinzugefügt)
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Low-Level-Ansatz: das vorhandene Jahr-PivotField aus BaseFields holen
// und es über PageFields.Add(PivotField) im Seitenbereich registrieren.
PivotField yearField = pivotTable.BaseFields["Year"];
pivotTable.PageFields.Add(yearField);

// Aktualisieren, damit das neue Seitenfeld in der gespeicherten Arbeitsmappe widergespiegelt wird
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Einzelauswahl-Filterung (Anzeigen eines Seitenelements)**

Im standardmäßigen Einzelauswahl-Verhalten wird das Seitenfeld als einzelnes Dropdown gerendert, und die Ganzzahl `PivotField.CurrentPageItem` wählt aus, welches Seitenelement den Pivot-Körper antreibt. Durch Zuweisen eines bestimmten Index wird dieses eine Element ausgewählt; durch Zuweisen des speziellen Sentinelwerts `0x7FFD` (Dezimalwert 32765) wird der Filter zurückgesetzt, sodass alle Seitenelemente gleichzeitig zusammengefasst werden. Die Einzelauswahl ist der Standard; Sie müssen sie nicht explizit aktivieren.

### Anzeigen aller Elemente

Das Setzen von `CurrentPageItem` auf den magischen Wert `0x7FFD` entspricht dem Aufheben des Seitenfilters: Der Pivot-Körper fasst alle Seitenelemente zusammen, als ob kein Filter angewendet worden wäre.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

class Program
{
    static void Main()
    {
        // Erstellen Sie eine neue Arbeitsmappe
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];

        // Fruit/Year/Amount-Daten einfügen
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

        // Pivot-Tabelle bei E3 erstellen
        var pivotTables = sheet.PivotTables;
        int index = pivotTables.Add("=A1:C7", "E3", "PivotTable1");
        PivotTable pivotTable = pivotTables[index];

        // Pivot-Felder konfigurieren: Fruit→Zeile, Amount→Daten, Year→Seite
        pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
        pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
        pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

        pivotTable.RefreshData();
        pivotTable.CalculateData();

        // Den Seitenfilter löschen, damit jedes Element im Seitenfeld sichtbar ist.
        // 0x7FFD (Dezimal 32765) ist der spezielle Sentinel-Wert, der "alle Elemente" bedeutet —
        // entspricht der Auswahl von "(Alle)" im Seitenfeld-Dropdown von Excel.
        pivotTable.PageFields[0].CurrentPageItem = 0x7FFD;

        workbook.Save("output.xlsx");
    }
}
```

### Anzeigen eines bestimmten Elements

Das Setzen von `CurrentPageItem` auf einen echten Index wählt genau dieses eine Seitenelement aus. Der Index ist die Position des Elements in der sortierten Elementliste des Seitenfelds, sodass beispielsweise `1` das zweite Element nach dem Sortieren auswählt.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Arbeitsmappe erstellen
var workbook = new Workbook();
var sheet = workbook.Worksheets[0];
var cells = sheet.Cells;

// Beispieldaten hinzufügen (Obst/Jahr/Betrag)
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

// Pivot-Tabelle bei E3 hinzufügen
var pivotTables = sheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:C5", "E3", "PivotTable1");
var pivotTable = pivotTables[pivotIndex];

// Felder hinzufügen: Obst→Zeile, Betrag→Daten, Jahr→Seite
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// Seitenfeldspezifische Operationen
pivotTable.PageFields[0].CurrentPageItem = 1; // 1 = zweites Element in sortierter Reihenfolge (z. B. "2021")

// Pivot-Tabelle aktualisieren und berechnen
pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

## **Mehrfachauswahl-Filterung**

Die Mehrfachauswahl-Filterung verwandelt das Seiten-Dropdown in eine Kontrollkästchenliste und ermöglicht es dem Endbenutzer, mehrere Seitenelemente gleichzeitig auszuwählen. Aspose.Cells stellt zwei Eigenschaften bereit, die zusammenarbeiten. `PivotField.IsMultipleItemSelectionAllowed` muss auf `true` gesetzt werden, bevor die Mehrfachauswahl-Benutzeroberfläche überhaupt wirksam wird. Nach der Aktivierung steuert `PivotItem.IsHidden`, welche Elemente in der Kontrollkästchenliste angezeigt werden, sodass Sie entweder alle Elemente anzeigen oder nur bestimmte Elemente auf eine Whitelist setzen können.

Der folgende Code aktiviert die Mehrfachauswahl für dasselbe Seitenfeld Year, das in Szenario 1a erstellt wurde, und zeigt anschließend zwei Muster: Teil A deckt alle Seitenelemente auf, indem `IsHidden` für jeden Eintrag auf `false` belassen wird, während Teil B nur die von Ihnen gewählten Quellwerte auf eine Whitelist setzt und alle anderen Elemente über einen `switch (pivotItems[i].GetStringValue())`-Block ausblendet.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// — Die Pivot-Tabelle und das Seitenfeld werden genau wie in
//   Szenario 1a erstellt (Fruit/Year/Amount-Daten, Pivot bei E3, Fruit→Zeile,
//   Amount→Daten, Year→Seite über AddFieldToArea).
//   Unten wenden wir Mehrfachauswahl-Filterung auf das Seitenfeld an.

Workbook workbook = new Workbook();
Worksheet sheet = workbook.Worksheets[0];
Cells cells = sheet.Cells;

// Beispieldaten: Fruit | Year | Amount
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
int pivotIndex = pivots.Add("E3", "A1:C10", "PivotTable1");
PivotTable pivotTable = pivots[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");
pivotTable.AddFieldToArea(PivotFieldType.Page, "Year");

// — Mehrfachauswahl auf dem Seitenfeld aktivieren
pivotTable.PageFields[0].IsMultipleItemSelectionAllowed = true;

// Teil A — ALLE Elemente auswählen (jedes Element sichtbar machen)
PivotItemCollection pivotItems = pivotTable.PageFields[0].PivotItems;
for (int i = 0; i < pivotItems.Count; i++)
{
    pivotItems[i].IsHidden = false;
}

// Teil B — nur bestimmte Elemente nach Quellwert auswählen
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

pivotTable.RefreshData();
pivotTable.CalculateData();

workbook.Save("output.xlsx");
```

> **Hinweis:** Bei Verwendung der Mehrfachauswahl-Filterung über `PivotItem.IsHidden` muss **mindestens ein `PivotItem` sichtbar bleiben** (`IsHidden == false`). Wenn jedes Element ausgeblendet ist, stürzt Excel entweder beim Öffnen der Datei ab oder zeigt eine leere Pivot-Tabelle an. Stellen Sie stets sicher, dass Ihre Mehrfachauswahl-Whitelist mindestens ein Element aus Ihren Quelldaten enthält.

## **Welche API und welcher Modus sollten verwendet werden?**

Die folgende Tabelle fasst zusammen, wann welche API und welcher Modus verwendet werden sollte, damit Sie die richtige Kombination wählen können, ohne jedes Szenario im Detail lesen zu müssen.

| Szenario / Anwendungsfall | Empfohlene API | Verwendete Eigenschaft | Hinweise |
|---|---|---|---|
| Seitenfeld nach Quellspaltenname hinzufügen (am häufigsten) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | n. a. | Übergeordnet, einzeilig. Verwenden Sie dies, sofern Sie keine `PivotField`-Referenz benötigen. |
| Seitenfeld hinzufügen, wenn Sie bereits über ein `PivotField`-Objekt verfügen | `PivotTable.PageFields.Add(PivotField)` | n. a. | Verwenden Sie dies, wenn das Feldobjekt bereits anderweitig bezogen wurde oder wiederverwendet werden muss. |
| Auf ein einzelnes Seitenelement filtern (Standardmodus) | `PivotField.CurrentPageItem` | auf einen bestimmten Index setzen | Beispielsweise zeigt `1` das zweite Element in der sortierten Liste an. |
| Alle Elemente anzeigen / Seitenfilter zurücksetzen | `PivotField.CurrentPageItem` | auf `0x7FFD` setzen | Der magische Wert `0x7FFD` (Dezimalwert 32765) ist der Sentinelwert für "alle Elemente". |
| Mehrfachauswahl-Benutzeroberfläche in Excel aktivieren | `PivotField.IsMultipleItemSelectionAllowed` | auf `true` setzen | Erforderlich, bevor `IsHidden`-Aufrufe wirksam werden. |
| Einzelne Elemente in einer Mehrfachauswahl-Liste ausblenden / anzeigen | `PivotItem.IsHidden` | pro Element setzen | Mindestens ein Element muss sichtbar bleiben (`IsHidden == false`). |

{{% alert color="primary" %}}
Beachten Sie stets die Sichtbarkeitsbeschränkung bei der Konfiguration der Mehrfachauswahl-Filterung. Wenn jedes `PivotItem` in einem Mehrfachauswahl-Seitenfeld ausgeblendet ist, stürzt Excel beim Öffnen ab oder zeigt eine leere Pivot-Tabelle an. Erstellen Sie Ihre Whitelist auf Grundlage Ihrer Quelldaten, sodass mindestens ein Element sichtbar bleibt, und Ihre gespeicherten Arbeitsmappen werden auf jedem Rechner zuverlässig geöffnet.
{{% /alert %}}



{{< app/cells/assistant language="csharp" >}}