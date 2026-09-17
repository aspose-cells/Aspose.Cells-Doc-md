---
title: Seitenfeldlayout in Pivot-Tabelle ändern
linktitle: Seitenfeldlayout in Pivot-Tabelle ändern
description: Erfahren Sie, wie Sie mit Aspose.Cells for Java das Layout des Seitenfeldbereichs in einer Pivot-Tabelle steuern, einschließlich der Anzeigereihenfolge, der Wrap-Anzahl und der Feldreihenfolge der Seitenfelder am oberen Rand der Pivot-Tabelle.
keywords: Aspose.Cells, Java-Bibliothek, Tabellenkalkulation, Pivot-Tabelle, Seitenfeld, Seitenfeldreihenfolge, Seitenfeld-Wrap-Anzahl, Seitenfeld verschieben
type: docs
weight: 191
url: /de/java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Dieser Artikel ist eine Fortsetzung des Themas **Seitenfeld in Pivot-Tabelle hinzufügen**. Er zeigt, wie Sie das Layout des Seitenfeldbereichs steuern – den Streifen mit Filtersteuerelementen am oberen Rand einer Pivot-Tabelle –, einschließlich der Anzeigereihenfolge, der Wrap-Anzahl und der Umordnung der Felder.
{{% /alert %}}

## **Einführung**
Eine Pivot-Tabelle in Microsoft Excel verfügt über einen dedizierten **Seitenfeldbereich**, der oberhalb des Zeilen-/Spalten-/Datenkörpers der Tabelle angeordnet ist. Dieser Bereich wird als Streifen mit Dropdown-Filtersteuerelementen dargestellt (eines pro Seitenfeld) und ist das Element, auf das Endbenutzer klicken, um die Pivot-Tabelle nach Kriterien wie Jahr oder Region aufzuteilen. Aspose.Cells modelliert diesen Bereich über die Sammlung `pivotTable.getPageFields()` und stellt drei Eigenschaften bereit, die die visuelle Anordnung des Streifens steuern:
- `pivotTable.getPageFieldOrder()` (ein `Aspose.Cells.PrintOrderType`-Wert) legt fest, ob zusätzliche Seitenfelder *neben* den vorhandenen oder *unterhalb* davon platziert werden.
- `pivotTable.getPageFieldWrapCount()` legt fest, wie viele Seitenfelder pro Zeile oder Spalte platziert werden, bevor ein Umbruch erfolgt.
- `pivotTable.getPageFields().move(currIndex, destIndex)` ordnet die Seitenfelder neu, ohne den Anordnungsmodus zu ändern.
Dieser Artikel führt durch drei Codebeispiele, die jede dieser Operationen an einem gemeinsamen Datensatz demonstrieren, sodass Sie die resultierenden Layouts direkt nebeneinander vergleichen können.

## **Quelldaten**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Alle acht Zeilen sind in jedem Codebeispiel in identischer Reihenfolge befüllt, sodass sich die Quelldaten zwischen den Szenarien niemals unterscheiden – nur die Layout-Eigenschaften der Seitenfelder tun dies.

## **Beispiel 1: Über, dann runter**
Im ersten Szenario konfigurieren wir die beiden Seitenfelder (`Year`, `Region`) so, dass sie **nebeneinander in einer einzigen Zeile** am oberen Rand der Pivot-Tabelle erscheinen. Wir weisen `Fruit` der Zeilenachse zu, setzen `Year` zuerst und `Region` als zweites auf die Seitenachse (die Reihenfolge der `addFieldToArea`-Aufrufe bestimmt den Startindex), fügen `Amount` (Summe) als Datenfeld hinzu und setzen anschließend `pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` mit `pivotTable.setPageFieldWrapCount(2)`. Mit `OVER_THEN_DOWN` und einer Wrap-Anzahl von 2 werden die beiden Seitenfelder horizontal nebeneinander in einer einzigen Zeile am oberen Rand der Pivot-Tabelle angeordnet, sodass der Streifen eine Zeile mit der Breite zwei einnimmt.

```java
import com.aspose.cells.*;
import java.io.File;
String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();
Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();
Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();
// Kopfzeilen (Zeile 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// Zeile 1: Apfel, 2022, Nord, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// Zeile 2: Apfel, 2023, Nord, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// Zeile 3: Banane, 2022, Süd, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// Zeile 4: Banane, 2023, Süd, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// Zeile 5: Kirsche, 2022, Ost, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// Zeile 6: Kirsche, 2023, Ost, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// Zeile 7: Traube, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// Zeile 8: Traube, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// PivotTableReport-Blatt hinzufügen
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();
// Pivot-Tabelle erstellen, die aus PivotData!A1:D9 stammt und bei A1 auf PivotTableReport platziert wird
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);
// Felder hinzufügen
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // Frucht
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // Jahr
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // Region
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // Betrag
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);
// Layout des Seitenfeldbereichs konfigurieren: Seitenfelder zuerst horizontal anordnen, nach jeweils 2 umbrechen
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
// Aktualisieren und berechnen
pivotTable.calculateData();
// Speichern
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```

## **Beispiel 2: Runter, dann über**
In diesem Beispiel platzieren wir `Fruit` auf der Zeilenachse, `Year` und `Region` auf der Seitenachse (mit `Year` zuerst) und `Amount` (Summe) als Datenfeld – genau wie in Beispiel 1. Anschließend setzen wir `pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` und `pivotTable.setPageFieldWrapCount(2)`. Mit `DOWN_THEN_OVER` und einer Wrap-Anzahl von 2 werden die beiden Seitenfelder vertikal gestapelt – `Year` oben, `Region` direkt darunter – und bilden so eine einzelne Spalte am oberen Rand der Pivot-Tabelle. Der Streifen nimmt daher zwei Zeilen mit der Breite eins ein, im Gegensatz zu Beispiel 1.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
int pivotReportIdx = workbook.getWorksheets().add();
Worksheet pivotReport = workbook.getWorksheets().get(pivotReportIdx);
pivotReport.setName("PivotTableReport");
String[] headers = new String[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}
Object[][] data = new Object[][]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};
for (int r = 0; r < data.length; r++)
{
    for (int c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
int idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
PivotTable pivotTable = pivotReport.getPivotTables().get(idx);
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Beispiel 3: Ein Seitenfeld verschieben**
Im dritten Szenario behalten wir diesen Datensatz und diese Feldzuordnung bei, legen ein neutrales Layout fest (`OVER_THEN_DOWN` mit Wrap-Anzahl `2`) und demonstrieren anschließend die Operation `pageFields.move`. Der Aufruf `move(0, 1)` verschiebt das Seitenfeld an Index 0 (`Year`) an Position 1, und das Seitenfeld, das sich an Position 1 befand (`Region`), rückt auf Position 0. Nach diesem Aufruf ist `Region` das erste Seitenfeld und `Year` das zweite. Der Umbruch- und der Anordnungsmodus bleiben unverändert, sodass der Streifen weiterhin horizontal nebeneinander dargestellt wird – nur die Reihenfolge der beiden Dropdowns wurde vertauscht.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");
dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);
dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);
dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);
dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);
dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);
dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);
dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);
dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);
Worksheet pivotSheet = workbook.getWorksheets().add("PivotTableReport");
int pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.getPivotTables().get(pivotIdx);
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **Verwandte Artikel**
- [Seitenfeld in Pivot-Tabelle hinzufügen](/cells/de/java/add-page-field-in-pivot-table/) – die übergeordnete Seite, die beschreibt, wie Seitenfelder zu einer Pivot-Tabelle hinzugefügt werden.
- [Zeilen- und Spaltenfelder in Pivot-Tabelle](/cells/de/java/row-and-column-fields/) – behandelt die Zuordnung von Feldern zu den Zeilen- und Spaltenachsen und ergänzt die hier gezeigten Arbeiten an der Seitenachse.
- [Wertfelder in Pivot-Tabelle verwalten](/cells/de/java/manage-value-fields/) – beschreibt, wie der Daten- (Wert-) Bereich konfiguriert wird, einschließlich der in diesem Artikel verwendeten `Sum`-Aggregation.
- [Pivot-Tabelle aktualisieren](/cells/de/java/refresh-pivot-table/) – erläutert `refreshData()` und `calculateData()`, die nach dem Neuordnen der Seitenfelder erforderlich sind.
- [Stil auf Pivot-Tabelle anwenden](/cells/de/java/apply-style-to-pivot-table/) – zeigt, wie die gerenderte Pivot-Tabelle formatiert wird, nachdem der Seitenfeldstreifen angeordnet wurde.

{{< app/cells/assistant language="java" >}}