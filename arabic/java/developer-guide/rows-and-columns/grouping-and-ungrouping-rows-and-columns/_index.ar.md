---
title: تجميع وإلغاء تجميع الصفوف والأعمدة
type: docs
weight: 40
url: /ar/java/grouping-and-ungrouping-rows-and-columns/
---

## **مقدمة**
في ملف Microsoft Excel، يمكنك إنشاء مخطط للبيانات للسماح لك بإظهار وإخفاء مستويات التفاصيل بنقرة واحدة على الفأرة.

انقر على **رموز المخطط**، 1,2,3، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل بسرعة، أو يمكنك استخدام الرموز لرؤية التفاصيل تحت ملخص أو عنوان فردي كما يظهر أدناه في الشكل:

تجميع الصفوف والأعمدة 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **إدارة تجميع الصفوف والأعمدة**
توفر Aspose.Cells فئة، [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. ورقة العمل يتم تمثيلها بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل، ويتم مناقشة بعض هذه الطرق أدناه بالتفصيل.
### **تجميع الصفوف والأعمدة**
من الممكن تجميع الصفوف أو الأعمدة من خلال استدعاء طرق [groupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows-int-int-boolean-) و [groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns-int-int-boolean-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). كلا الطريقتين تأخذان المعلمات التالية:

- مؤشر الصف أو العمود الأول في المجموعة.
- مؤشر الصف أو العمود الأخير في المجموعة.
- يتم إخفاءها، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف/الأعمدة بعد التجميع أم لا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **إعدادات التجميع**
Microsoft Excel يسمح أيضًا بتكوين إعدادات التجميع لعرض:

- صفوف ملخصية أسفل التفاصيل.
- أعمدة الملخص على يمين التفاصيل.

**إعدادات التجميع** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

من الممكن تكوين إعدادات التجميع باستخدام خاصية Outline لفئة Worksheet.
### **صفوف الملخص أدناه التفصيل**
يمكن للمطورين التحكم في عرض صفوف الملخص أدناه التفاصيل عن طريق استخدام الطريقة [SummaryRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) لفئة [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **أعمدة ملخصية على يمين التفاصيل**
من الممكن التحكم في ما إذا كانت أعمدة الملخص تُعرض على يمين التفاصيل باستخدام الطريقة [SummaryColumnRight](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight) لفئة [Outline](https://reference.aspose.com/cells/java/com.aspose.cells/Outline).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **إلغاء تجميع الصفوف والأعمدة**
لفك تجميع الصفوف أو الأعمدة المجمعة، استدعي طرق [ungroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows-int-int-) و [ungroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns-int-int-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). كلا الطريقتين تأخذان نفس المعلمات:

- الصف الأول أو فهرس العمود، الصف/العمود الأول الذي سيتم إلغاء تجميعه.
- الصف/العمود الأخير الذي سيتم إلغاء تجميعه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
{{< app/cells/assistant language="java" >}}
