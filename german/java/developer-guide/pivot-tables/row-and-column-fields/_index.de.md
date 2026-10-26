---
title: Hinzufügen von Zeilen- und Spaltenfeldern zu Pivot-Tabellen in Aspose.Cells for Java
description: Erfahren Sie, wie Sie Basisfelder zu den Zeilen- und Spaltenbereichen einer Pivot-Tabelle hinzufügen und Pivot-Feld-Zwischensummen mit PivotField.setSubtotals in Aspose.Cells for Java steuern.
linktitle: Zeilen- und Spaltenfelder
keywords: Aspose.Cells, Java, Pivot-Tabelle, Zeilenfeld, Spaltenfeld, PivotField, setSubtotals, PivotFieldSubtotalType, Zwischensummen
type: docs
weight: 220
url: /de/java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**
Die Methode `PivotTable.addFieldToArea(int fieldType, String fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Pivot-Bereiche. Das Argument `fieldType` akzeptiert einen der folgenden `PivotFieldType`-Werte.
- `ROW` — vertikal auf der linken Seite angeordnete Felder
- `COLUMN` — horizontal oben angeordnete Felder
- `DATA` — Felder, deren Werte aggregiert werden
- `PAGE` — als Berichtsfilter verwendete Felder
Die Reihenfolge der Feldverschachtelung ist wichtig. Das Hinzufügen von `Category` zuerst zum Zeilenbereich und dann `Item` erzeugt eine Pivot-Tabelle, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Das Umkehren der Reihenfolge kehrt die Hierarchie um.

## **Zwischensummen der Pivot-Felder**
Die Methode `PivotField.setSubtotals(int subtotalType, boolean shown)` steuert, welche Zwischensummenzeilen für ein Pivot-Feld angezeigt werden. Jeder Aufruf aktiviert unabhängig einen einzelnen Zwischensummen-Typ. Wird `shown = true` übergeben, wird die Zwischensumme angezeigt, während `shown = false` sie ausblendet. Da jeder Aufruf nur einen Typ betrifft, wird durch mehrfaches Aufrufen der Methode mit unterschiedlichen `subtotalType`-Werten eine benutzerdefinierte Teilmenge von Zwischensummen erstellt.
Die Enumeration `PivotFieldSubtotalType` definiert die verfügbaren Zwischensummenarten.
- `AUTOMATIC` — Aspose.Cells wählt die Standardauswahl (in der Regel `SUM` für numerische Felder)
- `NONE` — unterdrückt jede Zwischensummenzeile
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Zwischensummen werden nur dann gerendert, wenn zwei oder mehr Pivot-Felder im Zeilenbereich (oder im Spaltenbereich) vorhanden sind. Ein einzelnes Feld hat nichts Sinnvolles zum Zusammenfassen, daher haben `setSubtotals`-Aufrufe in diesem Fall keine sichtbare Wirkung. Dieser Artikel platziert daher in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Zwischensummengrenze zwischen jeder `Category`-Gruppe sichtbar ist.
{{% /alert %}}

## **Szenario 1 — Automatische (Standard-)Zwischensummen**
Wenn Sie `setSubtotals` überhaupt nicht aufrufen, wendet Aspose.Cells die Auswahl `AUTOMATIC` auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten explizit durch den Aufruf von `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` auf dem äußeren Zeilenfeld `Category`.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
PivotTable pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Szenario 2 — Unterdrücken aller Zwischensummen (Keine)**
Der Aufruf `setSubtotals(PivotFieldSubtotalType.NONE, true)` entfernt jede Zwischensummenzeile aus der Pivot-Tabelle, sodass nur die Feldzeilen und die Gesamtsumme am unteren Rand übrig bleiben. Dies ist nützlich, wenn Sie die rohen gruppierten Daten ohne Zusammenfassungszeilen wünschen.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}
Object[][] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};
for (int i = 0; i < data.length; i++)
{
    for (int j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}
PivotTable pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Szenario 3 — Benutzerdefinierte Zwischensummen-Teilmenge (Summe + Durchschnitt)**
Sie sind nicht auf einen einzelnen Zwischensummen-Typ beschränkt. Jeder `setSubtotals`-Aufruf wirkt unabhängig auf einen Typ, sodass das zweimalige Aufrufen der Methode — einmal mit `SUM` und einmal mit `AVERAGE` — eine benutzerdefinierte Teilmenge von zwei Zwischensummenzeilen für jede `Category`-Gruppe erzeugt.

```java
import com.aspose.cells.*;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");
worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");
worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);
worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);
worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);
worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);
worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);
worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);
worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);
worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);
PivotTableCollection pivotTables = worksheet.getPivotTables();
PivotTable pivotTable = pivotTables.add("A1:D9", 2, 5);
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
PivotField categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Zusammenfassung**
Die drei Szenarien unterscheiden sich lediglich in den `setSubtotals`-Aufrufen. Alles andere — der Datensatz, die Felder und die Bereiche, denen sie zugeordnet sind — ist identisch, was die Layouts direkt miteinander vergleichbar macht.
- **Platzieren von Feldern.** `PivotTable.addFieldToArea(PivotFieldType.ROW, fieldName)` verschiebt eine Quellspalte in einen Bereich. Innerhalb eines Bereichs bestimmt die Reihenfolge der Aufrufe die Anzeigereihenfolge, sodass der erste Aufruf die äußerste Gruppe bildet. Subsummen benötigen zwei oder mehr Felder im selben Bereich: Bei einem einzelnen Feld gibt es zwischen den Gruppen keine Daten, für die eine Subsumme gebildet werden könnte.
- **Szenario 1 — automatische Subsummen.** Wenn `setSubtotals` nicht aufgerufen wird, trifft Excel die Entscheidung selbst und wendet automatisch seine eigene Standard-Subsumme auf numerische Felder an. Ein Aufruf von `setSubtotals` mit `PivotFieldSubtotalType.AUTOMATIC` dokumentiert diese Entscheidung explizit, anstatt sie implizit zu belassen.
- **Szenario 2 — keine Subsummen.** Ein Aufruf von `setSubtotals` mit `PivotFieldSubtotalType.NONE` deaktiviert die Standard-Subsumme, sodass das Pivot-Table die Zeilen des Felds und die Gesamtsumme behält, aber die Zwischenseiten mit den Subsummen entfernt, die Excel andernfalls dazwischen einfügen würde.
- **Szenario 3 — eine ausgewählte Teilmenge.** Jeder Aufruf schaltet genau einen Subsummentyp um, und die Aufrufeakkumulieren sich, anstatt sich gegenseitig zurückzusetzen. Ein einmaliger Aufruf mit `PivotFieldSubtotalType.SUM` und ein weiterer Aufruf mit `PivotFieldSubtotalType.AVERAGE` lassen somit beide aktiviert, und das Pivot-Table zeigt sowohl eine Subsumme (Summe) als auch eine Subsumme (Durchschnitt) sowie die Gesamtsumme an.

{{% alert color="primary" %}}
Nichts an Subsummen ist auf den Zeilenbereich beschränkt. Die gleichen `setSubtotals`-Aufrufe für ein Feld aus `PivotTable.ColumnFields` erzeugen dieselben drei Layouts entlang der Spaltenachse, da die Einstellung zum Pivot-Feld selbst gehört und nicht zur Achse, auf der es sich befindet.
{{% /alert %}}

## **Verwandte Artikel**
- [Seitenfelder in Pivot-Tabellen](/cells/de/java/add-page-field-in-pivot-table/)
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells for Java](/cells/de/java/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/java/apply-style-to-pivot-table/)java

{{< app/cells/assistant language="java" >}}