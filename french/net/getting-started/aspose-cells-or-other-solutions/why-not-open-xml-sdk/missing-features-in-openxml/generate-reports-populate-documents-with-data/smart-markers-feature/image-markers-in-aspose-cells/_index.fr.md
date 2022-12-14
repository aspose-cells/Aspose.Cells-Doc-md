---
title: Marqueurs d'image dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/image-markers-in-aspose-cells/
---
Les marqueurs intelligents Aspose.Cells prennent également en charge les marqueurs d'image. Cette section vous montre comment insérer des images à l'aide de marqueurs intelligents.
## **Paramètres d'image**
Paramètres de marqueurs intelligents pour la gestion des images.

- **Image : Ajuster à la cellule** - Ajustez automatiquement l'image à la hauteur de ligne et à la largeur de colonne de la cellule.
- **Image : ÉchelleN** - Mettre à l'échelle la hauteur et la largeur à N pour cent.
- **Image : largeur : Nin et hauteur : Nin** - Rendez l'image N pouces de haut et N pouces de large. Vous pouvez également
 spécifiez les positions Gauche et Haut (en points).

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
## **Télécharger l'exemple de code**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
