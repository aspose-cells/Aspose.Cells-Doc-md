---
title: Zeilen- und Spaltenfelder zu einer PivotTable in Aspose.Cells für .NET hinzufügen
linktitle: Zeilen- und Spaltenfelder
description: Erfahren Sie, wie Sie Basisfelder zu den Zeilen- und Spaltenbereichen einer PivotTable hinzufügen und PivotField-Zwischensummen mit PivotField.setSubtotals in Aspose.Cells for Java steuern.
keywords: Aspose.Cells, Java, PivotTable, Zeilenfeld, Spaltenfeld, PivotField, setSubtotals, PivotFieldSubtotalType, Zwischensummen
type: docs
weight: 220
url: /de/java/pivot-table-add-row-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Hinzufügen eines Felds zum Zeilen- oder Spaltenbereich**

Die Methode `PivotTable.addFieldToArea(int fieldType, String fieldName)` verschiebt ein Basisfeld aus den Quelldaten in einen der vier Pivot-Bereiche. Das Argument `fieldType` akzeptiert einen der folgenden `PivotFieldType`-Werte.

- `ROW` — Felder, die vertikal auf der linken Seite platziert werden
- `COLUMN` — Felder, die horizontal über die Oberseite platziert werden
- `DATA` — Felder, deren Werte aggregiert werden
- `PAGE` — Felder, die als Berichtsfilter verwendet werden

Nachdem Felder hinzugefügt wurden, können Sie über die Eigenschaften `PivotTable.getRowFields()` und `PivotTable.getColumnFields()` darauf zugreifen. Jede Eigenschaft gibt eine `PivotFieldCollection` zurück. Das Feld mit Index 0 von `RowFields` ist das äußerste Zeilenfeld, und nachfolgende Indizes stellen Felder dar, die darin verschachtelt sind. Die gleiche Indizierungskonvention gilt für `ColumnFields`.

Die Verschachtelungsreihenfolge der Felder ist wichtig. Wenn Sie zuerst `Category` zum Zeilenbereich und dann `Item` hinzufügen, entsteht eine Pivot-Tabelle, deren äußere Gruppierung `Category` und deren innere Gruppierung `Item` ist. Eine Umkehrung der Reihenfolge kehrt die Hierarchie um.

## **Zwischensummen von Pivot-Feldern**

Die Methode `PivotField.setSubtotals(int subtotalType, boolean shown)` steuert, welche Zwischensummenzeilen für ein Pivot-Feld angezeigt werden. Jeder Aufruf schaltet einen einzelnen Zwischensummentyp unabhängig um. Die Übergabe von `shown = true` zeigt die Zwischensumme an, während `shown = false` sie ausblendet. Da jeder Aufruf nur einen Typ betrifft, können durch mehrere Aufrufe der Methode mit unterschiedlichen `subtotalType`-Werten benutzerdefinierte Teilmengen von Zwischensummen erstellt werden.

Die Enum `PivotFieldSubtotalType` definiert die verfügbaren Arten von Zwischensummen.

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
Zwischensummen werden nur angezeigt, wenn sich zwei oder mehr Pivot-Felder im Zeilenbereich (oder im Spaltenbereich) befinden. Ein einzelnes Feld hat keine sinnvolle Zwischensumme, daher haben `setSubtotals`-Aufrufe in diesem Fall keine sichtbare Wirkung. Dieser Artikel platziert daher in jedem Beispiel zwei Zeilenfelder (`Category` außen, `Item` innen), damit die Zwischensummengrenze zwischen jeder `Category`-Gruppe sichtbar ist.
{{% /alert %}}

## **Szenario 1 — Automatische (Standard-)Zwischensummen**

Wenn Sie `setSubtotals` überhaupt nicht aufrufen, wendet Aspose.Cells die Auswahl `AUTOMATIC` auf numerische Felder an. Das folgende Beispiel bestätigt dieses Verhalten explizit, indem `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` auf dem äußeren Zeilenfeld `Category` aufgerufen wird.

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

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

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

Der Aufruf von `setSubtotals(PivotFieldSubtotalType.NONE, true)` entfernt jede Zwischensummenzeile aus der Pivot-Tabelle und lässt nur die Feldzeilen und die Gesamtsumme am Ende übrig. Dies ist nützlich, wenn Sie die rohen gruppierten Daten ohne irgendwelche Zusammenfassungszeilen wünschen.

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

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

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

Sie sind nicht auf einen einzelnen Zwischensummentyp beschränkt. Jeder `setSubtotals`-Aufruf wirkt unabhängig auf einen Typ. Wenn Sie die Methode also zweimal aufrufen — einmal mit `SUM` und einmal mit `AVERAGE` — erzeugen Sie eine benutzerdefinierte Teilmenge von zwei Zwischensummenzeilen für jede `Category`-Gruppe.

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
int pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

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

Die drei oben genannten Szenarien verwenden denselben Datensatz und dieselbe PivotTable-Struktur. Der einzige Unterschied zwischen ihnen ist der `setSubtotals`-Aufruf, der auf das äußere Zeilenfeld `Category` angewendet wird. Denken Sie an die Zwei-Felder-Regel: Ein einzelnes Feld in einem Bereich hat keine Zwischensumme. Platzieren Sie daher immer mindestens zwei Felder im Zeilen- oder Spaltenbereich, wenn Sie möchten, dass `setSubtotals` eine sichtbare Wirkung hat.

## **Verwandte Artikel**

- [Seitenfelder in Pivot-Tabellen](/cells/de/java/add-page-field-in-pivot-table/)
- [Aktualisieren von Pivot-Tabellen in Aspose.Cells for Java](/cells/de/java/refresh-pivot-table/)
- [Anwenden von Stilen auf Pivot-Tabellen](/cells/de/java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
