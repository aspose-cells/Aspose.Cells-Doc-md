---
title: تجميع وإلغاء تجميع الصفوف والأعمدة
type: docs
weight: 50
url: /ar/python-net/grouping-and-ungrouping-rows-and-columns/
description: يظهر هذا المقال كيفية تجميع الصفوف وعدم تجميعها بواسطة Aspose.Cells لمكتبة Python via .NET.
keywords: مكتبة Python Excel, كيفية تجميع الصفوف والأعمدة بواسطة Python, كيفية عدم تجميع الصفوف والأعمدة بواسطة Python, إدارة تجميع الصفوف والأعمدة بواسطة Python, كيفية تعيين الصفوف الختامية إلى أسفل التفاصيل, كيفية تعيين الأعمدة الختامية عن يمين التفاصيل.
---

## **مقدمة**

في ملف Microsoft Excel، يمكنك إنشاء مخطط للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة على الفأرة.

انقر على **رموز المخطط**، 1,2,3، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل بسرعة، أو يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص أو عنوان فردي كما يظهر أدناه في الشكل:

|**تجميع الصفوف والأعمدة.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **إدارة تجميع الصفوف والأعمدة**

توفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة عمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) تمثل جميع الخلايا في الورقة العمل.

تقدم مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة عمل، تم مناقشة بعض هذه الطرق أدناه بالمزيد من التفاصيل.

### **كيفية تجميع الصفوف والأعمدة**

يمكن تجميع الصفوف أو الأعمدة عن طريق استدعاء [**group_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_rows/#int-int-bool) و [**group_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/group_columns/#int-int-bool) من مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). تأخذ كلا الطريقتين المعلمات التالية:

- مؤشر الصف أو العمود الأول في المجموعة.
- مؤشر الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-GroupingRowsAndColumns-1.py" >}}

#### **إعدادات التجميع**

يسمح Microsoft Excel لك بتكوين إعدادات التجميع لعرض:

- صفوف ملخصية أسفل التفاصيل.
- أعمدة ملخصية على يمين التفاصيل.

يمكن للمطورين تكوين إعدادات التجميع باستخدام خاصية [**outline**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/outline/) لفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

### **كيفية تعيين الصفوف الإجمالية أدناه التفاصيل**

من الممكن التحكم في ما إذا كانت الصفوف الملخصية تُعرض أسفل التفاصيل عن طريق تعيين خاصية [**summary_row_below**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_row_below/) لفئة [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) إلى **صحيح** أو **خطأ**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowBelow-1.py" >}}

### **كيفية تعيين الأعمدة الإجمالية على يمين التفاصيل**

يمكن للمطورين أيضًا التحكم في عرض الأعمدة الملخصية على يمين التفاصيل عن طريق تعيين خاصية [**summary_column_right**](https://reference.aspose.com/cells/python-net/aspose.cells/outline/summary_column_right/) لفئة [**Outline**](https://reference.aspose.com/cells/python-net/aspose.cells/outline) إلى **صحيح** أو **خطأ**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-SummaryRowRight-1.py" >}}

## **كيفية عدمتجميع الصفوف والأعمدة**

لإلغاء تجميع أي صفوف أو أعمدة مجمعة، يُمكن استدعاء [**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/) و [**ungroup_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_columns/#int-int) من مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells). تأخذ كلا الطريقتين معلمتين:

- الصف الأول أو فهرس العمود، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- الصف/العمود الأخير الذي سيتم إلغاء تجميعه.

[**ungroup_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/ungroup_rows/#int-int-bool) لديه تحميل زائد يأخذ معامل بولياني ثالث. يتم تعيينه على **صحيح** يزيل جميع المعلومات المجمّعة. وإلا، يتم إزالة معلومات المجموعة الخارجية فقط.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Grouping-UngroupingRowsAndColumns-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
