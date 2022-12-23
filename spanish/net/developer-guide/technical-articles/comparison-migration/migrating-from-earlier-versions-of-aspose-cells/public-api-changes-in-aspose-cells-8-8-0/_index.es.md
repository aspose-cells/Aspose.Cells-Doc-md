---
title: Público API Cambios en Aspose.Cells 8.8.0
type: docs
weight: 260
url: /es/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

Este documento describe los cambios al Aspose.Cells API de la versión 8.7.2 a la 8.8.0 que pueden ser de interés para los desarrolladores de módulos/aplicaciones. Incluye no solo métodos públicos nuevos y actualizados, clases agregadas y eliminadas, etc., sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.Cells.

{{% /alert %}} 
## **API añadidas**
### **Obtenga referencias Cell para conexión externa**
Aspose.Cells for .NET 8.8.0 ha expuesto las siguientes propiedades nuevas que son útiles para recuperar las referencias de celda de destino y salida para conexiones externas almacenadas en la hoja de cálculo.

1. QueryTable.ConnectionId: Obtiene el Id. de conexión de la tabla de consulta.
1. ExternalConnection.Id: Obtiene el Id de la conexión externa.
1. ListObject.QueryTable: Obtiene el QueryTable vinculado.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Encuentre tablas de consulta y objetos de lista relacionados con conexiones de datos externas](/cells/es/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **Se agregó la propiedad HTMLLoadOptions.KeepPrecision**
Aspose.Cells for .NET 8.8.0 agregó la propiedad HTMLLoadOptions.KeepPrecision para controlar la conversión de valores numéricos largos a notación exponencial al importar archivos HTML. De forma predeterminada, cualquier valor de más de 15 dígitos se convierte a notación exponencial si los datos se importan desde la cadena o el archivo HTML. Sin embargo, ahora los usuarios pueden controlar este comportamiento con la ayuda de la propiedad HTMLLoadOptions.KeepPrecision. Si dicha propiedad se establece en verdadero, los valores se importarán tal como están en la fuente.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[ Evite la conversión de valores numéricos grandes a notación exponencial](/cells/es/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

El siguiente es el escenario de uso simple.

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Se agregó la propiedad HTMLLoadOptions.DeleteRedundantSpaces**
Aspose.Cells for .NET 8.8.0 ha expuesto la propiedad HTMLLoadOptions.DeleteRedundantSpaces para mantener o eliminar los espacios adicionales después de la etiqueta de salto de línea (<br>Tag) al importar los datos de la cadena o archivo HTML. La propiedad HTMLLoadOptions.DeleteRedundantSpaces tiene el valor predeterminado falso, lo que significa que todos los espacios adicionales se conservarán e importarán al objeto Libro de trabajo; sin embargo, cuando se establece en verdadero, API eliminará todos los espacios redundantes que vienen después de la etiqueta de salto de línea.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Eliminar espacios redundantes del HTML](/cells/es/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

El escenario de uso simple se ve de la siguiente manera.

**C#**

{{< highlight "csharp" >}}

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

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Se agregó la propiedad Style.QuotePrefix**
Aspose.Cells for .NET 8.8.0 ha expuesto la propiedad Style.QuotePrefix para detectar si un valor de celda comienza con un símbolo de comilla simple.

{{% alert color="primary" %}} 

 Para obtener más detalles sobre esta función, consulte el artículo detallado sobre[Detectar comillas simples al comienzo del valor Cell](/cells/es/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

El escenario de uso simple se ve de la siguiente manera.

**C#**

{{< highlight "csharp" >}}

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
## **API obsoletas**
### **Propiedad LoadOptions.ConvertNumericData obsoleta**
Aspose.Cells 8.8.0 marcó la propiedad LoadOptions.ConvertNumericData como obsoleta. Utilice la propiedad correspondiente de las clases HTMLLoadOptions o TxtLoadOptions.
