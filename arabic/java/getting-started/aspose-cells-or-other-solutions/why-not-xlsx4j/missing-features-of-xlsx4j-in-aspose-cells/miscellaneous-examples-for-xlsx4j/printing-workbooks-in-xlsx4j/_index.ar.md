---
title: طباعة مصنفات في xlsx4j
type: docs
weight: 30
url: /ar/java/printing-workbooks-in-xlsx4j/
---
## **Aspose.Cells - طباعة دفاتر العمل**
بعد الانتهاء من إنشاء جدول البيانات ، قد ترغب في طباعة نسخة ورقية من الورقة حسب حاجتك. عندما تقوم بالطباعة ، يفترض MS Excel أنك تريد طباعة منطقة ورقة العمل بأكملها ما لم تحدد اختيارك.

**ورقة عمل الطباعة**

**Java**

{{< highlight "java" >}}

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

**كتاب الطباعة**

**Java**

{{< highlight "java" >}}

 //Create a WorkbookRender object with respect to your workbook

WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook

wr.toPrinter("Samsung ML-1520 Series");

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/printworkbook/AsposePrintWorkbook.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[ دفاتر الطباعة](/cells/ar/java/printing-workbooks).

{{% /alert %}}
