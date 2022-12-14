---
title: 使用页眉和页脚
type: docs
weight: 110
url: /zh/net/working-with-headers-and-footers/
---
## **Aspose.Cells - 使用页眉和页脚**
**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = worksheet.PageSetup;

//Setting worksheet name at the left  header

pageSetup.SetHeader(0, "&A");

//Setting current date and current time at the central header

//and changing the font of the header

pageSetup.SetHeader(1, "&\"Times New Roman,Bold\"&D-&T");

//Setting current file name at the right header and changing the font of the header

pageSetup.SetHeader(2, "&\"Times New Roman,Bold\"&12&F");

//Setting a string at the left footer and changing the font of the footer

pageSetup.SetFooter(0, "Hello World! &\"Courier New\"&14 123");

//Setting picture at the central footer

pageSetup.SetFooter(1, "&G");

workbook.Save("../../data/headerfooter.xlsx");


{{< /highlight >}}
## **NPOI - HSSF XSSF - 使用页眉和页脚**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

IHeader header = sheet1.Header;

header.Center = "Center Header";

header.Left = "Left Header";

header.Right = "Right Header";            

FileStream sw = File.Create("../../data/header.xls");

wb.Write(sw);

sw.Close(); 

{{< /highlight >}}
## **下载运行代码**
下载**使用页眉和页脚**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Headers.and.Footers.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[使用工作表](/cells/zh/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
