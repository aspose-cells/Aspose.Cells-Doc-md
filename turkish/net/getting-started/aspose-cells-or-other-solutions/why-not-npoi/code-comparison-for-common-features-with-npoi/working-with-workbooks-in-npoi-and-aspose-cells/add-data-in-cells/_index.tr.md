---
title: Cells'e Veri Ekle
type: docs
weight: 10
url: /tr/net/add-data-in-cells/
description: Bu makalede, Aspose.Cells for .NET API'leri kullanılarak Cells'e nasıl Veri Ekleneceği açıklanmaktadır.
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **Aspose.Cells for .NET'i Kullanarak Cells'e Veri Ekleme**
Aspose.Cells, Microsoft Excel dosyasını temsil eden Çalışma Kitabı adlı bir sınıf sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişime izin veren bir WorksheetCollection içerir. Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı bir Cellscollection sağlar. Cells koleksiyonundaki her öğe, Cell sınıfının bir nesnesini temsil eder.

**C#**

{{< highlight "cs" >}}

 //Bir Çalışma Kitabı nesnesinin başlatılması

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı();

//Excel dosyasına eklenen çalışma sayfasına erişim

Çalışma sayfası çalışma sayfası = çalışma kitabı.Çalışma sayfaları[0];

int x = 1;

for (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF - Cells'e Veri Ekle**
NPOI'de row.createCell(1).setCellValue hücrelere veri eklemek için kullanılabilir.

**C#**

{{< highlight "cs" >}}

 IWorkbook çalışma kitabı = yeni XSSFWorkbook();

ISheet sayfa1 = çalışma kitabı.CreateSheet("Sayfa1");

Sheet1.CreateRow(0).CreateCell(0).SetCellValue("Bu bir Örnektir");

int x = 1;

for (int i = 1; i<= 15; i++)

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
##  **Çalışan Kodu İndir**
 İndirmek**Cells'e Veri Ekle** Aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için şu adresi ziyaret edin:[Cells'e Veri Ekleme](/cells/tr/net/add-data-in-cells/).

{{% /alert %}}
