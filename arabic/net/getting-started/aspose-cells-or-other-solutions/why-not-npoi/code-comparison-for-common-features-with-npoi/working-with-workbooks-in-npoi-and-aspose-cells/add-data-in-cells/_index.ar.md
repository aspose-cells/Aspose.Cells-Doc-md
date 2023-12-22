---
title: أضف البيانات في Cells
type: docs
weight: 10
url: /ar/net/add-data-in-cells/
description: تشرح هذه المقالة كيفية إضافة البيانات في Cells باستخدام Aspose.Cells for .NET APIs.
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **كيفية إضافة البيانات في Cells باستخدام Aspose.Cells for .NET**
يوفر Aspose.Cells فئة، Workbook، التي تمثل ملف Excel Microsoft. تحتوي فئة المصنف على WorksheetCollection الذي يسمح بالوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. توفر فئة ورقة العمل مجموعة خلايا. يمثل كل عنصر في مجموعة Cells كائنًا من فئة Cell.

**C#**

{{< highlight "cs" >}}

 // إنشاء كائن مصنف

مصنف المصنف = مصنف جديد ()؛

// الوصول إلى ورقة العمل المضافة في ملف Excel

ورقة عمل ورقة العمل = Workbook.Worksheets[0];

كثافة العمليات س = 1؛

من أجل (int i = 1؛ i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF - أضف البيانات في Cells**
في NPOI، يمكن استخدام Row.createCell(1).setCellValue لإضافة البيانات في الخلايا.

**C#**

{{< highlight "cs" >}}

 IWorkbook Workbook = new XSSFWorkbook();

ISheet Sheet1 = Workbook.CreateSheet("Sheet1");

Sheet1.CreateRow(0).CreateCell(0).SetCellValue("هذه عينة");

كثافة العمليات س = 1؛

من أجل (int i = 1؛ i<= 15; i++)

{

	IRow row = sheet1.CreateRow(i);

	for (int j = 0; j < 15; j++)

	{

		row.CreateCell(j).SetCellValue(x++);

	}

}

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
##  **تحميل كود التشغيل**
 تحميل**أضف البيانات في Cells** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل، قم بزيارة[إضافة البيانات إلى Cells](/cells/ar/net/add-data-in-cells/).

{{% /alert %}}
