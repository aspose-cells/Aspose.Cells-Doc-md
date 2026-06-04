---
title: Renderización de matriz de una sola celda con SmartMarker | Aspose.Cells for Node.js via Java
description: Aprenda cómo renderizar datos de matriz en una sola celda utilizando los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for Node.js via Java.
keywords: Aspose.Cells, biblioteca Node.js via Java, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, matriz de una sola celda, renderización de matriz, plantilla
type: docs
weight: 195
url: /es/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells admite la renderización de datos de matriz en una sola celda a través de Smart Markers. Mediante el uso del atributo `ArrayAsSingle` junto con el atributo `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos de la matriz dentro de una sola celda, proporcionando un formato flexible para informes y plantillas.

{{% /alert %}}

## **Introducción**

Los Smart Markers en Aspose.Cells son una potente función basada en plantillas que le permite poblar dinámicamente las hojas de cálculo con datos utilizando expresiones de marcadores como `&=DataSource.Field`. El marcador se coloca en un libro de diseño, y cuando la plantilla es procesada por el `WorkbookDesigner`, los marcadores se reemplazan con valores del origen de datos proporcionado.

Por defecto, cuando un Smart Marker hace referencia a una propiedad de matriz (por ejemplo, `&=DataSource.Numbers`), el motor expande la matriz y coloca cada elemento en una celda adyacente separada, ya sea horizontalmente a lo largo de una fila o verticalmente hacia abajo en una columna. Si bien este comportamiento es conveniente en muchos escenarios, hay situaciones en las que preferiría renderizar toda la matriz en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.

Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados juntos dentro de una etiqueta Smart Marker, abordan exactamente este requisito. Le permiten mantener diseños de informes compactos y predecibles mientras sigue trabajando de forma nativa con orígenes de datos de matrices.

## **Por qué se necesita esta función**

### **Comportamiento predeterminado de expansión de matrices**

Cuando un Smart Marker hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz a través de varias celdas por defecto. Por ejemplo, un marcador como `&=Product.Tags` contra un `string[]` que contiene cuatro valores colocará cada valor en su propia celda, empujando el resto del contenido de la plantilla hacia afuera y potencialmente rompiendo los diseños de informes cuidadosamente diseñados.

### **Limitaciones de los casos de uso**

Hay muchos escenarios prácticos donde el comportamiento de expansión predeterminado no es deseable:

- **Informes de estilo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de tags, etiquetas o palabras clave** que necesitan mostrarse como valores separados por comas o por tuberías dentro de una sola celda.
- **Indicadores de chips de filtro o de estado** que agrupan múltiples valores en un solo lugar para facilitar la lectura.
- **Pipelines posteriores** (exportación a CSV, renderización a PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, donde algunos consumidores no toleran matrices que se extienden a través de varias celdas.

### **El vacío que llena**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar los datos en JavaScript, uniendo matrices en cadenas delimitadas antes de vincularlas al `WorkbookDesigner`. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al manejar el formato de forma declarativa dentro del propio Smart Marker.

## **Beneficios de la función**

El uso de los atributos `ArrayAsSingle` y `ExtraDelimiter` en sus Smart Markers proporciona varias ventajas:

- **Contención en una sola celda**: Todos los elementos de la matriz se renderizan en exactamente una celda, manteniendo los diseños compactos y predecibles.
- **Control personalizado del delimitador**: Especifique cualquier cadena separadora que desee: coma, punto y coma, guión, tubería, nueva línea o cualquier texto personalizado.
- **Formato basado en plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato viven dentro de la etiqueta Smart Marker.
- **Informes más limpios**: Los datos de matriz ya no empujan el contenido de la plantilla vecina a diferentes filas o columnas.
- **Tipos de datos versátiles**: Funciona con cadenas, números, fechas y cualquier otro tipo de datos que se pueda unir con un delimitador.
- **Compatibilidad con versiones anteriores**: Cuando se omiten los atributos, se conserva el comportamiento de expansión original, por lo que las plantillas existentes siguen funcionando sin cambios.

## **Cómo usar esta función**

### **Sintaxis del Smart Marker**

Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

El marcador se compone de las siguientes partes:

- `&=DataSource.ArrayProperty` — el Smart Marker estándar que hace referencia a la propiedad de matriz en el origen de datos vinculado.
- `arrayasSingle=true` — indica al motor que renderice toda la matriz en una sola celda. Solo el valor `true` activa el comportamiento de una sola celda.
- `extraDelimiter=", "` — define el separador colocado entre los elementos de la matriz. El valor es una cadena literal; puede estar vacío, ser un solo carácter o una cadena de varios caracteres.

{{% alert color="primary" %}}

El atributo `extraDelimiter` acepta cualquier cadena literal, incluidos delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para salida separada por nuevas líneas. Si la matriz está vacía, la celda resultante se deja en blanco.

{{% /alert %}}

### **Flujo de trabajo paso a paso**

El siguiente flujo de trabajo describe cómo renderizar una matriz en una sola celda utilizando Smart Markers.

1. **Prepare el origen de datos**: Cree una clase (o estructura de datos) que exponga una propiedad que devuelva una matriz. La propiedad puede devolver `string[]`, `int[]` o cualquier otro tipo de matriz admitido.
2. **Cree un libro de diseño**: Cree un nuevo `Workbook`, agregue una fila de encabezado y coloque una celda Smart Marker que haga referencia a la propiedad de matriz con los atributos `arrayasSingle` y `extraDelimiter`.
3. **Cree una instancia del WorkbookDesigner**: Cree un objeto `WorkbookDesigner`, adjunte el libro de diseño y vincule su origen de datos utilizando el método `setDataSource`.
4. **Procese los marcadores**: Llame al método `workbookDesigner.process()` para expandir los Smart Markers y poblar el libro con datos reales.
5. **Guarde el resultado**: Guarde el libro resultante en disco en formato XLSX o cualquier otro formato de archivo admitido.

### **Ejemplo de código 1 — Renderización básica de matriz de cadenas**

```javascript
class Product {
    constructor() {
        this.Tags = null;
    }
}

const product = new Product();
product.Tags = ["C#", "Aspose", "SmartMarker", "Excel"];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Tags");
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

const designer = new AsposeCells.WorkbookDesigner();
designer.setWorkbook(workbook);
designer.setDataSource("Product", product);
designer.process();

workbook.save("output_arraySingle.xlsx");
```

### **Ejemplo de código 2 — Matriz numérica con delimitador personalizado**

```javascript
class Student {
    constructor() {
        this.Scores = [];
    }
}

const student = new Student();
student.Scores = [95, 88, 76, 100, 67];

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

worksheet.getCells().get("A1").putValue("Scores");
worksheet.getCells().get("A2").putValue(student.Scores.join(" - "));

workbook.save("output_numericArray.xlsx");
```

### **Ejemplo de código 3 — Comparación entre el comportamiento predeterminado y ArrayAsSingle**

```javascript
const AsposeCells = require("aspose.cells");

function main() {
    const order = {
        Items: ["Apple", "Banana", "Cherry", "Date"]
    };

    const workbook = new AsposeCells.Workbook();
    const sheet = workbook.getWorksheets().get(0);
    const cells = sheet.getCells();

    // Sección 1: Marcador Inteligente predeterminado - valores distribuidos horizontalmente entre celdas
    cells.get("A1").putValue("Comportamiento de Distribución Predeterminado:");
    cells.get("A2").putValue("&=Order.Items");

    // Sección 2: Nueva renderización de celda única usando arrayasSingle y extraDelimiter
    cells.get("A4").putValue("Renderización de Celda Única (arrayasSingle=true):");
    cells.get("A5").putValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Vincular la fuente de datos y procesar los Marcadores Inteligentes
    const designer = new AsposeCells.WorkbookDesigner(workbook);
    designer.setDataSource("Order", order);
    designer.process();

    // Guardar el libro de trabajo resultante
    workbook.save("output_comparison.xlsx");
}

main();
```

### **Notas y mejores prácticas**

Tenga en cuenta los siguientes puntos al trabajar con los atributos `ArrayAsSingle` y `ExtraDelimiter`:

- El valor de `extraDelimiter` se trata como una cadena literal; escape cualquier carácter especial que su procesador de plantillas pueda interpretar.
- El atributo `arrayasSingle` acepta un valor booleano (`true` / `false`). Solo `true` activa el comportamiento de una sola celda; cualquier otro valor vuelve al comportamiento de expansión predeterminado.
- Si la matriz está vacía o es nula, la celda se deja vacía (o contiene una cadena en blanco según el tipo de datos).
- La función funciona con orígenes de datos de objetos, así como con orígenes `DataSet` y `DataTable` donde una columna se puede dividir en matrices.
- Para salida separada por nuevas líneas, puede usar `\n` como valor del delimitador.
- Coloque el Smart Marker en una celda que tenga ancho suficiente para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente hacia las celdas adyacentes según el formato.



{{< app/cells/assistant language="javascript" >}}