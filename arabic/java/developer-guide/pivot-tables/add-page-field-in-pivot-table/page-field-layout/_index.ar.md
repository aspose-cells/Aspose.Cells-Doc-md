---
title: تعديل تخطيط حقل الصفحة في الجدول المحوري
linktitle: تعديل تخطيط حقل الصفحة في الجدول المحوري
description: تعلّم كيفية التحكم في تخطيط منطقة حقل الصفحة في جدول محوري باستخدام Aspose.Cells for Java، بما في ذلك تعيين ترتيب العرض وعدد الالتفاف وترتيب الحقول لحقول الصفحة في أعلى الجدول المحوري.
keywords: Aspose.Cells, مكتبة Java, جدول بيانات, جدول محوري, حقل صفحة, ترتيب حقل الصفحة, عدد التفاف حقل الصفحة, نقل حقل الصفحة
type: docs
weight: 191
url: /ar/java/change-page-field-layout/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
هذه المقالة هي تتمة لموضوع **إضافة حقل صفحة في الجدول المحوري**. فهي توضح كيفية التحكم في تخطيط منطقة حقل الصفحة — وهي شريط عناصر تحكم التصفية الموجود في أعلى الجدول المحوري — بما في ذلك ترتيب العرض وعدد الالتفاف وإعادة ترتيب الحقول.
{{% /alert %}}
## **المقدمة**
يعرض الجدول المحوري في Microsoft Excel **منطقة حقل صفحة** مخصصة تقع فوق جسم الصفوف/الأعمدة/البيانات في الجدول. يتم عرض هذه المنطقة كشريط من عناصر تحكم التصفية المنسدلة (واحد لكل حقل صفحة) وهو ما ينقر عليه المستخدمون النهائيون لتقطيع الجدول المحوري حسب معايير مثل السنة أو المنطقة. يقوم Aspose.Cells بنمذجة هذه المنطقة من خلال مجموعة `pivotTable.getPageFields()` ويعرض ثلاث خصائص تتحكم في كيفية تخطيط الشريط بصريًا:
- `pivotTable.getPageFieldOrder()` (قيمة `Aspose.Cells.PrintOrderType`) يقرر ما إذا كانت حقول الصفحة الإضافية ستوضع *بجوار* الحقول الحالية أم *أسفلها*.
- `pivotTable.getPageFieldWrapCount()` يحدد عدد حقول الصفحة التي ستوضع في كل صف أو عمود قبل الالتفاف.
- `pivotTable.getPageFields().move(currIndex, destIndex)` يعيد ترتيب حقول الصفحة دون تغيير نمط الترتيب.
تستعرض هذه المقالة ثلاثة أمثلة برمجية توضح كل عملية من هذه العمليات على مجموعة بيانات مشتركة، حتى تتمكن من مقارنة التخطيطات الناتجة جنبًا إلى جنب.
## **بيانات المصدر**
تقوم جميع الأمثلة الثلاثة أدناه بتحميل هذه الصفوف الثمانية من بيانات المبيعات إلى ورقة عمل باسم `PivotData`. تحتوي البيانات على مرشحين لحقل الصفحة (`Year`، `Region`)، ومرشحًا واحدًا لحقل الصف (`Fruit`)، ومقياسًا واحدًا (`Amount`)، مما يجعل شريط حقل الصفحة ذا فائدة لفحصه.
يتم ملء جميع الصفوف الثمانية في كل مثال برمجي، وبنفس الترتيب، بحيث لا تختلف بيانات المصدر أبدًا بين السيناريوهات — فقط خصائص تخطيط حقل الصفحة هي التي تختلف.
## **المثال 1: أفقي ثم عمودي**
في السيناريو الأول نقوم بتكوين حقلي الصفحة (`Year`، `Region`) ليظهروا **جنبًا إلى جنب في صف واحد** في أعلى الجدول المحوري. نخصص `Fruit` لمحور الصف، ونضع `Year` أولاً و`Region` ثانيًا على محور الصفحة (يحدد ترتيب استدعاءات `addFieldToArea` الفهرس الابتدائي)، ونضيف `Amount` (Sum) كحقل بيانات، ثم نعيّن `pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN)` مع `pivotTable.setPageFieldWrapCount(2)`. مع `OVER_THEN_DOWN` وعدد التفاف يساوي 2، يتم تخطيط حقلي الصفحة أفقيًا جنبًا إلى جنب في صف واحد في أعلى الجدول المحوري، بحيث يشغل الشريط صفًا واحدًا بعرض اثنين.
```java
import com.aspose.cells.*;
import java.io.File;

String dataDir = "output";
if (!new File(dataDir).exists()) new File(dataDir).mkdirs();

Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet pivotDataSheet = worksheets.add("PivotData");
Cells pivotDataCells = pivotDataSheet.getCells();

// العناوين (الصف 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");

// الصف 1: تفاح، 2022، شمال، 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// الصف 2: تفاح، 2023، شمال، 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// الصف 3: موز، 2022، جنوب، 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// الصف 4: موز، 2023، جنوب، 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// الصف 5: كرز، 2022، شرق، 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// الصف 6: كرز، 2023، شرق، 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// الصف 7: عنب، 2022، غرب، 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// الصف 8: عنب، 2023، غرب، 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// إضافة ورقة PivotTableReport
Worksheet pivotTableSheet = worksheets.add("PivotTableReport");
PivotTableCollection pivotTables = pivotTableSheet.getPivotTables();

// إنشاء جدول محوري مصدره PivotData!A1:D9 موضوع في A1 على PivotTableReport
int pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables.get(pivotIndex);

// إضافة الحقول
pivotTable.addFieldToArea(PivotFieldType.ROW, 0);   // الفاكهة
pivotTable.addFieldToArea(PivotFieldType.PAGE, 1);  // السنة
pivotTable.addFieldToArea(PivotFieldType.PAGE, 2);  // المنطقة
pivotTable.addFieldToArea(PivotFieldType.DATA, 3);  // المبلغ
pivotTable.getDataFields().get(0).setFunction(ConsolidationFunction.SUM);

// تكوين تخطيط منطقة حقل الصفحة: ضع حقول الصفحة أفقياً أولاً، ثم التفاف بعد كل 2
pivotTable.setPageFieldOrder(PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);

// التحديث والحساب
pivotTable.calculateData();

// الحفظ
workbook.save(dataDir + "/pageFieldLayout_overThenDown.xlsx");
```
## **المثال 2: عمودي ثم أفقي**
في هذا المثال نضع `Fruit` على محور الصف، و`Year` و`Region` على محور الصفحة (مع `Year` أولاً)، و`Amount` (Sum) كحقل بيانات — تمامًا كما في المثال 1. ثم نعيّن `pivotTable.setPageFieldOrder(PrintOrderType.DOWN_THEN_OVER)` و`pivotTable.setPageFieldWrapCount(2)`. مع `DOWN_THEN_OVER` وعدد التفاف يساوي 2، يتم تكديس حقلي الصفحة عموديًا — `Year` في الأعلى، و`Region` تحته مباشرة — مكونين عمودًا واحدًا في أعلى الجدول المحوري. وبالتالي يشغل الشريط صفين بعرض واحد، على عكس المثال 1.
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
## **المثال 3: نقل حقل صفحة**
في السيناريو الثالث نحتفظ بمجموعة البيانات وتخصيص الحقول هذا، ونعيّن تخطيطًا محايدًا (`OVER_THEN_DOWN` مع عدد التفاف `2`)، ثم نوضح عملية `pageFields.move`. ينقل استدعاء `move(0, 1)` حقل الصفحة الموجود في الفهرس 0 (`Year`) إلى الموضع 1، وينتقل حقل الصفحة الذي كان في الموضع 1 (`Region`) إلى الموضع 0. بعد هذا الاستدعاء، يصبح `Region` هو حقل الصفحة الأول ويصبح `Year` هو الثاني. يظل نمط الالتفاف والترتيب كما هو، لذا لا يزال يتم عرض الشريط أفقيًا جنبًا إلى جنب — فقط ترتيب القائمتين المنسدلتين قد تم تبديلهما.
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
## **مقالات ذات صلة**
- [إضافة حقل صفحة في الجدول المحوري](/cells/ar/java/add-page-field-in-pivot-table/) — الصفحة الأم التي تقدم كيفية إضافة حقول الصفحة إلى جدول محوري.
- [حقول الصفوف والأعمدة في الجدول المحوري](/cells/ar/java/row-and-column-fields/) — يغطي تخصيص الحقول لمحوري الصفوف والأعمدة، مكملًا العمل على محور الصفحة الموضح هنا.
- [إدارة حقول القيم في الجدول المحوري](/cells/ar/java/manage-value-fields/) — يصف كيفية تكوين منطقة البيانات (القيم)، بما في ذلك تجميع `Sum` المستخدم في هذه المقالة.
- [تحديث الجدول المحوري](/cells/ar/java/refresh-pivot-table/) — يشرح `refreshData()` و`calculateData()`، واللذين يكونان مطلوبين بعد إعادة ترتيب حقول الصفحة.
- [تطبيق نمط على الجدول المحوري](/cells/ar/java/apply-style-to-pivot-table/) — يوضح كيفية تنسيق الجدول المحوري المعروض بعد أن يتم تخطيط شريط حقل الصفحة.
{{< app/cells/assistant language="java" >}}