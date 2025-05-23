---
title: Cambios en la API pública en Aspose.Cells 8.0.2
type: docs
weight: 30
url: /es/net/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.0.1 hasta 8.0.2, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Propiedad TextDirection agregada a la clase Shape**
La clase Shape ha expuesto la propiedad TextDirection que se puede utilizar para obtener o establecer la dirección del flujo de texto para el objeto Shape. La propiedad TextDirection también se puede utilizar para establecer la dirección de texto deseada para los comentarios en una hoja de cálculo, como se demuestra a continuación.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

var book = new Workbook();

//Get the first worksheet

var sheet = book.Worksheets[0];

//Add a comment to A1 cell

var comment = sheet.Comments[sheet.Comments.Add("A1")];

//Set its vertical alignment setting            

comment.CommentShape.TextVerticalAlignment  = TextAlignmentType.Center;

//Set its horizontal alignment setting

comment.CommentShape.TextHorizontalAlignment = TextAlignmentType.Right;

//Set the Text Direction - Right-to-Left

comment.CommentShape.TextDirection = TextDirectionType.RightToLeft;

//Set the Comment note

comment.Note = "This is my Comment Text. This is test";

//Save the Excel file

book.Save(myDir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

Consulte el artículo detallado sobre [Cambiar la dirección del texto del comentario](/cells/es/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **Propiedad ConvertFormulasData agregada a la clase HTMLLoadOptions**
Se ha agregado la propiedad ConvertFormulasData a la clase HTMLLoadOptions, para facilitar a los desarrolladores cargar fórmulas de Excel desde archivos HTML. La propiedad booleana ConvertFormulasData indica si convertir o no la cadena en una fórmula cuando el valor de la cadena comienza con el carácter '='.

**C#**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

El valor predeterminado de la propiedad ConvertFormulasData es falso.

{{% /alert %}}
## **Propiedad ImageOptions agregada a la clase HtmlSaveOptions**
Se ha agregado la propiedad ImageOptions a la clase HtmlSaveOptions. La exposición de la propiedad ImageOptions ha permitido a los desarrolladores establecer las preferencias para las imágenes incrustadas en HTML al exportar hojas de cálculo.
## **Se ha marcado como obsoleta la propiedad HtmlSaveOptions.ExportChartImageFormat a partir de Aspose.Cells for .NET 8.0.2. Se recomienda utilizar HtmlSaveOptions.ImageOptions en su lugar para la configuración del formato de imagen al exportar hojas de cálculo al formato HTML.**
HtmlSaveOptions.ExportChartImageFormat ha sido marcado como obsoleto a partir de Aspose.Cells for .NET 8.0.2. Se recomienda utilizar HtmlSaveOptions.ImageOptions en su lugar para la configuración del formato de imagen al exportar hojas de cálculo al formato HTML.
{{< app/cells/assistant language="csharp" >}}
