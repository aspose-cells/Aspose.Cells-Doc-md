---
title: احفظ كل ورقة عمل إلى PDF مختلف باستخدام Aspose.Cells
type: docs
weight: 80
url: /ar/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
---
## **Aspose.Cells - احفظ كل ورقة عمل في ملف PDF مختلف**
يدعم Aspose.Cells تحويل ملفات XLS (التي تحتوي على صور ومخططات وما إلى ذلك) إلى مستندات PDF. يمكن أن يعمل Aspose.Cells for Java بشكل مستقل لتحويل جدول بيانات إلى مستند Pdf ولن تحتاج إلى استخدام Aspose.Pdf for Java للتحويل بعد الآن. لا يتطلب التحويل إنشاء / استخدام أي ملف (ملفات) مؤقتة أيضًا حيث يمكن إجراء العملية بأكملها في الذاكرة.

**Java**

{{< highlight "java" >}}

// احصل على مسار ملف Excel

String filePath = dataDir + "workbook.xlsx" ؛

// إنشاء مصنف جديد وافتح ملف Excel

// ملف من موقعه

مصنف المصنف = مصنف جديد (filePath) ؛

// احصل على عدد أوراق العمل في المصنف

int sheetCount = workbook.getWorksheets (). getCount () ؛

// اجعل جميع الأوراق غير مرئية باستثناء ورقة العمل الأولى

 لـ (int i = 1 ؛ i< workbook.getWorksheets().getCount(); i++)

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
## **تحميل كود الجري**
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[احفظ كل ورقة عمل في ملف PDF مختلف](/cells/ar/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
