---
title: Marcatori immagine in Aspose.Cells
type: docs
weight: 20
url: /it/net/image-markers-in-aspose-cells/
---
I marcatori intelligenti Aspose.Cells supportano anche i marcatori immagine. Questa sezione mostra come inserire immagini utilizzando i marcatori intelligenti.
## **Parametri dell'immagine**
Parametri di marker intelligenti per la gestione delle immagini.

- **Immagine:FitToCell** - Adatta automaticamente l'immagine all'altezza della riga e alla larghezza della colonna della cella.
- **Immagine:ScalaN** - Ridimensiona l'altezza e la larghezza all'N percento.
- **Immagine: Larghezza: Nin e Altezza: Nin** - Rendi l'immagine alta N pollici e larga N pollici. Puoi anche
 specificare le posizioni Left e Top (in punti).

{{< highlight "csharp" >}}

 //Get the image data.

byte[]imageData = File.ReadAllBytes("Thumbnail.jpg");

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

imageData = File.ReadAllBytes("Desert.jpg");

row = t.NewRow();

row[0]= imageData;

t.Rows.Add(row);

//Create WorkbookDesigner object.

WorkbookDesigner designer = new WorkbookDesigner();

//Open the temple Excel file.

designer.Workbook = new Workbook("ImageSmartBook.xls");

//Set the datasource.

designer.SetDataSource(t);

//Process the markers.

designer.Process();

//Save the Excel file.

designer.Workbook.Save("out_ImageSmartBook.xls");

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
