---
title: عرض أو إخفاء شريطي التمرير في Aspose.Cells
type: docs
weight: 70
url: /ar/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

شريطي التمرير يُستخدمان بشكل كبير لتصفح محتويات أي ملف. عادةً، هناك نوعان من شريطي التمرير:

- شرائط التمرير العمودية
- شرائط التمرير الأفقية

توفر Microsoft Excel أيضًا شرائط تمرير أفقية وعمودية بحيث يمكن للمستخدمين التمرير من خلال محتويات ورقة العمل. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية كلا أنواع شرائط التمرير في ملفات Excel.

{{% /alert %}}

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Excel. توفر فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) مجموعة واسعة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية شريطي التمرير، استخدم خصائص فئة [**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) و [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible). [**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) و [**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) هما خصائص بوليانية، مما يعني أنه يمكن لهذه الخصائص أن تخزن القيم **صح** أو **خطأ** فقط.

فيما يلي كود كامل يفتح ملف Excel، book1.xls، يخفي كلا شريطي التمرير ثم يحفظ الملف المعدل بصيغة output.xls.

يُظهر اللقطة الشاشية أدناه ملف Book1.xls الذي يحتوي على كلا شريطي التمرير. الملف المعدل يتم حفظه بصيغة output.xls كما هو موضح أدناه أيضًا.

**Book1.xls: ملف Excel قبل أي تعديل**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: ملف Excel بعد التعديل**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **تحميل رمز عينة**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
