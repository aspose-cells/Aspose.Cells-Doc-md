---
title: طباعة كتب العمل في Aspose.Cells
type: docs
weight: 20
url: /ar/net/printing-workbooks-in-aspose-cells/
---
## **Aspose.Cells - طباعة دفاتر العمل**
بعد الانتهاء من إنشاء جدول البيانات ، قد ترغب في طباعة نسخة ورقية من الورقة حسب حاجتك. عندما تقوم بالطباعة ، يفترض MS Excel أنك تريد طباعة منطقة ورقة العمل بأكملها ما لم تحدد اختيارك.

ورقة عمل الطباعة

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Create an object for ImageOptions

ImageOrPrintOptions imgOptions = new ImageOrPrintOptions();

//Get the first worksheet

Worksheet sheet = workbook.Worksheets[0];

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.ToPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
 تحميل**دفاتر الطباعة** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[دفاتر الطباعة](/cells/ar/net/printing-workbooks/).

{{% /alert %}}
