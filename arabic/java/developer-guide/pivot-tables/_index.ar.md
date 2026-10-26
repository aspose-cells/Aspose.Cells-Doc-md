---
title: إنشاء جدول محوري
linktitle: إنشاء جدول محوري
description: إنشاء وتنسيق الجداول المحورية باستخدام Aspose.Cells for Java.
keywords: إنشاء جدول محوري, إدراج جدول محوري, تنسيق جدول محوري.
type: docs
weight: 160
url: /ar/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **ما هو الجدول المحوري؟**
الجدول المحوري هو تقرير ملخص تفاعلي يختصر كتلة كبيرة من البيانات الخام المرتبة صفًا بصف في مصفوفة مضغوطة دون الحاجة إلى استخدام أي صيغة. تحدد أي الأعمدة تتحول إلى تسميات صفوف، وأيها تتحول إلى تسميات أعمدة، وأيها تُجمَّع كقيم — ويتولى الجدول المحوري عمليات التجميع والحساب:
- **تلخيص** — إجمالي المبيعات حسب المنتج أو المنطقة أو ربع السنة بدلاً من سلاسل الصيغ الطويلة.
- **مقارنة** — يحوّل عرض الفئات في الصفوف والفترات في الأعمدة قائمة مسطحة إلى تقرير متقاطع تصبح فيه الاتجاهات ظاهرة بوضوح.
- **التنقل إلى التفاصيل** — انقر نقرًا مزدوجًا على أي قيمة ملخصة لفحص الصفوف المصدر التي تقف خلفها.
- **تحديث** — عند تغير بيانات المصدر، يكفي تحديث واحد لإعادة حساب التقرير بالكامل.
تشمل السيناريوهات النموذجية لوحات معلومات المبيعات وتفصيلات المصروفات وتحليل المخزون، وكذلك أي سؤال من النوع "كيف تُفصَّل هذه الأرقام حسب الفئة والوقت؟". ينشئ Aspose.Cells for Java جداول محورية مماثلة برمجيًا، لذا يمكن للمصنفات التي ينشئها تطبيقك أن تحمل تقارير جاهزة للاستخدام بدلاً من البيانات الخام وحدها.

### **إنشاء جدول محوري باستخدام Aspose.Cells**

{{% alert color="primary" %}}
يمكن باستخدام Aspose.Cells إضافة جداول محورية إلى جداول البيانات. تضم Aspose.Cells عددًا من الفئات المخصصة تحديدًا لإنشاء الجداول المحورية والتحكم فيها. تُستخدم هذه الفئات لإنشاء كائن [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) وضبط خصائصه، ويُعد هذا الكائن أساسًا لبناء الجدول المحوري.
كائنات الجدول المحوري هي:
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): يمثل حقلًا في جدول محوري.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): يمثل مجموعة جميع كائنات [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) في الجدول المحوري.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): يمثل جدولًا محوريًا.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): يمثل مجموعة جميع كائنات الجدول المحوري في ورقة العمل.
{{% /alert %}}

### **إنشاء جدول محوري بسيط**
تنطوي عملية إنشاء جدول محوري على ثلاث خطوات: كتابة بيانات المصدر في خلايا ورقة العمل، وإضافة الجدول المحوري في موضع الوجهة، ووضع حقول الجدول المحوري في مناطق الصفوف والأعمدة والبيانات.
1. أضف البيانات إلى خلايا ورقة العمل باستخدام طريقة [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-) الخاصة بكائن [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) (`putValue` في معظم الأمثلة). ستُستخدم هذه البيانات كمصدر للبيانات الخاصة بالجدول المحوري.
2. أضف جدولًا محوريًا إلى ورقة العمل من خلال استدعاء طريقة [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) في فئة [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): `add(sourceData, row, column)`. يمثل `sourceData` نطاق المصدر (على سبيل المثال، "A1:C8")؛ ويمثل `row` و`column` إحداثيات خلية الوجهة، مفهرسة بدءًا من الصفر، عند الركن العلوي الأيسر للجدول المحوري (تشير الخلية E3 إلى الصف 2 والعمود 4). تعيد الطريقة كائن [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) الجديد مباشرة.
3. ضع حقول الجدول المحوري باستخدام طريقة `addFieldToArea` الخاصة بكائن [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): يوضع اسم الحقل في منطقة الصفوف (`PivotFieldType.ROW`)، أو منطقة الأعمدة (`PivotFieldType.COLUMN`)، أو منطقة البيانات (`PivotFieldType.DATA`).
4. احفظ المصنف — إذ يُكتب الجدول المحوري في الملف المحفوظ.
ينشئ مثال التعليمات البرمجية أدناه جدولًا محوريًا بسيطًا وفقًا لهذه الخطوات. وعند تشغيله، يُضاف إلى ورقة العمل جدول محوري قائم على بيانات المصدر:
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// إنشاء مصنف جديد والحصول على ورقة العمل الأولى
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// كتابة بيانات المصدر: المبيعات حسب الرياضة والربع
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// إضافة جدول محوري في خلية الوجهة E3، بمصدر A1:C8
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// تعيين حقول الجدول المحوري: Sport إلى Rows، Quarter إلى Columns، Sales إلى Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// حفظ المصنف
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
عند تعيين نطاق من الخلايا كمصدر للبيانات، يجب تحديد النطاق من الزاوية العلوية اليسرى إلى الزاوية السفلية اليمنى. على سبيل المثال، النطاق "A1:C3" صالح، بينما النطاق "C3:A1" غير صالح.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}