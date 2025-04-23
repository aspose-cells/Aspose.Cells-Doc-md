---
title: Cambios en la API pública en Aspose.Cells 8.8.0
type: docs
weight: 260
url: /es/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

Este documento describe los cambios en la API de Aspose.Cells desde la versión 8.7.2 hasta la 8.8.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo nuevos y actualizados métodos públicos, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **APIs Añadidas**
### **Obtener referencias de celda para conexión externa**
Aspose.Cells for .NET 8.8.0 ha expuesto las siguientes propiedades nuevas que son útiles para recuperar las referencias de celdas de destino y salida para conexiones externas almacenadas en la hoja de cálculo.

1. QueryTable.ConnectionId: Obtiene el Id de conexión de la tabla de consulta.
1. ExternalConnection.Id: Obtiene el Id de la conexión externa.
1. ListObject.QueryTable: Obtiene la QueryTable vinculada.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, consulte el artículo detallado sobre [Encontrar Tablas de Consulta y Objetos de Lista relacionados con Conexiones de Datos Externas](/cells/es/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Propiedad HTMLLoadOptions.KeepPrecision agregada**
Aspose.Cells for .NET 8.8.0 ha añadido la propiedad HTMLLoadOptions.KeepPrecision para controlar la conversión de valores numéricos largos a notación exponencial al importar archivos HTML. Por defecto, cualquier valor mayor de 15 dígitos se convierte a notación exponencial si se importan los datos desde una cadena o archivo HTML. Sin embargo, ahora los usuarios pueden controlar este comportamiento con la ayuda de la propiedad HTMLLoadOptions.KeepPrecision. Si dicha propiedad se fija en true, los valores se importarán tal como están en la fuente.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, consulte el artículo detallado sobre [Evitar la Conversión de Grandes Valores Numéricos a Notación Exponencial](/cells/es/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

A continuación se muestra un escenario de uso simple.

**C#**

{{< highlight csharp >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Propiedad HTMLLoadOptions.DeleteRedundantSpaces agregada**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, consulte el artículo detallado sobre [Eliminar Espacios Redundantes de HTML](/cells/es/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

Un escenario de uso simple se ve como sigue.

**C#**

{{< highlight csharp >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Propiedad Style.QuotePrefix agregada**
Aspose.Cells for .NET 8.8.0 ha expuesto la propiedad Style.QuotePrefix para detectar si el valor de una celda comienza con un solo símbolo de comillas.

{{% alert color="primary" %}} 

Para obtener más detalles sobre esta característica, revise el artículo detallado sobre [Detectar comilla simple al comienzo del valor de la celda](/cells/es/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

Un escenario de uso simple se ve como sigue.

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **APIs obsoletas**
### **Propiedad Obsoleta LoadOptions.ConvertNumericData**
Aspose.Cells 8.8.0 ha marcado la propiedad LoadOptions.ConvertNumericData como obsoleta. Por favor, utilice la propiedad correspondiente de las clases HTMLLoadOptions o TxtLoadOptions.
{{< app/cells/assistant language="csharp" >}}
