---
title: Anwenden von Stilen auf Pivot-Tabellen
linktitle: Anwenden von Stilen
description: Erfahren Sie, wie Sie in Aspose.Cells for .NET integrierte und benutzerdefinierte Stile auf Pivot-Tabellen anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Excel 2007+ Stilen, benutzerdefinierten Pivot-Tabellenstilen und der FormatAll-Verknüpfung.
keywords: Aspose.Cells .NET Pivot-Tabellenstil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/net/apply-style-to-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Anwendung sowohl von Legacy-Pivot-Autoformaten (für `.xls`-Dateien vorgesehen) als auch von modernen benannten oder benutzerdefinierten Pivot-Tabellenstilen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, und nicht vom Format, aus dem sie geladen wurde.

{{% /alert %}}

## **Einführung**

Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden, und in diesem Fall gilt die moderne Stil-API statt der Legacy-API.

Für die Legacy-Ausgabe im `.xls`-Format verwenden Sie die Eigenschaft `PivotTable.AutoFormatType` zusammen mit der Enumeration `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Diese API entspricht der Autoformat-Auswahl, die das klassische Excel für Pivot-Tabellen angeboten hat.

Für die moderne Ausgabe im `.xlsx`-, `.xlsm`- und `.xlsb`-Format stehen zwei Varianten der Stil-API zur Verfügung:

- `PivotTable.PivotTableStyleType` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `PivotTable.PivotTableStyleName` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` definieren. Benutzerdefinierte Stile sind erforderlich, wenn Sie Farben, Rahmen oder Schriftarten ändern möchten, die über die Voreinstellungen hinausgehen.

Darüber hinaus ist `PivotTable.FormatAll(Style)` eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und alle über die beiden oben genannten Stilnamen-APIs vorgenommenen Einstellungen überschreibt. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrunde liegenden Design erforderlich ist.

## **Anwenden eines Legacy-XLS-Voreinstellungs-Autoformats**

`PivotTable.AutoFormatType` akzeptiert einen Wert aus der Enumeration `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `Report1` bis `Report10`, `Classic` und `Table1` bis `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` wird nur berücksichtigt, wenn die Arbeitsmappe als `.xls` gespeichert wird. Wenn dieselbe Arbeitsmappe als `.xlsx`, `.xlsm` oder `.xlsb` gespeichert wird, ignoriert Excel diese Eigenschaft und greift auf die Einstellungen `PivotTableStyleType` und `PivotTableStyleName` zurück.

{{% /alert %}}

Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Beispieldaten Fruit/Year/Amount, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.Report5` an und speichert das Ergebnis als `.xls`.

{{% alert color="primary" %}}

**Warum keine Spaltenfelder?** Die Autoformate der Report-Serie (`Report1` bis `Report10`, `Table1` bis `Table10`) wurden im klassischen Excel für **eindimensionale Pivot-Tabellen** mit nur Zeilenfeldern und Werten entworfen — sie haben keine integrierte Formatierung für Spaltenfeld-Überschriften. Wenn Ihre Pivot-Tabelle Spaltenfelder benötigt, verwenden Sie stattdessen die modernen `PivotTableStyleType`-Voreinstellungen aus Szenario 2 unten, die für das zweidimensionale Layout moderner Excel-Versionen entwickelt wurden.

{{% /alert %}}

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Szenario 1: Ein Legacy-XLS-Preset-Autoformat anwenden
// Verwendete API: PivotTable.AutoFormatType
// Zieldateiformat: .xls (Legacy)
// Für vollständige Beispiele und Datendateien besuchen Sie bitte https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Eine neue Arbeitsmappe erstellen
Workbook workbook = new Workbook();

// Das erste Arbeitsblatt abrufen
Worksheet sheet = workbook.Worksheets[0];

// Quelldaten mit Kopfzeile (Fruit, Year, Amount) befüllen
// und 9 Datenzeilen mit grape, blueberry, kiwi, cherry über 2020 und 2021
sheet.Cells[0, 0].PutValue("Fruit");
sheet.Cells[0, 1].PutValue("Year");
sheet.Cells[0, 2].PutValue("Amount");

sheet.Cells[1, 0].PutValue("grape");
sheet.Cells[1, 1].PutValue(2020);
sheet.Cells[1, 2].PutValue(50);

sheet.Cells[2, 0].PutValue("blueberry");
sheet.Cells[2, 1].PutValue(2020);
sheet.Cells[2, 2].PutValue(30);

sheet.Cells[3, 0].PutValue("kiwi");
sheet.Cells[3, 1].PutValue(2020);
sheet.Cells[3, 2].PutValue(25);

sheet.Cells[4, 0].PutValue("cherry");
sheet.Cells[4, 1].PutValue(2020);
sheet.Cells[4, 2].PutValue(40);

sheet.Cells[5, 0].PutValue("grape");
sheet.Cells[5, 1].PutValue(2021);
sheet.Cells[5, 2].PutValue(60);

sheet.Cells[6, 0].PutValue("blueberry");
sheet.Cells[6, 1].PutValue(2021);
sheet.Cells[6, 2].PutValue(35);

sheet.Cells[7, 0].PutValue("kiwi");
sheet.Cells[7, 1].PutValue(2021);
sheet.Cells[7, 2].PutValue(28);

sheet.Cells[8, 0].PutValue("cherry");
sheet.Cells[8, 1].PutValue(2021);
sheet.Cells[8, 2].PutValue(45);

sheet.Cells[9, 0].PutValue("grape");
sheet.Cells[9, 1].PutValue(2020);
sheet.Cells[9, 2].PutValue(45);

// Eine Pivot-Tabelle in der Zielzelle E3 mit dem Namen "Pivot1" unter Verwendung des Quellbereichs A1:C10 hinzufügen
int pivotIndex = sheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.PivotTables[pivotIndex];

// Felder zuweisen: Fruit -> Zeilen, Year -> Spalten, Amount -> Daten
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Das Legacy-XLS-Preset-Autoformat "Report5" anwenden
// Hinweis: Diese Eigenschaft ist nur beim Speichern als .xls relevant.
// Beim Speichern als .xlsx/.xlsm/.xlsb ignoriert Excel AutoFormatType
// und verwendet das, was PivotTableStyleType / PivotTableStyleName angibt.
pivotTable.AutoFormatType = PivotTableAutoFormatType.Report5;

// Die Arbeitsmappe im Legacy-.xls-Format speichern
workbook.Save("output.xls");
```

## **Anwenden eines modernen benannten Pivot-Tabellen-Voreinstellungsstils**

`PivotTable.PivotTableStyleType` akzeptiert einen Wert aus der Enumeration `Aspose.Cells.PivotTableStyleType`. Die Enumeration umfasst helle Designs `PivotTableStyleLight1` bis `PivotTableStyleLight28` und dunkle Designs `PivotTableStyleDark1` bis `PivotTableStyleDark28`. Die in Excel 2017 hinzugefügten Stile (die zweite Welle heller und dunkler Designs) sind über dieselbe Enumeration erreichbar.

Dies ist die empfohlene API für jedes moderne Dateiformat. Im Gegensatz zum Legacy-Autoformat wird der hier ausgewählte Stil von Excel originalgetreu wiedergegeben und übersteht Roundtrips durch andere Office-Werkzeuge.

Das folgende Beispiel verwendet dieselben Fruit/Year/Amount-Daten, erstellt eine identische Pivot-Tabelle, wendet `PivotTableStyleDark1` an und speichert die Arbeitsmappe als `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Szenario 2: Anwendung eines modernen, benannten Excel 2007+ Voreinstellungsstils mit PivotTableStyleType.
// Zieldateiformat: .xlsx. Die PivotTableStyleType-Enumeration befindet sich im Aspose.Cells-Namespace
// (nicht in Aspose.Cells.Pivot) — deshalb benötigen wir keine zusätzliche using-Anweisung dafür.
// GitHub-Referenz: https://github.com/aspose-cells/Aspose.Cells-for-.NET/blob/master/Examples/CSharp/PivotTables/ApplyStyleToPivotTable2.cs

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Kopfzeile: Fruit / Year / Amount
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

// 9 Datenzeilen mit Fruit / Year / Amount
worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(150);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(200);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(180);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(120);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(170);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(210);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(190);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(130);

// Hinzufügen einer Pivot-Tabelle an E3 mit dem Namen "Pivot1", basierend auf A1:C10
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Pivot-Felder zuweisen: Fruit -> Zeilenbereich, Year -> Spaltenbereich, Amount -> Datenbereich
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Anwendung eines modernen, benannten Excel 2007+ Pivot-Voreinstellungsstils.
// PivotTableStyleType ist die korrekte API für .xlsx / .xlsm / .xlsb-Dateien; AutoFormatType
// wird von Excel für diese Formate ignoriert. PivotTableStyleDark1 gehört zur Dunkel-Themen-Familie
// (PivotTableStyleDark1..PivotTableStyleDark28), und dieselbe Enumeration stellt auch die
// neueren Excel 2017 Hell/Dunkel-Themen bereit (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleDark1;

// Speichern als modernes .xlsx — dies ist das Format, für das PivotTableStyleType relevant ist.
workbook.Save("output.xlsx");
```

## **Definieren und Anwenden eines benutzerdefinierten Pivot-Tabellenstils**

Die integrierten Voreinstellungen können nicht geändert werden. Wann immer Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Workflow umfasst drei Schritte:

1. Fügen Sie der `TableStyles`-Sammlung der Arbeitsmappe einen benutzerdefinierten Stil über `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` hinzu. Dies gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WholeTable` oder `GrandTotalRow`) über `TableStyle.TableStyleElements.Add(TableStyleElementType)` hinzufügen und dann jedem Element über `TableStyleElement.SetElementStyle(Style)` einen `Style` zuweisen.
3. Wenden Sie den benutzerdefinierten Stil auf die Pivot-Tabelle an, indem Sie `PivotTable.PivotTableStyleName` auf den Namen des Stils setzen. Verwenden Sie hier nicht `PivotTableStyleType`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}

`PivotTableStyleName` und `PivotTableStyleType` sind nicht austauschbar. Verwenden Sie `PivotTableStyleType` für integrierte Voreinstellungen und `PivotTableStyleName` für benutzerdefinierte Stile, die Sie über `AddPivotTableStyle` definiert haben. Beide zu setzen ist harmlos, aber nur das mit der beabsichtigten Quelle übereinstimmende wird wiedergegeben.

{{% /alert %}}

Die verfügbaren `TableStyleElementType`-Werte umfassen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` und `PageFieldValues`.

Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen für `WholeTable` und einer fetten roten Schriftart für `GrandTotalRow`, wendet ihn dann über `PivotTableStyleName` an und speichert als `.xlsx`.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
using Aspose.Cells.Tables;
using System.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Quelldaten befüllen: Kopfzeile + 9 Datenzeilen (A1:C10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(100);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(200);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(300);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(400);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(500);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(600);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(700);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(800);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(900);

// Pivot-Tabelle hinzufügen, Datenquelle A1:C10, verankert bei E3, Name "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Schritt 1: Neuen benutzerdefinierten Pivot-Tabellenstil registrieren und Index erfassen
int styleIndex = workbook.Worksheets.TableStyles.AddPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.Worksheets.TableStyles[styleIndex];

// Schritt 2: WholeTable-Element hinzufügen und dünne schwarze Rahmen auf allen vier Seiten anwenden
int wholeTableElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.WholeTable);
TableStyleElement wholeTableElement = tableStyle.TableStyleElements[wholeTableElementIndex];
Style wholeTableStyle = workbook.CreateStyle();
wholeTableStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.TopBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.BottomBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.LeftBorder].Color = Color.Black;
wholeTableStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
wholeTableStyle.Borders[BorderType.RightBorder].Color = Color.Black;
wholeTableElement.SetElementStyle(wholeTableStyle);

// Schritt 3: GrandTotalRow-Element hinzufügen und fettgedruckte rote Schrift anwenden
int grandTotalElementIndex = tableStyle.TableStyleElements.Add(TableStyleElementType.GrandTotalRow);
TableStyleElement grandTotalElement = tableStyle.TableStyleElements[grandTotalElementIndex];
Style grandTotalStyle = workbook.CreateStyle();
grandTotalStyle.Font.IsBold = true;
grandTotalStyle.Font.Color = Color.Red;
grandTotalElement.SetElementStyle(grandTotalStyle);

// Schritt 4: Den benutzerdefinierten Stil namentlich anwenden (NICHT über PivotTableStyleType, dies gilt für eingebaute Voreinstellungen)
pivotTable.PivotTableStyleName = "CustomPivotStyle";

workbook.Save("output.xlsx");
```

## **Anwenden eines einzelnen Stils auf jede Pivot-Zelle mit FormatAll**

`PivotTable.FormatAll(Style)` ist eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Summen. Alles, was zuvor über `PivotTableStyleType` oder `PivotTableStyleName` gesetzt wurde, wird überschrieben.

{{% alert color="primary" %}}

`FormatAll` überschreibt sowohl `PivotTableStyleType` als auch `PivotTableStyleName`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle hinweg erforderlich ist.

{{% /alert %}}

Das folgende Beispiel erstellt einen `Style` mit gelber Vollfüllung, fetter dunkelblauer Schriftart und dünnen schwarzen Rahmen auf allen Seiten, wendet ihn dann mit `FormatAll` an und speichert als `.xlsx`.

```csharp
using System;
using System.Drawing;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;

// Szenario 4: Einen einzelnen Stil auf jede Pivot-Tabellen-Zelle mit FormatAll anwenden
// Verwendete API: PivotTable.FormatAll(Style)
// Zielformat: .xlsx
// GitHub-Referenz: siehe Aspose.Cells-for-.NET-Repository — Beispiele zur Pivot-Tabellen-Formatierung

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

// Quelldaten befüllen: Kopfzeile (Zeile 1) + 9 Datenzeilen (Zeilen 2-10)
worksheet.Cells["A1"].PutValue("Fruit");
worksheet.Cells["B1"].PutValue("Year");
worksheet.Cells["C1"].PutValue("Amount");

worksheet.Cells["A2"].PutValue("Grape");
worksheet.Cells["B2"].PutValue(2020);
worksheet.Cells["C2"].PutValue(5000);

worksheet.Cells["A3"].PutValue("Blueberry");
worksheet.Cells["B3"].PutValue(2020);
worksheet.Cells["C3"].PutValue(3000);

worksheet.Cells["A4"].PutValue("Kiwi");
worksheet.Cells["B4"].PutValue(2020);
worksheet.Cells["C4"].PutValue(4000);

worksheet.Cells["A5"].PutValue("Cherry");
worksheet.Cells["B5"].PutValue(2020);
worksheet.Cells["C5"].PutValue(2000);

worksheet.Cells["A6"].PutValue("Grape");
worksheet.Cells["B6"].PutValue(2021);
worksheet.Cells["C6"].PutValue(6000);

worksheet.Cells["A7"].PutValue("Blueberry");
worksheet.Cells["B7"].PutValue(2021);
worksheet.Cells["C7"].PutValue(3500);

worksheet.Cells["A8"].PutValue("Kiwi");
worksheet.Cells["B8"].PutValue(2021);
worksheet.Cells["C8"].PutValue(4500);

worksheet.Cells["A9"].PutValue("Cherry");
worksheet.Cells["B9"].PutValue(2021);
worksheet.Cells["C9"].PutValue(2500);

worksheet.Cells["A10"].PutValue("Grape");
worksheet.Cells["B10"].PutValue(2021);
worksheet.Cells["C10"].PutValue(5500);

// Pivot-Tabelle hinzufügen: Quellbereich A1:C10, Zielzelle E3, Name "Pivot1"
int pivotIndex = worksheet.PivotTables.Add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

// Pivot-Felder zuweisen: Fruit -> Zeilenbereich, Year -> Spaltenbereich, Amount -> Datenbereich
pivotTable.AddFieldToArea(PivotFieldType.Row, "Fruit");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

// Einen Stil erstellen, der auf jede Zelle der Pivot-Tabelle angewendet wird
Style style = workbook.CreateStyle();
style.ForegroundColor = Color.Yellow;
style.Pattern = BackgroundType.Solid;
style.Font.IsBold = true;
style.Font.Color = Color.DarkBlue;
style.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.TopBorder].Color = Color.Black;
style.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.BottomBorder].Color = Color.Black;
style.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.LeftBorder].Color = Color.Black;
style.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;
style.Borders[BorderType.RightBorder].Color = Color.Black;

// FormatAll anwenden: erzwingt diesen einzelnen Stil auf jede Zelle der Pivot-Tabelle,
// überschreibt alle zuvor festgelegten PivotTableStyleType / PivotTableStyleName
pivotTable.FormatAll(style);

// Arbeitsmappe im modernen .xlsx-Format speichern
workbook.Save("output.xlsx");
```

## **Welche Stil-API sollte ich verwenden?**

Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzreferenz.

| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `PivotTable.AutoFormatType` | Werte aus `Aspose.Cells.Pivot.PivotTableAutoFormatType` (z. B. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `PivotTable.PivotTableStyleType` | Werte aus `Aspose.Cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich Excel 2017 Ergänzungen). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Verwenden Sie dies, wenn die integrierten Voreinstellungen nicht ausreichen. Konfigurieren Sie über `TableStyleElement.SetElementStyle(...)`. |
| Beliebiges Format (einheitliche Überschreibung) | `PivotTable.FormatAll(Style)` | Verknüpfung, die jede andere Stileinstellung in der gesamten Pivot-Tabelle überschreibt. |

Im Zweifelsfall speichern Sie als `.xlsx` und verwenden Sie `PivotTableStyleType` für integrierte Designs oder `PivotTableStyleName` für benutzerdefinierte Designs.

{{< app/cells/assistant language="csharp" >}}