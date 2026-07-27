---
title: إضافة حقول الصفوف والأعمدة إلى جدول محوري في Aspose.Cells لـ .NET
linktitle: حقول الصفوف والأعمدة
description: تعلّم كيفية إضافة حقول أساسية إلى منطقتي الصفوف والأعمدة في الجدول المحوري وكيفية التحكم في المجاميع الفرعية لحقول المحور باستخدام PivotField.setSubtotals في Aspose.Cells for Java.
keywords: Aspose.Cells, Java, جدول محوري, حقل صف, حقل عمود, PivotField, setSubtotals, PivotFieldSubtotalType, مجاميع فرعية
type: docs
weight: 220
url: /ar/java/pivot-table-add-row-column-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

تُعد الحقول الصفية والعمودية اللبنات الأساسية للجدول المحوري. يظهر الحقل الموضوع في منطقة الصفوف عموديًا على يسار المحور، بينما يظهر الحقل الموضوع في منطقة الأعمدة أفقيًا عبر الأعلى. توضح هذه المقالة كيفية إضافة الحقول الأساسية إلى تلك المناطق برمجيًا وكيفية التحكم في المجاميع الفرعية التي تظهر بين مجموعات الحقول باستخدام الطريقة `PivotField.setSubtotals`.

## **إضافة حقل إلى منطقة الصفوف أو الأعمدة**

تقوم الطريقة `PivotTable.addFieldToArea(int fieldType, String fieldName)` بنقل حقل أساسي من البيانات المصدر إلى إحدى مناطق المحور الأربع. تقبل الوسيطة `fieldType` إحدى قيم `PivotFieldType` التالية.

- `ROW` — الحقول الموضوعة عموديًا على اليسار
- `COLUMN` — الحقول الموضوعة أفقيًا عبر الأعلى
- `DATA` — الحقول التي يتم تجميع قيمها
- `PAGE` — الحقول المستخدمة كمرشحات للتقرير

بعد إضافة الحقول، يمكنك الوصول إليها من خلال الخصائص `PivotTable.getRowFields()` و`PivotTable.getColumnFields()`. تُرجع كل خاصية كائن `PivotFieldCollection`. الحقل عند الفهرس 0 من `RowFields` هو حقل الصف الأبعد، وتمثل الفهارس اللاحقة الحقول المتداخلة داخله. ينطبق نفس اصطلاح الفهرسة على `ColumnFields`.

يهم ترتيب تداخل الحقول. تؤدي إضافة `Category` إلى منطقة الصفوف أولاً ثم `Item` إلى إنشاء محور تكون فيه المجموعة الخارجية `Category` والمجموعة الداخلية `Item`. يؤدي عكس الترتيب إلى عكس التسلسل الهرمي.

## **المجاميع الفرعية لحقل المحور**

تتحكم الطريقة `PivotField.setSubtotals(int subtotalType, boolean shown)` في صفوف المجاميع الفرعية التي تظهر لحقل المحور. يؤدي كل استدعاء إلى تبديل نوع مجموع فرعي واحد بشكل مستقل. يعرض تمرير `shown = true` المجموع الفرعي، بينما يخفيه `shown = false`. نظرًا لأن كل استدعاء يؤثر على نوع واحد فقط، فإن استدعاء الطريقة عدة مرات بقيم `subtotalType` مختلفة يُنشئ مجموعة فرعية مخصصة من المجاميع الفرعية.

يحدد التعداد `PivotFieldSubtotalType` أنواع المجاميع الفرعية المتاحة.

- `AUTOMATIC` — يختار Aspose.Cells التحديد الافتراضي (عادةً `SUM` للحقول الرقمية)
- `NONE` — إلغاء جميع صفوف المجاميع الفرعية
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
لا تظهر المجاميع الفرعية إلا عند وجود حقلين أو أكثر من حقول المحور في منطقة الصفوف (أو في منطقة الأعمدة). لا يوجد لدى حقل واحد ما يمكن حساب مجموع فرعي بينه وبين غيره، لذلك لا يكون لاستدعاءات `setSubtotals` أي تأثير مرئي في تلك الحالة. لذلك تضع هذه المقالة حقلين من حقول الصفوف (`Category` خارجي، `Item` داخلي) في كل مثال بحيث يكون حد المجموع الفرعي بين كل مجموعة `Category` مرئيًا.
{{% /alert %}}

## **السيناريو 1 — المجاميع الفرعية التلقائية (الافتراضية)**

عندما لا تستدعي `setSubtotals` على الإطلاق، يطبق Aspose.Cells تحديد `AUTOMATIC` على الحقول الرقمية. يؤكد المثال التالي صراحةً هذا السلوك من خلال استدعاء `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` على حقل الصف الخارجي `Category`.

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

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **السيناريو 2 — إلغاء جميع المجاميع الفرعية (بلا)**

يؤدي استدعاء `setSubtotals(PivotFieldSubtotalType.NONE, true)` إلى إزالة جميع صفوف المجاميع الفرعية من المحور، مع ترك صفوف الحقول والمجموع الكلي في الأسفل فقط. يكون هذا مفيدًا عندما تريد البيانات المجمعة الأولية دون أي صفوف ملخصة.

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
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **السيناريو 3 — مجموعة فرعية مخصصة من المجاميع الفرعية (المجموع + المتوسط)**

لست مقيدًا بنوع مجموع فرعي واحد. يعمل كل استدعاء `setSubtotals` بشكل مستقل على نوع واحد، لذا فإن استدعاء الطريقة مرتين — مرة بـ `SUM` ومرة بـ `AVERAGE` — يُنتج مجموعة فرعية مخصصة من صفّي مجاميع فرعية لكل مجموعة `Category`.

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

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
```

## **ملخص**

تتشارك السيناريوهات الثلاثة أعلاه في نفس مجموعة البيانات وهيكل الجدول المحوري. الفرق الوحيد بينها هو استدعاء `setSubtotals` المطبق على حقل الصف الخارجي `Category`. تذكر قاعدة الحقلين: لا يوجد لدى حقل واحد في منطقة ما ما يمكن حساب مجموع فرعي بينه وبين غيره، لذلك ضع دائمًا حقلين على الأقل في منطقة الصفوف أو الأعمدة عندما تريد أن يكون لاستدعاء `setSubtotals` تأثير مرئي.

## **مقالات ذات صلة**

- [حقول الصفحات في الجداول المحورية](/cells/ar/java/add-page-field-in-pivot-table/)
- [تحديث الجداول المحورية في Aspose.Cells for Java](/cells/ar/java/refresh-pivot-table/)
- [تطبيق الأنماط على الجداول المحورية](/cells/ar/java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
