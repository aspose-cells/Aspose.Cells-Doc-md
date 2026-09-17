---
title: Anwenden von Stilen auf Pivot-Tabellen in Aspose.Cells for Java
description: Erfahren Sie, wie Sie in Aspose.Cells for Java integrierte und benutzerdefinierte Stile auf Pivot-Tabellen anwenden, einschließlich Legacy-XLS-Autoformaten, modernen benannten Stilen ab Excel 2007+, benutzerdefinierten Pivot-Tabellen-Stilen und der FormatAll-Verknüpfung.
linktitle: Pivot-Tabellen-Stile anwenden
keywords: Aspose.Cells for Java Pivot-Tabellen-Stil, PivotTableStyleType, AutoFormatType, FormatAll, benutzerdefinierter Stil, PivotTableStyleName, TableStyles
type: docs
weight: 200
url: /de/java/apply-style-to-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells unterstützt das Anwenden sowohl von Legacy-Pivot-Autoformaten (für `.xls`-Dateien vorgesehen) als auch von modernen benannten oder benutzerdefinierten Pivot-Tabellen-Stilen (für `.xlsx`-, `.xlsm`- und `.xlsb`-Dateien vorgesehen). Welche API Sie aufrufen sollten, hängt vom Dateiformat ab, in dem die Arbeitsmappe gespeichert wird, und nicht vom Format, aus dem sie geladen wurde.
{{% /alert %}}

## **Einführung**
Aspose.Cells stellt zwei parallele Stil-APIs für Pivot-Tabellen bereit. Die Entscheidung zwischen ihnen wird durch das Dateiformat bestimmt, in dem Sie die Arbeitsmappe speichern, und nicht durch das Format, aus dem Sie sie lesen. Eine aus einer `.xls`-Datei geladene Arbeitsmappe kann als `.xlsx` neu gespeichert werden, und in diesem Fall kommt die moderne Stil-API statt der Legacy-API zur Anwendung.
- `PivotTable.PivotTableStyleType` wählt einen der integrierten benannten Stile aus (helle und dunkle Designs, einschließlich der in Excel 2017 hinzugefügten Stile). Diese Voreinstellungen sind schreibgeschützt.
- `PivotTable.PivotTableStyleName` wählt einen benutzerdefinierten Stil aus, den Sie selbst über `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(...)` definieren. Benutzerdefinierte Stile sind erforderlich, wenn Sie Farben, Rahmen oder Schriftarten über das hinaus ändern möchten, was die Voreinstellungen bieten.
Darüber hinaus ist `PivotTable.formatAll(Style)` eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle des Pivots anwendet und überschreibt, was auch immer über eine der oben genannten Stil-Namens-APIs festgelegt wurde. Dies ist nützlich, wenn ein einheitliches Erscheinungsbild unabhängig vom zugrunde liegenden Design erforderlich ist.

## **Anwenden eines Legacy-XLS-Voreinstellungs-Autoformats**
`PivotTable.AutoFormatType` akzeptiert einen Wert aus der Enumeration `com.aspose.cells.PivotTableAutoFormatType`. Die verfügbaren Werte sind `REPORT_1` bis `REPORT_10`, `CLASSIC` und `TABLE_1` bis `TABLE_10`.
Das folgende Beispiel lädt eine neue Arbeitsmappe, füllt die Fruit/Year/Amount-Beispieldaten, fügt eine Pivot-Tabelle hinzu, wendet `PivotTableAutoFormatType.REPORT_5` an und speichert das Ergebnis als `.xls`.

{{% alert color="primary" %}}
**Warum keine Spaltenfelder?** Autoformate der Report-Serie (`Report1` bis `Report10`, `Table1` bis `Table10`) wurden im klassischen Excel für **eindimensionale Pivot-Tabellen** mit nur Zeilenfeldern und Werten entwickelt — sie enthalten keine integrierte Formatierung für Spaltenfeld-Header. Wenn Ihre Pivot-Tabelle Spaltenfelder benötigt, verwenden Sie stattdessen die modernen `PivotTableStyleType`-Voreinstellungen aus [Szenario 2](#apply-a-modern-named-preset-pivot-table-style), die für das zweidimensionale Layout ausgelegt sind, das modernes Excel verwendet.
{{% /alert %}}

```java
import com.aspose.cells.*;
// Szenario 1: Ein Legacy-XLS-Autoformat-Preset anwenden
// Verwendete API: PivotTable.AutoFormatType
// Zieldateiformat: .xls (Legacy)
// Für vollständige Beispiele und Datendateien besuchen Sie bitte https://github.com/aspose-cells/Aspose.Cells-for-.NET
// Eine neue Arbeitsmappe erstellen
Workbook workbook = new Workbook();
// Das erste Arbeitsblatt abrufen
Worksheet sheet = workbook.getWorksheets().get(0);
// Die Quelldaten mit Kopfzeile (Fruit, Year, Amount) befüllen
// und 9 Datenzeilen, die Trauben, Blaubeeren, Kiwi, Kirsche über 2020 und 2021 abdecken
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
// Eine Pivot-Tabelle an der Zielzelle E3 hinzufügen, benannt "Pivot1", unter Verwendung des Quellbereichs A1:C10
int pivotIndex = sheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = sheet.getPivotTables().get(pivotIndex);
// Felder zuweisen: Fruit -> Zeilen, Amount -> Daten
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Das Legacy-XLS-Autoformat-Preset "Report5" anwenden
// Hinweis: Diese Eigenschaft ist nur beim Speichern als .xls relevant.
// Beim Speichern als .xlsx/.xlsm/.xlsb ignoriert Excel AutoFormatType
// und verwendet stattdessen die Angaben aus PivotTableStyleType / PivotTableStyleName.
pivotTable.setAutoFormatType(PivotTableAutoFormatType.REPORT_5);
// Die Arbeitsmappe im Legacy-.xls-Format speichern
workbook.save("output.xls");
```

## **Anwenden eines modernen benannten Pivot-Tabellen-Voreinstellungsstils**

## **Definieren und Anwenden eines benutzerdefinierten Pivot-Tabellen-Stils**
Die integrierten Voreinstellungen können nicht geändert werden. Wenn Sie Farben, Rahmen oder Schriftarten überschreiben müssen, müssen Sie einen benutzerdefinierten Pivot-Stil definieren. Der Workflow besteht aus drei Schritten:
1. Fügen Sie der `TableStyles`-Sammlung der Arbeitsmappe über `Workbook.getWorksheets().getTableStyles().addPivotTableStyle(String name)` einen benutzerdefinierten Stil hinzu. Dies gibt den Index des neu erstellten Stils zurück.
2. Konfigurieren Sie den Stil, indem Sie Elemente (wie `WholeTable` oder `GrandTotalRow`) über `TableStyle.getTableStyleElements().add(TableStyleElementType)` hinzufügen, und weisen Sie dann jedem Element über `TableStyleElement.setElementStyle(Style)` einen `Style` zu.
3. Wenden Sie den benutzerdefinierten Stil auf den Pivot an, indem Sie `PivotTable.PivotTableStyleName` auf den Namen des Stils setzen. Verwenden Sie hier nicht `PivotTableStyleType`, da diese Eigenschaft integrierte Voreinstellungen auswählt.

{{% alert color="primary" %}}
`PivotTableStyleName` und `PivotTableStyleType` sind nicht austauschbar. Verwenden Sie `PivotTableStyleType` für integrierte Voreinstellungen und `PivotTableStyleName` für benutzerdefinierte Stile, die Sie über `addPivotTableStyle` definiert haben. Das Festlegen beider ist harmlos, aber nur diejenige, die der beabsichtigten Quelle entspricht, wird gerendert.
{{% /alert %}}

Die verfügbaren `TableStyleElementType`-Werte umfassen `WHOLE_TABLE`, `FIRST_ROW`, `LAST_ROW`, `FIRST_COLUMN`, `LAST_COLUMN`, `GRAND_TOTAL_ROW`, `GRAND_TOTAL_COLUMN`, `PAGE_FIELD_LABELS` und `PAGE_FIELD_VALUES`.
Das folgende Beispiel definiert einen benutzerdefinierten Pivot-Stil mit einem dünnen schwarzen Rahmen auf `WholeTable` und einer fett formatierten roten Schriftart auf `GrandTotalRow`, wendet ihn dann über `PivotTableStyleName` an und speichert als `.xlsx`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
// Pivot-Tabelle aus A1:C10 hinzufügen, verankert bei E3, benannt "Pivot1"
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Schritt 1: Einen neuen benutzerdefinierten Pivot-Tabellen-Stil registrieren und dessen Index erfassen
int styleIndex = workbook.getWorksheets().getTableStyles().addPivotTableStyle("CustomPivotStyle");
TableStyle tableStyle = workbook.getWorksheets().getTableStyles().get(styleIndex);
// Schritt 2: Ein WholeTable-Element hinzufügen und dünne schwarze Rahmen auf allen vier Seiten anwenden
int wholeTableElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.WHOLE_TABLE);
TableStyleElement wholeTableElement = tableStyle.getTableStyleElements().get(wholeTableElementIndex);
Style wholeTableStyle = workbook.createStyle();
BorderCollection borders = wholeTableStyle.getBorders();
Border borderTop = borders.getByBorderType(BorderType.TOP_BORDER);
borderTop.setLineStyle(CellBorderType.THIN);
borderTop.setColor(Color.getBlack());
Border borderBottom = borders.getByBorderType(BorderType.BOTTOM_BORDER);
borderBottom.setLineStyle(CellBorderType.THIN);
borderBottom.setColor(Color.getBlack());
Border borderLeft = borders.getByBorderType(BorderType.LEFT_BORDER);
borderLeft.setLineStyle(CellBorderType.THIN);
borderLeft.setColor(Color.getBlack());
Border borderRight = borders.getByBorderType(BorderType.RIGHT_BORDER);
borderRight.setLineStyle(CellBorderType.THIN);
borderRight.setColor(Color.getBlack());
wholeTableElement.setElementStyle(wholeTableStyle);
// Schritt 3: Ein GrandTotalRow-Element hinzufügen und eine fette rote Schriftart anwenden
int grandTotalElementIndex = tableStyle.getTableStyleElements().add(TableStyleElementType.GRAND_TOTAL_ROW);
TableStyleElement grandTotalElement = tableStyle.getTableStyleElements().get(grandTotalElementIndex);
Style grandTotalStyle = workbook.createStyle();
grandTotalStyle.getFont().setBold(true);
grandTotalStyle.getFont().setColor(Color.getRed());
grandTotalElement.setElementStyle(grandTotalStyle);
// Schritt 4: Den benutzerdefinierten Stil nach Namen anwenden (NICHT über PivotTableStyleType, das für integrierte Voreinstellungen ist)
pivotTable.setPivotTableStyleName("CustomPivotStyle");
workbook.save("output.xlsx");
```

## **Anwenden eines Stils auf jede Pivot-Zelle mit FormatAll**
`PivotTable.formatAll(Style)` ist eine Verknüpfung, die ein einzelnes `Style`-Objekt auf jede Zelle der Pivot-Tabelle anwendet, einschließlich des Datenbereichs, der Zeilen- und Spalten-Header sowie der Summen. Was auch immer zuvor über `PivotTableStyleType` oder `PivotTableStyleName` festgelegt wurde, wird überschrieben.

{{% alert color="primary" %}}
`FormatAll` überschreibt sowohl `PivotTableStyleType` als auch `PivotTableStyleName`. Verwenden Sie es nur, wenn ein einheitliches, designunabhängiges Erscheinungsbild über die gesamte Pivot-Tabelle hinweg erforderlich ist.
{{% /alert %}}

Das folgende Beispiel erstellt einen `Style` mit gelber Vollfüllung, fett formatierter dunkelblauer Schriftart und dünnen schwarzen Rändern auf allen Seiten, wendet ihn dann mit `formatAll` an und speichert als `.xlsx`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
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
int pivotIndex = worksheet.getPivotTables().add("A1:C10", "E3", "Pivot1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);
// Pivot-Felder zuweisen: Fruit -> Zeilenbereich, Year -> Spaltenbereich, Amount -> Datenbereich
pivotTable.addFieldToArea(PivotFieldType.ROW, "Fruit");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
// Einen Stil erstellen, der auf jede Zelle der Pivot-Tabelle angewendet wird
Style style = workbook.createStyle();
style.setForegroundColor(Color.getYellow());
style.setPattern(BackgroundType.SOLID);
style.getFont().setBold(true);
style.getFont().setColor(Color.getDarkBlue());
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.TOP_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.BOTTOM_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.LEFT_BORDER).setColor(Color.getBlack());
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN);
style.getBorders().getByBorderType(BorderType.RIGHT_BORDER).setColor(Color.getBlack());
// FormatAll anwenden: erzwingt diesen einzelnen Stil auf jede Zelle der Pivot-Tabelle,
// und überschreibt jeden zuvor gesetzten PivotTableStyleType / PivotTableStyleName
pivotTable.formatAll(style);
// Arbeitsmappe im modernen .xlsx-Format speichern
workbook.save("output.xlsx");
```

## **Welche Stil-API sollte ich verwenden?**
Die Wahl der Stil-API hängt vom Dateiformat ab, in dem Sie speichern. Verwenden Sie die folgende Tabelle als Kurzreferenz.
| Zieldateiformat | Zu verwendende API | Hinweise |
|---|---|---|
| `.xls` (Legacy) | `PivotTable.AutoFormatType` | Werte aus `com.aspose.cells.PivotTableAutoFormatType` (z. B. `REPORT_1`–`REPORT_10`, `CLASSIC`, `TABLE_1`–`TABLE_10`). Wird beim Speichern in modernen Formaten ignoriert. |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, integrierter Stil) | `PivotTable.PivotTableStyleType` | Werte aus `com.aspose.cells.PivotTableStyleType` (helle/dunkle Designs, einschließlich Excel 2017-Ergänzungen). |
| `.xlsx` / `.xlsm` / `.xlsb` (modern, benutzerdefinierter Stil) | `PivotTable.PivotTableStyleName` + `Worksheets.TableStyles.addPivotTableStyle(...)` | Verwenden Sie dies, wenn die integrierten Voreinstellungen nicht ausreichen. Konfigurieren Sie über `TableStyleElement.setElementStyle(...)`. |
| Beliebiges Format (einheitliche Überschreibung) | `PivotTable.formatAll(Style)` | Verknüpfung, die jede andere Stileinstellung in der gesamten Pivot-Tabelle überschreibt. |
Im Zweifelsfall speichern Sie als `.xlsx` und verwenden Sie `PivotTableStyleType` für integrierte Designs oder `PivotTableStyleName` für benutzerdefinierte Designs.

{{< app/cells/assistant language="java" >}}