---
title: Renderización de matriz en una sola celda con SmartMarker | Aspose.Cells .NET
description: Aprenda a renderizar datos de matriz en una sola celda utilizando los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for .NET.
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, matriz en una sola celda, renderización de matriz, plantilla
type: docs
weight: 195
url: /es/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells admite la renderización de datos de matriz en una sola celda mediante Smart Markers. Al utilizar el atributo `ArrayAsSingle` junto con el atributo `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos de la matriz dentro de una sola celda, proporcionando un formato flexible para informes y plantillas.

{{% /alert %}}

## **Introducción**

Los Smart Markers en Aspose.Cells son una potente característica basada en plantillas que le permite completar dinámicamente datos de hojas de cálculo utilizando expresiones de marcadores como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando la plantilla es procesada por el `WorkbookDesigner`, los marcadores se reemplazan con valores de la fuente de datos proporcionada.

Por defecto, cuando un Smart Marker hace referencia a una propiedad de matriz (por ejemplo, `&=DataSource.Numbers`), el motor expande la matriz y coloca cada elemento en una celda adyacente separada, ya sea horizontalmente a lo largo de una fila o verticalmente en una columna. Aunque este comportamiento es conveniente en muchos escenarios, hay situaciones en las que preferiría renderizar toda la matriz en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.

Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados juntos dentro de una etiqueta de Smart Marker, abordan exactamente este requisito. Le permiten mantener los diseños de informes compactos y predecibles mientras trabaja de forma nativa con fuentes de datos de matrices.

## **Por Qué Se Necesita Esta Característica**

### **Comportamiento Predeterminado de Expansión de Matrices**

Cuando un Smart Marker hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz a través de varias celdas por defecto. Por ejemplo, un marcador como `&=Product.Tags` contra un `string[]` que contiene cuatro valores colocará cada valor en su propia celda, empujando el contenido de la plantilla hacia afuera y posiblemente rompiendo los diseños de informes cuidadosamente diseñados.

### **Limitaciones de Casos de Uso**

Existen muchos escenarios prácticos en los que el comportamiento de expansión predeterminado no es deseable:

- **Informes estilo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que necesitan mostrarse como valores separados por comas o por tuberías dentro de una sola celda.
- **Indicadores de chips de filtro o estado** que agrupan varios valores en un solo lugar para facilitar la lectura.
- **Pipelines posteriores** (exportación CSV, renderización PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, donde algunos consumidores no toleran matrices que se desbordan a través de varias celdas.

### **El Vacío Que Llena**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar datos en C# o VB.NET, uniendo matrices en cadenas delimitadas antes de vincularlas al diseñador de libros de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al manejar el formato de forma declarativa dentro del propio Smart Marker.

## **Beneficios de la Característica**

El uso de los atributos `ArrayAsSingle` y `ExtraDelimiter` en sus Smart Markers proporciona varias ventajas:

- **Contención en una sola celda**: Todos los elementos de la matriz se renderizan en exactamente una celda, manteniendo los diseños compactos y predecibles.
- **Control personalizado del delimitador**: Especifique cualquier cadena separadora que desee: coma, punto y coma, guion, tubería, nueva línea o cualquier texto personalizado.
- **Formato basado en plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato viven dentro de la etiqueta del Smart Marker.
- **Informes más limpios**: Los datos de la matriz ya no empujan el contenido de la plantilla vecina a diferentes filas o columnas.
- **Tipos de datos versátiles**: Funciona con cadenas, números, fechas y cualquier otro tipo de dato que se pueda unir con un delimitador.
- **Compatibilidad hacia atrás**: Cuando se omiten los atributos, se conserva el comportamiento de expansión original, por lo que las plantillas existentes continúan funcionando sin cambios.

## **Cómo Usar Esta Característica**

### **Sintaxis del Smart Marker**

Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

El marcador se compone de las siguientes partes:

- `&=DataSource.ArrayProperty` — el Smart Marker estándar que hace referencia a la propiedad de matriz en la fuente de datos vinculada.
- `arrayasSingle=true` — indica al motor que renderice toda la matriz en una sola celda. Solo el valor `true` activa el comportamiento de una sola celda.
- `extraDelimiter=", "` — define el separador colocado entre los elementos de la matriz. El valor es una cadena literal; puede estar vacío, ser un solo carácter o una cadena de varios caracteres.

{{% alert color="primary" %}}

El atributo `extraDelimiter` acepta cualquier cadena literal, incluidos delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para salida separada por nueva línea. Si la matriz está vacía, la celda resultante se deja en blanco.

{{% /alert %}}

### **Flujo de Trabajo Paso a Paso**

El siguiente flujo de trabajo describe cómo renderizar una matriz en una sola celda utilizando Smart Markers.

1. **Prepare la fuente de datos**: Cree una clase (o estructura de datos) que exponga una propiedad que devuelva una matriz. La propiedad puede devolver `string[]`, `int[]` o cualquier otro tipo de matriz admitido.
2. **Cree un libro de trabajo de diseño**: Cree un nuevo `Workbook`, agregue una fila de encabezado y coloque una celda de Smart Marker que haga referencia a la propiedad de matriz con los atributos `arrayasSingle` y `extraDelimiter`.
3. **Cree una instancia del WorkbookDesigner**: Cree un objeto `WorkbookDesigner`, adjunte el libro de trabajo de diseño a él y vincule su fuente de datos utilizando el método `SetDataSource`.
4. **Procese los marcadores**: Llame al método `WorkbookDesigner.Process()` para expandir los Smart Markers y llenar el libro de trabajo con datos reales.
5. **Guarde el resultado**: Guarde el libro de trabajo resultante en disco en formato XLSX o cualquier otro formato de archivo admitido.

### **Ejemplo de Código 1 — Renderización Básica de Matriz de Cadenas**

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

### **Ejemplo de Código 2 — Matriz Numérica con Delimitador Personalizado**

```csharp
using Aspose.Cells;

public class Student
{
    public int[] Scores { get; set; }
}

public class Program
{
    public static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayasSingle=true, extraDelimiter=\" - \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Student", student);
        designer.Process();

        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Ejemplo de Código 3 — Comparación del Comportamiento Predeterminado vs. ArrayAsSingle**

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

        // Sección 1: Marcador inteligente predeterminado - valores distribuidos horizontalmente entre las celdas
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // Sección 2: Nueva renderización de celda única usando arrayasSingle y extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        // Vincular el origen de datos y procesar los marcadores inteligentes
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();

        // Guardar el libro resultante
        workbook.Save("output_comparison.xlsx");
    }
}

public class Order
{
    public string[] Items { get; set; }
}
```

### **Notas y Mejores Prácticas**

Tenga en cuenta los siguientes puntos al trabajar con los atributos `ArrayAsSingle` y `ExtraDelimiter`:

- El valor de `extraDelimiter` se trata como una cadena literal; escape cualquier carácter especial que su procesador de plantillas pueda interpretar.
- El atributo `arrayasSingle` acepta un valor booleano (`true` / `false`). Solo `true` activa el comportamiento de una sola celda; cualquier otro valor vuelve al comportamiento de expansión predeterminado.
- Si la matriz está vacía o es nula, la celda se deja vacía (o contiene una cadena en blanco según el tipo de dato).
- La característica funciona con fuentes de datos de objetos, así como con fuentes `DataSet` y `DataTable` donde una columna se puede dividir en matrices.
- Para salida separada por nueva línea, puede usar `\n` o `Environment.NewLine` como valor del delimitador.
- Coloque el Smart Marker en una celda que tenga ancho suficiente para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente en celdas adyacentes según el formato.

## **Artículos Relacionados**

- [Smart Markers](/cells/es/net/smart-markers/)
- [Combinar y Descombinar Celdas](/cells/es/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}