---
title: حفظ كل ورق عمل في مستند PDF مختلف في xlsx4j
type: docs
weight: 50
url: /ar/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---

## **Aspose.Cells - حفظ كل ورقة عمل إلى ملف PDF مختلف**
تدعم Aspose.Cells تحويل ملفات XLS (التي تحتوي على صور ورسومات إلخ) إلى وثائق PDF. يمكن لـ Aspose.Cells for Java العمل بشكل مستقل لتحويل جدول بيانات إلى مستند Pdf ولا تحتاج إلى استخدام Aspose.Pdf for Java للتحويل بعد الآن. التحويل لا يتطلب إنشاء / استخدام أي ملف (ملفات) مؤقتة أيضًا حيث يمكن القيام بكل العملية في الذاكرة.

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [حفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
