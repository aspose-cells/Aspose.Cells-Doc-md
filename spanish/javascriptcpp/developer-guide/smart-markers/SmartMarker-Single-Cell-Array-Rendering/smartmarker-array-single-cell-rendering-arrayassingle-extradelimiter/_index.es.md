---
title: Renderizado de matrices en una sola celda con SmartMarker | Aspose.Cells for JavaScript via C++
description: Aprenda a renderizar datos de matriz en una sola celda mediante los atributos ArrayAsSingle y ExtraDelimiter en Smart Markers con Aspose.Cells for JavaScript via C++.
linktitle: Renderizado de matrices en una sola celda con SmartMarker | Aspose.Cells
url: /es/javascript-cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, biblioteca Aspose.Cells for JavaScript via C++, hoja de cálculo, Smart Markers, ArrayAsSingle, ExtraDelimiter, matriz en una sola celda, renderizado de matrices, plantilla
type: docs
weight: 195
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells permite renderizar datos de matriz en una sola celda mediante Smart Markers. Al usar el atributo `ArrayAsSingle` junto con el atributo `ExtraDelimiter`, los desarrolladores pueden controlar cómo se separan los elementos de la matriz dentro de una sola celda, lo que ofrece un formato flexible para informes y plantillas.
{{% /alert %}}

## **Introducción**
Los Smart Markers de Aspose.Cells constituyen una potente función basada en plantillas que permite rellenar dinámicamente los datos de una hoja de cálculo mediante expresiones de marcador como `&=DataSource.Field`. El marcador se coloca en un libro de trabajo de diseño y, cuando `WorkbookDesigner` procesa la plantilla, los marcadores se reemplazan por valores de la fuente de datos proporcionada.
De forma predeterminada, cuando un Smart Marker hace referencia a una propiedad de matriz (por ejemplo, `&=DataSource.Numbers`), el motor expande la matriz y coloca cada elemento en una celda adyacente independiente, ya sea horizontalmente en una fila o verticalmente en una columna. Aunque este comportamiento resulta práctico en muchos escenarios, hay situaciones en las que es preferible renderizar toda la matriz en una sola celda, concatenando sus elementos y separándolos con el delimitador que se elija.
Los atributos `ArrayAsSingle` y `ExtraDelimiter`, utilizados en conjunto dentro de una etiqueta de Smart Marker, cubren exactamente esta necesidad. Permiten mantener los diseños de informes compactos y predecibles al tiempo que se trabaja de forma nativa con fuentes de datos de matrices.

## **Por qué se necesita esta función**

### **Comportamiento predeterminado de propagación de matrices**
Cuando un Smart Marker hace referencia a una propiedad de matriz, Aspose.Cells expande la matriz en varias celdas de forma predeterminada. Por ejemplo, un marcador como `&=Product.Tags` aplicado a una matriz que contiene cuatro cadenas colocará cada valor en su propia celda, desplazando el resto del contenido de la plantilla y potencialmente alterando los diseños de informes cuidadosamente diseñados.

### **Limitaciones de los casos de uso**
Existen numerosos escenarios prácticos en los que el comportamiento predeterminado de propagación no resulta adecuado:
- **Informes de estilo resumen** que necesitan un diseño compacto de una fila por registro.
- **Listas de etiquetas, rótulos o palabras clave** que deben mostrarse como valores separados por comas o barras verticales dentro de una sola celda.
- **Filtros o indicadores de estado** que agrupan varios valores en un mismo lugar para facilitar la lectura.
- **Procesos posteriores** (exportación a CSV, renderizado a PDF, combinación de correspondencia) que esperan un único valor consolidado por celda en lugar de un rango expandido.
- **Compatibilidad multiplataforma**, donde algunos consumidores no admiten matrices que se extienden por varias celdas.

### **La necesidad que cubre**
Sin un mecanismo integrado, los desarrolladores se verían obligados a preprocesar los datos en JavaScript, combinando las matrices en cadenas delimitadas antes de vincularlas al diseñador de libros de trabajo. Esto duplica la lógica, complica los modelos de datos y aumenta la posibilidad de errores. Los atributos `ArrayAsSingle` y `ExtraDelimiter` eliminan esta solución alternativa al gestionar el formato de forma declarativa dentro del propio Smart Marker.

## **Ventajas de la función**
El uso de los atributos `ArrayAsSingle` y `ExtraDelimiter` en los Smart Markers ofrece varias ventajas:
- **Contención en una sola celda**: Todos los elementos de la matriz se renderizan en exactamente una celda, lo que mantiene los diseños compactos y predecibles.
- **Control del delimitador personalizado**: Especifique cualquier cadena como separador: coma, punto y coma, guion, barra vertical, nueva línea o cualquier texto personalizado.
- **Formato basado en plantillas**: No se requiere código adicional para preprocesar los datos; las reglas de formato se definen dentro de la etiqueta de Smart Marker.
- **Informes más limpios**: Los datos de matriz ya no desplazan el contenido vecino de la plantilla hacia otras filas o columnas.
- **Tipos de datos versátiles**: Funciona con cadenas, números, fechas y cualquier otro tipo de datos que pueda combinarse con un delimitador.
- **Compatibilidad con versiones anteriores**: Cuando se omiten los atributos, se conserva el comportamiento original de propagación, por lo que las plantillas existentes siguen funcionando sin cambios.

## **Cómo usar esta función**

### **Sintaxis de Smart Marker**
Los atributos `ArrayAsSingle` y `ExtraDelimiter` se pasan como pares de clave-valor dentro de los paréntesis de un Smart Marker estándar. La sintaxis general es:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const product = {
                Tags: ["C#", "Aspose", "SmartMarker", "Excel"]
            };
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Tags";
            cells.get("A2").value = '&=Product.Tags(arrayasSingle=true, extraDelimiter=", ")';
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Product", product);
            designer.process();
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_arraySingle.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

El marcador está compuesto por las siguientes partes:
- `&=DataSource.ArrayProperty` — el Smart Marker estándar que hace referencia a la propiedad de matriz de la fuente de datos vinculada.
- `arrayasSingle=true` — instruye al motor para que renderice toda la matriz en una sola celda. Solo el valor `true` activa el comportamiento de celda única.
- `extraDelimiter=", "` — define el separador que se coloca entre los elementos de la matriz. El valor es un literal de cadena; puede estar vacío, ser un único carácter o una cadena de varios caracteres.

{{% alert color="primary" %}}
El atributo `extraDelimiter` acepta cualquier literal de cadena, incluidos delimitadores de varios caracteres, texto personalizado o secuencias de escape como `\n` para obtener una salida separada por nuevas líneas. Si la matriz está vacía, la celda resultante se deja en blanco.
{{% /alert %}}

### **Flujo de trabajo paso a paso**
El siguiente flujo de trabajo describe cómo renderizar una matriz en una sola celda mediante Smart Markers.
1. **Preparar la fuente de datos**: Cree un objeto o una estructura de datos que exponga una propiedad que devuelva una matriz. La propiedad puede devolver una matriz de cadenas, números o cualquier otro tipo de valor admitido.
2. **Crear un libro de trabajo de diseño**: Cree un nuevo `Workbook`, añada una fila de encabezado y coloque una celda de Smart Marker que haga referencia a la propiedad de la matriz con los atributos `arrayasSingle` y `extraDelimiter`.
3. **Instanciar `WorkbookDesigner`**: Cree un objeto `WorkbookDesigner`, adjunte el libro de trabajo de diseño y vincule la fuente de datos mediante el método `setDataSource`.
4. **Procesar los marcadores**: Llame al método `workbookDesigner.process()` para expandir los Smart Markers y rellenar el libro de trabajo con datos reales.
5. **Guardar el resultado**: Guarde el libro de trabajo resultante en el disco en XLSX o cualquier otro formato de archivo admitido.

### **Ejemplo de código 1 — Renderizado básico de una matriz de cadenas**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        class Student {
            constructor(scores) {
                this.Scores = scores;
            }
        }
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            document.getElementById("runExample").disabled = false;
            console.log("Aspose.Cells initialized");
        });
        document.getElementById("runExample").addEventListener("click", async () => {
            const student = new Student([95, 88, 76, 100, 67]);
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Scores";
            cells.get("A2").value = student.Scores.join(" - ");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById("downloadLink");
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_numericArray.xlsx";
            downloadLink.style.display = "block";
            document.getElementById("result").innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Ejemplo de código 2 — Matriz numérica con delimitador personalizado**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, WorkbookDesigner, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const order = {
                Items: ["Apple", "Banana", "Cherry", "Date"]
            };
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            const cells = sheet.cells;
            // Sección 1: Marcador inteligente predeterminado: los valores se distribuyen horizontalmente entre las celdas
            cells.get("A1").value = "Default Spreading Behavior:";
            cells.get("A2").value = "&=Order.Items";
            // Sección 2: Nueva renderización en una sola celda usando arrayasSingle y extraDelimiter
            cells.get("A4").value = "Single Cell Rendering (arrayasSingle=true):";
            cells.get("A5").value = '&=Order.Items(arrayasSingle=true, extraDelimiter="; ")';
            // Vincular la fuente de datos y procesar los marcadores inteligentes
            const designer = new WorkbookDesigner();
            designer.setWorkbook(workbook);
            designer.setDataSource("Order", order);
            designer.process();
            // Guardar el libro de trabajo resultante
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_comparison.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Ejemplo de código 3 — Comparación del comportamiento predeterminado y de ArrayAsSingle**

### **Notas y prácticas recomendadas**
Al trabajar con los atributos `ArrayAsSingle` y `ExtraDelimiter`, tenga en cuenta lo siguiente:
- El valor `extraDelimiter` se trata como un literal de cadena; escape cualquier carácter especial que el procesador de plantillas pueda interpretar.
- El atributo `arrayasSingle` acepta un valor booleano (`true` / `false`). Solo `true` activa el comportamiento de celda única; cualquier otro valor vuelve al comportamiento predeterminado de propagación.
- Si la matriz está vacía o es `null`, la celda queda vacía o contiene una cadena vacía, según el tipo de datos.
- La función funciona tanto con fuentes de datos de objetos como con fuentes de datos tabulares en las que una columna puede dividirse en matrices.
- Para obtener una salida separada por nuevas líneas, use `\n` como valor del delimitador.

{{< app/cells/assistant language="javascript-cpp" >}}