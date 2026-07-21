---
title: Anwenden von Stilen auf Pivot-Tabellen
linktitle: Anwenden von Stilen auf Pivot-Tabellen
description: Erfahren Sie, wie Sie in Aspose.Cells for Node.js via Java integrierte und benutzerdefinierte Stile auf Pivot-Tabellen anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Stilen aus Excel 2007+, benutzerdefinierten Pivot-Tabellen-Stilen und der FormatAll-Verknüpfung.
keywords: Aspose.Cells Node.js via Java Pivot-Tabellen-Stil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/nodejs-java/apply-style-to-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells unterstützt die Anwendung sowohl von Legacy-Pivot-Autoformaten (für `.xls`-Dateien vorgesehen) als auch von modernen benannten oder benutzerdefinierten Pivot-Tabellen-Stilen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, nicht vom Format, aus dem sie geladen wurde.

{{% /alert %}}

## **Einführung**

Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden, und in diesem Fall gilt die moderne Stil-API anstelle der Legacy-API.

Für die Legacy-`.xls`-Ausgabe verwenden Sie die Eigenschaft `PivotTable.autoFormatType` zusammen mit der Aufzählung `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Diese API entspricht der Autoformat-Auswahl, die das klassische Excel für Pivot-Tabellen angeboten hat.

Für die moderne `.xlsx`-, `.xlsm`- und `.xlsb`-Ausgabe stehen zwei Varianten der Stil-API zur Verfügung:

- `PivotTable.pivotTableStyleType` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `PivotTable.pivotTableStyleName` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `Worksheets.getTableStyles().addPivotTableStyle(...)` definieren. Benutzerdefinierte Stile sind erforderlich, wenn Sie Farben, Rahmen oder Schriftarten ändern möchten, die über das hinausgehen, was die Voreinstellungen bieten.

Darüber hinaus ist `PivotTable.formatAll(Style)` eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet und alles überschreibt, was über eine der oben genannten Stilnamen-APIs festgelegt wurde. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrunde liegenden Design erforderlich ist.

## **Anwenden eines Legacy-XLS-Voreinstellungs-Autoformats**

`PivotTable.autoFormatType` akzeptiert einen Wert aus der Aufzählung `Aspose.Cells.Pivot.PivotTableAutoFormatType`. Die verfügbaren Werte sind `Report1` bis `Report10`, `Classic` und `Table1` bis `Table10`.

{{% alert color="primary" %}}

`autoFormatType` wird nur berücksichtigt, wenn die Arbeitsmappe als `.xls` gespeichert wird. Wenn dieselbe Arbeitsmappe als `.xlsx`, `.xlsm` oder `.xlsb` gespeichert wird, ignoriert Excel diese Eigenschaft und greift auf die Einstellungen `pivotTableStyleType` und `pivotTableStyleName` zurück.

{{% /alert %}}

Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Fruit/Year/Amount-Beispieldaten ein, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.Report5` an und speichert das Ergebnis als `.xls`.

```javascript
let workbook = new AsposeCells.Workbook();

// Erstes Arbeitsblatt abrufen
let sheet = workbook.getWorksheets().get(0);

// Quelldaten mit Kopfzeile (Obst, Jahr, Menge) füllen
// und 9 Datenzeilen mit Trauben, Blaubeeren, Kiwi, Kirsche für 2020 und 2021
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

// Pivot-Tabelle an Zielzelle E3 hinzufügen, benannt "Pivot1", mit Quellbereich A1:C10
let pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = sheet.getPivotTables().get(pivotIndex);

// Felder zuweisen: Obst -> Zeilen, Jahr -> Spalten, Menge -> Daten
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Legacy-XLS-Voreinstellungs-Autoformat "Report5" anwenden
// Hinweis: Diese Eigenschaft ist nur beim Speichern als .xls relevant.
// Beim Speichern als .xlsx/.xlsm/.xlsb ignoriert Excel den AutoFormatType
// und verwendet das, was PivotTableStyleType / PivotTableStyleName angibt.
pivotTable.setAutoFormatType(AsposeCells.PivotTableAutoFormatType.REPORT_5);

// Arbeitsmappe im Legacy-.xls-Format speichern
workbook.save("output.xls");
```

## **Anwenden eines modernen benannten Pivot-Tabellen-Voreinstellungs-Stils**

`PivotTable.pivotTableStyleType` akzeptiert einen Wert aus der Aufzählung `Aspose.Cells.PivotTableStyleType`. Die Aufzählung umfasst helle Designs `PivotTableStyleLight1` bis `PivotTableStyleLight28` und dunkle Designs `PivotTableStyleDark1` bis `PivotTableStyleDark28`. Die in Excel 2017 hinzugefügten Stile (die zweite Welle der hellen und dunklen Designs) sind über dieselbe Aufzählung erreichbar.

Dies ist die empfohlene API für jedes moderne Dateiformat. Im Gegensatz zum Legacy-Autoformat wird der hier ausgewählte Stil von Excel originalgetreu wiedergegeben und übersteht Roundtrips durch andere Office-Tools.

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

// Eine Pivot-Tabelle bei E3 mit dem Namen "Pivot1" hinzufügen, basierend auf A1:C10
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot-Felder zuweisen: Frucht -> Zeilenbereich, Jahr -> Spaltenbereich, Betrag -> Datenbereich
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Einen modernen benannten Pivot-Stil für Excel 2007+ anwenden.
// PivotTableStyleType ist die korrekte API für .xlsx / .xlsm / .xlsb-Dateien; AutoFormatType
// wird von Excel für diese Formate ignoriert. PivotTableStyleDark1 gehört zur Familie der dunklen Designs
// (PivotTableStyleDark1..PivotTableStyleDark28), und dasselbe Enum stellt auch die
// neueren Excel 2017 hellen/dunklen Designs bereit (PivotTableStyleLight1..Light28 / Dark1..Dark28).
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_DARK_1);

// Als modernes .xlsx speichern — dies ist das Format, für das PivotTableStyleType von Bedeutung ist.
workbook.save("output.xlsx");
```

## **Definieren und Anwenden eines benutzerdefinierten Pivot-Tabellen-Stils**

Die integrierten Voreinstellungen können nicht geändert werden. Wenn Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Arbeitsablauf umfasst drei Schritte:

1. Fügen Sie der `TableStyles`-Sammlung der Arbeitsmappe über `Worksheets.getTableStyles().addPivotTableStyle(String name)` einen benutzerdefinierten Stil hinzu. Dies gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WholeTable` oder `GrandTotalRow`) über `TableStyle.tableStyleElements.add(TableStyleElementType)` hinzufügen und dann über `TableStyleElement.setElementStyle(Style)` jedem Element ein `Style` zuweisen.
3. Wenden Sie den benutzerdefinierten Stil auf die Pivot-Tabelle an, indem Sie `PivotTable.pivotTableStyleName` auf den Namen des Stils setzen. Verwenden Sie hier nicht `pivotTableStyleType`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}

`pivotTableStyleName` und `pivotTableStyleType` sind nicht austauschbar. Verwenden Sie `pivotTableStyleType` für integrierte Voreinstellungen und `pivotTableStyleName` für benutzerdefinierte Stile, die Sie über `addPivotTableStyle` definiert haben. Das Setzen beider Werte ist harmlos, aber nur derjenige, der der beabsichtigten Quelle entspricht, wird gerendert.

{{% /alert %}}

Die verfügbaren `TableStyleElementType`-Werte umfassen `WholeTable`, `FirstRow`, `LastRow`, `FirstColumn`, `LastColumn`, `GrandTotalRow`, `GrandTotalColumn`, `PageFieldLabels` und `PageFieldValues`.

Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen auf `WholeTable` und einer fetten roten Schriftart auf `GrandTotalRow`, wendet ihn dann über `pivotTableStyleName` an und speichert als `.xlsx`.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Quellendaten befüllen: Kopfzeile + 9 Datenzeilen (A1:C10)
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

// Pivot-Tabelle aus A1:C10 hinzufügen, verankert bei E3, benannt "Pivot1"
let pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");

// Schritt 1: Neuen benutzerdefinierten Pivot-Tabellenstil registrieren und Index erfassen
let styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
let tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);

// Schritt 2: WholeTable-Element hinzufügen und dünne schwarze Rahmen auf allen vier Seiten anwenden
let wholeTableElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.WHOLE_TABLE);
let wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
let wholeTableStyle = workbook.createStyle();
let topBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.TOP_BORDER);
topBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
topBorder.setColor(AsposeCells.Color.BLACK);

let bottomBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.BOTTOM_BORDER);
bottomBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
bottomBorder.setColor(AsposeCells.Color.BLACK);

let leftBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.LEFT_BORDER);
leftBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
leftBorder.setColor(AsposeCells.Color.BLACK);

let rightBorder = wholeTableStyle.getBorders().get(AsposeCells.BorderType.RIGHT_BORDER);
rightBorder.setLineStyle(AsposeCells.CellBorderType.THIN);
rightBorder.setColor(AsposeCells.Color.BLACK);

wholeTableElement.setElementStyle(wholeTableStyle);

// Schritt 3: GrandTotalRow-Element hinzufügen und fette rote Schrift anwenden
let grandTotalElementIndex = tableStyle.getTableStyleElements().add(AsposeCells.TableStyleElementType.GRAND_TOTAL_ROW);
let grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
let grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(AsposeCells.Color.RED);
grandTotalElement.setElementStyle(grandTotalStyle);

// Schritt 4: Benutzerdefinierten Stil namentlich anwenden (NICHT über PivotTableStyleType, das ist für eingebaute Voreinstellungen)
pivotTable.setPivotTableStyleName("CustomPivotStyle");

workbook.save("output.xlsx");
```

## **Anwenden eines einzelnen Stils auf jede Pivot-Zelle mit FormatAll**

`PivotTable.formatAll(Style)` ist eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spaltenüberschriften sowie der Summen. Alles, was zuvor über `pivotTableStyleType` oder `pivotTableStyleName` festgelegt wurde, wird überschrieben.

{{% alert color="primary" %}}

`formatAll` überschreibt sowohl `pivotTableStyleType` als auch `pivotTableStyleName`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle hinweg erforderlich ist.

{{% /alert %}}

Das folgende Beispiel erstellt ein `Style` mit gelber Vollfüllung, fetter dunkelblauer Schriftart und dünnen schwarzen Rahmen auf allen Seiten, wendet es dann mit `formatAll` an und speichert als `.xlsx`.

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

// Einen Stil erstellen, der auf jede Zelle der Pivot-Tabelle angewendet wird
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

// FormatAll anwenden: erzwingt diesen einzelnen Stil auf jede Zelle der Pivot-Tabelle,
// überschreibt jeden zuvor gesetzten PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);

// Arbeitsmappe im modernen .xlsx-Format speichern
workbook.save("output.xlsx");
```

## **Welche Stil-API sollte ich verwenden?**

Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzreferenz.

| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `PivotTable.autoFormatType` | Werte aus `Aspose.Cells.Pivot.PivotTableAutoFormatType` (z. B. `Report1`–`Report10`, `Classic`, `Table1`–`Table10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `PivotTable.pivotTableStyleType` | Werte aus `Aspose.Cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich der Ergänzungen aus Excel 2017). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `PivotTable.pivotTableStyleName` + `Worksheets.getTableStyles().addPivotTableStyle(...)` | Verwenden Sie dies, wenn die integrierten Voreinstellungen nicht ausreichen. Konfigurieren Sie über `TableStyleElement.setElementStyle(...)`. |
| Beliebiges Format (einheitliche Überschreibung) | `PivotTable.formatAll(Style)` | Verknüpfung, die jede andere Stileinstellung über die gesamte Pivot-Tabelle hinweg überschreibt. |

Im Zweifelsfall speichern Sie als `.xlsx` und verwenden Sie `pivotTableStyleType` für integrierte Designs oder `pivotTableStyleName` für benutzerdefinierte Designs.

{{< app/cells/assistant language="javascript" >}}