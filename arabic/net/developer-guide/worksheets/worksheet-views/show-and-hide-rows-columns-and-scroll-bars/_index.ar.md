---
title: إظهار وإخفاء الصفوف والأعمدة وأشرطة التمرير
type: docs
weight: 20
url: /ar/net/show-and-hide-rows-columns-and-scroll-bars/
description: يوضح هذا المقال كيفية عرض وإخفاء صفوف وأعمدة ورقة عمل Excel برمجيًا باستخدام لغة C# وAPI أو مكتبة .NET. يمكن ضبط رؤية أشرطة التمرير، ويمكن إخفاء عدة صفوف وأعمدة.
---

{{% alert color="primary" %}}

توفر Aspose.Cells وسائل للتحكم في رؤية الصفوف، الأعمدة وأشرطة التمرير بورقة العمل.

{{% /alert %}}

## **إظهار وإخفاء الصفوف والأعمدة**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، تمثل ملف Microsoft Excel. فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تحتوي على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) تتيح للمطورين الوصول إلى كل ورق عمل في ملف Excel. يتم تمثيل ورقة العمل بفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) تمثل جميع الخلايا في ورقة العمل. توفر مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) العديد من الطرق لإدارة الصفوف أو الأعمدة في ورقة عمل. يتم مناقشة بعض هذه الطرق أدناه.

### **إظهار الصفوف والأعمدة**

يمكن للمطورين عرض أي صف أو عمود مخفي عن طريق استدعاء طرق [**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) و[**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) على التوالي. تأخذ كلا الطريقين معلمتين:

- **فهرس الصف أو العمود** - فهرس الصف أو العمود المستخدم لعرض الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المعين للصف أو العمود بعد عرضه.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

أثناء جعل العمود المخفي مرئيًا، إذا كنت بحاجة إلى استعادته إلى العرض المعين سابقًا أو إلى عرضه الأصلي، يرجى عرض العمود بعرض سلبي. على سبيل المثال: worksheet.Cells.UnhideColumn(5, -1)

{{% /alert %}}

### **إخفاء الصفوف والأعمدة**

يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء طرق [**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) و[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) على التوالي. تأخذ كلا الطريقين فهم فهرس الصف والعمود كمعلمة لإخفاء الصف أو العمود المحدد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق تعيين ارتفاع الصف أو عرض العمود إلى 0 على التوالي.

{{% /alert %}}

### **إخفاء صفوف وأعمدة متعددة**

يمكن للمطورين إخفاء عدة صفوف أو أعمدة دفعة واحدة عن طريق استدعاء طرق [**HideRows**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) و[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) من مجموعة [**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) على التوالي. تأخذ كلا الطريقين فهرس الصف أو العمود البدء وعدد الصفوف أو الأعمدة التي يجب إخفاؤها كمعلمات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **إظهار وإخفاء شريط التمرير**

يُستخدم شريط التمرير للتنقل في محتويات أي ملف. عادة ما تكون هناك نوعين من شرائط التمرير:

- شرائط التمرير العمودية
- شرائط التمرير الأفقية

توفر Microsoft Excel أيضًا شرائط تمرير أفقية وعمودية بحيث يمكن للمستخدمين التمرير من خلال محتويات ورقة العمل. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية كلا أنواع شرائط التمرير في ملفات Excel.

### **التحكم في رؤية شرائط التمرير**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) تمثل ملف Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية شرائط التمرير، استخدم خصائص فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) و [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible). [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) و [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) هما خصائص منطقية، مما يعني أن هذه الخصائص يمكنها تخزين قيم **صحيحة** أو **غير صحيحة** فقط.

#### **جعل أشرطة التمرير مرئية**

اجعل شرائط التمرير مرئية عن طريق تعيين خصائص الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) أو [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) إلى **صحيحة**.

#### **إخفاء أشرطة التمرير**

إخفاء أشرطة التمرير عن طريق تعيين خصائص الصنف [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) أو [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) إلى **false**.

**كود عينة**

بالأسفل يوجد شيفرة كاملة تفتح ملف إكسل، book1.xls، ثم تخفي كلتي الشريطين وتحفظ الملف المعدل بشكل output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
