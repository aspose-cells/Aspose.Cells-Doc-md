---
title: Cells'de Veri Ekle
type: docs
weight: 10
url: /tr/net/add-data-in-cells/
---
## **Aspose.Cells - Cells'de Veri Ekle**
Aspose.Cells, bir Microsoft Excel dosyasını temsil eden bir Çalışma Kitabı sınıfı sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası, Worksheet sınıfı tarafından temsil edilir. Worksheet sınıfı bir Cellscollection sağlar. Cells koleksiyonundaki her öğe, Cell sınıfının bir nesnesini temsil eder.

**C#**

{{< highlight "cs" >}}

 //Çalışma Kitabı nesnesinin somutlaştırılması

Çalışma kitabı çalışma kitabı = yeni Çalışma Kitabı();

//Eklenen çalışma sayfasına Excel dosyasından erişim

Çalışma sayfası çalışma sayfası = çalışma kitabı.Çalışma Sayfaları[0];

int x = 1;

 için (int ben = 1; ben<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - Cells'de Veri Ekle**
NPOI'de row.createCell(1).setCellValue, hücrelere veri eklemek için kullanılabilir.

**C#**

{{< highlight "cs" >}}

 IWorkbook çalışma kitabı = new XSSFWorkbook();

ISheet sayfası1 = çalışma kitabı.CreateSheet("Sayfa1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("Bu Bir Örnektir");

int x = 1;

 için (int ben = 1; ben<= 15; i++)

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
 İndirmek**Cells'de Veri Ekle** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Cells'e Veri Ekleme](/cells/tr/net/add-data-in-cells/).

{{% /alert %}}
