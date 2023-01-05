---
title: Yeni Çalışma Kitabı Oluştur
type: docs
weight: 20
url: /tr/net/create-new-workbook/
---
## **Aspose.Cells - Yeni Çalışma Kitabı Oluştur**
Çalışma kitabı sınıfı basit kullanım için mevcuttur

**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Yeni Çalışma Kitabı Oluştur**
Workbook sınıfını kullanarak yeni Workbook oluşturun ve FileOutputStream kullanarak kaydedin.

**C#**

{{< highlight "cs" >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Yeni Çalışma Kitabı Oluştur** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
