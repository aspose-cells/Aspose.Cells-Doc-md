---
title: عرض أو إخفاء رؤوس أعمدة الصفوف في Aspose.Cells
type: docs
weight: 60
url: /ar/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

تتكون جميع أوراق العمل في ملف Excel من خلايا مرتبة في صفوف وأعمدة. تحتوي جميع الصفوف والأعمدة على قيم فريدة تُستخدم لتعريفها ولتعريف الخلايا الفردية. على سبيل المثال ، يتم ترقيم الصفوف - 1 ، 2 ، 3 ، 4 ، وما إلى ذلك - ويتم ترتيب الأعمدة أبجديًا - A ، B ، C ، D ، إلخ. يتم عرض قيم الصفوف والأعمدة في الرؤوس. باستخدام Aspose.Cells ، يمكن للمطورين التحكم في رؤية رؤوس الصفوف والأعمدة هذه.

{{% /alert %}}

## **التحكم في رؤية أوراق العمل**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. للتحكم في رؤية رؤوس الصفوف والأعمدة ، استخدم ملحق[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) منشأه.[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) هي خاصية منطقية ، مما يعني أنه يمكنها فقط تخزين ملف**حقيقي** أو**خاطئة** القيمة.

 ويرد أدناه مثال كامل يوضح كيفية استخدام ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) الخاصية لإخفاء رؤوس الصفوف والأعمدة في ورقة العمل الأولى في ملف.

تظهر لقطة الشاشة Book1.xls ، ملف الإدخال. يحتوي على ثلاث أوراق عمل: الورقة 1 والورقة 2 والورقة 3. تعرض كل ورقة عمل رؤوس الصفوف والأعمدة.

**Book1.xls: ورقة عمل قبل التعديل**

![ما يجب القيام به: image_بديل_نص](display-or-hide-row-column-headers-in-aspose-cells_1.png)

يتم فتح Book1.xls عن طريق استدعاء الأسلوب Open لفئة المصنفات ويتم إخفاء رؤوس الصفوف والأعمدة في ورقة العمل الأولى. يتم حفظ الملف المعدل باسم output.xls.

**Output.xls: ورقة عمل بعد التعديل** 

![ما يجب القيام به: image_بديل_نص](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
