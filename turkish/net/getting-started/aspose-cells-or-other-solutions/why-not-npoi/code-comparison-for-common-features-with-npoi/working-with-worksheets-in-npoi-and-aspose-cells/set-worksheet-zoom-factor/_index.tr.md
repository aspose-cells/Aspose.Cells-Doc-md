---
title: Çalışma Sayfası Yakınlaştırma Faktörünü Ayarla
type: docs
weight: 80
url: /tr/net/set-worksheet-zoom-factor/
---
## **Aspose.Cells - Çalışma Sayfası Yakınlaştırma Faktörünü Ayarla**
**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

worksheet.Zoom = 75;

//Saving the Excel file

workbook.Save("../../data/newWorksheet.xls");


{{< /highlight >}}
## **NPOI - HSSF XSSF - Çalışma Sayfası Yakınlaştırma Faktörünü Ayarla**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **Çalışan Kodu İndir**
 İndirmek**Çalışma Sayfası Yakınlaştırma Faktörünü Ayarla** aşağıda belirtilen sosyal kodlama sitelerinden herhangi birini oluşturun:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Çalışma Sayfalarıyla Çalışmak](/cells/tr/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
