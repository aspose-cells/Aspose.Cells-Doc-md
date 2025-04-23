---
title: إضافة بيانات في الخلايا
type: docs
weight: 10
url: /ar/net/add-data-in-cells/
description: يشرح هذا المقال كيفية إضافة البيانات في الخلايا باستخدام واجهات برمجة التطبيقات Aspose.Cells for .NET.
keywords: إضافة بيانات في الخلايا بلغة C#، إدراج البيانات في ورقة العمل بلغة C#، تعيين بيانات الخلية بلغة C#.
---


## **كيفية إضافة البيانات في الخلايا باستخدام Aspose.Cells for .NET**
يوفر Aspose.Cells فئةً تسمى الكتاب، تمثل ملف Microsoft Excel. تحتوي الفئة Workbook على مجموعة ورق العمل تتيح الوصول إلى كل ورق العمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة فئة Worksheet. توفر فئة Worksheet مجموعة من الخلايا. يُمثل كل عنصر في مجموعة الخلايا كائنًا من فئة الخلية.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

int x = 1;

for (int i = 1; i <= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - إضافة بيانات في الخلايا**
يمكن استخدام row.createCell(1).setCellValue في NPOI لإضافة البيانات في الخلايا.

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("This is a Sample");

int x = 1;

for (int i = 1; i <= 15; i++)

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
## **تحميل رمز التشغيل**
قم بتنزيل **إضافة بيانات في الخلايا** من أي من المواقع الاجتماعية المذكورة أدناه:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [إضافة البيانات إلى الخلايا](/cells/ar/net/add-data-in-cells/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
