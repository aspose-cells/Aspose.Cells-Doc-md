---
title: إظهار وإخفاء أعمدة الصفوف وأشرطة التمرير
type: docs
weight: 20
url: /ar/net/show-and-hide-rows-columns-and-scroll-bars/
---
{{% alert color="primary" %}}

يوفر Aspose.Cells طرقًا للتحكم في رؤية الصفوف والعمود وأشرطة التمرير الخاصة بورقة العمل.

{{% /alert %}}

## **إظهار وإخفاء الصفوف والأعمدة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح للمطورين بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة توفر أ[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) مجموعة تمثل جميع الخلايا في ورقة العمل. ال[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)توفر المجموعة عدة طرق لإدارة الصفوف أو الأعمدة في ورقة العمل. تمت مناقشة القليل من هذه أدناه.

### **إظهار الصفوف والأعمدة**

 يمكن للمطورين إظهار أي صف أو عمود مخفي عن طريق استدعاء[**UnhideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhiderow) و[**UnhideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/unhidecolumn) طرق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)جمع على التوالي. تأخذ كلتا الطريقتين معلمتين:

- **فهرس الصف أو العمود** - فهرس صف أو عمود يُستخدم لإظهار الصف أو العمود المحدد.
- **ارتفاع الصف أو عرض العمود** - ارتفاع الصف أو عرض العمود المخصص للصف أو العمود بعد الإخفاء.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-UnhidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

أثناء جعل عمود مخفي مرئيًا ، إذا كنت بحاجة إلى استعادته إلى العرض المعين مسبقًا أو عرضه الأصلي ، فيرجى إظهار العمود بعرض سلبي. على سبيل المثال: ورقة عمل .Cells.UnhideColumn (5، -1)

{{% /alert %}}

### **إخفاء الصفوف والأعمدة**

 يمكن للمطورين إخفاء صف أو عمود عن طريق استدعاء[**HideRow**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderow) و[**HideColumn**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumn) طرق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)جمع على التوالي. تأخذ كلتا الطريقتين فهرس الصف والعمود كمعامل لإخفاء الصف أو العمود المحدد.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingRowsAndColumns-1.cs" >}}

{{% alert color="primary" %}}

من الممكن أيضًا إخفاء صف أو عمود عن طريق ضبط ارتفاع الصف أو عرض العمود على 0 على التوالي.

{{% /alert %}}

### **إخفاء عدة صفوف وأعمدة**

 يمكن للمطورين إخفاء صفوف أو أعمدة متعددة مرة واحدة عن طريق استدعاء[**إخفاء الصفوف**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hiderows) و[**HideColumns**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/hidecolumns) طرق[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells)جمع على التوالي. تأخذ كلتا الطريقتين صف البداية أو فهرس العمود وعدد الصفوف أو الأعمدة التي يجب إخفاؤها كمعلمات.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Hiding-HidingMultipleRowsAndColumns-1.cs" >}}

## **إظهار وإخفاء أشرطة التمرير**

تُستخدم أشرطة التمرير للتنقل عبر محتويات أي ملف. عادة ، هناك نوعان من أشرطة التمرير:

- أشرطة التمرير العمودية
- أشرطة التمرير الأفقية

يوفر Microsoft Excel أيضًا أشرطة تمرير أفقية ورأسية بحيث يمكن للمستخدمين التمرير عبر محتويات ورقة العمل. باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية كلا النوعين من أشرطة التمرير في ملفات Excel.

### **التحكم في رؤية أشرطة التمرير**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) توفر class مجموعة كبيرة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية أشرطة التمرير ، استخدم ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) و[**WorkbookSettings.SHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)الخصائص.[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) و[**WorkbookSettings.SHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) هي خصائص منطقية ، مما يعني أن هذه الخصائص يمكن تخزينها فقط**حقيقي** أو**خاطئة** القيم.

#### **جعل أشرطة التمرير مرئية**

 اجعل أشرطة التمرير مرئية من خلال ضبط ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) أو[**WorkbookSettings.SHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) الملكية ل**حقيقي**.

#### **إخفاء أشرطة التمرير**

 إخفاء أشرطة التمرير عن طريق ضبط[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي'[**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) أو[**WorkbookSettings.SHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) الملكية ل**خاطئة**.

**عينة من الرموز**

يوجد أدناه رمز كامل يفتح ملف Excel ، book1.xls ، ويخفي شريطي التمرير ثم يحفظ الملف المعدل كـ output.xls.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-DisplayHideScrollBars-1.cs" >}}
