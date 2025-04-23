---
title: Lägg till bild i arbetsblad
type: docs
weight: 20
url: /sv/net/add-image-in-worksheet/
---

## **Aspose.Cells - Lägg till bild i arbetsblad**
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
## **NPOI - HSSF XSSF - Lägg till bild i arbetsblad**
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
## **Ladda ned körbar kod**
Ladda ner **Lägg till bild i arbetsblad** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Add.Image.in.Worksheet.zip)

{{% alert color="primary" %}} 

För mer information, besök [Arbeta med kalkylblad](/cells/sv/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
