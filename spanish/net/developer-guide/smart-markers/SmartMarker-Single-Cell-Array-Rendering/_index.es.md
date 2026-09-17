---
title: Representación de matrices en una sola celda con SmartMarker | Aspose.Cells .NET
linktitle: Representación de matrices en una sola celda con SmartMarker | Aspose.Cells .NET
description: Aprenda a representar datos de matrices en una sola celda mediante los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for .NET.
keywords: Aspose.Cells, biblioteca de .NET, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, matriz de una sola celda, representación de matrices, plantilla
type: docs
weight: 195
url: /es/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permite representar datos de matrices en una sola celda mediante Smart Markers. Al usar los atributos `ArrayAsSingle` y `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos de la matriz dentro de una sola celda, lo que ofrece un formato flexible para informes y plantillas.
{{% /alert %}}

## **Introduction**
Los Smart Markers de Aspose.Cells son una potente función basada en plantillas que permite rellenar dinámicamente datos de hojas de cálculo mediante expresiones de marcadores como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando la plantilla se procesa mediante `WorkbookDesigner`, los marcadores se sustituyen por valores procedentes del origen de datos proporcionado.
De forma predeterminada, cuando un Smart Marker hace referencia a una propiedad de matriz, por ejemplo, `&=DataSource.Numbers`, el motor expande la matriz y coloca cada elemento en una celda adyacente independiente, ya sea horizontalmente a lo largo de una fila o verticalmente por una columna. Aunque este comportamiento resulta práctico en muchos escenarios, existen situaciones en las que puede ser preferible representar toda la matriz en una sola celda, con los elementos concatenados y separados por un delimitador elegido por el usuario.
Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados conjuntamente dentro de una etiqueta Smart Marker, satisfacen exactamente este requisito. Permiten mantener diseños de informes compactos y predecibles, a la vez que se trabaja de forma nativa con orígenes de datos de matrices.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Cuando un Smart Marker hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz entre varias celdas de forma predeterminada. Por ejemplo, un marcador como `&=Product.Tags` aplicado a un `string[]` que contiene cuatro valores colocará cada valor en su propia celda, desplazando el resto del contenido de la plantilla y pudiendo alterar diseños de informes cuidadosamente diseñados.

### **Use Case Limitations**
Existen muchos escenarios prácticos en los que no resulta conveniente el comportamiento de expansión predeterminado:
- **Informes de estilo resumen** que requieren un diseño compacto de una fila por registro.
- **Listas de etiquetas, categorías o palabras clave** que deben mostrarse como valores separados por comas o barras verticales dentro de una sola celda.
- **Filtros de selección o indicadores de estado** que agrupan varios valores en un mismo lugar para mejorar la legibilidad.
- **Procesos posteriores** (exportación a CSV, representación a PDF o combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, ya que algunos consumidores no admiten matrices que se extiendan entre varias celdas.

### **The Gap It Fills**
Sin un mecanismo integrado, los desarrolladores tendrían que preprocesar los datos en C# o VB.NET, unir las matrices en cadenas delimitadas antes de enlazarlas al diseñador del libro de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta el riesgo de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al gestionar el formato de forma declarativa dentro del propio Smart Marker.

## **Feature Benefits**
El uso de los atributos `ArrayAsSingle` y `ExtraDelimiter` en los Smart Markers ofrece varias ventajas:
- **Inclusión en una sola celda**: todos los elementos de la matriz se representan exactamente en una celda, lo que mantiene los diseños compactos y predecibles.
- **Control personalizado del delimitador**: permite especificar cualquier cadena separadora, como una coma, un punto y coma, un guion, una barra vertical, una nueva línea o texto personalizado.
- **Formato basado en plantillas**: no se requiere código adicional para preprocesar los datos; las reglas de formato se encuentran dentro de la etiqueta Smart Marker.
- **Informes más limpios**: los datos de la matriz ya no desplazan el contenido adyacente de la plantilla hacia otras filas o columnas.
- **Tipos de datos versátiles**: funciona con cadenas, números, fechas y cualquier otro tipo de datos que pueda unirse mediante un delimitador.
- **Compatibilidad con versiones anteriores**: cuando se omiten los atributos, se conserva el comportamiento de expansión original, por lo que las plantillas existentes siguen funcionando sin cambios.

## **How to Use This Feature**

### **Smart Marker Syntax**
Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

El marcador se compone de las partes siguientes:
- `&=DataSource.ArrayProperty` — Smart Marker estándar que hace referencia a la propiedad de matriz del origen de datos enlazado.
- `arrayasSingle=true` — indica al motor que debe representar toda la matriz en una sola celda. Solo el valor `true` activa el comportamiento de una sola celda.
- `extraDelimiter=", "` — define el separador que se coloca entre los elementos de la matriz. El valor es una cadena literal y puede estar vacío, contener un solo carácter o varios caracteres.

{{% alert color="primary" %}}
El atributo `extraDelimiter` acepta cualquier cadena literal, incluidos delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para generar resultados separados por saltos de línea. Si la matriz está vacía, la celda resultante se deja en blanco.

### **Step-by-Step Workflow**
El siguiente flujo de trabajo explica cómo representar una matriz en una sola celda mediante Smart Markers.
1. **Prepare el origen de datos**: cree una clase o estructura de datos que exponga una propiedad que devuelva una matriz. La propiedad puede devolver `string[]`, `int[]` o cualquier otro tipo de matriz compatible.
2. **Cree un libro de trabajo de diseño**: cree un nuevo `Workbook`, añada una fila de encabezado y coloque una celda con un Smart Marker que haga referencia a la propiedad de matriz mediante los atributos `arrayasSingle` y `extraDelimiter`.
3. **Cree una instancia de WorkbookDesigner**: cree un objeto `WorkbookDesigner`, adjunte el libro de trabajo de diseño y enlace el origen de datos mediante el método `SetDataSource`.
4. **Procese los marcadores**: llame al método `WorkbookDesigner.Process()` para expandir los Smart Markers y rellenar el libro de trabajo con datos reales.
5. **Guarde el resultado**: guarde el libro de trabajo resultante en el disco en formato XLSX o en cualquier otro formato de archivo compatible.

### **Code Example 1 — Basic String Array Rendering**

```csharp
using System;
using Aspose.Cells;
class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }
    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");
        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();
        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```csharp
public class Student
{
    public int[] Scores { get; set; }
}
public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));
        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```csharp
using System;
using Aspose.Cells;
public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;
        // Sección 1: Smart Marker por defecto - valores distribuidos horizontalmente entre celdas
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");
        // Sección 2: Nueva renderización en una sola celda usando arrayasSingle y extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
        // Vincular la fuente de datos y procesar los Smart Markers
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();
        // Guardar el libro de trabajo resultante
        workbook.Save("output_comparison.xlsx");
    }
}
public class Order
{
    public string[] Items { get; set; }
}
```

### **Notes & Best Practices**
Tenga en cuenta los siguientes aspectos al trabajar con los atributos `ArrayAsSingle` y `ExtraDelimiter`:
- El valor `extraDelimiter` se trata como una cadena literal; escape cualquier carácter especial que pueda interpretar el procesador de plantillas.
- El atributo `arrayasSingle` acepta un valor booleano (`true` / `false`). Solo `true` activa el comportamiento de una sola celda; cualquier otro valor recurre al comportamiento de expansión predeterminado.
- Si la matriz está vacía o es nula, la celda se deja vacía o contiene una cadena en blanco, según el tipo de datos.
- La función funciona con orígenes de datos de objetos, así como con orígenes `DataSet` y `DataTable` en los que una columna puede dividirse en matrices.
- Para generar resultados separados por saltos de línea, puede usar `\n` o `Environment.NewLine` como valor del delimitador.
{{% /alert %}}

## Related Articles
- [Añadir campos de filtro a una tabla dinámica en Aspose.Cells for .NET](/cells/es/net/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for .NET](/cells/es/net/apply-style-to-pivot-table/)
- [Modificar el diseño de los campos de página en una tabla dinámica](/cells/es/net/change-page-field-layout/)
- [Convertir un minigráfico a imagen y HTML en Aspose.Cells for .NET](/cells/es/net/convert-sparkline-to-image-and-html/)
- [Conversión de Excel al formato OFD](/cells/es/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}