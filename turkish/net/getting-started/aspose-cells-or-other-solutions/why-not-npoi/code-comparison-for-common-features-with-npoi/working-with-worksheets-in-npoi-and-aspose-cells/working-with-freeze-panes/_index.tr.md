---
title: Dondurulmuş Panellerle Çalışma
type: docs
weight: 100
url: /tr/net/working-with-freeze-panes/
---

## **Aspose.Cells - Dondurulmuş Panellerle Çalışma**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

worksheet.FreezePanes(2, 2, 2, 0);

workbook.Save("output-FreezeFile-Aspose.Cells.xls");


{{< /highlight >}}

{{% alert color="primary" %}} 

Daha fazla bilgi için [FreezePanes Method](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index) sayfasını ziyaret edin.

{{% /alert %}} 
## **NPOI - HSSF XSSF - Dondurulmuş Panellerle Çalışma**
**C#**

{{< highlight cs >}}

 HSSFWorkbook hssfworkbook = new HSSFWorkbook();

ISheet sheet1 = hssfworkbook.CreateSheet("new sheet");

ISheet sheet2 = hssfworkbook.CreateSheet("second sheet");

ISheet sheet3 = hssfworkbook.CreateSheet("third sheet");

// Freeze just one row

sheet1.CreateFreezePane(0, 2, 0, 2);

// Freeze just one column

sheet2.CreateFreezePane(2, 0, 2, 0);

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.CreateFreezePane(2, 2);

FileStream file = new FileStream(@"output-FreezeFile-NPOI.xls", FileMode.Create);

hssfworkbook.Write(file);

file.Close();


{{< /highlight >}}
## **Çalışan Kodu İndir**
Aşağıda belirtilen sosyal kodlama sitelerinden **Dondurulmuş Panellerle Çalışma** formunu indirin:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.3/Freeze.Panes.zip)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Çalışma Sayfaları İle Çalışma](/cells/tr/net/working-with-worksheets-in-npoi-and-aspose-cells/) ziyaret edin.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
