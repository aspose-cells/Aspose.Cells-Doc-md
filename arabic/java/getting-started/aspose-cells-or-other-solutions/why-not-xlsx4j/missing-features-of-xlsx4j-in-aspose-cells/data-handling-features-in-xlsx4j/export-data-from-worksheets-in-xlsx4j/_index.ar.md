---
title: تصدير البيانات من أوراق العمل في xlsx4j
type: docs
weight: 20
url: /ar/java/export-data-from-worksheets-in-xlsx4j/
---
## **Aspose.Cells - تصدير البيانات من أوراق العمل**
لا يتيح Aspose.Cells لمستخدميه استيراد البيانات إلى أوراق العمل من مصادر البيانات الخارجية فحسب ، بل يسمح لهم أيضًا بتصدير بيانات ورقة العمل إلى مصفوفة.

**Java**

{{< highlight "java" >}}

 // إنشاء دفق ملف يحتوي على ملف Excel ليتم فتحه

FileInputStream fstream = جديد FileInputStream (dataDir + "workbook.xls") ؛

// إنشاء كائن مصنف

مصنف المصنف = مصنف جديد (fstream) ؛

// الوصول إلى ورقة العمل الأولى في ملف Excel

ورقة عمل ورقة العمل = workbook.getWorksheets (). get (0)؛

// تصدير محتويات 7 صفوف وعمودين بدءًا من الخلية الأولى إلى المصفوفة.

كائن dataTable [] [] = workheet.getCells (). exportArray (4،0،7،8) ؛

 لـ (int i = 0 ؛ i< dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

{{< /highlight >}}
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[تصدير البيانات من أوراق العمل](/java/exporting-data-from-worksheets).

{{% /alert %}}
