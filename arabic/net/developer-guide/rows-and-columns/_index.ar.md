---
title: تنسيق الصفوف والأعمدة
linktitle: الصفوف و الأعمة
type: docs
weight: 100
url: /ar/net/adjusting-row-height-and-column-width/
description: Aspose.Cells for .NET يمكنه دعم تغيير ارتفاع الصف أو عرض العمود، بالإضافة إلى تطبيق التنسيق على الصفوف أو الأعمدة.
keywords: Set row height and column width, Adjust row height and column width, change the row height or column width, format rows and columns, how to set row height and column width.
---
{{% alert color="primary" %}}

عند العمل باستخدام جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة، قد تحتاج إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. في بعض الأحيان، يعني تطبيق التنسيق على الصفوف أو الأعمدة أن الارتفاع أو العرض الحالي يحتاج إلى التغيير لعرض البيانات. عادةً، يقوم المستخدمون بضبط ارتفاعات الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ولكن مع Aspose.Cells يمكن للمطورين تنفيذ هذه العمليات في وقت التشغيل.

{{% /alert %}}

##  **العمل مع الصفوف**

###  **كيفية ضبط ارتفاع الصف**

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يحتوي الفصل على أ[**مجموعة أوراق العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)الذي يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فصل. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) يوفر الفصل أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)المجموعة التي تمثل كافة الخلايا في ورقة العمل.

 ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. وتناقش بعض هذه أدناه بمزيد من التفصيل.

###  **كيفية ضبط ارتفاع الصف**

 من الممكن ضبط ارتفاع صف واحد عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight) طريقة. ال[**SetRowHeight**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setrowheight)تأخذ الطريقة المعلمات التالية كما يلي:

- *فهرس الصف**، فهرس الصف الذي تقوم بتغيير ارتفاعه.
- *ارتفاع الصف**، ارتفاع الصف الذي سيتم تطبيقه على الصف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightOfRow-1.cs" >}}

###  **كيفية ضبط ارتفاع كافة الصفوف في ورقة العمل**

 إذا كان المطورون بحاجة إلى تعيين نفس ارتفاع الصف لجميع الصفوف في ورقة العمل، فيمكنهم القيام بذلك باستخدام[**الارتفاع القياسي**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardheight) ملكية[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)مجموعة.

**مثال:**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingHeightAllRows-1.cs" >}}

##  **العمل مع الأعمدة**

###  **كيفية ضبط عرض العمود**

 قم بتعيين عرض العمود عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**عرض_SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth) طريقة. ال[**عرض_SetColumnWidth**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidth)تأخذ الطريقة المعلمات التالية:

- *فهرس العمود**، فهرس العمود الذي تقوم بتغيير عرضه.
- *عرض العمود**، عرض العمود المطلوب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.cs" >}}

###  **كيفية ضبط عرض العمود بالبكسل**

قم بتعيين عرض العمود عن طريق استدعاء[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)المجموعة[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)طريقة. ال[**SetColumnWidthPixel**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/setcolumnwidthpixel)تأخذ الطريقة المعلمات التالية:

- *فهرس العمود**، فهرس العمود الذي تقوم بتغيير عرضه.
- *عرض العمود**، عرض العمود المطلوب بالبكسل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.cs" >}}

###  **كيفية ضبط عرض جميع الأعمدة في ورقة العمل**

 لتعيين نفس عرض العمود لجميع الأعمدة في ورقة العمل، استخدم الأمر[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) المجموعة[**العرض القياسي**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/standardwidth)ملكية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.cs" >}}

##  **مواضيع متقدمة**
- [الاحتواء التلقائي للصفوف والأعمدة](/cells/ar/net/autofit-rows-and-columns/)
- [تحويل النص إلى أعمدة باستخدام Aspose.Cells](/cells/ar/net/convert-text-to-columns-using-aspose-cells/)
- [نسخ الصفوف والأعمدة](/cells/ar/net/copying-rows-and-columns/)
- [حذف الصفوف والأعمدة الفارغة في ورقة العمل](/cells/ar/net/delete-blank-rows-and-columns-in-a-worksheet/)
- [تجميع وفك تجميع الصفوف والأعمدة](/cells/ar/net/grouping-and-ungrouping-rows-and-columns/)
- [إخفاء وإظهار الصفوف والأعمدة](/cells/ar/net/hiding-and-showing-rows-and-columns/)
- [إدراج أو حذف صفوف في ورقة عمل Excel](/cells/ar/net/insert-or-delete-rows-in-an-excel-worksheet/)
- [إدراج وحذف الصفوف والأعمدة في ملف Excel](/cells/ar/net/inserting-and-deleting-rows-and-columns/)
- [إزالة الصفوف المكررة في ورقة العمل](/cells/ar/net/remove-duplicate-rows-in-a-worksheet/)
- [قم بتحديث المراجع في أوراق العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل](/cells/ar/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
