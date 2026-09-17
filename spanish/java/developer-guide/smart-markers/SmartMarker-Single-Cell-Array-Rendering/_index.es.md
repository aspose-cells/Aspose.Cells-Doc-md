---
title: Renderización de matrices en una sola celda con SmartMarker | Aspose.Cells Java
linktitle: Renderización de matrices en una sola celda con SmartMarker | Aspose.Cells Java
description: Aprenda a renderizar datos de matriz en una sola celda usando los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for Java.
keywords: Aspose.Cells, biblioteca de Java, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, matriz de celda única, renderización de matriz, plantilla
type: docs
weight: 195
url: /es/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la renderización de datos de matriz en una sola celda mediante Smart Markers. Al usar el atributo `ArrayAsSingle` junto con el atributo `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos de la matriz dentro de una sola celda, lo que proporciona un formato flexible para informes y plantillas.

## **Introduction**
Los Smart Markers en Aspose.Cells son una potente función basada en plantillas que permite rellenar dinámicamente datos de hojas de cálculo mediante expresiones de marcadores como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseñador, y cuando la plantilla es procesada por el `WorkbookDesigner`, los marcadores se reemplazan con valores del origen de datos proporcionado.
Por defecto, cuando un Smart Marker hace referencia a una propiedad de matriz (por ejemplo, `&=DataSource.Numbers`), el motor expande la matriz y coloca cada elemento en una celda adyacente, ya sea horizontalmente en una fila o verticalmente en una columna. Si bien este comportamiento es conveniente en muchos escenarios, existen situaciones en las que preferiría renderizar toda la matriz en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.
Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados juntos dentro de una etiqueta de Smart Marker, abordan exactamente este requisito. Le permiten mantener los diseños de informes compactos y predecibles mientras siguen trabajando de forma nativa con orígenes de datos de matriz.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
Cuando un Smart Marker hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz a través de varias celdas por defecto. Por ejemplo, un marcador como `&=Product.Tags` contra un `string[]` que contiene cuatro valores colocará cada valor en su propia celda, empujando otros contenidos de la plantilla hacia afuera y posiblemente rompiendo los diseños de informes cuidadosamente elaborados.

### **Use Case Limitations**
Existen muchos escenarios prácticos donde el comportamiento de expansión por defecto es indeseable:
- **Informes de estilo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que necesitan mostrarse como valores separados por comas o por barras verticales dentro de una sola celda.
- **Fichas de filtro o indicadores de estado** que agrupan múltiples valores en un solo lugar para una mejor legibilidad.
- **Pipelines downstream** (exportación a CSV, renderización a PDF, combinación de correo) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, donde algunos consumidores no toleran matrices que se extienden a través de varias celdas.

### **The Gap It Fills**
Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar los datos en Java, uniendo matrices en cadenas delimitadas antes de vincularlas al diseñador del libro de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al manejar el formato de forma declarativa dentro del propio Smart Marker.

## **Feature Benefits**
Usar los atributos `ArrayAsSingle` y `ExtraDelimiter` en sus Smart Markers ofrece varias ventajas:
- **Contención en una sola celda**: todos los elementos de la matriz se renderizan en exactamente una celda, manteniendo los diseños compactos y predecibles.
- **Control personalizado del delimitador**: especifique cualquier cadena separadora que desee: coma, punto y coma, guion, barra vertical, nueva línea o cualquier texto personalizado.
- **Formato dirigido por plantilla**: no se requiere código adicional para preprocesar los datos; las reglas de formato viven dentro de la etiqueta del Smart Marker.
- **Informes más limpios**: los datos de matriz ya no empujan el contenido vecino de la plantilla a diferentes filas o columnas.
- **Tipos de datos versátiles**: funciona con cadenas, números, fechas y cualquier otro tipo de datos que se pueda unir con un delimitador.
- **Compatibilidad hacia atrás**: cuando se omiten los atributos, se conserva el comportamiento de expansión original, por lo que las plantillas existentes siguen funcionando sin cambios.

## **How to Use This Feature**

### **Smart Marker Syntax**
Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

El marcador se compone de las siguientes partes:
- `&=DataSource.ArrayProperty` — el Smart Marker estándar que hace referencia a la propiedad de matriz en el origen de datos vinculado.
- `arrayasSingle=true` — indica al motor que renderice toda la matriz en una sola celda. Solo el valor `true` activa el comportamiento de celda única.
- `extraDelimiter=", "` — define el separador colocado entre los elementos de la matriz. El valor es un literal de cadena; puede estar vacío, ser un solo carácter o una cadena de varios caracteres.

{{% alert color="primary" %}}
El atributo `extraDelimiter` acepta cualquier literal de cadena, incluidos delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para una salida separada por nueva línea. Si la matriz está vacía, la celda resultante se deja en blanco.

### **Step-by-Step Workflow**
El siguiente flujo de trabajo describe cómo renderizar una matriz en una sola celda usando Smart Markers.
1. **Prepare el origen de datos**: cree una clase (o estructura de datos) que exponga una propiedad que devuelva una matriz. La propiedad puede devolver `String[]`, `int[]` o cualquier otro tipo de matriz admitido.
2. **Cree un libro de trabajo de diseñador**: cree un nuevo `Workbook`, agregue una fila de encabezado y coloque una celda de Smart Marker que haga referencia a la propiedad de matriz con los atributos `arrayasSingle` y `extraDelimiter`.
3. **Cree una instancia de WorkbookDesigner**: cree un objeto `WorkbookDesigner`, adjunte el libro de trabajo de diseñador a este y vincule su origen de datos usando el método `setDataSource`.
4. **Procese los marcadores**: llame al método `WorkbookDesigner.process()` para expandir los Smart Markers y rellenar el libro de trabajo con datos reales.
5. **Guarde el resultado**: guarde el libro de trabajo resultante en disco en formato XLSX o cualquier otro formato de archivo admitido.

### **Code Example 1 — Basic String Array Rendering**

```java
import com.aspose.cells.*;
class Product {
    public String[] Tags;
}
public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");
        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();
        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **Code Example 2 — Numeric Array with Custom Delimiter**

```java
import com.aspose.cells.*;
class Student
{
    public int[] Scores;
}
public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());
        workbook.save("output_numericArray.xlsx");
    }
}
```

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

```java
class Order
{
    private String[] items;
    public String[] getItems()
    {
        return items;
    }
    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **Notes & Best Practices**
Tenga en cuenta los siguientes puntos cuando trabaje con los atributos `ArrayAsSingle` y `ExtraDelimiter`:
- El valor `extraDelimiter` se trata como un literal de cadena; escape cualquier carácter especial que su procesador de plantillas pudiera interpretar.
- El atributo `arrayasSingle` acepta un valor booleano (`true` / `false`). Solo `true` activa el comportamiento de celda única; cualquier otro valor vuelve al comportamiento de expansión por defecto.
- Si la matriz está vacía o es nula, la celda se deja vacía (o contiene una cadena en blanco según el tipo de datos).
- La función funciona con orígenes de datos de objetos, así como con orígenes `DataSet` y `DataTable` donde una columna se puede dividir en matrices.
- Para una salida separada por nueva línea, puede usar `\n` o `System.lineSeparator()` como valor del delimitador.
- Coloque el Smart Marker en una celda que tenga ancho suficiente para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente hacia las celdas adyacentes según el formato.
{{% /alert %}}

{{% /alert %}}

## Related Articles
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for Java](/cells/es/java/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for Java](/cells/es/java/apply-style-to-pivot-table/)
- [Modificar el diseño del campo de página en la tabla dinámica](/cells/es/java/change-page-field-layout/)
- [Convertir minigráfico a imagen y HTML en Aspose.Cells for Java](/cells/es/java/convert-sparkline-to-image-and-html/)
- [Conversión de Excel al formato OFD](/cells/es/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}