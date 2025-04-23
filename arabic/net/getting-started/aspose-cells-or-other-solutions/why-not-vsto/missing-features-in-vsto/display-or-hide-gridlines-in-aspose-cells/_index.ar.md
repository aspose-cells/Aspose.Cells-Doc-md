---
title: عرض أو إخفاء خطوط الشبكة في Aspose.Cells
type: docs
weight: 50
url: /ar/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

جميع ورق العمل في إكسل لديها خطوط شبكة افتراضيًا. إنها تساعد في تحديد الخلايا، بحيث يكون من السهل إدخال البيانات في الخلايا المعينة. تمكننا خطوط الشبكة من عرض ورق عمل كمجموعة من الخلايا، حيث يمكن الوصول إلى كل خلية بسهولة.

{{% /alert %}}

## **التحكم في رؤية خطوط الشبكة**

يوفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) التي تمثل ملف Microsoft Excel. يحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورق العمل في ملف Excel.

يُمثل ورق العمل من خلال فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورق العمل. للتحكم في رؤية خطوط الشبكة، استخدم خاصية [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) لفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). الخاصية [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) هي خاصية بوليانية، مما يعني أنه يمكنها تخزين قيمة **صحيحة** أو **خاطئة** فقط.

يتم توضيح مثال كامل أدناه يُظهر استخدام خاصية [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) لفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) لإخفاء خطوط الشبكة للورقة العمل الأولى في ملف Excel.

في اللقطة أدناه، يمكنك رؤية أن ملف Book1.xls يحتوي على ثلاث ورقات عمل: Sheet1، Sheet2 و Sheet3. جميع أوراق العمل تحتوي على خطوط شبكة.

**Book1.xls: عرض ورقة العمل قبل التعديل** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

تم فتح ملف Book1.xls باستخدام فئة Workbook وتم إخفاء خطوط الشبكة في ورقة العمل الأولى. تم حفظ الملف المعدل بشكل مخرج.xls.

**output.xls: ورقة العمل بعد التعديل** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **تحميل رمز عينة**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
