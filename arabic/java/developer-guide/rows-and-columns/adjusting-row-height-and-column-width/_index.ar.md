---
title: ضبط ارتفاع الصف وعرض العمود
type: docs
weight: 10
url: /ar/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

عند العمل باستخدام جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة ، قد تحتاج إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. في بعض الأحيان ، يعني تطبيق التنسيق على الصفوف أو الأعمدة أن الارتفاع الحالي أو العرض يحتاج إلى التغيير لإظهار البيانات. عادة ، يقوم المستخدمون بضبط ارتفاعات الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ولكن مع Aspose.Cells يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل. ستبدأ فهارس الصفوف والأعمدة من 0.

{{% /alert %}} 
## **العمل مع الصفوف**
### **ضبط ارتفاع الصف**
 Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة تمثل جميع الخلايا في ورقة العمل.

 ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. تمت مناقشة بعض هذه أدناه بمزيد من التفصيل.
### **ضبط ارتفاع الصف**
 من الممكن ضبط ارتفاع صف واحد عن طريق استدعاء[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\) ) طريقة. ال[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) تأخذ الطريقة المعلمات التالية:

- **فهرس الصف**، فهرس الصف الذي تقوم بتغيير ارتفاعه.
- **ارتفاع الصف**، ارتفاع الصف المراد تطبيقه على الصف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **ضبط ارتفاع كل الصفوف**
 لتعيين ارتفاع الصف نفسه لجميع الصفوف في ورقة العمل ، استخدم ملف[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)طريقة.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **العمل مع الأعمدة**
### **ضبط عرض العمود**
 اضبط عرض العمود عن طريق استدعاء[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\) ) طريقة. ال[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) تأخذ الطريقة المعلمات التالية:

- **فهرس العمود**، هو فهرس العمود الذي تقوم بتغيير عرضه.
- **عرض العمود**، عرض العمود المطلوب.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **ضبط عرض كل الأعمدة**
 لتعيين نفس عرض العمود لجميع الأعمدة في ورقة العمل ، استخدم ملف[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) المجموعة[setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)طريقة.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
