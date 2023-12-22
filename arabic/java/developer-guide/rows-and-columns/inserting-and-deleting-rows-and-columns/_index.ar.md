---
title: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns/
description: تعرف على كيفية إدراج وحذف الصفوف والأعمدة من خلال واجهات برمجة التطبيقات Aspose.Cells for Java.
keywords: How to Insert and Delete Rows and Columns in Java, Insert Rows and Columns using Java, Java Delete Rows and Columns, Insert Rows or Columns with Java, Delete Rows or Columns via Java.
---
##  **مقدمة**
سواء قمت بإنشاء ورقة عمل جديدة من البداية أو العمل على ورقة عمل موجودة، فقد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. وعلى العكس من ذلك، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواضع محددة في ورقة العمل.

لتحقيق هذه المتطلبات، يوفر Aspose.Cells مجموعة أبسط جدًا من الفئات والأساليب، الموضحة أدناه.
##  **كيفية إدارة الصفوف/الأعمدة**
 Aspose.Cells يوفر أ[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يحتوي الفصل على أ[مجموعة أوراق العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) الذي يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) يوفر الفصل أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)المجموعة التي تمثل كافة الخلايا في ورقة العمل.

 ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)توفر المجموعة عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل. وتناقش بعض هذه أدناه.

{{% alert color="primary" %}} 

عند إضافة صفوف أو أعمدة، يتم نقل المحتوى الموجود في ورقة العمل إلى الأسفل أو إلى اليمين، ولكن إذا تمت إزالة الصفوف أو الأعمدة، فسيتم نقل المحتوى إلى الأعلى أو إلى اليسار.

{{% /alert %}} 
##  **كيفية إدراج صف**
 أدخل صفًا في أي مكان عن طريق الاتصال بـ[this.insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) طريقة[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[this.insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) تأخذ الطريقة فهرس الصف الذي سيتم إدراج الصف الجديد فيه كوسيطة أولى، وعدد الصفوف التي سيتم إدراجها كوسيطة ثانية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
##  **كيفية إدراج صفوف متعددة**
 لإدراج صفوف متعددة في ورقة العمل، قم باستدعاء[this.insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) طريقة[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[this.insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) تأخذ الطريقة معلمتين:

- فهرس الصف: فهرس الصف الذي سيتم إدراج الصفوف الجديدة منه.
- عدد الصفوف: إجمالي عدد الصفوف التي يجب إدراجها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
##  **كيفية إدراج صف مع التنسيق**
لإدراج صف يحتوي على خيارات التنسيق، استخدم الزر[this.insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)الزائد الذي يأخذ[خيارات الإدراج](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)كمعلمة. تعيين[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)ممتلكات[خيارات الإدراج](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)فئة مع[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)تعداد. ال[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)التعداد لديه ثلاثة أعضاء كما هو موضح أدناه.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): يقوم بتنسيق الصف بنفس الصف أعلاه.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): يقوم بتنسيق الصف بنفس الصف الموجود أدناه.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): مسح التنسيق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
##  **كيفية حذف صف**
 لحذف صف في أي مكان، اتصل بالرقم[this.deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) طريقة[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[this.deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) تأخذ الطريقة معلمتين:

- فهرس الصف: فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف: إجمالي عدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
##  **كيفية حذف صفوف متعددة**
 لحذف صفوف متعددة من ورقة العمل، اتصل بـ[this.deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) طريقة[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[this.deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) تأخذ الطريقة معلمتين:

- فهرس الصف: فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف: إجمالي عدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
##  **كيفية إدراج عمود واحد أو عدة أعمدة**
 يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء[this.insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) طريقة[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة. ال[this.insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) تأخذ الطريقة معلمتين:

- فهرس العمود، فهرس العمود الذي سيتم إدراج العمود منه
- عدد الأعمدة، إجمالي عدد الأعمدة التي يجب إدراجها

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
##  **كيفية حذف عمود**
 لحذف عمود من ورقة العمل في أي مكان، اتصل بـ[this.deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) طريقة[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[this.deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) تأخذ الطريقة المعلمات التالية:

- فهرس العمود: فهرس العمود الذي سيتم حذف العمود منه.
- عدد الأعمدة: إجمالي عدد الأعمدة التي يجب حذفها.
- تحديث المرجع: معلمة منطقية للإشارة إلى ما إذا كان سيتم تحديث المراجع في أوراق العمل الأخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

