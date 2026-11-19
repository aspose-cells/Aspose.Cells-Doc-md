---
title: Renderizado de arrays en una sola celda con SmartMarker | Aspose.Cells for Node.js via Java
description: Aprenda a renderizar datos de arrays en una sola celda usando los atributos de Smart Marker arrayassingle y arraydelimiter en Aspose.Cells for Node.js via Java.
linktitle: Renderizado de arrays en una sola celda con SmartMarker | Aspose.Cells for Node.js via Java
url: /es/nodejs-java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, biblioteca de Node.js via Java, hoja de cálculo, Smart Markers, arrayassingle, arraydelimiter, array de una sola celda, renderizado de arrays, plantilla
type: docs
weight: 195
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells puede renderizar un origen de datos de array en una sola celda mediante Smart Markers. El atributo `arrayassingle` desactiva la expansión predeterminada elemento por elemento y el atributo `arraydelimiter` selecciona el separador que se coloca entre los elementos concatenados: una coma de forma predeterminada, o cualquier carácter individual o cadena de varios caracteres entre comillas que especifique.
{{% /alert %}}

## **Introducción**

Los Smart Markers de Aspose.Cells son una funcionalidad basada en plantillas que completa dinámicamente los datos de hojas de cálculo mediante expresiones de marcador como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando la plantilla se procesa con `WorkbookDesigner`, los marcadores se sustituyen por valores del origen de datos proporcionado.
De forma predeterminada, cuando un Smart Marker hace referencia a un campo de array, por ejemplo `&=Product.Tags` enlazado a un array de cuatro valores, el motor expande el array y coloca cada elemento en su propia celda, extendiendo los valores verticalmente hacia abajo por la columna, debajo del marcador. Aunque este comportamiento resulta práctico en muchos escenarios, en algunos casos es preferible renderizar el array completo en una sola celda, con los elementos concatenados y separados por un delimitador de su elección.
Los atributos `arrayassingle` y `arraydelimiter`, escritos dentro de los paréntesis de un Smart Marker en forma `name:value`, cubren exactamente esta necesidad. Permiten mantener los diseños de informes compactos y predecibles al tiempo que se trabaja de forma nativa con orígenes de datos de array.

## **Por qué se necesita esta funcionalidad**

### **Comportamiento predeterminado de expansión de arrays**

Cuando un Smart Marker hace referencia a un campo de array, Aspose.Cells expande el array en varias celdas de forma predeterminada. Por ejemplo, un marcador como `&=Product.Tags` aplicado a un array con cuatro valores coloca cada valor en su propia celda debajo del marcador, desplazando el resto del contenido de la plantilla y posiblemente alterando diseños de informes cuidadosamente elaborados.

### **Limitaciones de los casos de uso**

Existen muchos escenarios prácticos en los que el comportamiento predeterminado de expansión no es deseable:
- **Informes de tipo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que deben mostrarse como valores separados por comas o barras verticales dentro de una sola celda.
- **Chips de filtro o indicadores de estado** que agrupan varios valores en un mismo lugar para facilitar la lectura.
- **Flujos de procesamiento posteriores** (exportación CSV, renderizado PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, donde algunos consumidores no admiten arrays que se propagan por varias celdas.

### **La necesidad que cubre**

Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar los datos en JavaScript, uniendo los arrays en cadenas delimitadas antes de enlazarlos al diseñador del libro de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `arrayassingle` y `arraydelimiter` eliminan esta solución alternativa al gestionar el formato de forma declarativa dentro del propio Smart Marker.

## **Ventajas de la funcionalidad**

El uso de los atributos `arrayassingle` y `arraydelimiter` en los Smart Markers ofrece varias ventajas:
- **Contención en una sola celda**: Todos los elementos del array se renderizan exactamente en una celda, lo que mantiene los diseños compactos y predecibles.
- **Control personalizado del delimitador**: Especifique el separador que prefiera: una coma de forma predeterminada, un punto y coma, un guion, una barra vertical o una cadena de varios caracteres entre comillas como `" | "`.
- **Formato basado en plantillas**: No se necesita código adicional para preprocesar los datos; las reglas de formato se definen dentro de la etiqueta Smart Marker.
- **Informes más claros**: Los datos de los arrays ya no desplazan el contenido vecino de la plantilla a otras filas o columnas.
- **Tipos de datos versátiles**: Funciona con arrays de cadenas proporcionados como filas JSON, incluidos valores numéricos representados como cadenas.
- **Compatibilidad hacia atrás**: Cuando se omiten los atributos, se conserva el comportamiento original de expansión, por lo que las plantillas existentes continúan funcionando sin cambios.

## **Cómo utilizar esta funcionalidad**

### **Sintaxis de Smart Marker**

Los atributos `arrayassingle` y `arraydelimiter` utilizan la gramática de atributos `name:value` de Aspose.Cells dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```
&=DataSource.ArrayField(arrayassingle:true,arraydelimiter:;)
```

El marcador se compone de las siguientes partes:
- `&=DataSource.ArrayField` — el Smart Marker estándar que hace referencia al campo de array del origen de datos enlazado.
- `arrayassingle:true` — indica al motor que debe renderizar el array completo en una sola celda en lugar de expandir sus elementos.
- `arraydelimiter:;` — opcional; define el separador que se coloca entre los elementos del array. Si se omite, se utiliza una coma.

{{% alert color="warning" %}}
Escriba los atributos en forma `name:value` (dos puntos, no un signo igual) y separe varios atributos con una coma **sin espacios**. Un espacio después de la coma desplaza el valor analizado un carácter: `(arrayassingle:true, arraydelimiter:;)` uniría los elementos con el separador erróneo `:;` en lugar de `;`.
{{% /alert %}}

### **Formas del delimitador**

- Un carácter individual sigue directamente a los dos puntos: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- Un separador de varios caracteres se escribe entre comillas dobles: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Flujo de trabajo paso a paso**

El siguiente flujo de trabajo describe cómo renderizar un array en una sola celda mediante Smart Markers.
1. **Preparar el origen de datos**: Organice cada registro como un objeto JSON cuyo campo contiene un array, por ejemplo `{"Tags": ["C#", "Aspose"]}`. Los objetos y arrays de JavaScript ordinarios que se pasan a `setDataSource` no se enlazan en esta plataforma; las filas JSON constituyen el formato tabular admitido.
2. **Crear un libro de trabajo de diseño**: Cree un nuevo `Workbook`, añada una fila de encabezado y coloque una celda de Smart Marker que haga referencia al campo de array con el atributo `arrayassingle` y con `arraydelimiter` cuando sea necesario un separador personalizado.
3. **Instanciar el WorkbookDesigner**: Cree un `WorkbookDesigner` alrededor del libro de trabajo y adjunte las filas JSON con `setJsonDataSource`.
4. **Procesar los marcadores**: Llame al método `workbookDesigner.process()` para expandir los Smart Markers y completar el libro de trabajo con los datos reales.
5. **Guardar el resultado**: Guarde el libro de trabajo resultante en disco en formato XLSX o en cualquier otro formato de archivo admitido.

### **Ejemplo de código 1: renderizado básico de un array de cadenas**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Tags");
// No spaces inside the parentheses: attributes are name:value pairs
worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Product",
    '[{"Tags": ["C#", "Aspose", "SmartMarker", "Excel"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-single.xlsx");
```

El ejemplo imprime el valor concatenado de todo el array. Las cuatro etiquetas quedan en una sola celda, separadas por la coma predeterminada:

```
C#,Aspose,SmartMarker,Excel
```

### **Ejemplo de código 2: valores numéricos con un delimitador personalizado**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().get("A1").putValue("Scores");
// arraydelimiter:- joins the values with a hyphen
worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Student",
    '[{"Scores": ["95", "88", "76", "100", "67"]}]');
designer.process();
console.log(worksheet.getCells().get("A2").getStringValue());
workbook.save("output-array-numeric.xlsx");
```

Cuando las puntuaciones se proporcionan como cadenas JSON, la salida concatenada conserva los valores numéricos sin decimales adicionales:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Los números JSON que pasan por el motor Java llegan como números de doble precisión, por lo que `[95, 88]` se concatenaría como `95.0-88.0`. Ponga entre comillas los números de las filas JSON cuando necesite que la celda concatenada contenga exactamente el texto entero.
{{% /alert %}}

### **Ejemplo de código 3: comparación entre el renderizado predeterminado y en una sola celda**

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const cells = workbook.getWorksheets().get(0).getCells();
// Column B: default marker — values spread vertically down the column
cells.get("B1").putValue("Default");
cells.get("B2").putValue("&=Order.Items");
// Column C: single-cell rendering — the whole array joins into one cell
cells.get("C1").putValue("Single cell");
cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
const designer = new AsposeCells.WorkbookDesigner(workbook);
designer.setJsonDataSource(
    "Order",
    '[{"Items": ["Apple", "Banana", "Cherry", "Date"]}]');
designer.process();
for (let row = 1; row <= 5; row++) {
    const b = cells.get(row, 1).getStringValue() || "";
    const c = cells.get(row, 2).getStringValue() || "";
    if (b || c) console.log(`B${row + 1}=[${b}]  C${row + 1}=[${c}]`);
}
workbook.save("output-array-comparison.xlsx");
```

El marcador predeterminado llena una celda por cada elemento hacia abajo en la columna B, mientras que el marcador `arrayassingle` condensa el mismo array en una sola celda de la columna C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Notas y prácticas recomendadas**

Al trabajar con los atributos `arrayassingle` y `arraydelimiter`, tenga en cuenta lo siguiente:
- Los valores de los atributos usan la forma `name:value`. Una forma con signo igual, como `arrayassingle=true`, no se reconoce y vuelve silenciosamente al comportamiento predeterminado de expansión.
- Separe los atributos con una coma y sin espacios; un espacio después de la coma desplaza el valor del delimitador un carácter, como se indica en la advertencia anterior.
- El valor de `arraydelimiter` puede ser un carácter individual escrito directamente después de los dos puntos o una cadena de varios caracteres entre comillas dobles.
- Cuando se omite `arraydelimiter`, los elementos se unen con una coma.
- Proporcione los campos de array mediante objetos de fila de `setJsonDataSource`; los objetos y arrays de JavaScript ordinarios que se pasan a `setDataSource` no se enlazan en esta plataforma.
- Los números JSON llegan como números de doble precisión a través del motor Java (`95` se concatena como `95.0`); ponga entre comillas los valores numéricos de las filas JSON cuando sea importante conservar el texto entero exacto.
- Coloque el Smart Marker en una celda con anchura suficiente para mostrar la cadena concatenada resultante; de lo contrario, el contenido puede desbordarse visualmente hacia las celdas adyacentes, según el formato.

## **Artículos relacionados**
- [Agregar campos de filtro a una tabla dinámica en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/add-page-field-in-pivot-table/)
- [Aplicar estilos a tablas dinámicas en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/apply-style-to-pivot-table/)
- [Modificar el diseño del campo de página en una tabla dinámica](/cells/es/nodejs-java/change-page-field-layout/)
- [Convertir Sparkline a Imagen y HTML en Aspose.Cells for Node.js via Java](/cells/es/nodejs-java/convert-sparkline-to-image-and-html/)
- [Conversión de Excel a formato OFD](/cells/es/nodejs-java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="nodejs-java" >}}