---
title: احفظ كل ورقة عمل في ملف PDF مختلف
type: docs
weight: 10
url: /ar/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - احفظ كل ورقة عمل في ملف PDF مختلف**
يدعم Aspose.Cells تحويل ملفات XLS (التي تحتوي على صور ومخططات وما إلى ذلك) إلى مستندات PDF. يمكن أن يعمل Aspose.Cells for .NET بشكل مستقل لتحويل جدول بيانات إلى مستند Pdf ولن تحتاج إلى استخدام Aspose.Pdf for .NET للتحويل بعد الآن. لا يتطلب التحويل إنشاء / استخدام أي ملف (ملفات) مؤقتة أيضًا حيث يمكن إجراء العملية بأكملها في الذاكرة.

**C#**

{{< highlight "cs" >}}

 // إنشاء مصنف جديد وافتح ملف Excel

// ملف من موقعه

مصنف المصنف = مصنف جديد ("../../ data / test.xlsx")؛

// احصل على عدد أوراق العمل في المصنف

int sheetCount = workbook.Worksheets.Count ؛

// اجعل جميع الأوراق غير مرئية باستثناء ورقة العمل الأولى

 لـ (int i = 1 ؛ i< workbook.Worksheets.Count; i++)

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
## **قم بتنزيل كود التشغيل**
 تحميل**احفظ كل ورقة عمل في ملف PDF مختلف** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[احفظ كل ورقة عمل في ملف PDF مختلف](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
