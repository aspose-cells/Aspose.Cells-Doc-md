---
title: Hücrelere Veri Ekleme
type: docs
weight: 10
url: /tr/net/add-data-in-cells/
description: Bu makale, Aspose.Cells for .NET API ları kullanarak Hücrelere Veri Ekleme işlemini açıklar.
keywords: C# ile Hücrelere Veri Ekleme, C# ile Çalışma Sayfasına Veri Ekleme, C# te Hücrenin Verisini Ayarlama.
---


## ****Aspose.Cells for .NET** ile Hücrelere Veri Eklemenin Nasıl Yapılacağı**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir Workbook sınıfı sağlar. Workbook sınıfı, Excel dosyasındaki her bir çalışma sayfasına erişmeyi sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı, Cells koleksiyonunu sağlar. Cells koleksiyonundaki her öğe, Cell sınıfının bir nesnesini temsil eder.

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
## **NPOI HSSF XSSF - Hücrelere Veri Ekleme**
NPOI'de row.createCell(1).setCellValue metodu hücrelere veri eklemek için kullanılabilir.

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
## **Çalışan Kodu İndir**
Aşağıda belirtilen herhangi bir sosyal kodlama sitesinden **Hücrelere Veri Ekleme** formunu indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Hücrelere Veri Ekleme](/cells/tr/net/add-data-in-cells/)ne bakın.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
