---
title: Gestiona las Propiedades del Documento con JavaScript a través de C++
linktitle: Propiedades del documento
type: docs
weight: 80
url: /es/javascript-cpp/managing-document-properties/
description: Aprende cómo gestionar las Propiedades del Documento mediante las APIs Aspose.Cells for JavaScript a través de C++.
keywords: Cómo gestionar las Propiedades del Documento en JavaScript a través de C++, obtener o establecer Propiedades del Documento usando JavaScript a través de C++, agregar o eliminar Propiedades del Documento via JavaScript a través de C++, insertar o quitar Propiedades del Documento con JavaScript a través de C++, cómo acceder a las Propiedades del Documento usando APIs Aspose.Cells for JavaScript a través de C++.
---

## **Introducción**

Microsoft Excel proporciona la capacidad de agregar propiedades a los archivos de hojas de cálculo. Estas propiedades del documento proporcionan información útil y se dividen en 2 categorías como se detalla a continuación.

- Propiedades predeterminadas del sistema (integradas): Las propiedades integradas contienen información general sobre el documento, como el título del documento, el nombre del autor, estadísticas del documento, entre otros.
- Propiedades definidas por el usuario (personalizadas): Propiedades personalizadas definidas por el usuario final en forma de par nombre-valor.

{{% alert color="primary" %}}

El punto más importante a tener en cuenta sobre las propiedades integradas y personalizadas es que las propiedades integradas se pueden acceder y modificar, pero no crear ni eliminar. Sin embargo, las propiedades personalizadas se pueden crear y gestionar.

{{% /alert %}}

## **Cómo administrar propiedades de documento utilizando Microsoft Excel**

Microsoft Excel te permite gestionar las propiedades del documento de los archivos de Excel de forma WYSIWYG. Por favor, sigue los pasos a continuación para abrir el diálogo de **Propiedades** en Excel 2016.

1. Desde el menú **Archivo**, seleccione **Información**.

|**Seleccionar menú Información**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. Haga clic en el encabezado **Propiedades** y seleccione "Propiedades avanzadas".

|**Haciendo clic en la selección de Propiedades avanzadas**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Administre las propiedades del documento del archivo.

|**Cuadro de propiedades**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
En el cuadro de propiedades, hay pestañas diferentes, como General, Resumen, Estadísticas, Contenidos y Aduanas. Cada pestaña ayuda a configurar diferentes tipos de información relacionada con el archivo. La pestaña Aduanas se usa para gestionar propiedades personalizadas.

## **Cómo trabajar con las propiedades del documento usando Aspose.Cells**

Los desarrolladores pueden gestionar dinámicamente las propiedades del documento usando las APIs de Aspose.Cells. Esta característica ayuda a los desarrolladores a almacenar información útil junto con el archivo, como cuándo se recibió el archivo, se procesó, se marcó con la hora, y así sucesivamente.

{{% alert color="primary" %}}

Aspose.Cells for JavaScript a través de C++ escribe directamente la información sobre la API y el Número de Versión en los documentos de salida. Por ejemplo, al renderizar el Documento a PDF, Aspose.Cells for JavaScript a través de C++ llena el campo **Aplicación** con el valor 'Aspose.Cells' y el campo **Productor de PDF** con el valor, por ejemplo, 'Aspose.Cells v17.9'.

Ten en cuenta que no puedes instruir a Aspose.Cells for JavaScript a través de C++ para cambiar o eliminar esta información de los Documentos de salida.

{{% /alert %}}

### **Cómo acceder a las propiedades del documento**

Las APIs de Aspose.Cells soportan ambos tipos de propiedades del documento, integradas y personalizadas. La clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) de Aspose.Cells representa un archivo de Excel y, como un archivo de Excel, la clase [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) puede contener múltiples hojas de cálculo, cada una representada por la clase [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) mientras que la colección de hojas de cálculo está representada por la clase [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection).

Utiliza [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) para acceder a las propiedades del documento del archivo como se describe a continuación.

- Para acceder a las propiedades de documento integradas, use [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--).
- Para acceder a las propiedades de documento personalizadas, use [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--).

Tanto [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) como [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--) devuelven la instancia de [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/). Esta colección contiene [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) objetos, cada uno de los cuales representa una sola propiedad del documento, ya sea integrada o personalizada.

Depende del requisito de la aplicación cómo acceder a una propiedad; es decir, usando el índice o el nombre de la propiedad desde [**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/) como se demuestra en el ejemplo a continuación.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

La clase [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) permite recuperar el nombre, valor y tipo de la propiedad del documento:

- Para obtener el nombre de la propiedad, use [**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--).
- Para obtener el valor de la propiedad, usa [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) devuelve el valor como un Objeto.
- Para obtener el tipo de propiedad, usa [**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--). Esto devuelve uno de los valores de la enumeración [**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/). Después de obtener el tipo de propiedad, usa uno de los métodos **DocumentProperty.ToXXX** para obtener el valor del tipo apropiado en lugar de usar [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). Los métodos **DocumentProperty.ToXXX** se describen en la tabla a continuación.

{{% alert color="primary" %}}

La clase [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) también proporciona un conjunto de métodos que devuelven los valores de otros tipos de datos.

{{% /alert %}}

|**Nombre de Miembro**|**Descripción**|**Método ToXXX**|
| :- | :- | :- |
|Boolean|El tipo de dato de propiedad es Booleano|ABoolean|
|Date|El tipo de datos de la propiedad es DateTime. Tenga en cuenta que Microsoft Excel solo almacena la parte de la fecha, no se puede almacenar la hora en una propiedad personalizada de este tipo|ToDateTime|
|Float|El tipo de datos de la propiedad es Double|ToDouble|
|Number|El tipo de datos de la propiedad es Int32|ToInt|
|String|El tipo de dato de la propiedad es string|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **Cómo agregar o eliminar propiedades de documento personalizadas**

Como hemos descrito anteriormente al principio de este tema, los desarrolladores no pueden agregar o eliminar propiedades integradas porque estas propiedades están definidas por el sistema, pero es posible agregar o eliminar propiedades personalizadas porque estas son definidas por el usuario.

### **Cómo agregar propiedades personalizadas**

Las APIs de Aspose.Cells han expuesto el método [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) para la clase [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/) con el fin de agregar propiedades personalizadas a la colección. El método [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) añade la propiedad al archivo de Excel y devuelve una referencia para la nueva propiedad del documento como un objeto [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **Cómo configurar la propiedad personalizada de “Vínculo con contenido”**

Para crear una propiedad personalizada vinculada al contenido de un rango dado, llama al método [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) y pasa el nombre de la propiedad y la fuente. Puedes verificar si una propiedad está configurada como vinculada al contenido usando la propiedad [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--). Además, también es posible obtener el rango fuente usando la propiedad [**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--) de la clase [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

Utilizamos un archivo de plantilla simple de Microsoft Excel en el ejemplo. El libro de trabajo tiene un rango con nombre definido etiquetado como **MiRango** que se refiere a un valor de celda.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **Cómo eliminar propiedades personalizadas**

Para eliminar propiedades personalizadas usando Aspose.Cells, llama al método [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-) y pasa el nombre de la propiedad del documento a eliminar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Agregar propiedades personalizadas visibles dentro del Panel de información del documento](/cells/es/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Establecer las propiedades ScaleCrop y LinksUpToDate de las propiedades de documento Integradas](/cells/es/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Especificar la versión del documento del archivo de Excel mediante propiedades de documento integradas](/cells/es/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Especificar el idioma del archivo de Excel mediante propiedades de documento integradas](/cells/es/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
