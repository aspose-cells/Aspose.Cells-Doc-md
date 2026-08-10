---
title: حقول القيم في Aspose.Cells for Java
linktitle: حقول القيم في Aspose.Cells for Java
description: تعلّم كيفية إضافة الحقول الأساسية إلى منطقة البيانات في الجدول المحوري، وتغيير دالة التلخيص باستخدام PivotField.Function، ورسم حقل القيمة على محور الصفوف أو الأعمدة في Aspose.Cells for Java
keywords: Aspose.Cells, Java, جدول محوري, حقل قيمة, PivotField, PivotField.Function, حقل بيانات, PivotTable.ValuesField, مجموع, متوسط
type: docs
weight: 230
url: /ar/java/manage-value-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## إضافة حقل إلى منطقة البيانات

تعد إضافة حقل أساسي إلى منطقة البيانات (القيم) الخطوة الأولى في تشكيل كيفية تجميع الجدول المحوري لبياناتك المصدرية. يعرض Aspose.Cells الأسلوب `PivotTable.addFieldToArea(PivotFieldType, String)`، وهو نسخة محمّلة تقبل الثابت `PivotFieldType.DATA` واسم عمود المصدر. بمجرد إضافة حقل إلى منطقة البيانات، يعرضه واجهة برمجة التطبيقات من خلال مجموعة `PivotTable.getDataFields()`، بالترتيب الذي تمت إضافة الحقول به. افتراضياً، يتم تلخيص عمود المصدر الرقمي باستخدام `ConsolidationFunction.SUM`، بينما يكون العمود غير الرقمي افتراضياً على `COUNT`.

```java
import com.aspose.cells.*;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

// العناوين في A1:D1
worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

// صفوف البيانات A2:D9 باستخدام حلقات متداخلة متفرعة على j
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

// إضافة جدول محوري عند F3 بالاسم PivotTable1
int pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1", true, false);
PivotTable pivotTable = worksheet.getPivotTables().get(pivotIndex);

// تخطيط الجدول المحوري: Category و Item في الصف، Year في العمود، Amount كحقل بيانات
pivotTable.addFieldToArea(PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Amount");

pivotTable.calculateData();
workbook.save("output_drag.xlsx");
```

## تغيير دالة التلخيص

كل حقل موضوع في منطقة البيانات يتم تغليفه داخلياً كمثيل من `PivotField`، وتُرجع خاصية `getFunction()` الخاصة به قيمة من تعداد `ConsolidationFunction`. تتيح لك نفس أداة الضبط `setFunction(...)` التبديل بين الدوال المجمّعة المتاحة، بما في ذلك `SUM` و`COUNT` و`AVERAGE` و`MAX` و`MIN` و`PRODUCT` و`STD_DEV` و`STD_DEVP` و`VAR` و`VARP`.

{{% alert color="primary" %}}
تغيير `Function` يؤثر فقط على التجميع، بينما يظل عمود المصدر دون تغيير.
{{% /alert %}}
لذلك يمكنك ترك حقل بيانات واحد كـ `SUM` بينما تضيف حقل بيانات ثانٍ يستهدف نفس عمود المصدر ولكنه يستخدم `COUNT` أو `AVERAGE`، كل ذلك في جدول محوري واحد.

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

## رسم حقول القيم على محور الصفوف أو الأعمدة

عندما يحتوي الجدول المحوري على حقلين أو أكثر من حقول البيانات، يعرض Aspose.Cells حقلاً افتراضياً إضافياً يسمى `PivotTable.getValuesField()`. يمثّل هذا الحقل الافتراضي تجميع كل حقل بيانات موجود في منطقة البيانات. يمكنك سحبه إلى منطقة الصفوف أو الأعمدة كحقل محوري أساسي، وهو أمر مفيد لعرض مقاييس متعددة جنباً إلى جنب.

{{% alert color="primary" %}}
`PivotTable.getValuesField()` لا يعمل إذا لم يكن هناك حقل قيمة أو كان هناك حقل قيمة واحد فقط.
{{% /alert %}}
تستعرض السيناريوهات أدناه ثلاثة أمثلة شاملة توضح كل قدرة من القدرات الموصوفة أعلاه على نفس بنية الجدول المحوري.

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