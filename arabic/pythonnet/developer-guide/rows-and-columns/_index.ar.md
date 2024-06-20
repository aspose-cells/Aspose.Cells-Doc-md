---
title: تنسيق الصفوف والأعمدة
linktitle: الصفوف والأعمدة
type: docs
weight: 100
url: /ar/python-net/adjusting-row-height-and-column-width/
description: Aspose.Cells for Python via .NET يمكن دعم تغيير ارتفاع الصف أو عرض العمود، وكذلك تطبيق التنسيق على الصفوف أو الأعمدة.
keywords: مكتبة Excel للبايتون، البايتون تعيين ارتفاع الصف وعرض العمود، البايتون ضبط ارتفاع الصف وعرض العمود، البايتون تغيير ارتفاع الصف أو عرض العمود، البايتون تنسيق الصفوف والأعمدة، كيفية ضبط ارتفاع الصف وعرض العمود في البايتون.
---


{{% alert color="primary" %}}

عند العمل مع جداول البيانات وإضافة البيانات إلى الصفوف أو الأعمدة، قد تحتاج إلى تغيير ارتفاع الصفوف أو عرض الأعمدة. في بعض الأحيان، تطبيق التنسيق على الصفوف أو الأعمدة يعني أن الارتفاع الحالي أو العرض يجب تغييره لعرض البيانات. عادةً ما يقوم المستخدمون بضبط ارتفاع الصفوف وعرض الأعمدة في بيئة WYSIWYG باستخدام Microsoft Excel. ولكن، باستخدام Aspose.Cells for Python via .NET، يمكن للمطورين تنفيذ هذه العمليات أثناء التشغيل.

{{% /alert %}}

## **العمل مع الصفوف**

### **كيفية ضبط ارتفاع الصف**

توفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، التي تمثل ملف Microsoft Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) تمثل جميع الخلايا في ورقة العمل.

توفر مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة عمل. يتم مناقشة بعض هذه الطرق أدناه بتفصيل أكثر.

### **كيفية ضبط ارتفاع الصف**

من الممكن ضبط ارتفاع صف واحد عن طريق استدعاء [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) الـ[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) مجموعة [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) الـ[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) الطريقة. تأخذ الطريقة [**set_row_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_row_height/#int-float) المعلمات التالية على النحو التالي:

- **الصف**, مؤشر الصف الذي تغيير ارتفاعه.
- **الارتفاع**, ارتفاع الصف المطلوب تطبيقه على الصف.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightOfRow-1.py" >}}

### **كيفية ضبط ارتفاع كل الصفوف في ورقة عمل**

إذا كان لدى المطورين حاجة لتعيين نفس ارتفاع الصف لكافة الصفوف في ورقة العمل، فيمكنهم القيام بذلك باستخدام [**standard_height**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_height) خاصية مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

**مثال:**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingHeightAllRows-1.py" >}}

## **العمل مع الأعمدة**

### **كيفية ضبط عرض العمود**

قم بتعيين عرض عمود بالاستدعاء [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) الـ[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) مجموعة [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) الـ[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) الطريقة. تأخذ الطريقة [**set_column_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width/#int-float) المعلمات التالية:

- **العمود**, مؤشر العمود الذي تغيير عرضه.
- **العرض**, العرض المطلوب للعمود.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfColumn-1.py" >}}

### **كيفية تعيين عرض العمود بالبكسل**

قم بتعيين عرض عمود بالاستدعاء [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) الـ[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) مجموعة [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) الـ[**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells) الطريقة. تأخذ الطريقة [**set_column_width_pixel**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/set_column_width_pixel/#int-int) المعلمات التالية:

- **العمود**, مؤشر العمود الذي تغيير عرضه.
- **البكسلات**، عرض العمود المطلوب بالبكسل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SetColumnWidthInPixels-1.py" >}}

### **كيفية ضبط عرض جميع الأعمدة في ورقة العمل**

لضبط نفس عرض العمود لجميع الأعمدة في ورقة العمل، استخدم خاصية [**standard_width**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/standard_width) لمجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-HeightAndWidth-SettingWidthOfAllColumns-1.py" >}}

## **مواضيع متقدمة**
- [تكييف صفوف وأعمدة تلقائيًا](/cells/ar/python-net/autofit-rows-and-columns/)
- [تحويل النص إلى أعمدة باستخدام Aspose.Cells](/cells/ar/python-net/convert-text-to-columns-using-aspose-cells/)
- [نسخ الصفوف والأعمدة](/cells/ar/python-net/copying-rows-and-columns/)
- [حذف الصفوف والأعمدة الفارغة في ورقة العمل](/cells/ar/python-net/delete-blank-rows-and-columns-in-a-worksheet/)
- [تجميع وفك تجميع الصفوف والأعمدة](/cells/ar/python-net/grouping-and-ungrouping-rows-and-columns/)
- [إخفاء وإظهار الصفوف والأعمدة](/cells/ar/python-net/hiding-and-showing-rows-and-columns/)
- [إدراج أو حذف الصفوف في ورقة عمل Excel](/cells/ar/python-net/insert-or-delete-rows-in-an-excel-worksheet/)
- [إدراج وحذف الصفوف والأعمدة من ملف Excel](/cells/ar/python-net/inserting-and-deleting-rows-and-columns/)
- [إزالة الصفوف المكررة في ورقة العمل](/cells/ar/python-net/remove-duplicate-rows-in-a-worksheet/)
- [تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل](/cells/ar/python-net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
