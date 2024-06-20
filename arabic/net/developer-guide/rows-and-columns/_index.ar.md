---
title: تنسيق الصفوف والأعمدة
linktitle: الصفوف والأعمدة
type: docs
weight: 100
url: /ar/net/adjusting-row-height-and-column-width/
description: يمكن لـ Aspose.Cells for .NET دعم تغيير ارتفاع الصف أو عرض العمود، وكذلك تطبيق التنسيق على الصفوف أو الأعمدة.
keywords: تعيين ارتفاع الصف وعرض العمود، ضبط ارتفاع الصف وعرض العمود، تغيير ارتفاع الصف أو عرض العمود، تنسيق الصفوف والأعمدة، كيفية تعيين ارتفاع الصف وعرض العمود.
---


{{% alert color="primary" %}}

عند العمل مع جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة، قد تحتاج في بعض الأحيان إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. في بعض الأحيان، تطبيق التنسيق على الصفوف أو الأعمدة يعني أن الارتفاع أو العرض الحالي يحتاج إلى التغيير لعرض البيانات. عادةً ما يقوم المستخدمون بضبط ارتفاع الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ومع Aspose.Cells، يمكن للمطورين تنفيذ هذه العمليات أثناء التشغيل.

{{% /alert %}}

## **العمل مع الصفوف**

### **كيفية ضبط ارتفاع الصف**

توفر Aspose.Cells فئة تُسمى [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تمثل ملف Microsoft Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) تسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة عمل. يتم مناقشة بعض هذه الطرق أدناه بتفصيل أكثر.

### **كيفية ضبط ارتفاع الصف**

من الممكن ضبط ارتفاع صف واحد عن طريق استدعاء [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) الـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) الـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) الطريقة. تأخذ الطريقة [**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) المعلمات التالية على النحو التالي:

- **مؤشر الصف**, مؤشر الصف الذي كنت تغير ارتفاعه.
- **ارتفاع الصف**, ارتفاع الصف المطبق على الصف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **كيفية ضبط ارتفاع كل الصفوف في ورقة عمل**

إذا كان لدى المطورين حاجة لتعيين نفس ارتفاع الصف لكافة الصفوف في ورقة العمل، فيمكنهم القيام بذلك باستخدام [**StandardHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) خاصية مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

**مثال:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **العمل مع الأعمدة**

### **كيفية ضبط عرض العمود**

قم بتعيين عرض عمود بالاستدعاء [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) الـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) الـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) الطريقة. تأخذ الطريقة [**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) المعلمات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, العرض المطلوب للعمود.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **كيفية تعيين عرض العمود بالبكسل**

قم بتعيين عرض عمود بالاستدعاء [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) الـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) مجموعة [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) الـ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) الطريقة. تأخذ الطريقة [**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel) المعلمات التالية:

- **فهرس العمود**, فهرس العمود الذي تريد تغيير عرضه.
- **عرض العمود**, عرض العمود المطلوب بالبكسل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **كيفية ضبط عرض جميع الأعمدة في ورقة العمل**

لضبط نفس عرض العمود لجميع الأعمدة في ورقة العمل، استخدم خاصية [**StandardWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth) لمجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **مواضيع متقدمة**
- [تكييف صفوف وأعمدة تلقائيًا](/cells/ar/net/autofit-rows-and-columns/)
- [تحويل النص إلى أعمدة باستخدام Aspose.Cells](/cells/ar/net/convert-text-to-columns-using-aspose-cells/)
- [نسخ الصفوف والأعمدة](/cells/ar/net/copying-rows-and-columns/)
- [حذف الصفوف والأعمدة الفارغة في ورقة العمل](/cells/ar/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [تجميع وفك تجميع الصفوف والأعمدة](/cells/ar/net/grouping-and-ungrouping-rows-and-columns/)
- [إخفاء وإظهار الصفوف والأعمدة](/cells/ar/net/hiding-and-showing-rows-and-columns/)
- [إدراج أو حذف الصفوف في ورقة عمل Excel](/cells/ar/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [إدراج وحذف الصفوف والأعمدة من ملف Excel](/cells/ar/net/inserting-and-deleting-rows-and-columns/)
- [إزالة الصفوف المكررة في ورقة العمل](/cells/ar/net/remove-duplicate-rows-in-a-worksheet/)
- [تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل](/cells/ar/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
