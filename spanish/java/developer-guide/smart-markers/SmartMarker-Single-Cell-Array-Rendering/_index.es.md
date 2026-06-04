---
title: Representación de matriz en celda única de SmartMarker | Aspose.Cells Java
description: Aprenda cómo representar datos de matriz en una sola celda utilizando los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for Java.
keywords: Aspose.Cells, biblioteca Java, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, matriz en celda única, representación de matriz, plantilla
type: docs
weight: 195
url: /es/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells admite la representación de datos de matriz en una sola celda mediante Smart Markers. Al usar el atributo `ArrayAsSingle` junto con el atributo `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos de la matriz dentro de una sola celda, lo que proporciona un formato flexible para informes y plantillas.

{{% /alert %}}

## **Introducción**

Los Smart Markers en Aspose.Cells son una potente función basada en plantillas que le permite completar dinámicamente los datos de una hoja de cálculo mediante expresiones de marcadores como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando la plantilla es procesada por el `WorkbookDesigner`, los marcadores se reemplazan con valores del origen de datos proporcionado.

De forma predeterminada, cuando un Smart Marker hace referencia a una propiedad de matriz (por ejemplo, `&=DataSource.Numbers`), el motor expande la matriz y coloca cada elemento en una celda adyacente separada, ya sea horizontalmente a lo largo de una fila o verticalmente a lo largo de una columna. Si bien este comportamiento es conveniente en muchos escenarios, hay situaciones en las que preferiría representar la matriz completa en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.

Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados juntos dentro de una etiqueta de Smart Marker, abordan exactamente este requisito. Le permiten mantener diseños de informes compactos y predecibles mientras sigue trabajando de forma nativa con orígenes de datos de matriz.

## **Por qué se necesita esta función**

### **Comportamiento predeterminado de expansión de matrices**

Cuando un Smart Marker hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz a través de varias celdas de forma predeterminada. Por ejemplo, un marcador como `&=Product.Tags` contra un `string[]` que contiene cuatro valores colocará cada valor en su propia celda, empujando hacia afuera otro contenido de la plantilla y potencialmente rompiendo diseños de informes cuidadosamente diseñados.

### **Limitaciones de los casos de uso**

Hay muchos escenarios prácticos donde el comportamiento de expansión predeterminado no es deseable:

- **Informes de tipo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que deben mostrarse como valores separados por comas o por plecas dentro de una sola celda.
- **Indicadores de filtros o estado** que agrupan múltiples valores en un solo lugar para facilitar la lectura.
- **Procesos posteriores** (exportación a CSV, representación en PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad entre plataformas**, donde algunos consumidores no toleran matrices que se extienden a través de varias celdas.

### **El vacío que llena**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar los datos en Java, uniendo matrices en cadenas delimitadas antes de vincularlas al diseñador del libro de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al manejar el formato de forma declarativa dentro del propio Smart Marker.

## **Beneficios de la función**

El uso de los atributos `ArrayAsSingle` y `ExtraDelimiter` en sus Smart Markers proporciona varias ventajas:

- **Contención en una sola celda**: Todos los elementos de la matriz se representan en exactamente una celda, manteniendo diseños compactos y predecibles.
- **Control personalizado del delimitador**: Especifique cualquier cadena separadora que desee: coma, punto y coma, guion, pleca, nueva línea o cualquier texto personalizado.
- **Formato dirigido por plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato viven dentro de la etiqueta del Smart Marker.
- **Informes más limpios**: Los datos de la matriz ya no empujan el contenido adyacente de la plantilla a diferentes filas o columnas.
- **Tipos de datos versátiles**: Funciona con cadenas, números, fechas y cualquier otro tipo de dato que se pueda unir con un delimitador.
- **Compatibilidad con versiones anteriores**: Cuando se omiten los atributos, se conserva el comportamiento de expansión original, por lo que las plantillas existentes siguen funcionando sin cambios.

## **Cómo usar esta función**

### **Sintaxis del Smart Marker**

Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

El marcador se compone de las siguientes partes:

- `&=DataSource.ArrayProperty` — el Smart Marker estándar que hace referencia a la propiedad de matriz en el origen de datos vinculado.
- `arrayasSingle=true` — indica al motor que represente toda la matriz en una sola celda. Solo el valor `true` activa el comportamiento de celda única.
- `extraDelimiter=", "` — define el separador colocado entre los elementos de la matriz. El valor es un literal de cadena; puede estar vacío, ser un solo carácter o una cadena de varios caracteres.

{{% alert color="primary" %}}

El atributo `extraDelimiter` acepta cualquier literal de cadena, incluidos delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para salida separada por nuevas líneas. Si la matriz está vacía, la celda resultante se deja en blanco.

{{% /alert %}}

### **Flujo de trabajo paso a paso**

El siguiente flujo de trabajo describe cómo representar una matriz en una sola celda utilizando Smart Markers.

1. **Prepare el origen de datos**: Cree una clase (o estructura de datos) que exponga una propiedad que devuelva una matriz. La propiedad puede devolver `String[]`, `int[]` o cualquier otro tipo de matriz compatible.
2. **Cree un libro de trabajo de diseño**: Cree un nuevo `Workbook`, agregue una fila de encabezado y coloque una celda de Smart Marker que haga referencia a la propiedad de matriz con los atributos `arrayasSingle` y `extraDelimiter`.
3. **Cree una instancia de WorkbookDesigner**: Cree un objeto `WorkbookDesigner`, adjunte el libro de trabajo de diseño y vincule su origen de datos utilizando el método `setDataSource`.
4. **Procese los marcadores**: Llame al método `WorkbookDesigner.process()` para expandir los Smart Markers y completar el libro de trabajo con datos reales.
5. **Guarde el resultado**: Guarde el libro de trabajo resultante en disco en formato XLSX o cualquier otro formato de archivo compatible.

### **Ejemplo de código 1 — Representación básica de matriz de cadenas**

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

### **Ejemplo de código 2 — Matriz numérica con delimitador personalizado**

```java
import com.aspose.cells.*;

class Student {
    public int[] Scores;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayasSingle=true, extraDelimiter=\" - \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Student", student);
        designer.process();

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **Ejemplo de código 3 — Comparación del comportamiento predeterminado frente a ArrayAsSingle**

```java
import com.aspose.cells.*;

class Order {
    public String[] Items;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.Items = new String[] { "Apple", "Banana", "Cherry", "Date" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Default");
        worksheet.getCells().get("A2").putValue("&=Order.Items");

        worksheet.getCells().get("C1").putValue("ArrayAsSingle");
        worksheet.getCells().get("C2").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Order", order);
        designer.process();

        workbook.save("output_comparison.xlsx");
    }
}
```

### **Notas y buenas prácticas**

Tenga en cuenta los siguientes puntos al trabajar con los atributos `ArrayAsSingle` y `ExtraDelimiter`:

- El valor `extraDelimiter` se trata como un literal de cadena; escape cualquier carácter especial que su procesador de plantillas pueda interpretar.
- El atributo `arrayasSingle` acepta un valor booleano (`true` / `false`). Solo `true` activa el comportamiento de celda única; cualquier otro valor recurre al comportamiento de expansión predeterminado.
- Si la matriz está vacía o es nula, la celda se deja vacía (o contiene una cadena en blanco según el tipo de dato).
- La función funciona con orígenes de datos de objetos, así como con orígenes `DataSet` y `DataTable` donde una columna se puede dividir en matrices.
- Para la salida separada por nuevas líneas, puede usar `\n` o `System.lineSeparator()` como valor del delimitador.
- Coloque el Smart Marker en una celda que tenga ancho suficiente para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente en celdas adyacentes según el formato.

## **Artículos relacionados**

- [Smart Markers](/cells/es/java/smart-markers/)
- [Combinar y separar celdas](/cells/es/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}