---
title: تجميع وإلغاء تجميع الصفوف والأعمدة
type: docs
weight: 50
url: /ar/net/grouping-and-ungrouping-rows-and-columns/
---

## **مقدمة**

في ملف Microsoft Excel، يمكنك إنشاء مخطط للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة على الفأرة.

انقر على **رموز المخطط**، 1,2,3، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل بسرعة، أو يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص أو عنوان فردي كما يظهر أدناه في الشكل:

|**تجميع الصفوف والأعمدة.**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **إدارة تجميع الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) تمثل جميع الخلايا في ورقة العمل.

تقدم مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة عمل، تم مناقشة بعض هذه الطرق أدناه بالمزيد من التفاصيل.

### **تجميع الصفوف والأعمدة**

يمكن تجميع الصفوف أو الأعمدة عن طريق استدعاء [**GroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) و [**GroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). تأخذ كلا الطريقتين المعلمات التالية:

- مؤشر الصف أو العمود الأول في المجموعة.
- مؤشر الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **إعدادات التجميع**

يسمح Microsoft Excel لك بتكوين إعدادات التجميع لعرض:

- صفوف ملخصية أسفل التفاصيل.
- أعمدة ملخصية على يمين التفاصيل.

يمكن للمطورين تكوين إعدادات التجميع باستخدام خاصية [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) لفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

### **صفوف ملخصية أسفل التفاصيل**

من الممكن التحكم في ما إذا كانت الصفوف الملخصية تُعرض أسفل التفاصيل عن طريق تعيين خاصية [**SummaryRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) لفئة [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) إلى **صحيح** أو **خطأ**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **أعمدة ملخصية على يمين التفاصيل**

يمكن للمطورين أيضًا التحكم في عرض الأعمدة الملخصية على يمين التفاصيل عن طريق تعيين خاصية [**SummaryColumnRight**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) لفئة [**Outline**](https://reference.aspose.com/cells/net/aspose.cells/outline) إلى **صحيح** أو **خطأ**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **إلغاء تجميع الصفوف والأعمدة**

لإلغاء تجميع أي صفوف أو أعمدة مجمعة، يُمكن استدعاء [**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) و [**UngroupColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells). تأخذ كلا الطريقتين معلمتين:

- الصف الأول أو فهرس العمود، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- الصف/العمود الأخير الذي سيتم إلغاء تجميعه.

[**UngroupRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) لديه تحميل زائد يأخذ معامل بولياني ثالث. يتم تعيينه على **صحيح** يزيل جميع المعلومات المجمّعة. وإلا، يتم إزالة معلومات المجموعة الخارجية فقط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
