---
title: Bildmarkörer
type: docs
weight: 20
url: /sv/net/image-markers/
---

Aspose.Cells smarta markörer stödjer också bildmarkörer. Den här sektionen visar dig hur du sätter in bilder med hjälp av smarta markörer.
## **Bildparametrar**
Smarta markörsparametrar för hantering av bilder.

- **Bild:FitToCell** - Justera automatiskt bilden till cellens radhöjd och kolumnbredd.
- **Bild:SkalaN** - Skala höjd och bredd till N procent.
- **Bild:bredd:N tum&Höjd:N tum** - Rendera bilden N tum hög och N tum bred. Du kan också
  ange vänster och översta positioner (i punkter).

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Image Markers.xlsx";

//Get the image data.

byte[] imageData = File.ReadAllBytes(FilePath + "Aspose.Cells.png");

//Create a datatable.

DataTable t = new DataTable("Table1");

//Add a column to save pictures.

DataColumn dc = t.Columns.Add("Picture");

//Set its data type.

dc.DataType = typeof(object);

//Add a new new record to it.

DataRow row = t.NewRow();

row[0] = imageData;

t.Rows.Add(row);

//Add another record (having picture) to it.

//imageData = File.ReadAllBytes(FilePath + "Desert.jpg");

//row = t.NewRow();

//row[0] = imageData;

//t.Rows.Add(row);

//Create WorkbookDesigner object.

WorkbookDesigner designer = new WorkbookDesigner();

//Open the temple Excel file.

designer.Workbook = new Workbook(FileName);

//Set the datasource.

designer.SetDataSource(t);

//Process the markers.

designer.Process();

//Save the Excel file.

designer.Workbook.Save(FileName);

{{< /highlight >}}
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
