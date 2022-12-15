---
title: عرض أو إخفاء أشرطة التمرير في Aspose.Cells
type: docs
weight: 70
url: /ar/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

تُستخدم أشرطة التمرير كثيرًا للتنقل في محتويات أي ملف. عادة ، هناك نوعان من أشرطة التمرير:

- أشرطة التمرير العمودية
- أشرطة التمرير الأفقية

يوفر Microsoft Excel أيضًا أشرطة تمرير أفقية ورأسية بحيث يمكن للمستخدمين التمرير عبر محتويات ورقة العمل. باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية كلا النوعين من أشرطة التمرير في ملفات Excel.

{{% /alert %}}

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) توفر class مجموعة كبيرة من الخصائص والأساليب لإدارة ملف Excel. للتحكم في رؤية أشرطة التمرير ، استخدم ملف[**إعدادات المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) صف دراسي'[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) و[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) الخصائص.[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) و[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) هي خصائص منطقية ، مما يعني أن هذه الخصائص يمكن تخزينها فقط**حقيقي** أو**خاطئة** القيم.

يوجد أدناه رمز كامل يفتح ملف Excel ، book1.xls ، ويخفي شريطي التمرير ثم يحفظ الملف المعدل كـ output.xls.

توضح لقطة الشاشة أدناه ملف Book1.xls الذي يحتوي على شريطي التمرير. يتم حفظ الملف المعدل كملف output.xls ، كما هو موضح أدناه.

**Book1.xls: ملف Excel قبل أي تعديل**

![ما يجب القيام به: image_بديل_نص](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: ملف Excel بعد التعديل**

![ما يجب القيام به: image_بديل_نص](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

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

## **تحميل كود الجري**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
