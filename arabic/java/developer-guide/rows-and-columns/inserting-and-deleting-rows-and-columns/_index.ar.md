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
قم بإدراج صف في أي مكان عن طريق استدعاء طريقة [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ طريقة [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) الموقع حيث سيتم إدراج الصف الجديد كوسيط أول، وعدد الصفوف التي سيتم إدراجها كوسيط ثاني.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingARow-InsertingARow.java" >}}
## **كيفية إدراج عدة صفوف**
لإدراج عدة صفوف في ورقة العمل، استدعي طريقة [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ الطريقة وسيطين:

- فهرس الصف: فهرس الصف من حيث سيتم إدراج الصفوف الجديدة.
- عدد الصفوف: العدد الإجمالي للصفوف التي يجب إدراجها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingMultipleRows-InsertingMultipleRows.java" >}}
## **كيفية إدراج صف مع تنسيق**
لإدراج صف بتنسيقات، استعمل النسخة المحملة من [insertRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertRows-int-int-com.aspose.cells.InsertOptions-) التي تأخذ [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) كوسيط. قم بضبط الخاصية [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/insertoptions#CopyFormatType) لفئة [InsertOptions](https://reference.aspose.com/cells/java/com.aspose.cells/InsertOptions) باستخدام تعداد [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType). تحتوي تعداد [CopyFormatType](https://reference.aspose.com/cells/java/com.aspose.cells/CopyFormatType) على ثلاثة أعضاء كما هو مدرج أدناه.

- [SAME_AS_ABOVE](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-ABOVE): تنسيق الصف مثل الصف أعلاه.
- [SAME_AS_BELOW](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#SAME-AS-BELOW): تنسيق الصف مثل الصف أدناه.
- [CLEAR](https://reference.aspose.com/cells/java/com.aspose.cells/copyformattype#CLEAR): يقوم بمسح التنسيق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-InsertingARowWithFormatting-1.java" >}}
## **كيفية حذف صف**
لحذف صف في أي مكان، استدعي طريقة [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ الطريقة وسيطين:

- فهرس الصف: فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف: إجمالي عدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteARow-DeleteARow.java" >}}
## **كيفية حذف عدة صفوف**
لحذف عدة صفوف من ورقة العمل، استدعي طريقة [deleteRows](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteRows-int-int-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ الطريقة وسيطين:

- فهرس الصف: فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف: إجمالي عدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteMultipleRows-DeleteMultipleRows.java" >}}
## **كيفية إدراج عمود واحد أو عدة أعمدة**
يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء طريقة [insertColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#insertColumns-int-int-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ الطريقة وسيطين:

- فهرس العمود، فهرس العمود الذي سيتم إدراج العمود منه
- عدد الأعمدة، العدد الإجمالي للأعمدة التي يجب إدراجها

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-InsertingAColumn-InsertingAColumn.java" >}}
## **كيفية حذف عمود**
لحذف عمود من ورقة العمل في أي مكان، استدعِ طريقة [deleteColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#deleteColumns-int-int-boolean-) لمجموعة [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells). تأخذ الطريقة المعلمات التالية:

- فهرس العمود: فهرس العمود الذي سيتم حذف العمود منه.
- عدد الأعمدة: العدد الإجمالي للأعمدة التي يجب حذفها.
- تحديث المرجع: مُعامل منطقي للإشارة إلى ما إذا كان من اللازم تحديث المراجع في ورقات العمل الأخرى.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-DeleteAColumn-DeleteAColumn.java" >}}

{{< app/cells/assistant language="java" >}}
