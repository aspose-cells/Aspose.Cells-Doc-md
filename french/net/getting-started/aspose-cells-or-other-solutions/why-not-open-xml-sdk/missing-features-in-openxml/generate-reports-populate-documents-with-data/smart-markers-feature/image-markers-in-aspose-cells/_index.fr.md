---
title: Marqueurs d Image dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/image-markers-in-aspose-cells/
---

Les marqueurs intelligents d'Aspose.Cells prennent également en charge les marqueurs d'image. Cette section montre comment insérer des images à l'aide de marqueurs intelligents.
## **Paramètres de l'image**
Paramètres de marqueurs intelligents pour gérer les images.

- **Image:Ajusteràlacellule** - Ajuster automatiquement l'image à la hauteur de la ligne et à la largeur de la colonne de la cellule.
- **Image:EchelleN** - Adapter la hauteur et la largeur à N pour cent.
- **Image:Largeur:Nin&Hauteur:Nin** - Rendre l'image N pouces de haut et N pouces de large. Vous pouvez également
  spécifier les positions Gauche et Haut (en points).

{{< highlight csharp >}}

 //Get the image data.

byte[] imageData = File.ReadAllBytes("Thumbnail.jpg");

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

imageData = File.ReadAllBytes("Desert.jpg");

row = t.NewRow();

row[0] = imageData;

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
## **Télécharger le code source d'exemple**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
