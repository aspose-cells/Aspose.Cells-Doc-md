---
title: طباعة صفحات العمل في xlsx4j
type: docs
weight: 30
url: /ar/java/printing-workbooks-in-xlsx4j/
---

## **Aspose.Cells - طباعة دفاتر العمل**
بعد الانتهاء من إنشاء ورقة البيانات الخاصة بك، من المحتمل أن ترغب في طباعة نسخة ورقية من الورقة لحاجتك. عند الطباعة، يفترض MS Excel أنك تريد طباعة منطقة ورقة العمل بأكملها ما لم تحدد تحديدك.

**طباعة ورقة العمل**

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

**طباعة صفحات العمل**

**Java**

{{< highlight java >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [طباعة الدفاتر ](/cells/ar/java/printing-workbooks).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
