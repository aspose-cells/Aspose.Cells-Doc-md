---
title: طباعة الدفاتر باستخدام Aspose.Cells
type: docs
weight: 20
url: /ar/java/printing-workbooks-using-aspose-cells/
---

## **Aspose.Cells - طباعة دفاتر العمل**
بعد الانتهاء من إنشاء ورقة البيانات الخاصة بك، من المحتمل أن ترغب في طباعة نسخة ورقية من الورقة لحاجتك. عند الطباعة، يفترض MS Excel أنك تريد طباعة منطقة ورقة العمل بأكملها ما لم تحدد تحديدك.

طباعة ورقة البيانات

**Java**

{{< highlight java >}}

 //Instantiate a new workbook

Workbook book = new Workbook(dataDir + "AsposeDataInput.xls");

//Create an object for ImageOptions

ImageOrPrintOptions  imgOptions = new ImageOrPrintOptions ();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Create a SheetRender object with respect to your desired sheet

SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet

sr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}

طباعة الدفتر

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **تحميل رمز التشغيل**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [طباعة الدفاتر](/cells/ar/java/printing-workbooks).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
