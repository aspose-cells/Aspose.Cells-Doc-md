---
title: Marcadores de imagen
type: docs
weight: 20
url: /es/net/image-markers/
---

Aspose.Cells admite marcadores inteligentes de imágenes. Esta sección te muestra cómo insertar imágenes usando marcadores inteligentes.
## **Parámetros de la Imagen**
Parámetros de marcadores inteligentes para gestionar imágenes.

- **Imagen:AjustarACelda** - Ajusta automáticamente la imagen a la altura de la fila y al ancho de la columna de la celda.
- **Imagen:EscalarN** - Escala la altura y el ancho al N por ciento.
- **Imagen:Ancho:Npulg&Alto:Npulg** - Renderiza la imagen con N pulgadas de alto y N pulgadas de ancho. También puedes especificar las posiciones Izquierda y Arriba (en puntos).
  especificar las posiciones Izquierda y Arriba (en puntos).

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
## **Descargar Código de Ejemplo**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Image%20Markers%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
