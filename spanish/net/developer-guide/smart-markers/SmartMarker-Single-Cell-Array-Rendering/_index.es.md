---
title: Representación de matrices en una sola celda con marcadores inteligentes | Aspose.Cells .NET
description: Aprenda a representar datos de matrices en una sola celda mediante los atributos arrayassingle y arraydelimiter de los marcadores inteligentes en Aspose.Cells for .NET.
linktitle: Representación de matrices en una sola celda con marcadores inteligentes | Aspose.Cells
url: /es/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, biblioteca .NET, hoja de cálculo, marcadores inteligentes, arrayassingle, arraydelimiter, matriz en una sola celda, renderizado de matrices, plantilla
type: docs
weight: 195
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells puede representar un origen de datos de matrices en una sola celda mediante marcadores inteligentes. El atributo `arrayassingle` desactiva la distribución predeterminada elemento por elemento y el atributo `arraydelimiter` elige el separador que se coloca entre los elementos unidos: una coma de forma predeterminada, o cualquier carácter individual o cadena de varios caracteres entre comillas que especifique.
{{% /alert %}}

## **Introducción**

Los marcadores inteligentes de Aspose.Cells son una función basada en plantillas que completa dinámicamente los datos de una hoja de cálculo mediante expresiones de marcador como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando la plantilla se procesa con `WorkbookDesigner`, los marcadores se reemplazan por los valores del origen de datos proporcionado.
De forma predeterminada, cuando un marcador inteligente hace referencia a una propiedad de matriz (por ejemplo, `&=Product.Tags` vinculada a un `string[]` de cuatro valores), el motor expande la matriz y coloca cada elemento en su propia celda, distribuyendo los valores verticalmente hacia abajo en la columna, debajo del marcador. Aunque este comportamiento resulta práctico en muchos escenarios, hay situaciones en las que se prefiere representar la matriz completa en una sola celda, concatenando los elementos y separándolos mediante un delimitador de su elección.
Los atributos `arrayassingle` y `arraydelimiter`, escritos dentro de los paréntesis de un marcador inteligente en forma `name:value`, cubren exactamente esta necesidad. Permiten mantener los diseños de informes compactos y predecibles mientras siguen funcionando de forma nativa con orígenes de datos de matrices.

## **Por qué se necesita esta función**

### **Comportamiento predeterminado de distribución de matrices**

Cuando un marcador inteligente hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz en varias celdas de forma predeterminada. Por ejemplo, un marcador como `&=Product.Tags` asociado a un `string[]` que contiene cuatro valores coloca cada valor en su propia celda debajo del marcador, desplazando el resto del contenido de la plantilla y posiblemente dañando diseños de informes cuidadosamente elaborados.

### **Limitaciones en casos de uso**

Existen muchos escenarios prácticos en los que el comportamiento predeterminado de distribución no es deseable:
- **Informes de resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que deben mostrarse como valores separados por comas o barras verticales dentro de una sola celda.
- **Chips de filtrado o indicadores de estado** que agrupan varios valores en un mismo lugar para facilitar la lectura.
- **Tuberías posteriores** (exportación a CSV, renderizado a PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad entre plataformas**, donde algunos consumidores no pueden tolerar matrices que se desbordan por varias celdas.

### **La brecha que cubre**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar los datos en C# o VB.NET, uniendo las matrices en cadenas delimitadas antes de enlazarlas al diseñador de libros de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `arrayassingle` y `arraydelimiter` eliminan esta solución alternativa al gestionar el formato de forma declarativa dentro del propio marcador inteligente.

## **Ventajas de la función**

El uso de los atributos `arrayassingle` y `arraydelimiter` en los marcadores inteligentes ofrece varias ventajas:
- **Contención en una sola celda**: Todos los elementos de la matriz se representan en exactamente una celda, lo que mantiene los diseños compactos y predecibles.
- **Control del delimitador personalizado**: Especifique el separador que prefiera: la coma predeterminada, un punto y coma, un guion, una barra vertical o una cadena de varios caracteres entre comillas, como `" | "`.
- **Formato basado en plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato se definen dentro de la etiqueta del marcador inteligente.
- **Informes más limpios**: Los datos de matrices ya no desplazan el contenido contiguo de la plantilla hacia otras filas o columnas.
- **Tipos de datos versátiles**: Funciona con matrices de cadenas y matrices numéricas procedentes de orígenes de datos de objetos.
- **Compatibilidad con versiones anteriores**: Cuando se omiten los atributos, se conserva el comportamiento original de distribución, por lo que las plantillas existentes continúan funcionando sin cambios.

## **Cómo usar esta función**

### **Sintaxis del marcador inteligente**

Los atributos `arrayassingle` y `arraydelimiter` utilizan la gramática de atributos `name:value` de Aspose.Cells dentro de los paréntesis de un marcador inteligente estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

El marcador está compuesto por las siguientes partes:
- `&=DataSource.ArrayProperty` — el marcador inteligente estándar que hace referencia a la propiedad de matriz del origen de datos vinculado.
- `arrayassingle:true` — indica al motor que represente toda la matriz en una sola celda en lugar de distribuir sus elementos.
- `arraydelimiter:;` — es opcional y define el separador que se coloca entre los elementos de la matriz. Si se omite, se utiliza una coma.

{{% alert color="warning" %}}
Escriba los atributos en forma `name:value` (con dos puntos, no un signo igual) y separe varios atributos con una coma **sin espacios**. Un espacio después de la coma desplaza el valor analizado un carácter: `(arrayassingle:true, arraydelimiter:;)` uniría los elementos con el separador incorrecto `:;` en lugar de `;`.
{{% /alert %}}

### **Formas del delimitador**

- Un carácter individual sigue directamente a los dos puntos: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separador de varios caracteres se escribe entre comillas dobles: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flujo de trabajo paso a paso**

El siguiente flujo de trabajo describe cómo representar una matriz en una sola celda mediante marcadores inteligentes.
1. **Prepare el origen de datos**: Cree una clase que exponga una propiedad que devuelva una matriz, como `string[]` o `int[]`, y enlace un `List<T>` de esa clase para que el motor lea un registro por fila.
2. **Cree el libro de trabajo de diseño**: Cree un nuevo `Workbook`, añada una fila de encabezado y coloque una celda de marcador inteligente que haga referencia a la propiedad de matriz con el atributo `arrayassingle` (y con `arraydelimiter` cuando necesite un separador personalizado).
3. **Instancie `WorkbookDesigner`**: Cree un `WorkbookDesigner` alrededor del libro de trabajo y enlace su origen de datos con `SetDataSource`.
4. **Procese los marcadores**: Llame al método `WorkbookDesigner.Process()` para expandir los marcadores inteligentes y completar el libro de trabajo con los datos reales.
5. **Guarde el resultado**: Guarde el libro de trabajo resultante en disco en XLSX o en cualquier otro formato de archivo compatible.

### **Ejemplo de código 1: representación básica de una matriz de cadenas**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

El ejemplo imprime el valor concatenado de la matriz completa. Las cuatro etiquetas se incluyen en una celda, separadas por la coma predeterminada:

```
C#,Aspose,SmartMarker,Excel
```

### **Ejemplo de código 2: matriz numérica con un delimitador personalizado**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

Las matrices numéricas se unen exactamente igual que las matrices de cadenas: cada elemento conserva su texto numérico literal:

```
95-88-76-100-67
```

### **Ejemplo de código 3: comparación entre la representación predeterminada y la representación en una sola celda**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

El marcador predeterminado llena una celda por elemento hacia abajo en la columna B, mientras que el marcador `arrayassingle` contrae la misma matriz en una sola celda de la columna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notas y prácticas recomendadas**

Al trabajar con los atributos `arrayassingle` y `arraydelimiter`, tenga en cuenta lo siguiente:
- Los valores de los atributos usan la forma `name:value`. No se reconoce una forma con signo igual, como `arrayassingle=true`, y se recurre silenciosamente al comportamiento predeterminado de distribución.
- Separe los atributos con una coma y sin espacios; un espacio después de la coma desplaza el valor del delimitador un carácter (consulte la advertencia anterior).
- El valor de `arraydelimiter` puede ser un carácter individual escrito directamente después de los dos puntos o una cadena de varios caracteres entre comillas dobles.
- Cuando se omite `arraydelimiter`, los elementos se unen con una coma.
- El origen de datos debe permitir que el motor enumere los registros: enlace un `List<T>` (u otra colección) cuyo tipo de elemento exponga la propiedad de matriz. Enlazar un solo objeto deja los marcadores del cuerpo sin resolver.
- Los mismos atributos funcionan con matrices de cadenas y numéricas; cada elemento se representa con el texto de su valor literal.

## **Artículos relacionados**
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for .NET](/cells/es/net/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for .NET](/cells/es/net/apply-style-to-pivot-table/)
- [Modificar el diseño del campo de página en una tabla dinámica](/cells/es/net/change-page-field-layout/)
- [Convertir minigráficos a imagen y HTML en Aspose.Cells for .NET](/cells/es/net/convert-sparkline-to-image-and-html/)
- [Conversión de Excel a formato OFD](/cells/es/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}