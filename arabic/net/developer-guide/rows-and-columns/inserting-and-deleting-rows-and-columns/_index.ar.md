---
title: إدراج وحذف الصفوف والأعمدة في ملف Excel
linktitle: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 70
url: /ar/net/inserting-and-deleting-rows-and-columns/
description: توضح هذه المقالة كيفية إدراج وحذف الصفوف والأعمدة بواسطة Aspose.Cells for .NET API.
keywords: Aspose.Cells C# manage rows and columns, insert rows and columns, delete rows and columns
---
##  **مقدمة**

سواء قمت بإنشاء ورقة عمل جديدة من البداية أو العمل على ورقة عمل موجودة، فقد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. وعلى العكس من ذلك، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواضع محددة في ورقة العمل.
لتحقيق هذه المتطلبات، يوفر Aspose.Cells مجموعة أبسط جدًا من الفئات والأساليب، الموضحة أدناه.

###  **إدارة الصفوف والأعمدة**

Aspose.Cells يوفر فئة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)المجموعة التي تمثل كافة الخلايا في ورقة العمل.

 ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)توفر المجموعة عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل. وتناقش بعض هذه أدناه.

{{% alert color="primary" %}}

عند إضافة صفوف أو أعمدة، يتم نقل المحتوى الموجود في ورقة العمل إلى الأسفل أو إلى اليمين، وإذا تمت إزالة الصفوف أو الأعمدة، يتم نقل المحتوى إلى الأعلى أو إلى اليسار.

{{% /alert %}}


##  **إدراج صفوف وأعمدة**

###  **كيفية إدراج صف**

 قم بإدراج صف في ورقة العمل في أي مكان عن طريق استدعاء[**الصف إدراج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**الصف إدراج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)تأخذ الطريقة فهرس الصف الذي سيتم إدراج الصف الجديد فيه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

###  **كيفية إدراج صفوف متعددة**

 لإدراج صفوف متعددة في ورقة عمل، قم باستدعاء[**إدراج صفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**إدراج صفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)تأخذ الطريقة معلمتين:

- فهرس الصف، فهرس الصف الذي سيتم إدراج الصفوف الجديدة منه.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

###  **كيفية إدراج صف مع التنسيق**

لإدراج صف يحتوي على خيارات التنسيق، استخدم الزر[**إدراج صفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)الزائد الذي يأخذ[**خيارات الإدراج**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) كمعلمة. تعيين[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) ممتلكات[**خيارات الإدراج**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) فئة مع[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) تعداد. ال[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)التعداد لديه ثلاثة أعضاء كما هو موضح أدناه.

- SameAsAbove: يقوم بتنسيق الصف بنفس الصف الموجود أعلاه.
- SameAsBelow: يقوم بتنسيق الصف بنفس الصف الموجود أدناه.
- مسح: مسح التنسيق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

###  **كيفية إدراج عمود**

 يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء[**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة. ال[**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)تأخذ الطريقة فهرس العمود الذي سيتم إدراج العمود الجديد فيه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

##  **حذف الصفوف والأعمدة**

###  **كيفية حذف صفوف متعددة**

 لحذف صفوف متعددة من ورقة العمل، اتصل بـ[**حذف الصفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**حذف الصفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)تأخذ الطريقة معلمتين:

- فهرس الصف، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


###  **كيفية حذف عمود**

 لحذف عمود من ورقة العمل في أي مكان، اتصل بـ[**حذف العمود**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**حذف العمود**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)تأخذ الطريقة فهرس العمود المراد حذفه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
