---
title: Marcadores de imagen en Aspose.Cells
type: docs
weight: 20
url: /es/net/image-markers-in-aspose-cells/
---

Aspose.Cells admite marcadores inteligentes de imágenes. Esta sección te muestra cómo insertar imágenes usando marcadores inteligentes.
## **Parámetros de la Imagen**
Parámetros de marcadores inteligentes para gestionar imágenes.

- **Imagen:AjustarACelda** - Ajusta automáticamente la imagen a la altura de la fila y al ancho de la columna de la celda.
- **Imagen:EscalarN** - Escala la altura y el ancho al N por ciento.
- **Imagen:Ancho:Npulg&Alto:Npulg** - Renderiza la imagen con N pulgadas de alto y N pulgadas de ancho. También puedes especificar las posiciones Izquierda y Arriba (en puntos).
  especificar las posiciones Izquierda y Arriba (en puntos).

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
## **Descargar Código de Ejemplo**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
