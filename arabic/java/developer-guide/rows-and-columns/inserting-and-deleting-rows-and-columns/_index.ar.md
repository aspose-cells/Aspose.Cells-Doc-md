---
title: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 60
url: /ar/java/inserting-and-deleting-rows-and-columns/
description: تعلم كيفية إدراج وحذف الصفوف والأعمدة من خلال Aspose.Cells for Java واجهات برمجة التطبيقات.
keywords: كيفية إدراج وحذف الصفوف والأعمدة في جافا، إدراج الصفوف والأعمدة باستخدام جافا، حذف الصفوف والأعمدة في جافا، إدراج الصفوف أو الأعمدة باستخدام جافا، حذف الصفوف والأعمدة via Java.
---

## **مقدمة**
سواء كنت تقوم بإنشاء ورقة عمل جديدة من الصفر أو العمل في ورقة عمل موجودة، قد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بالعكس، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.

لتلبية هذه المتطلبات، توفر Aspose.Cells مجموعة بسيطة جدًا من الفئات والأساليب، والتي سنناقشها أدناه.
## **كيفية إدارة الصفوف / الأعمدة**
توفر Aspose.Cells فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel من Microsoft. تحتوي فئة [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) التي تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) عدة أساليب لإدارة الصفوف والأعمدة في ورقة العمل. يتم مناقشة بعض هذه الأساليب أدناه.

{{% alert color="primary" %}} 

عند إضافة صفوف أو أعمدة، يتم تحريك المحتوى في ورقة العمل إلى الأسفل أو اليمين، ولكن إذا تمت إزالة الصفوف أو الأعمدة، يتم تحريك المحتوى إلى الأعلى أو اليسار.

{{% /alert %}} 
## **كيفية إدراج صف**
قم بإدراج صف في أي موقع باستدعاء طريقة [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) من مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ الطريقة [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) الفهرس للصف الذي سيتم إدراج الصف الجديد فيه كالمعامل الأول، وعدد الصفوف التي يجب إدراجها كالمعامل الثاني.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **كيفية إدراج عدة صفوف**
لإدراج عدة صفوف في ورقة العمل، قم باستدعاء طريقة [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) من مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ الطريقة [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int\)) معاملين:

- فهرس الصف: فهرس الصف من حيث سيتم إدراج الصفوف الجديدة.
- عدد الصفوف: العدد الإجمالي للصفوف التي يجب إدراجها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **كيفية إدراج صف مع تنسيق**
لإدراج صف مع خيارات التنسيق، استخدم النسخة الإضافية [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows\(int,%20int,%20com.aspose.cells.InsertOptions\)) التي تأخذ [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) كمعامل. ضع خاصية الـ [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) من فئة [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) باستخدام تعداد الـ [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType). يحتوي تعداد الـ [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) على ثلاثة أعضاء كما هو مدرج أدناه.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_ABOVE): يقوم بتنسيق الصف بنفس تنسيق الصف أعلاه.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME_AS_BELOW): يقوم بتنسيق الصف بنفس تنسيق الصف أدناه.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): يقوم بمسح التنسيق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **كيفية حذف صف**
لحذف صف في أي موقع، قم باستدعاء طريقة [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) من مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ الطريقة [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) معاملين:

- فهرس الصف: فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف: إجمالي عدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **كيفية حذف عدة صفوف**
لحذف عدة صفوف من ورقة العمل، اُستدعِ الأسلوب [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) من مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). يأخذ الأسلوب [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows\(int,%20int\)) متغيرين:

- فهرس الصف: فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف: إجمالي عدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **كيفية إدراج عمود واحد أو عدة أعمدة**
يُستطيع المطورون أيضًا إدراج عمود في ورقة العمل في أي موقع باستدعاء الأسلوب [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) من مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). يأخذ الأسلوب [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns\(int,%20int\)) متغيرين:

- فهرس العمود، فهرس العمود الذي سيتم إدراج العمود منه
- عدد الأعمدة، العدد الإجمالي للأعمدة التي يجب إدراجها

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **كيفية حذف عمود**
لحذف عمود من ورقة العمل في أي موقع، اُستدعِ الأسلوب [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) من مجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). يأخذ الأسلوب [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns\(int,%20int,%20boolean\)) المتغيرات التالية:

- فهرس العمود: فهرس العمود الذي سيتم حذف العمود منه.
- عدد الأعمدة: العدد الإجمالي للأعمدة التي يجب حذفها.
- تحديث المرجع: مُعامل منطقي للإشارة إلى ما إذا كان من اللازم تحديث المراجع في ورقات العمل الأخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

