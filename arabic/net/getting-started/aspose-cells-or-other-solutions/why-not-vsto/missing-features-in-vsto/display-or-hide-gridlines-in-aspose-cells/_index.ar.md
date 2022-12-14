---
title: عرض أو إخفاء خطوط الشبكة في Aspose.Cells
type: docs
weight: 50
url: /ar/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

تحتوي جميع أوراق عمل Excel على خطوط شبكة بشكل افتراضي. إنها تساعد في تحديد الخلايا ، بحيث يسهل إدخال البيانات في خلايا معينة. تمكننا خطوط الشبكة من عرض ورقة العمل كمجموعة من الخلايا ، حيث يمكن التعرف على كل خلية بسهولة.

{{% /alert %}}

## **التحكم في رؤية خطوط الشبكة**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) توفر class مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. للتحكم في رؤية خطوط الشبكة ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) صف دراسي'[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) منشأه.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) هي خاصية منطقية ، مما يعني أنه يمكنها فقط تخزين ملف**حقيقي** أو**خاطئة** القيمة.

 ويرد أدناه مثال كامل يوضح استخدام[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) ممتلكات[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) فئة لإخفاء خطوط الشبكة الخاصة بورقة العمل الأولى من ملف Excel.

في لقطة الشاشة أدناه ، يمكنك أن ترى أن ملف Book1.xls يحتوي على ثلاث أوراق عمل: Sheet1 و Sheet2 و Sheet3. تحتوي جميع أوراق العمل على خطوط شبكية.

**Book1.xls: طريقة عرض ورقة العمل قبل التعديل** 

![ما يجب القيام به: image_بديل_نص](display-or-hide-gridlines-in-aspose-cells_1.png)

يتم فتح الملف Book1.xls باستخدام فئة المصنف وتكون خطوط الشبكة في ورقة العمل الأولى مخفية. يتم حفظ الملف المعدل باسم output.xls.

**Output.xls: ورقة عمل بعد التعديل** 

![ما يجب القيام به: image_بديل_نص](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **قم بتنزيل كود التشغيل**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **تنزيل نموذج التعليمات البرمجية**

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
