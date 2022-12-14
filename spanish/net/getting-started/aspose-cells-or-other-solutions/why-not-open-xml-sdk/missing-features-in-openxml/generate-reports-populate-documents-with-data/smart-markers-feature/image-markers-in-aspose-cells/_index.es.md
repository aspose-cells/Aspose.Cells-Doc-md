---
title: Marcadores de imagen en Aspose.Cells
type: docs
weight: 20
url: /es/net/image-markers-in-aspose-cells/
---
Los marcadores inteligentes Aspose.Cells también admiten marcadores de imagen. Esta sección le muestra cómo insertar imágenes usando marcadores inteligentes.
## **Parámetros de imagen**
Parámetros de marcadores inteligentes para la gestión de imágenes.

- **Imagen:FitToCell** - Ajuste automático de la imagen a la altura de la fila y al ancho de la columna de la celda.
- **Imagen:EscalaN** - Escalar alto y ancho al N por ciento.
- **Imagen:Ancho:NinAltura:Nin** - Renderice la imagen N pulgadas de alto y N pulgadas de ancho. Tú también puedes
 Especifique las posiciones Izquierda y Superior (en puntos).

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
## **Descargar código de muestra**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
