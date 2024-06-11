---
title: 在工作表中添加图像
type: docs
weight: 20
url: /zh/net/add-image-in-worksheet/
---

## **Aspose.Cells - 在工作表中添加图像**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

//Insert a string value to a cell

worksheet.Cells["C2"].Value = "Image";

//Set the 4th row height

worksheet.Cells.SetRowHeight(3, 150);

//Set the C column width

worksheet.Cells.SetColumnWidth(2, 50);

//Add a picture to the C4 cell

int index = worksheet.Pictures.Add(3, 2, 3, 2, "../../data/aspose.png");

//Get the picture object

//Picture pic = worksheet.getPictures().get(index);

Picture pic = worksheet.Pictures[index];

//Set the placement type

pic.Placement = PlacementType.FreeFloating;

workbook.Save("../../data/image.xlsx");


{{< /highlight >}}
## **NPOI - HSSF XSSF - 在工作表中添加图像**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

//add picture data to this workbook.

byte[] bytes = File.ReadAllBytes("../../data/aspose.png");

int pictureIdx = wb.AddPicture(bytes, PictureType.PNG);

ICreationHelper helper = wb.GetCreationHelper();

// Create the drawing patriarch.  This is the top level container for all shapes.

IDrawing drawing = sheet1.CreateDrawingPatriarch();

// add a picture shape

IClientAnchor anchor = helper.CreateClientAnchor();

//set top-left corner of the picture,

//subsequent call of Picture#resize() will operate relative to it

anchor.Col1 = 3;

anchor.Row1 = 2;

IPicture pict = drawing.CreatePicture(anchor, pictureIdx);

//auto-size picture relative to its top-left corner

pict.Resize();

FileStream sw = File.Create("../../data/image.xlsx");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载**在工作表中添加图像**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Add.Image.in.Worksheet.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[使用工作表](/cells/zh/net/working-with-worksheets-in-npoi-and-aspose-cells/)。

{{% /alert %}}
