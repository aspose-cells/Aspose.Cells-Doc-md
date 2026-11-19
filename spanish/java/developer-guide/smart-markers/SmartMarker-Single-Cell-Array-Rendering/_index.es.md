---
title: Renderizado de matrices en una sola celda con marcadores inteligentes | Aspose.Cells Java
description: Aprenda a renderizar datos de matriz en una sola celda mediante los atributos arrayassingle y arraydelimiter de los marcadores inteligentes en Aspose.Cells for Java.
linktitle: Renderizado de matrices en una sola celda con marcadores inteligentes | Aspose.Cells
url: /es/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, biblioteca Java, hoja de cálculo, marcadores inteligentes, arrayassingle, arraydelimiter, matriz en una sola celda, renderizado de matrices, plantilla
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells puede renderizar un origen de datos de matriz en una sola celda mediante marcadores inteligentes. El atributo `arrayassingle` desactiva la expansión predeterminada elemento por elemento y el atributo `arraydelimiter` elige el separador que se coloca entre los elementos concatenados: una coma de forma predeterminada, o cualquier carácter individual o cadena de varios caracteres entre comillas que especifique.
{{% /alert %}}

## **Introducción**

Los marcadores inteligentes de Aspose.Cells son una función basada en plantillas que rellena dinámicamente los datos de una hoja de cálculo mediante expresiones de marcador como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando la plantilla se procesa mediante `WorkbookDesigner`, los marcadores se sustituyen por los valores del origen de datos proporcionado.
De forma predeterminada, cuando un marcador inteligente hace referencia a una propiedad de matriz (por ejemplo, `&=Product.Tags` vinculada a un `String[]` de cuatro valores), el motor expande la matriz y coloca cada elemento en su propia celda, extendiendo los valores verticalmente hacia abajo por la columna situada debajo del marcador. Aunque este comportamiento resulta práctico en muchos escenarios, hay situaciones en las que sería preferible renderizar la matriz completa en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.
Los atributos `arrayassingle` y `arraydelimiter`, escritos dentro de los paréntesis de un marcador inteligente con el formato `name:value`, cubren exactamente esta necesidad. Le permiten mantener los diseños de informes compactos y predecibles al mismo tiempo que trabajan de forma nativa con orígenes de datos de matriz.

## **Por qué se necesita esta función**

### **Comportamiento predeterminado de expansión de matrices**

Cuando un marcador inteligente hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz en varias celdas de forma predeterminada. Por ejemplo, un marcador como `&=Product.Tags` que opera sobre un `String[]` con cuatro valores coloca cada valor en su propia celda debajo del marcador, desplazando el resto del contenido de la plantilla y posiblemente alterando diseños de informe cuidadosamente elaborados.

### **Limitaciones de los casos de uso**

Hay muchos escenarios prácticos en los que no resulta deseable el comportamiento predeterminado de expansión:
- **Informes de estilo resumen** que necesitan un diseño compacto con una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que deben mostrarse como valores separados por comas o barras verticales dentro de una sola celda.
- **Distintivos de filtro o indicadores de estado** que agrupan varios valores en un mismo lugar para facilitar la lectura.
- **Flujos de procesamiento posteriores** (exportación a CSV, renderizado de PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad entre plataformas**, donde algunos consumidores no pueden tolerar matrices que se desbordan en varias celdas.

### **La carencia que resuelve**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar los datos en Java: unir las matrices en cadenas delimitadas antes de vincularlas al `WorkbookDesigner`. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `arrayassingle` y `arraydelimiter` eliminan esta solución alternativa al gestionar el formato de forma declarativa dentro del propio marcador inteligente.

## **Ventajas de la función**

Al utilizar los atributos `arrayassingle` y `arraydelimiter` en los marcadores inteligentes, se obtienen varias ventajas:
- **Contención en una sola celda**: Todos los elementos de la matriz se renderizan en exactamente una celda, lo que mantiene los diseños compactos y predecibles.
- **Control del delimitador personalizado**: Especifique el separador que prefiera: la coma predeterminada, un punto y coma, un guion, una barra vertical o una cadena de varios caracteres entre comillas como `" | "`.
- **Formato controlado por plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato se definen dentro de la etiqueta del marcador inteligente.
- **Informes más limpios**: Los datos de matriz ya no desplazan el contenido vecino de la plantilla hacia otras filas o columnas.
- **Tipos de datos versátiles**: Funciona con matrices de cadenas y valores numéricos representados como cadenas desde orígenes de datos de JavaBean.
- **Compatibilidad hacia atrás**: Cuando se omiten los atributos, se conserva el comportamiento original de expansión, por lo que las plantillas existentes siguen funcionando sin cambios.

## **Cómo utilizar esta función**

### **Sintaxis del marcador inteligente**

Los atributos `arrayassingle` y `arraydelimiter` utilizan la gramática de atributos `name:value` de Aspose.Cells dentro de los paréntesis de un marcador inteligente estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

El marcador se compone de las siguientes partes:
- `&=DataSource.ArrayProperty` — el marcador inteligente estándar que hace referencia a la propiedad de matriz del origen de datos vinculado.
- `arrayassingle:true` — indica al motor que renderice toda la matriz en una sola celda en lugar de expandir sus elementos.
- `arraydelimiter:;` — opcional; define el separador que se coloca entre los elementos de la matriz. Si se omite, se utiliza una coma.

{{% alert color="warning" %}}
Escriba los atributos en formato `name:value` (con dos puntos, no un signo igual) y separe varios atributos con una coma **sin espacios**. Un espacio después de la coma desplaza el valor analizado un carácter: `(arrayassingle:true, arraydelimiter:;)` uniría los elementos con el separador erróneo `:;` en lugar de `;`.
{{% /alert %}}

### **Formas del delimitador**

- Un carácter individual se escribe inmediatamente después de los dos puntos: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separador de varios caracteres se escribe entre comillas dobles: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flujo de trabajo paso a paso**

El siguiente flujo de trabajo describe cómo renderizar una matriz en una sola celda mediante marcadores inteligentes.
1. **Prepare el origen de datos**: Cree una clase de JavaBean con el modificador `public` y un método de lectura que devuelva la matriz, como `String[] getTags()`, y vincule una `java.util.List` de JavaBeans para que el motor lea un registro por fila. Los campos públicos por sí solos no se vinculan: el motor lee los métodos de acceso de JavaBean.
2. **Cree un libro de trabajo de diseño**: Cree un nuevo `Workbook`, añada una fila de encabezado y coloque en una celda un marcador inteligente que haga referencia a la propiedad de matriz con el atributo `arrayassingle` (y `arraydelimiter` cuando necesite un separador personalizado).
3. **Instancie `WorkbookDesigner`**: Cree un `WorkbookDesigner` alrededor del libro de trabajo y vincule su lista con `setDataSource`.
4. **Procese los marcadores**: Llame al método `WorkbookDesigner.process()` para expandir los marcadores inteligentes y rellenar el libro de trabajo con datos reales.
5. **Guarde el resultado**: Guarde el libro de trabajo resultante en disco en XLSX o en cualquier otro formato de archivo compatible.

### **Ejemplo de código 1 — Renderizado básico de una matriz de cadenas**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

El ejemplo imprime el valor concatenado de la matriz completa. Las cuatro etiquetas se colocan en una sola celda, separadas por la coma predeterminada:

```
C#,Aspose,SmartMarker,Excel
```

### **Ejemplo de código 2 — Valores numéricos con un delimitador personalizado**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

Los valores numéricos se concatenan exactamente igual que las cadenas cuando la propiedad de matriz devuelve `String[]`:

```
95-88-76-100-67
```

{{% alert color="note" %}}
En Java, mantenga la propiedad de matriz como `String[]`. Una propiedad primitiva `int[]` concatenada en una sola celda renderiza el texto `toString` del objeto de matriz (por ejemplo, `[I@1a2b3c4d`) en lugar de los números, porque la concatenación opera sobre la forma de cadena de cada elemento y una matriz primitiva es un único elemento opaco.
{{% /alert %}}

### **Ejemplo de código 3 — Comparación entre el renderizado predeterminado y en una sola celda**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

El marcador predeterminado llena una celda por elemento hacia abajo en la columna B, mientras que el marcador con `arrayassingle` concentra la misma matriz en una sola celda de la columna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notas y prácticas recomendadas**

Tenga en cuenta los siguientes puntos al trabajar con los atributos `arrayassingle` y `arraydelimiter`:
- Los valores de los atributos usan el formato `name:value`. No se reconoce una forma con signo igual, como `arrayassingle=true`, y se recurre silenciosamente al comportamiento predeterminado de expansión.
- Separe los atributos con una coma y sin espacios; un espacio después de la coma desplaza el valor del delimitador un carácter (consulte la advertencia anterior).
- El valor de `arraydelimiter` puede ser un carácter individual escrito directamente después de los dos puntos o una cadena de varios caracteres entre comillas dobles.
- Cuando se omite `arraydelimiter`, los elementos se concatenan con una coma.
- Vincule una `java.util.List` de JavaBeans públicos con métodos de lectura de matrices. Un único objeto JavaBean o los campos públicos por sí solos dejan los marcadores sin resolver.
- Mantenga las propiedades de matriz como `String[]`; una matriz primitiva `int[]` renderiza su texto `toString` al concatenarse (consulte la nota anterior).
- Coloque el marcador inteligente en una celda con suficiente anchura para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente hacia las celdas adyacentes, en función del formato.

## **Artículos relacionados**
- [Agregar Campos de Filtro a una Tabla Dinámica en Aspose.Cells for Java](/cells/es/java/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for Java](/cells/es/java/apply-style-to-pivot-table/)
- [Modificar el diseño del campo de página en una tabla dinámica](/cells/es/java/change-page-field-layout/)
- [Convertir minigráficos a imágenes y HTML con Aspose.Cells for Java](/cells/es/java/convert-sparkline-to-image-and-html/)
- [Conversión de Excel a formato OFD](/cells/es/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}