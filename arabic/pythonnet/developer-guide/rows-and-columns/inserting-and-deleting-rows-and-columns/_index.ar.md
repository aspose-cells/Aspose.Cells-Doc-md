---
title: إدراج وحذف الصفوف والأعمدة من ملف إكسل
linktitle: إدراج وحذف الصفوف والأعمدة
type: docs
weight: 70
url: /ar/python-net/inserting-and-deleting-rows-and-columns/
description: يوضح هذا المقال كيفية إدراج وحذف الصفوف والأعمدة باستخدام واجهة برمجة التطبيقات Aspose.Cells for Python via .NET.
keywords: مكتبة Python Excel ، Aspose.Cells Python لإدارة الصفوف والأعمدة ، إدراج صفوف وأعمدة باستخدام Python ، حذف الصفوف والأعمدة باستخدام Python ، إزالة الصفوف والأعمدة.
---

## **مقدمة**

سواء كنت تقوم بإنشاء ورقة عمل جديدة من الصفر أو العمل في ورقة عمل موجودة، قد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بالعكس، قد نحتاج أيضًا إلى حذف صفوف أو أعمدة من مواقع محددة في ورقة العمل.
لتلبية هذه المتطلبات ، توفر Aspose.Cells for Python via .NET مجموعة بسيطة جدًا من الصفوف والأساليب ، التي سيتم مناقشتها أدناه.

### **إدارة الصفوف والأعمدة**

تقدم Aspose.Cells for Python via .NET فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) ، التي تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) التي تمثل جميع الخلايا في ورقة العمل.

تقدم مجموعة الفئة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) العديد من الأساليب لإدارة الصفوف والأعمدة في ورقة عمل. يتم مناقشة بعض هذه الأساليب أدناه.

{{% alert color="primary" %}}

عند إضافة صفوف أو أعمدة، يتم نقل المحتوى في ورقة العمل لأسفل أو لليمين، وإذا تمت إزالة الصفوف أو الأعمدة، يتم نقل المحتوى لأعلى أو لليسار.

{{% /alert %}}


## **إدراج الصفوف والأعمدة**

### **كيفية إدراج صف**

قم بإدراج صف في ورقة العمل في أي موقع عن طريق استدعاء ال[**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) من مجموعة ال[**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). يأخذ ال[**insert_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_row/) المؤشر للصف الذي سيتم إدراج الصف الجديد فيه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARow-1.py" >}}

### **كيفية إدراج عدة صفوف**

لإدراج عدة صفوف في ورقة العمل، اتصل بالطريقة [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) في تجميعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). طريقة [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int) تأخذ محددتين:

- فهرس الصف، الفهرس للصف من حيث إن الصفوف الجديدة ستدرج.
- عدد الصفوف، إجمالي عدد الصفوف التي يجب إدراجها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.py" >}}

### **كيفية إدراج صف مع تنسيق**

لإدراج صف بخيارات تنسيق، استخدم الحمولة [**insert_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_rows/#int-int-aspose.cells.InsertOptions) التي تأخذ [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) كمعلمة. ثبّت خصية [**copy_format_type**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions/copy_format_type/) لفئة [**InsertOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/insertoptions) بقيمة الترقيم [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/). الفئة [**CopyFormatType**](https://reference.aspose.com/cells/python-net/aspose.cells/copyformattype/) لها ثلاثة أعضاء كما هو مدرج أدناه.

- SAME_AS_ABOVE: ينسق الصف نفس الصف أعلاه.
- SAME_AS_BELOW: ينسق الصف نفس الصف أدناه.
- CLEAR: يُمسح التنسيق.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.py" >}}

### **كيفية إدراج عمود**

يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي موقع عن طريق استدعاء الطريقة [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) في تجميعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). الطريقة [**insert_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/insert_column/#int) تأخذ مؤشر العمود حيث سيتم إدراج العمود الجديد.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-InsertingAColumn-1.py" >}}

## **حذف الصفوف والأعمدة**

### **كيفية حذف عدة صفوف**

لحذف صفوف متعددة من ورقة العمل، اتصل بالطريقة [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) في تجميعة [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). الطريقة [**delete_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_rows/#int-int) تأخذ محددتين:

- فهرس الصف، الفهرس للصف من حيث سيتم حذف الصفوف.
- عدد الصفوف، الإجمالي لعدد الصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.py" >}}


### **كيفية حذف عمود**

لحذف عمود من ورقة العمل في أي موقع، اتصل بالطريقة [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) في تجميعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). الطريقة [**delete_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/delete_column/#int) تأخذ مؤشر العمود للحذف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-InsertingAndDeleting-DeletingAColumn-1.py" >}}
