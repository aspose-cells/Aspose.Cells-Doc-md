---
title: Top 10 in PivotTables anzeigen oder filtern
linktitle: Top 10 in PivotTables anzeigen oder filtern
description: Erfahren Sie, wie Sie mit Aspose.Cells for Java nur die höchst- oder niedrigstplatzierten Elemente eines Pivot-Felds anzeigen. Dieser Artikel behandelt die Methode Top10AutoShow in Excel 97-2003, das Lesen von Optionen mit Top10AutoShowSettings sowie den Top-10-Filter in Excel 2007-365 über FilterTop10.
keywords: Aspose.Cells, Java, PivotTable, Top 10, AutoShow, top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, filterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /de/java/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Mögliche Anwendungsfälle**
Eine PivotTable, die jedes Element eines Zeilenfelds auflistet, kann schwer lesbar sein, wenn das Feld Dutzende Elemente enthält. Ein Top-10-Bericht behält nur die höchst- oder niedrigstplatzierten Elemente und eignet sich daher ideal für Berichte mit Rangfolge – „die 5 umsatzstärksten Produkte“ oder „die 3 Regionen mit der niedrigsten Verkaufsanzahl“. Aspose.Cells unterstützt hierfür zwei Mechanismen, die den beiden Generationen von Microsoft Excel entsprechen.
- **Excel 97-2003 AutoShow** – die Methode `PivotField.top10AutoShow()`. Dies ist die klassische Einstellung zum Anzeigen der obersten bzw. untersten N Elemente, die direkt am Pivot-Feld gespeichert wird. Sie funktioniert in allen alten und neuen Excel-Versionen, da sie Teil des ursprünglichen PivotTable-Formats ist.
- **Excel 2007-365 Top-10-Filter** – die Methode `PivotField.filterTop10()`. Dies ist der moderne Top-10-Wertfilter, der im Feldmenü unter „Wertfilter“ zu finden ist. Er wird als `PivotFilter`-Objekt gespeichert, das dem Feld zugeordnet ist, und bietet eine Rangfolge nach Elementanzahl oder Prozentwert.

## **Top 10 in Excel 97-2003 anzeigen (top10AutoShow)**
Das klassische AutoShow wird mit einem einzigen Aufruf der Methode `PivotField.top10AutoShow(boolean isAutoShow, boolean isTop, int count, int rankBy)` konfiguriert:
- `isAutoShow` – aktiviert oder deaktiviert die AutoShow-Einstellung am Feld.
- `isTop` – `true` behält die höchstplatzierten Elemente bei (Oben), `false` die niedrigstplatzierten (Unten).
- `count` – die Anzahl der beizubehaltenden Elemente, beispielsweise 10 für einen klassischen Top-10-Bericht.
- `rankBy` – der nullbasierte Index des **Datenfelds**, dessen Werte die Rangfolge der Elemente bestimmen. Geben Sie -1 an, um die Elemente nach dem Feld selbst einzustufen.
Die Rangfolge kann durch ein Wertfeld oder durch das Feld selbst bestimmt werden. Es gibt zwei naheliegende Varianten, die nachfolgend dargestellt werden.

### **Nach einem Wertfeld einstufen**
Stufen Sie die Elemente des Zeilenfelds nach einem herkömmlichen Wertfeld wie „Summe der Verkäufe“ ein. Das folgende Beispiel erstellt eine PivotTable mit einem Zeilenfeld (`Sport`) und einem Datenfeld (`Sales`) und zeigt anschließend die zwei umsatzstärksten Sportarten. `rankBy` ist 0, da „Summe der Verkäufe“ das Datenfeld mit dem Index 0 ist.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Die Top-2-Elemente nach "Sum of Sales" anzeigen (Index 0 des Datenfelds)
sportField.top10AutoShow(true, true, 2, 0);
pivotTable.calculateData();
workbook.save("output-top10-by-value-field.xlsx");
```

### **Nach dem Feld selbst einstufen**
Ein Feld kann auch nach sich selbst eingestuft werden – geben Sie -1 als `rankBy` an. Für diese Variante ist kein zusätzliches Datenfeld erforderlich; das Feld muss lediglich im Zeilen- oder Spaltenbereich liegen. Das folgende Beispiel zeigt die drei Sportarten mit den niedrigsten Werten, wenn die Rangfolge durch das Feld selbst bestimmt wird. Beim Speichern dieser Einstellung wird das Attribut `rankBy` aus dem XML der PivotTable weggelassen, da -1 der Standardwert des Formats ist. `Top10AutoShowSettings.getRankBy()` liest -1 zurück.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Die unteren 3 Elemente anzeigen, die nach dem Feld selbst sortiert sind (rankBy = -1)
sportField.top10AutoShow(true, false, 3, -1);
pivotTable.calculateData();
workbook.save("output-top10-by-field-itself.xlsx");
```

## **Aktuelle Optionen lesen (Top10AutoShowSettings)**
Die Methode `PivotField.getTop10AutoShowSettings()` gibt ein `PivotFieldTop10AutoShowSettings`-Objekt zurück, das die aktuell am Feld gespeicherten AutoShow-Optionen enthält. Verwenden Sie es, um zu prüfen, wie eine vorhandene Arbeitsmappe oder eine gerade konfigurierte PivotTable ihre Elemente darstellt – auch wenn die Arbeitsmappe aus einer Datei geladen wurde.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.getWorksheets().get(0).getPivotTables().get(0);
PivotField sportField = pivotTable.getRowFields().get(0);
PivotFieldTop10AutoShowSettings settings = sportField.getTop10AutoShowSettings();
System.out.println("AutoShow enabled: " + settings.isAutoShow());
System.out.println("Direction: " + (settings.isTop() ? "Top" : "Bottom"));
System.out.println("Item count: " + settings.getAutoShowCount());
System.out.println("Ranking data field index: " + settings.getRankBy());
```

Die vier Eigenschaften bilden die klassischen AutoShow-Attribute ab, die in das XML der PivotTable geschrieben werden (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`), sodass die zurückgelesenen Werte von jeder Excel-Version berücksichtigt werden.

## **Hinweis**

{{% alert color="primary" %}}
- Die direkten `PivotField`-Eigenschaften, die über `isAutoShow()`, `isAscendShow()`, `getAutoShowCount()` und `getAutoShowField()` verfügbar sind, sind als veraltet markiert. Verwenden Sie stattdessen das `Top10AutoShowSettings`-Objekt: `Top10AutoShowSettings.isAutoShow()` ersetzt `PivotField.isAutoShow()`, `Top10AutoShowSettings.isTop()` ersetzt `PivotField.isAscendShow()`, `Top10AutoShowSettings.getAutoShowCount()` ersetzt `PivotField.getAutoShowCount()` und `Top10AutoShowSettings.getRankBy()` ersetzt `PivotField.getAutoShowField()`. Zum Ändern der Einstellungen verwenden Sie die Methode `PivotField.top10AutoShow()`.
- `top10AutoShow` funktioniert mit Zeilen- und Spaltenfeldern. Ein Feld, das ausschließlich im Seiten- beziehungsweise Filterbereich liegt, kann auf diese Weise nicht eingestuft werden, da seine Elemente nicht im PivotTable-Körper angeordnet sind.
{{% /alert %}}

## **Excel 2007-365: Top-10-Filter (filterTop10)**
Moderne Excel-Versionen bieten Top 10 im Feldmenü als Wertfilter („Wertfilter“, „Top 10...“) an. Aspose.Cells bildet dies mit der Methode `PivotField.filterTop10(int valueFieldIndex, PivotFilterType type, boolean isTop, int itemCount)` ab, die den erstellten `PivotFilter` zurückgibt:
- `valueFieldIndex` – der nullbasierte Index des Datenfelds, dessen aggregierte Werte die Rangfolge der Elemente bestimmen.
- `type` – legt fest, was `itemCount` bedeutet. `PivotFilterType.COUNT` behält eine feste Anzahl von Elementen bei (die Option „Elemente“ im Dialog). `PivotFilterType.PERCENT` behält einen bestimmten Prozentsatz der Elemente bei, sodass `itemCount` selbst der Prozentsatz ist – der Wert 30 behält die besten 30 Prozent. `PivotFilterType.SUM` bestimmt die Rangfolge anhand der kumulierten Abdeckung der Werte.
- `isTop` – `true` für Oben, `false` für Unten.
- `itemCount` – der Wert N in Top N; seine Einheit hängt von `type` ab.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Sport");
worksheet.getCells().get("B1").putValue("Quarter");
worksheet.getCells().get("C1").putValue("Sales");
String[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
for (String sport : sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.getCells().get(row, 0).putValue(sport);
        worksheet.getCells().get(row, 1).putValue("Qtr" + quarter);
        worksheet.getCells().get(row, 2).putValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:C16", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");
pivotTable.calculateData();
PivotField sportField = pivotTable.getRowFields().get(0);
// Top-10-Filter – die beiden höchsten Elemente nach „Summe von Sales“ beibehalten (Datenfeldindex 0)
sportField.filterTop10(0, PivotFilterType.COUNT, true, 2);
// Prozentbasierter Filter: behalten Sie stattdessen die besten 30 % der Elemente:
// sportField.filterTop10(0, PivotFilterType.PERCENT, true, 30);
pivotTable.getPivotCache().refresh();
pivotTable.calculateData();
workbook.save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`top10AutoShow` und `filterTop10` sind zwei getrennte Funktionen. AutoShow schreibt das klassische `autoShow`-Attribut, das am Pivot-Feld gesetzt wird, und wird von allen Excel-Versionen ab Excel 97 berücksichtigt. `filterTop10` schreibt einen modernen `PivotFilter`-Eintrag, der Excel 2007 oder höher erfordert. Wird eine Arbeitsmappe in einer älteren Excel-Version geöffnet, greift eine PivotTable, die den modernen Filter verwendet, auf die Anzeige aller Elemente zurück. Für Dokumente, die mit Tools für ältere Excel-Versionen kompatibel bleiben müssen, ist `top10AutoShow` vorzuziehen. Für moderne Arbeitsmappen ist `filterTop10` vorzuziehen, da es sich mit den übrigen Wertfiltern kombinieren lässt.
{{% /alert %}}

## **Verwandte Artikel**
- [PivotTables nach Bezeichnung oder Wert filtern](/cells/de/java/filter-by-label-or-value-of-pivot-table/)
- [Zeilen- und Spaltenfelder zur PivotTable hinzufügen](/cells/de/java/pivot-table-add-row-and-column-fields/)
- [Pivot-Felder in der PivotTable gruppieren](/cells/de/java/group-pivot-fields-in-the-pivot-table/)
- [PivotTable aktualisieren](/cells/de/java/refresh-pivot-table/)
- [Seitenfeld zur PivotTable hinzufügen](/cells/de/java/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="java" >}}