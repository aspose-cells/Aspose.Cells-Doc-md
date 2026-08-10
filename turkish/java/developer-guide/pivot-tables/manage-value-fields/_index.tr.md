---
title: Aspose.Cells for Java'da Değer Alanları
linktitle: Aspose.Cells for Java'da Değer Alanları
description: Aspose.Cells for Java'da bir özet tablonun veri bölgesine temel alanların nasıl ekleneceğini, PivotField.Function ile özet işlevinin nasıl değiştirileceğini ve değer alanının Satır veya Sütun eksenine nasıl yerleştirileceğini öğrenin.
keywords: Aspose.Cells, Java, özet tablo, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /tr/java/manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Veri Bölgesine Alan Ekleme
Veri (değer) bölgesine temel alan eklemek, bir özet tablonun kaynak verilerinizi nasıl topladığını şekillendirmedeki ilk adımdır. Aspose.Cells, `PivotFieldType.DATA` sabitini ve kaynak-sütun adını kabul eden bir aşırı yükleme olan `PivotTable.addFieldToArea(PivotFieldType, String)` öğesini kullanıma sunar. Bir alan veri bölgesine eklendiğinde, API onu alanların eklenme sırasıyla `PivotTable.getDataFields()` koleksiyonu aracılığıyla kullanıma sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.SUM` ile özetlenirken, sayısal olmayan bir sütun `COUNT` varsayılanına sahip olur.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// A1:D1 aralığındaki başlıklar
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// j üzerinde dallanma yapan iç içe döngüler kullanarak A2:D9 veri satırları
for (int i = 1; i <= 8; i++)
{
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 worksheet.getCells().get(i, j).putValue(i <= 4 ? "Fruit" : "Vegetable");
 break;
 case 1:
 if (i == 1 || i == 2) worksheet.getCells().get(i, j).putValue("Apple");
 else if (i == 3 || i == 4) worksheet.getCells().get(i, j).putValue("Banana");
 else if (i == 5 || i == 6) worksheet.getCells().get(i, j).putValue("Carrot");
 else worksheet.getCells().get(i, j).putValue("Daikon");
 break;
 case 2:
 worksheet.getCells().get(i, j).putValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) worksheet.getCells().get(i, j).putValue(100);
 else if (i == 2) worksheet.getCells().get(i, j).putValue(150);
 else if (i == 3) worksheet.getCells().get(i, j).putValue(80);
 else if (i == 4) worksheet.getCells().get(i, j).putValue(90);
 else if (i == 5) worksheet.getCells().get(i, j).putValue(50);
 else if (i == 6) worksheet.getCells().get(i, j).putValue(60);
 else if (i == 7) worksheet.getCells().get(i, j).putValue(40);
 else worksheet.getCells().get(i, j).putValue(45);
 break;
 }
 }
}

// F3 konumunda PivotTable1 adlı özet tablo ekle
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// Pivot düzeni: Satır olarak Kategori ve Öğe, Sütun olarak Yıl, veri alanı olarak Tutar
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## Özet İşlevini Değiştirme
Veri bölgesine yerleştirilen her alan dahili olarak bir `PivotField` örneği olarak sarılır ve `getFunction()` özelliği `ConsolidationFunction` enum'undan bir değer döndürür. Aynı `setFunction(...)` ayarlayıcısı, `SUM`, `COUNT`, `AVERAGE`, `MAX`, `MIN`, `PRODUCT`, `STD_DEV`, `STD_DEVP`, `VAR` ve `VARP` dahil mevcut toplamalar arasında geçiş yapmanızı sağlar.
{{% alert color="primary" %}}
`Function` değiştirmek yalnızca toplamayı etkiler, kaynak sütun değişmez.
{{% /alert %}}
Bu nedenle, tek bir özet tablo içinde bir veri alanını `SUM` olarak bırakırken aynı kaynak sütunu hedefleyen ancak `COUNT` veya `AVERAGE` kullanan ikinci bir veri alanı ekleyebilirsiniz.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");

pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

PivotField countField = pivotTable.getDataFields().get(1);
countField.setFunction(ConsolidationFunction.COUNT);

pivotTable.calculateData();
workbook.save("output_function.xlsx");
```

## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme
Bir özet tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells, `PivotTable.getValuesField()` adı verilen ek bir sanal alanı kullanıma sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Bunu temel bir özet alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz; bu, birden fazla ölçüyü yan yana düzenlemek için kullanışlıdır.
{{% alert color="primary" %}}
Hiç değer alanı yoksa veya yalnızca bir tane varsa `PivotTable.getValuesField()` çalışmaz.
{{% /alert %}}
Aşağıdaki senaryolar, aynı özet tablo yapısına karşı yukarıda açıklanan her bir yeteneği gösteren üç uçtan uca örnekten geçer.

```java
import com.aspose.cells.*;
import com.aspose.cells.pivot.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

String[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.length; j++) {
 worksheet.getCells().get(0, j).putValue(headers[j]);
}

Object[][] data = {
 { "Fruit", "Apple", 2020, 100 },
 { "Fruit", "Apple", 2021, 150 },
 { "Fruit", "Banana", 2020, 80 },
 { "Fruit", "Banana", 2021, 90 },
 { "Vegetable", "Carrot", 2020, 50 },
 { "Vegetable", "Carrot", 2021, 60 },
 { "Vegetable", "Daikon", 2020, 40 },
 { "Vegetable", "Daikon", 2021, 45 }
};

for (int i = 0; i < data.length; i++) {
 for (int j = 0; j < data[i].length; j++) {
 worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
 }
}

int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");
pivotTable.getDataFields().get(1).setFunction(ConsolidationFunction.COUNT);

pivotTable.addFieldToArea(PivotFieldType.COLUMN, pivotTable.getValuesField());

pivotTable.calculateData();
workbook.save("output_plot.xlsx");
```

{{< app/cells/assistant language="java" >}}