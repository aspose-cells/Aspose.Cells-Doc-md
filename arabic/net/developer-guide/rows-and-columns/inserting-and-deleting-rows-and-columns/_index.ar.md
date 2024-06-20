---
title: إدراج وحذف الصفوف والأعمدة من ملف إكسل
linktitle: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 70
url: /ar/net/inserting-and-deleting-rows-and-columns/
description: توضح هذه المقالة كيفية إدراج وحذف الصفوف والأعمدة بواسطة Aspose.Cells for .NET API.
keywords: تدير Aspose.Cells C# الصفوف والأعمدة، تقوم بإدراج الصفوف والأعمدة، تقوم بحذف الصفوف والأعمدة
---

## **مقدمة**

سواء كنت تقوم بإنشاء ورقة عمل جديدة من الصفر أو العمل في ورقة عمل موجودة، قد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بالعكس، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.
لتلبية هذه المتطلبات، توفر Aspose.Cells مجموعة بسيطة جدًا من الفئات والأساليب، والتي سنناقشها أدناه.

### **إدارة الصفوف والأعمدة**

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Excel من Microsoft. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) التي تمثل جميع الخلايا في ورقة العمل.

تقدم مجموعة الفئة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) العديد من الأساليب لإدارة الصفوف والأعمدة في ورقة عمل. يتم مناقشة بعض هذه الأساليب أدناه.

{{% alert color="primary" %}}

عند إضافة صفوف أو أعمدة، يتم نقل المحتوى في ورقة العمل لأسفل أو لليمين، وإذا تمت إزالة الصفوف أو الأعمدة، يتم نقل المحتوى لأعلى أو لليسار.

{{% /alert %}}


## **إدراج الصفوف والأعمدة**

### **كيفية إدراج صف**

قم بإدراج صف في ورقة العمل في أي موقع عن طريق استدعاء ال[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) من مجموعة ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). يأخذ ال[**InsertRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) المؤشر للصف الذي سيتم إدراج الصف الجديد فيه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **كيفية إدراج عدة صفوف**

لإدراج عدة صفوف في ورقة العمل، اتصل بالطريقة [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) في تجميعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). طريقة [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) تأخذ محددتين:

- فهرس الصف، الفهرس للصف من حيث إن الصفوف الجديدة ستدرج.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **كيفية إدراج صف مع تنسيق**

لإدراج صف بخيارات تنسيق، استخدم الحمولة [**InsertRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) التي تأخذ [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) كمعلمة. ثبّت خصية [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) لفئة [**InsertOptions**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) بقيمة الترقيم [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype). الفئة [**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) لها ثلاثة أعضاء كما هو مدرج أدناه.

- SameAsAbove: ينسق الصف نفسه كصف الذي في الأعلى.
- SameAsBelow: ينسق الصف نفسه كصف الذي في الأسفل.
- Clear: يُمسح التنسيق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **كيفية إدراج عمود**

يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي موقع عن طريق استدعاء الطريقة [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) في تجميعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). الطريقة [**InsertColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) تأخذ مؤشر العمود حيث سيتم إدراج العمود الجديد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **حذف الصفوف والأعمدة**

### **كيفية حذف عدة صفوف**

لحذف صفوف متعددة من ورقة العمل، اتصل بالطريقة [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) في تجميعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). الطريقة [**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) تأخذ محددتين:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، الإجمالي لعدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **كيفية حذف عمود**

لحذف عمود من ورقة العمل في أي موقع، اتصل بالطريقة [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) في تجميعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells). الطريقة [**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) تأخذ مؤشر العمود للحذف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
