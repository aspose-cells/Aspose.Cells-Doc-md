---
title: أضف البيانات في Cells
type: docs
weight: 10
url: /ar/net/add-data-in-cells/
---
## **Aspose.Cells - أضف بيانات في Cells**
يوفر Aspose.Cells فئة ، مصنف ، يمثل ملف إكسل Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة ورقة العمل. توفر فئة ورقة العمل مجموعة الخلايا. يمثل كل عنصر في مجموعة Cells عنصرًا من فئة Cell.

**C#**

{{< highlight "cs" >}}

 // إنشاء كائن مصنف

مصنف المصنف = مصنف جديد () ؛

// الوصول إلى ورقة العمل المضافة في ملف Excel

ورقة عمل ورقة العمل = workbook.Worksheets [0] ؛

كثافة العمليات س = 1 ؛

 لـ (int i = 1 ؛ i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - أضف البيانات في Cells**
في NPOI row.createCell (1). يمكن استخدام setCellValue لإضافة البيانات في الخلايا.

**C#**

{{< highlight "cs" >}}

 مصنف IWorkbook = جديد XSSFWorkbook () ؛

ISheet sheet1 = workbook.CreateSheet ("Sheet1") ؛

sheet1.CreateRow (0) .CreateCell (0) .SetCellValue ("This is a Sample") ؛

كثافة العمليات س = 1 ؛

 لـ (int i = 1 ؛ i<= 15; i++)

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
## **قم بتنزيل كود التشغيل**
 تحميل**أضف البيانات في Cells** من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[إضافة البيانات إلى Cells](/cells/ar/net/add-data-in-cells/).

{{% /alert %}}
