---
title: ادراج وحذف الصفوف والاعمده
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns/
---
## **مقدمة**
سواء أكنت تنشئ ورقة عمل جديدة من البداية أو تعمل على ورقة عمل موجودة ، فقد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بشكل عكسي ، قد نحتاج أيضًا إلى حذف الصفوف أو الأعمدة من المواضع المحددة في ورقة العمل.

للوفاء بهذه المتطلبات ، يوفر Aspose.Cells أبسط مجموعة من الفئات والطرق الموضحة أدناه.
## **إدارة الصفوف / الأعمدة**
 يوفر Aspose.Cells أ[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تمثل ملف Excel Microsoft. ال[دفتر العمل](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[ورقة العمل](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) صف دراسي. ال[ورقة عمل](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) فئة توفر أ[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)مجموعة تمثل جميع الخلايا في ورقة العمل.

 ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells)توفر المجموعة عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل. تمت مناقشة بعض هذه أدناه.

{{% alert color="primary" %}} 

عند إضافة صفوف أو أعمدة ، يتم إزاحة المحتوى في ورقة العمل لأسفل أو إلى اليمين ، ولكن إذا تمت إزالة الصفوف أو الأعمدة ، يتم إزاحة المحتوى لأعلى أو لليسار.

{{% /alert %}} 
## **إدخال صف**
 أدخل صفًا في أي مكان عن طريق استدعاء[إدراج صفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[إدراج صفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) تأخذ طريقة فهرس الصف حيث سيتم إدراج الصف الجديد كوسيطة أولى ، وعدد الصفوف التي سيتم إدراجها كوسيطة ثانية.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **إدراج صفوف متعددة**
 لإدراج عدة صفوف في ورقة العمل ، قم باستدعاء[إدراج صفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[إدراج صفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) تأخذ الطريقة معلمتين:

- فهرس الصفوف: فهرس الصف حيث سيتم إدراج الصفوف الجديدة.
- عدد الصفوف: العدد الإجمالي للصفوف التي يجب إدراجها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **أدخل صفًا بالتنسيق**
لإدراج صف بخيارات التنسيق ، استخدم ملف[إدراج صفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) الزائد الذي يستغرقه[إدراج خيارات](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)كمعامل. تعيين[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType)ممتلكات[إدراج خيارات](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions)فئة مع[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)تعداد. ال[CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType)العد من ثلاثة أعضاء كما هو مذكور أدناه.

- [نفس_كما_في الاعلى](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE)تنسيق الصف مثل الصف أعلاه.
- [نفس_كما_أقل](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): تنسيق الصف نفسه كما في الصف أدناه.
- [صافي](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): يمسح التنسيق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **حذف صف**
 لحذف صف في أي مكان ، اتصل بـ[حذف الصفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[حذف الصفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) تأخذ الطريقة معلمتين:

- فهرس الصفوف: فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف: العدد الإجمالي للصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **حذف عدة صفوف**
لحذف عدة صفوف من ورقة العمل ، قم باستدعاء[حذف الصفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[حذف الصفوف](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) تأخذ الطريقة معلمتين:

- فهرس الصفوف: فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف: العدد الإجمالي للصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **إدراج عمود واحد أو عدة أعمدة**
 يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء[insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)مجموعة. ال[insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) تأخذ الطريقة معلمتين:

- فهرس العمود ، فهرس العمود حيث سيتم إدراج العمود
- عدد الأعمدة ، العدد الإجمالي للأعمدة التي يجب إدراجها

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **حذف عمود**
 لحذف عمود من ورقة العمل في أي مكان ، قم باستدعاء[حذف الأعمدة](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\) ) طريقة ال[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) مجموعة. ال[حذف الأعمدة](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) تأخذ الطريقة المعلمات التالية:

- فهرس العمود: فهرس العمود الذي سيتم حذف العمود منه.
- عدد الأعمدة: العدد الإجمالي للأعمدة المطلوب حذفها.
- تحديث المرجع: معلمة منطقية للإشارة إلى ما إذا كان سيتم تحديث المراجع في أوراق العمل الأخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

