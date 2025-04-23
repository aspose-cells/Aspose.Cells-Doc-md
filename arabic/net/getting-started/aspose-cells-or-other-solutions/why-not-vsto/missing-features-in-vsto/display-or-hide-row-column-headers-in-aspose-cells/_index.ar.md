---
title: عرض أو إخفاء رؤوس الصف والعمود في Aspose.Cells
type: docs
weight: 60
url: /ar/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

جميع ورقات العمل في ملف Excel مكونة من خلايا مرتبة في صفوف وأعمدة. جميع الصفوف والأعمدة لها قيم فريدة يتم استخدامها لتحديدها، وتحديد الخلايا الفردية. على سبيل المثال، يتم ترقيم الصفوف – 1، 2، 3، 4، إلخ – وترتيب الأعمدة ترتيباً أبجديا – A، B، C، D، إلخ. تعرض القيم الصف والعمود في الرؤوس. باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤوس الصف والعمود هؤلاء.

{{% /alert %}}

## **التحكم في رؤية ورقات العمل**

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، التي تمثل ملف Excel لشركة Microsoft. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقات العمل. للتحكم في رؤوس الصف والعمود، استخدم خاصية [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) لفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) هي خاصية منطقية، مما يعني أنه يمكن تخزين قيمة **صحيح** أو **خطأ** فقط.

يتم تقديم مثال كامل أدناه يوضح كيفية استخدام خاصية [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) لفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) لإخفاء رؤوس الصف والعمود على ورقة العمل الأولى في ملف.

يظهر لقطة الشاشة ملف Book1.xls، الملف الداخلي. يحتوي على ثلاث ورقات عمل: ورقة1، ورقة2 وورقة3. تعرض كل ورقة عمل رؤوس الصف والعمود.

**Book1.xls: ورقة العمل قبل التعديل**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

يتم فتح ملف Book1.xls عن طريق استدعاء طريقة Open لفئة Workbook ويتم إخفاء رؤوس الصف والعمود على ورقة العمل الأولى. تم حفظ الملف المعدل بشكل مخرج.xls.

**output.xls: ورقة العمل بعد التعديل** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
