---
title: تجميع الصفوف والأعمدة وإلغاء تجميعها
type: docs
weight: 40
url: /ar/java/grouping-and-ungrouping-rows-and-columns/
---
## **مقدمة**
في ملف Excel Microsoft ، يمكنك إنشاء مخطط تفصيلي للبيانات للسماح لك بإظهار مستويات التفاصيل وإخفائها بنقرة واحدة بالماوس.

 انقر على**رموز المخطط التفصيلي**، 1 ، 2 ، 3 ، + و - لعرض الصفوف أو الأعمدة التي توفر ملخصات أو عناوين للأقسام في ورقة العمل فقط بسرعة ، أو يمكنك استخدام الرموز لمشاهدة التفاصيل ضمن ملخص فردي أو عنوان كما هو موضح أدناه في الشكل :

 تجميع الصفوف والأعمدة

![ما يجب القيام به: image_بديل_نص](grouping-and-ungrouping-rows-and-columns_1.png)
## **إدارة المجموعة للصفوف والأعمدة**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[أوراق عمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة تمثل جميع الخلايا في ورقة العمل.

 ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل ، وقد تمت مناقشة القليل منها أدناه بمزيد من التفصيل.
### **تجميع الصفوف والأعمدة**
 من الممكن تجميع الصفوف أو الأعمدة عن طريق استدعاء[GroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ) و[groupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) ) طرق[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة. تأخذ كلتا الطريقتين المعلمات التالية:

- أول صف / فهرس العمود ، أول صف أو عمود في المجموعة.
- فهرس الصف / العمود الأخير ، الصف أو العمود الأخير في المجموعة.
- مخفي ، معلمة منطقية تحدد ما إذا كان سيتم إخفاء الصفوف / الأعمدة بعد التجميع أم لا.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **إعدادات المجموعة**
Microsoft يسمح Excel أيضًا بتكوين إعدادات المجموعة لعرض:

- صفوف التلخيص أدناه التفاصيل.
- أعمدة التلخيص على يمين التفاصيل.

**إعدادات المجموعة** 

![ما يجب القيام به: image_بديل_نص](grouping-and-ungrouping-rows-and-columns_2.png)

من الممكن تكوين إعدادات المجموعة هذه باستخدام خاصية Outline لفئة ورقة العمل.
### **صفوف التلخيص أدناه التفاصيل**
 يمكن للمطورين التحكم في عرض صفوف التلخيص أدناه بالتفصيل باستخدام ملف[الخطوط العريضة](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) صف دراسي'[ملخص](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) طريقة.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **أعمدة التلخيص إلى يمين التفاصيل**
من الممكن التحكم في عرض أعمدة الملخص على يمين التفاصيل باستخدام ملف[الخطوط العريضة](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) صف دراسي'[ملخص العمود](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)طريقة.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **فك تجميع الصفوف والأعمدة**
 قم بفك تجميع الصفوف أو الأعمدة المجمعة عن طريق استدعاء ملف[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[UngroupRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ) و[UngroupColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) طُرق. تأخذ كلتا الطريقتين نفس المعلمات:

- الصف الأول أو فهرس العمود ، الصف / العمود الأول المراد فك تجميعه.
- فهرس الصف أو العمود الأخير ، الصف / العمود الأخير المراد فك تجميعه.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
