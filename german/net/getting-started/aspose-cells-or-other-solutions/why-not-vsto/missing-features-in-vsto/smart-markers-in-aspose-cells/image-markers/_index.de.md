---
title: Bildmarkierungen
type: docs
weight: 20
url: /de/net/image-markers/
---
Aspose.Cells Intelligente Markierungen unterstützen auch Bildmarkierungen. Dieser Abschnitt zeigt Ihnen, wie Sie Bilder mit intelligenten Markierungen einfügen.
## **Bildparameter**
Smart-Marker-Parameter zum Verwalten von Bildern.

- **Bild:FitToCell** - Passen Sie das Bild automatisch an die Zeilenhöhe und Spaltenbreite der Zelle an.
- **Bild:ScaleN** - Skalieren Sie Höhe und Breite auf N Prozent.
- **Bild:Breite:Nin&Höhe:Nin** - Rendern Sie das Bild N Zoll hoch und N Zoll breit. Du kannst auch
 Spezifizieren Sie die linken und oberen Positionen (in Punkten).

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Image Markers.xlsx";

//Get the image data.

byte[]imageData = File.ReadAllBytes(FilePath + "Aspose.Cells.png");

//Create a datatable.

DataTable t = new DataTable("Table1");

//Add a column to save pictures.

DataColumn dc = t.Columns.Add("Picture");

//Set its data type.

dc.DataType = typeof(object);

//Add a new new record to it.

DataRow row = t.NewRow();

row[0]= imageData;

t.Rows.Add(row);

//Add another record (having picture) to it.

//imageData = File.ReadAllBytes(FilePath + "Desert.jpg");

//row = t.NewRow();

//row[0]= imageData;

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
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
