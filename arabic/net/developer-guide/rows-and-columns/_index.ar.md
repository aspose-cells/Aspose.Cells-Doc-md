---
title: تنسيق الصفوف والأعمدة
linktitle: الصفوف و الأعمة
type: docs
weight: 100
url: /ar/net/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}}

عند العمل باستخدام جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة ، قد تحتاج إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. في بعض الأحيان ، يعني تطبيق التنسيق على الصفوف أو الأعمدة أن الارتفاع الحالي أو العرض يحتاج إلى التغيير لإظهار البيانات. عادة ، يقوم المستخدمون بضبط ارتفاعات الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ولكن مع Aspose.Cells يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل.

{{% /alert %}}

## **العمل مع الصفوف**

### **ضبط ارتفاع الصف**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة تمثل جميع الخلايا في ورقة العمل.

 ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. تمت مناقشة بعض هذه أدناه بمزيد من التفصيل.

### **ضبط ارتفاع الصف**

 من الممكن ضبط ارتفاع صف واحد عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) طريقة. ال[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)تأخذ الطريقة المعلمات التالية على النحو التالي:

- **فهرس الصف**، فهرس الصف الذي تقوم بتغيير ارتفاعه.
- **ارتفاع الصف**، ارتفاع الصف المراد تطبيقه على الصف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

### **ضبط ارتفاع كل الصفوف في ورقة عمل**

 إذا احتاج المطورون إلى تعيين ارتفاع الصف نفسه لجميع الصفوف في ورقة العمل ، فيمكنهم القيام بذلك باستخدام ملحق[**ارتفاع قياسي**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) ممتلكات[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة.

**مثال:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

## **العمل مع الأعمدة**

### **ضبط عرض العمود**

 اضبط عرض العمود عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) طريقة. ال[**SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)تأخذ الطريقة المعلمات التالية:

- **فهرس العمود**، هو فهرس العمود الذي تقوم بتغيير عرضه.
- **عرض العمود**، عرض العمود المطلوب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

### **ضبط عرض العمود بالبكسل**

اضبط عرض العمود عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)المجموعة[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)طريقة. ال[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)تأخذ الطريقة المعلمات التالية:

- **فهرس العمود**، هو فهرس العمود الذي تقوم بتغيير عرضه.
- **عرض العمود**، عرض العمود المطلوب بالبكسل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

### **ضبط عرض كل الأعمدة في ورقة عمل**

 لتعيين نفس عرض العمود لجميع الأعمدة في ورقة العمل ، استخدم ملف[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**العرض القياسي**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)خاصية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

## **موضوعات مسبقة**
- [احتواء تلقائي للصفوف والأعمدة](/cells/ar/net/autofit-rows-and-columns/)
- [تحويل النص إلى أعمدة باستخدام Aspose.Cells](/cells/ar/net/convert-text-to-columns-using-aspose-cells/)
- [نسخ الصفوف والأعمدة](/cells/ar/net/copying-rows-and-columns/)
- [احذف الصفوف والأعمدة الفارغة في ورقة عمل](/cells/ar/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [تجميع وإلغاء تجميع الصفوف والأعمدة](/cells/ar/net/grouping-and-ungrouping-rows-and-columns/)
- [إخفاء وإظهار الصفوف والأعمدة](/cells/ar/net/hiding-and-showing-rows-and-columns/)
- [قم بإدراج أو حذف صفوف في ورقة عمل Excel](/cells/ar/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [إدراج وحذف صفوف وأعمدة ملف إكسل](/cells/ar/net/inserting-and-deleting-rows-and-columns/)
- [قم بإزالة الصفوف المكررة في ورقة العمل](/cells/ar/net/remove-duplicate-rows-in-a-worksheet/)
- [قم بتحديث المراجع في أوراق العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل](/cells/ar/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
