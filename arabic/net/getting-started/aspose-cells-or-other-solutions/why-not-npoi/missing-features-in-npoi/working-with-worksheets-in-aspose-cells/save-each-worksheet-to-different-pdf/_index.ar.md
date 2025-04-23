---
title: حفظ كل ورقة عمل إلى ملف PDF مختلف
type: docs
weight: 10
url: /ar/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - حفظ كل ورقة عمل إلى ملف PDF مختلف**
Aspose.Cells تدعم تحويل ملفات XLS (التي تحتوي على صور، رسوم بيانية إلخ) إلى مستندات PDF. يمكن أن يعمل Aspose.Cells for .NET بشكل مستقل عن تحويل جدول بيانات إلى مستند Pdf ولا يلزمك استخدام Aspose.Pdf for .NET للتحويل بعد الآن. لا يتطلب التحويل إنشاء / استخدام أي ملف(ات) مؤقت(ة) أيضًا حيث يمكن إنجاز العملية بأكملها في الذاكرة.

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **تحميل رمز التشغيل**
تحميل **حفظ كل ورقة عمل إلى ملف PDF مختلف** من أيّ من المواقع الرمزية الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [حفظ كل ورقة عمل إلى ملف PDF مختلف](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
