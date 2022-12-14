---
title: Público API Cambios en Aspose.Cells 8.0.2
type: docs
weight: 30
url: /es/net/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.0.1 a la 8.0.2, que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **Se agregó la propiedad TextDirection a la clase de forma**
La clase Shape ha expuesto la propiedad TextDirection que se puede usar para obtener o establecer la dirección del flujo de texto para el objeto Shape. La propiedad TextDirection también se puede usar para establecer la dirección de texto deseada para los comentarios en una hoja de cálculo, como se muestra a continuación.

**C#**

{{< highlight "csharp" >}}

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

 Consulte el artículo detallado sobre[Cambiar la dirección del texto del comentario](/cells/es/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **Se agregó la propiedad ConvertFormulasData a la clase HTMLLoadOptions**
La propiedad ConvertFormulasData se ha agregado a la clase HTMLLoadOptions para facilitar a los desarrolladores la carga de fórmulas de Excel desde archivos HTML. La propiedad booleana ConvertFormulasData indica si se convierte o no la cadena en una fórmula cuando el valor de la cadena comienza con el carácter '='.

**C#**

{{< highlight "csharp" >}}

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
## **Se agregó la propiedad ImageOptions a la clase HtmlSaveOptions**
La propiedad ImageOptions se ha agregado a la clase HtmlSaveOptions. Exponer la propiedad ImageOptions ha permitido a los desarrolladores establecer las preferencias para las imágenes incrustadas en el HTML al exportar hojas de cálculo.
## **Propiedad HtmlSaveOptions.ExportChartImageFormat obsoleta**
HtmlSaveOptions.ExportChartImageFormat se marcó como obsoleto a partir de Aspose.Cells for .NET 8.0.2. Se recomienda utilizar HtmlSaveOptions.ImageOptions en su lugar para la configuración de formato de imagen al exportar hojas de cálculo a formato HTML.
