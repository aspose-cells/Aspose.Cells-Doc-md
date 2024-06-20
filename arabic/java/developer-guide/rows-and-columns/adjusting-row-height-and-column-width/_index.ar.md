---
title: ضبط ارتفاع الصف وعرض العمود
type: docs
weight: 10
url: /ar/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

عند العمل مع جداول البيانات وإضافة بيانات إلى الصفوف أو الأعمدة، قد تحتاج أحيانًا لتغيير ارتفاع الصفوف أو عرض الأعمدة. في بعض الأحيان، تعني تطبيق التنسيق على الصفوف أو الأعمدة أن ارتفاع الصف أو عرض العمود الحالي يحتاج إلى تغيير لعرض البيانات. عادةً ما يقوم المستخدمون بتعديل ارتفاع الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. لكن، باستخدام Aspose.Cells، يمكن للمطورين تنفيذ هذه العمليات أثناء التشغيل. يبدأ الفهارس للصفوف والأعمدة من 0.

{{% /alert %}} 
## **العمل مع الصفوف**
### **ضبط ارتفاع الصف**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على مجموعة [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة عمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة عمل. يتم مناقشة بعض هذه الطرق أدناه بمزيد من التفصيل.
### **ضبط ارتفاع الصف**
من الممكن تعيين ارتفاع صف واحد بالاتصال بطريقة [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)). تأخذ طريقة [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) المعلمات التالية:

- **مؤشر الصف**, مؤشر الصف الذي كنت تغير ارتفاعه.
- **ارتفاع الصف**, ارتفاع الصف المطبق على الصف.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **ضبط ارتفاع جميع الصفوف**
لتعيين نفس ارتفاع الصف لكافة الصفوف في ورقة العمل، استخدم أسلوب [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight) في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **العمل مع الأعمدة**
### **ضبط عرض العمود**
قم بتعيين عرض العمود عن طريق استدعاء أسلوب [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). يأخذ أسلوب [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) الباراميترات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, العرض المطلوب للعمود.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **ضبط عرض كافة الأعمدة**
لتعيين نفس عرض العمود لكافة الأعمدة في ورقة العمل، استخدم أسلوب [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth) في مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
