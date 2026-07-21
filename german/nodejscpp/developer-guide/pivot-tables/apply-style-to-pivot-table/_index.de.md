---
title: Anwenden von Stilen auf Pivot-Tabellen
linktitle: Anwenden von Stilen auf Pivot-Tabellen
description: Erfahren Sie, wie Sie in Aspose.Cells for Node.js via C++ integrierte und benutzerdefinierte Stile auf Pivot-Tabellen anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Excel 2007+ Stilen, benutzerdefinierten Pivot-Tabellenstilen und der FormatAll-Verknüpfung.
keywords: Aspose.Cells Node.js via C++ Pivot-Tabellenstil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/nodejs-cpp/apply-style-to-pivot-table/
ai_search_scope: cells_nodejs_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


{{% alert color="primary" %}}

Aspose.Cells unterstützt die Anwendung sowohl älterer Pivot-Autoformate (für `.xls`-Dateien vorgesehen) als auch moderner benannter oder benutzerdefinierter PivotTable-Formatvorlagen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, und nicht vom Format, aus dem sie geladen wurde.

{{% /alert %}}

## **Einführung**

Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, und nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden, und in diesem Fall kommt die moderne Stil-API zum Einsatz und nicht die ältere.

Für die Legacy-`.xls`-Ausgabe verwenden Sie die Eigenschaft `PivotTable.AutoFormatType` zusammen mit der Enumeration `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Diese API entspricht der Autoformat-Auswahl, die klassisches Excel für Pivot-Tabellen angeboten hat.

Für die moderne `.xlsx`-, `.xlsm`- und `.xlsb`-Ausgabe stehen zwei Varianten der Stil-API zur Verfügung:

- `PivotTable.PivotTableStyleType` wählt eine der integrierten benannten Formatvorlagen aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Formatvorlagen). Diese Voreinstellungen sind schreibgeschützt.
- `PivotTable.PivotTableStyleName` wählt eine benutzerdefinierte Formatvorlage aus, die Sie selbst über `Workbook.Worksheets.TableStyles.AddPivotTableStyle(...)` definieren. Benutzerdefinierte Formatvorlagen sind erforderlich, wenn Sie Farben, Rahmen oder Schriftarten über das hinaus ändern möchten, was die Voreinstellungen bieten.

Darüber hinaus ist `PivotTable.FormatAll(Style)` eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und alle über die beiden oben genannten Stilnamens-APIs vorgenommenen Einstellungen überschreibt. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrunde liegenden Design erforderlich ist.

## **Anwenden eines Legacy-XLS-Voreinstellungs-Autoformats**

`PivotTable.AutoFormatType` akzeptiert einen Wert aus der Enumeration `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `Report1` bis `Report10`, `Classic` und `Table1` bis `Table10`.

{{% alert color="primary" %}}

`AutoFormatType` wird nur berücksichtigt, wenn die Arbeitsmappe als `.xls` gespeichert wird. Wenn dieselbe Arbeitsmappe als `.xlsx`, `.xlsm` oder `.xlsb` gespeichert wird, ignoriert Excel diese Eigenschaft und greift auf die Einstellungen `PivotTableStyleType` und `PivotTableStyleName` zurück.

{{% /alert %}}

Das folgende Beispiel lädt eine neue Arbeitsmappe, befüllt die Beispieldaten Fruit/Year/Amount, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.Report5` an und speichert das Ergebnis als `.xls`.

```javascript
const AsposeCells = require("aspose.cells");

// Szenario 1: Ein Legacy-XLS-Voreinstellungs-Autoformat anwenden
// Verwendete API: PivotTable.AutoFormatType
// Zieldateiformat: .xls (Legacy)
// Für vollständige Beispiele und Datendateien besuchen Sie bitte https://github.com/aspose-cells/Aspose.Cells-for-.NET

// Eine neue Arbeitsmappe erstellen
const workbook = new AsposeCells.Workbook();

// Das erste Arbeitsblatt abrufen
const sheet = workbook.getWorksheets().get(0);

// Quelldaten mit Kopfzeile befüllen (Obst, Jahr, Betrag)
// und 9 Datenzeilen mit Trauben, Heidelbeeren, Kiwi, Kirsche über 2020 und 2021
sheet.getCells().get(0, 0).putValue("Fruit");
sheet.getCells().get(0, 1).putValue("Year");
sheet.getCells().get(0, 2).putValue("Amount");

sheet.getCells().get(1, 0).putValue("grape");
sheet.getCells().get(1, 1).putValue(2020);
sheet.getCells().get(1, 2).putValue(50);

sheet.getCells().get(2, 0).putValue("blueberry");
sheet.getCells().get(2, 1).putValue(2020);
sheet.getCells().get(2, 2).putValue(30);

sheet.getCells().get(3, 0).putValue("kiwi");
sheet.getCells().get(3, 1).putValue(2020);
sheet.getCells().get(3, 2).putValue(25);

sheet.getCells().get(4, 0).putValue("cherry");
sheet.getCells().get(4, 1).putValue(2020);
sheet.getCells().get(4, 2).putValue(40);

sheet.getCells().get(5, 0).putValue("grape");
sheet.getCells().get(5, 1).putValue(2021);
sheet.getCells().get(5, 2).putValue(60);

sheet.getCells().get(6, 0).putValue("blueberry");
sheet.getCells().get(6, 1).putValue(2021);
sheet.getCells().get(6, 2).putValue(35);

sheet.getCells().get(7, 0).putValue("kiwi");
sheet.getCells().get(7, 1).putValue(2021);
sheet.getCells().get(7, 2).putValue(28);

sheet.getCells().get(8, 0).putValue("cherry");
sheet.getCells().get(8, 1).putValue(2021);
sheet.getCells().get(8, 2).putValue(45);

sheet.getCells().get(9, 0).putValue("grape");
sheet.getCells().get(9, 1).putValue(2020);
sheet.getCells().get(9, 2).putValue(45);

// Eine Pivot-Tabelle in der Zielzelle E3 mit dem Namen "Pivot1" unter Verwendung des Quellbereichs A1:C10 hinzufügen
const pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
const pivotTable = sheet.getPivotTables().get(pivotIndex);

// Felder zuweisen: Obst -> Zeilen, Jahr -> Spalten, Betrag -> Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Das Legacy-XLS-Voreinstellungs-Autoformat "Report5" anwenden
// Hinweis: Diese Eigenschaft ist nur beim Speichern als .xls relevant.
// Beim Speichern als .xlsx/.xlsm/.xlsb ignoriert Excel AutoFormatType
// und verwendet, was auch immer PivotTableStyleType / PivotTableStyleName angibt.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.Report5);

// Die Arbeitsmappe im Legacy-.xls-Format speichern
workbook.save("output.xls");
```

## **Anwenden einer modernen benannten PivotTable-Voreinstellungs-Formatvorlage**

`PivotTable.PivotTableStyleType` akzeptiert einen Wert aus der Enumeration `Aspose.Cells.PivotTableStyleType`. Die Enumeration umfasst die hellen Designs `PivotTableStyleLight1` bis `PivotTableStyleLight28` und die dunklen Designs `PivotTableStyleDark1` bis `PivotTableStyleDark28`. Die in Excel 2017 hinzugefügten Formatvorlagen (die zweite Welle der hellen und dunklen Designs) sind über dieselbe Enumeration erreichbar.

Dies ist die empfohlene API für jedes moderne Dateiformat. Anders als beim Legacy-Autoformat wird die hier ausgewählte Formatvorlage von Excel originalgetreu wiedergegeben und übersteht Roundtrips durch andere Office-Tools.

Das folgende Beispiel verwendet dieselben Fruit/Year/Amount-Daten, erstellt eine identische Pivot-Tabelle, wendet `PivotTableStyleDark1` an und speichert die Arbeitsmappe als `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Kopfzeile: Frucht / Jahr / Betrag
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

// 9 Datenzeilen mit Frucht / Jahr / Betrag
worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(150);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(200);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(180);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(120);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(170);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(210);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(190);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(130);

// Fügt eine Pivot-Tabelle an E3 mit dem Namen "Pivot1" hinzu, basierend auf A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot-Felder zuweisen: Frucht -> Zeilenbereich, Jahr -> Spaltenbereich, Betrag -> Datenbereich
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Wendet einen modernen benannten Pivot-Stil für Excel 2007+ an.
// PivotTableStyleType ist die korrekte API für .xlsx- / .xlsm- / .xlsb-Dateien; AutoFormatType
// wird von Excel für diese Formate ignoriert. PivotTableStyleDark1 gehört zur dunklen Theme-Familie
// (PivotTableStyleDark1..PivotTableStyleDark28), und dieselbe Enumeration enthält auch die neueren
// Excel-2017-Themes hell/dunkel (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleDark1);

// Als modernes .xlsx speichern — dies ist das Format, für das PivotTableStyleType relevant ist.
workbook.save("output.xlsx");
```

## **Definieren und Anwenden einer benutzerdefinierten PivotTable-Formatvorlage**

Die integrierten Voreinstellungen können nicht geändert werden. Wann immer Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie eine benutzerdefinierte Pivot-Formatvorlage definieren. Der Arbeitsablauf umfasst drei Schritte:

1. Fügen Sie der `TableStyles`-Sammlung der Arbeitsmappe über `Workbook.Worksheets.TableStyles.AddPivotTableStyle(string name)` eine benutzerdefinierte Formatvorlage hinzu. Dies gibt den Index der neu erstellten Formatvorlage zurück.
2. Konfigurieren Sie die Formatvorlage, indem Sie Elemente (wie `WholeTable` oder `GrandTotalRow`) über `TableStyle.TableStyleElements.Add(TableStyleElementType)` hinzufügen, und weisen Sie dann jedem Element über `TableStyleElement.SetElementStyle(Style)` eine `Style` zu.
3. Wenden Sie die benutzerdefinierte Formatvorlage auf die Pivot-Tabelle an, indem Sie `PivotTable.PivotTableStyleName` auf den Namen der Formatvorlage setzen. Verwenden Sie hier nicht `PivotTableStyleType`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}

`PivotTableStyleName` und `PivotTableStyleType` sind nicht austauschbar. Verwenden Sie `PivotTableStyleType` für integrierte Voreinstellungen und `PivotTableStyleName` für benutzerdefinierte Formatvorlagen, die Sie über `AddPivotTableStyle` definiert haben. Beides zu setzen ist harmlos, aber nur die Einstellung, die zur beabsichtigten Quelle passt, wird wiedergegeben.

{{% /alert %}}

Die verfügbaren `TableStyleElementType`-Werte umfassen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` und `PageFieldValues`.

Das folgende Beispiel definiert eine benutzerdefinierte Pivot-Formatvorlage mit einem dünnen schwarzen Rahmen auf `WholeTable` und einer fett formatierten roten Schriftart auf `GrandTotalRow`, wendet sie dann über `PivotTableStyleName` an und speichert als `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Quelldaten befüllen: Kopfzeile + 9 Datenzeilen (A1:C10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(100);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(200);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(300);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(400);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(500);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(600);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(700);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(800);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(900);

// Pivot-Tabelle aus A1:C10 hinzufügen, verankert bei E3, mit dem Namen "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Schritt 1: Neuen benutzerdefinierten Pivot-Tabellenstil registrieren und dessen Index erfassen
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Schritt 2: WholeTable-Element hinzufügen und dünne schwarze Rahmen auf allen vier Seiten anwenden
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WholeTable);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
wholeTableStyle.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);
wholeTableElement.setElementStyle(wholeTableStyle);

// Schritt 3: GrandTotalRow-Element hinzufügen und fettgedruckte rote Schrift anwenden
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GrandTotalRow);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setIsBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.Red);
grandTotalElement.setElementStyle(grandTotalStyle);

// Schritt 4: Benutzerdefinierten Stil über den Namen anwenden (NICHT über PivotTableStyleType, dies ist für eingebaute Voreinstellungen)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Anwenden einer Formatvorlage auf jede Pivot-Zelle mit FormatAll**

`PivotTable.FormatAll(Style)` ist eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Summen. Alles, was zuvor über `PivotTableStyleType` oder `PivotTableStyleName` festgelegt wurde, wird überschrieben.

{{% alert color="primary" %}}

`FormatAll` überschreibt sowohl `PivotTableStyleType` als auch `PivotTableStyleName`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle erforderlich ist.

{{% /alert %}}

Das folgende Beispiel erstellt eine `Style` mit gelber Vollfüllung, fett formatierter dunkelblauer Schriftart und dünnen schwarzen Rahmen auf allen Seiten, wendet sie dann mit `FormatAll` an und speichert als `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Quelldaten befüllen: Kopfzeile (Zeile 1) + 9 Datenzeilen (Zeilen 2-10)
worksheet.getCells().get("A1").putValue("Fruit");
worksheet.getCells().get("B1").putValue("Year");
worksheet.getCells().get("C1").putValue("Amount");

worksheet.getCells().get("A2").putValue("Grape");
worksheet.getCells().get("B2").putValue(2020);
worksheet.getCells().get("C2").putValue(5000);

worksheet.getCells().get("A3").putValue("Blueberry");
worksheet.getCells().get("B3").putValue(2020);
worksheet.getCells().get("C3").putValue(3000);

worksheet.getCells().get("A4").putValue("Kiwi");
worksheet.getCells().get("B4").putValue(2020);
worksheet.getCells().get("C4").putValue(4000);

worksheet.getCells().get("A5").putValue("Cherry");
worksheet.getCells().get("B5").putValue(2020);
worksheet.getCells().get("C5").putValue(2000);

worksheet.getCells().get("A6").putValue("Grape");
worksheet.getCells().get("B6").putValue(2021);
worksheet.getCells().get("C6").putValue(6000);

worksheet.getCells().get("A7").putValue("Blueberry");
worksheet.getCells().get("B7").putValue(2021);
worksheet.getCells().get("C7").putValue(3500);

worksheet.getCells().get("A8").putValue("Kiwi");
worksheet.getCells().get("B8").putValue(2021);
worksheet.getCells().get("C8").putValue(4500);

worksheet.getCells().get("A9").putValue("Cherry");
worksheet.getCells().get("B9").putValue(2021);
worksheet.getCells().get("C9").putValue(2500);

worksheet.getCells().get("A10").putValue("Grape");
worksheet.getCells().get("B10").putValue(2021);
worksheet.getCells().get("C10").putValue(5500);

// Pivot-Tabelle hinzufügen: Quellbereich A1:C10, Zielzelle E3, Name "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot-Felder zuweisen: Fruit -> Zeilenbereich, Year -> Spaltenbereich, Amount -> Datenbereich
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

// Eine Stilvorlage erstellen, die auf jede Zelle der Pivot-Tabelle angewendet wird
let style = workbook.createStyle();
style.setForegroundColor(AsposeCells.Color.Yellow);
style.setPattern(AsposeCells.BackgroundType.Solid);
style.getFont().setIsBold(true);
style.getFont().setColor(AsposeCells.Color.DarkBlue);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.TopBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.BottomBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.LeftBorder).setColor(AsposeCells.Color.Black);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setLineStyle(AsposeCells.CellBorderType.Thin);
style.getBorders().get(AsposeCells.BorderType.RightBorder).setColor(AsposeCells.Color.Black);

// formatAll anwenden: erzwingt diesen einzelnen Stil auf jede Zelle der Pivot-Tabelle,
// und überschreibt alle zuvor gesetzten PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);

// Arbeitsmappe im modernen .xlsx-Format speichern
workbook.save("output.xlsx");
```

## **Welche Stil-API sollte ich verwenden?**

Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzreferenz.

| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `PivotTable.AutoFormatType` | Werte aus `Aspose.Cells.Pivot.PivotTableAutoFormatType` (z. B. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierte Formatvorlage) | `PivotTable.PivotTableStyleType` | Werte aus `Aspose.Cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich der Ergänzungen aus Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierte Formatvorlage) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.AddPivotTableStyle(...)` | Verwenden Sie dies, wenn die integrierten Voreinstellungen nicht ausreichen. Konfiguration über `TableStyleElement.SetElementStyle(...)`. |
| Beliebiges Format (einheitliche Überschreibung) | `PivotTable.FormatAll(Style)` | Verknüpfung, die jede andere Stileinstellung in der gesamten Pivot-Tabelle überschreibt. |

Im Zweifelsfall speichern Sie als `.xlsx` und verwenden `PivotTableStyleType` für integrierte Designs oder `PivotTableStyleName` für benutzerdefinierte Designs.

{{< app/cells/assistant language="javascript" >}}
