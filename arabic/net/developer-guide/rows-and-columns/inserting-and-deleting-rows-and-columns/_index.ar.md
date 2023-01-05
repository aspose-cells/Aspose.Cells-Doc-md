---
title: إدراج وحذف صفوف وأعمدة ملف إكسل
linktitle: ادراج وحذف الصفوف والاعمده
type: docs
weight: 70
url: /ar/net/inserting-and-deleting-rows-and-columns/
---
## **مقدمة**

سواء أكنت تنشئ ورقة عمل جديدة من البداية أو تعمل على ورقة عمل موجودة ، فقد نحتاج إلى إضافة صفوف أو أعمدة إضافية لاستيعاب المزيد من البيانات. بشكل عكسي ، قد نحتاج أيضًا إلى حذف الصفوف أو الأعمدة من المواضع المحددة في ورقة العمل.
للوفاء بهذه المتطلبات ، يوفر Aspose.Cells أبسط مجموعة من الفئات والطرق الموضحة أدناه.

### **إدارة الصفوف والأعمدة**

Aspose.Cells يوفر فئة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة تمثل جميع الخلايا في ورقة العمل.

 ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)توفر المجموعة عدة طرق لإدارة الصفوف والأعمدة في ورقة العمل. تمت مناقشة بعض هذه أدناه.

{{% alert color="primary" %}}

عند إضافة صفوف أو أعمدة ، يتم إزاحة المحتوى في ورقة العمل لأسفل أو إلى اليمين ، وإذا تمت إزالة الصفوف أو الأعمدة ، يتم إزاحة المحتوى لأعلى أو لليسار.

{{% /alert %}}


## **قم بإدراج صفوف وأعمدة**

### **أدخل صفًا**

 أدخل صفًا في ورقة العمل في أي مكان عن طريق استدعاء ملف[**الصف إدراج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**الصف إدراج**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrow)تأخذ الطريقة فهرس الصف حيث سيتم إدراج الصف الجديد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARow-1.cs" >}}

### **أدخل عدة صفوف**

 لإدراج عدة صفوف في ورقة عمل ، قم باستدعاء[**إدراج صفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**إدراج صفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)تأخذ الطريقة معلمتين:

- فهرس الصف ، فهرس الصف حيث سيتم إدراج الصفوف الجديدة.
- عدد الصفوف ، العدد الإجمالي للصفوف التي يجب إدراجها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingMultipleRows-1.cs" >}}

### **أدخل صفًا بالتنسيق**

لإدراج صف بخيارات التنسيق ، استخدم ملف[**إدراج صفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertrows)الزائد الذي يستغرقه[**إدراج خيارات**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) كمعامل. تعيين[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) ممتلكات[**إدراج خيارات**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions) فئة مع[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype) تعداد. ال[**CopyFormatType**](https://reference.aspose.com/cells/net/aspose.cells/insertoptions/properties/copyformattype)العد من ثلاثة أعضاء كما هو مذكور أدناه.

- SameAsAbove: تنسيق الصف مثل الصف أعلاه.
- SameAsBelow: ينسق الصف مثل الصف أدناه.
- مسح: يمسح التنسيق.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingARowWithFormatting-1.cs" >}}

### **أدخل عمود**

 يمكن للمطورين أيضًا إدراج عمود في ورقة العمل في أي مكان عن طريق استدعاء[**إدراج العمود**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)مجموعة. ال[**إدراج العمود**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/insertcolumn)تأخذ الطريقة فهرس العمود حيث سيتم إدراج العمود الجديد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-InsertingAColumn-1.cs" >}}

## **حذف الصفوف والأعمدة**

### **حذف عدة صفوف**

لحذف عدة صفوف من ورقة العمل ، قم باستدعاء[**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**DeleteRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deleterows)تأخذ الطريقة معلمتين:

- فهرس الصف ، فهرس الصف الذي سيتم حذف الصفوف منه.
- عدد الصفوف ، العدد الإجمالي للصفوف التي يجب حذفها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingMultipleRows-1.cs" >}}


### **احذف عمود**

 لحذف عمود من ورقة العمل في أي مكان ، قم باستدعاء[**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn) طريقة[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة. ال[**DeleteColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/deletecolumn)الأسلوب يأخذ فهرس العمود لحذفه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-InsertingAndDeleting-DeletingAColumn-1.cs" >}}
