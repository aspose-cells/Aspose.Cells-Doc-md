---
title: Indicatori Immagine
type: docs
weight: 20
url: /it/net/image-markers/
---

Gli smart marker di Aspose.Cells supportano anche i marker di immagini. Questa sezione ti mostra come inserire immagini utilizzando smart markers.
## **Parametri dell'Immagine**
Parametri smart marker per gestire le immagini.

- **Immagine: AdattaACella** - Adatta automaticamente l'immagine all'altezza della riga e alla larghezza della colonna della cella.
- **Immagine: ScalaN** - Scala altezza e larghezza al N percento.
- **Immagine:Larghezza:Nin&Altezza:Nin** - Rappresenta l'immagine N pollici alta e larga. Puoi anche
   specificare posizioni Sinistra e Superiore (in punti).

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
