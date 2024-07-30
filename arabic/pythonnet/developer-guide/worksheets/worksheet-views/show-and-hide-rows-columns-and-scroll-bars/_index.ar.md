---
title: إظهار وإخفاء الصفوف والأعمدة وأشرطة التمرير
type: docs
weight: 20
url: /ar/python-net/show-and-hide-rows-columns-and-scroll-bars/
description: توضح هذه المقالة كيفية عرض وإخفاء الصفوف والأعمدة برمجيًا في ورقة عمل Excel باستخدام Aspose.Cells for Python via .NET API. يمكن ضبط ظاهرية أشرطة التمرير وإخفاء العديد من الصفوف والأعمدة.
keywords: مكتبة Excel للبايثون، عرض وإخفاء الصفوف والأعمدة في Python، إخفاء الصفوف والأعمدة في Python، عرض شريط التمرير العمودي في Python، عرض شريط التمرير الأفقي في Python، إخفاء شريط التمرير العمودي في Python، إخفاء شريط التمرير الأفقي في Python، عرض وإخفاء الصفوف والأعمدة وأشرطة التمرير.
---

{{% alert color="primary" %}}

توفر Aspose.Cells for Python via .NET وسائل للتحكم في ظهور الصفوف والأعمدة وأشرطة التمرير في ورقة العمل.

{{% /alert %}}

## **إظهار وإخفاء الصفوف والأعمدة**

توفر Aspose.Cells for Python via .NET فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) تمثل ملف Excel. توفر الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) مجموعة واسعة من الخصائص والطرق لإدارة ملف Excel. للتحكم في ظهور أشرطة التمرير، استخدم خاصيتي الفئة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) و [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) و [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) هما خاصيتان بوليانيتان، مما يعني أن هذه الخصائص يمكنها تخزين قيمة **صحيحة** أو **كاذبة**.

### **إظهار الصفوف والأعمدة**

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء طرق [**unhide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_row/) و[**unhide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/unhide_column/) من مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells/) على التوالي. تأخذ كلا الطريقين معلمتين:

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-UnhidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

أثناء جعل العمود المخفي مرئيًا، إذا كنت بحاجة إلى استعادته إلى العرض المعين سابقًا أو إلى عرضه الأصلي، يرجى عرض العمود بعرض سلبي. على سبيل المثال: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **إخفاء الصفوف والأعمدة**

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء طرق [**hide_row**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_row/) و[**hide_column**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_column/) من مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) على التوالي. تأخذ كلا الطريقين فهم فهرس الصف والعمود كمعلمة لإخفاء الصف أو العمود المحدد.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingRowsAndColumns-1.py" >}}

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}}

### **إخفاء صفوف وأعمدة متعددة**

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء طرق [**hide_rows**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_rows/) و[**hide_columns**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/hide_columns) من مجموعة [**Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) على التوالي. تأخذ كلا الطريقين فهرس الصف أو العمود البدء وعدد الصفوف أو الأعمدة التي يجب إخفاؤها كمعلمات.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.py" >}}

## **إظهار وإخفاء شريط التمرير**

يُستخدم شريط التمرير للتنقل في محتويات أي ملف. عادة ما تكون هناك نوعين من شرائط التمرير:

- شرائط التمرير العمودية
- شرائط التمرير الأفقية

كما يوفر Microsoft Excel أيضًا أشرطة تمرير أفقية ورأسية بحيث يمكن للمستخدمين التمرير من خلال محتويات ورقة العمل. باستخدام Aspose.Cells for Python via .NET، يمكن للمطورين التحكم في رؤية كلا أنواع شرائط التمرير في ملفات Excel.

### **التحكم في رؤية شرائط التمرير**

توفر Aspose.Cells for Python via .NET فئةً [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) تمثل ملف Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) مجموعة واسعة من الخصائص والطرق لإدارة ملف Excel. للتحكم في رؤية شرائط التمرير، استخدم خصائص فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) و [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible). كلا الخصائص [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) و [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) هما خصائص مقولة، مما يعني أنه يمكن لهذه الخصائص أن تخزن فقط قيم **صحيحة** أو **خاطئة**.

#### **جعل أشرطة التمرير مرئية**

اجعل شرائط التمرير مرئية عن طريق تعيين خصائص الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) أو [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) إلى **صحيحة**.

#### **إخفاء أشرطة التمرير**

إخفاء أشرطة التمرير عن طريق تعيين خصائص الصنف [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) [**WorkbookSettings.is_v_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_v_scroll_bar_visible) أو [**WorkbookSettings.is_h_scroll_bar_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/is_h_scroll_bar_visible) إلى **false**.

**كود عينة**

بالأسفل يوجد شيفرة كاملة تفتح ملف إكسل، book1.xls، ثم تخفي كلتي الشريطين وتحفظ الملف المعدل بشكل output.xls.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Views-Worksheets-Display-DisplayHideScrollBars-1.py" >}}
