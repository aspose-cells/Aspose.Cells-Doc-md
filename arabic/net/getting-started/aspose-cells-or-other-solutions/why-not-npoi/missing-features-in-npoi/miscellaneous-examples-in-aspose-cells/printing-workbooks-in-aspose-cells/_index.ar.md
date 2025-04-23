---
title: طباعة دفاتر العمل في Aspose.Cells
type: docs
weight: 20
url: /ar/net/printing-workbooks-in-aspose-cells/
---

## **Aspose.Cells - طباعة دفاتر العمل**
بعد الانتهاء من إنشاء ورقة البيانات الخاصة بك، من المحتمل أن ترغب في طباعة نسخة ورقية من الورقة لحاجتك. عند الطباعة، يفترض MS Excel أنك تريد طباعة منطقة ورقة العمل بأكملها ما لم تحدد تحديدك.

طباعة ورقة البيانات

**C#**

{{< highlight cs >}}

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
## **تحميل رمز التشغيل**
تحميل **طباعة دفاتر العمل** من أي من المواقع المذكورة أدناه للتعليم الاجتماعي للبرمجة:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Printing.Workbooks.Aspose.Cells.zip)

{{% alert color="primary" %}} 

للحصول على مزيد من التفاصيل، قم بزيارة [طباعة دفاتر العمل](/cells/ar/net/printing-workbooks/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
