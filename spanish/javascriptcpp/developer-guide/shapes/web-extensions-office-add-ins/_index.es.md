---
title: Extensiones web  Complementos de Office con JavaScript vía C++
linktitle: Extensiones Web  Complementos de Office
type: docs
weight: 130
url: /es/javascript-cpp/web-extensions-office-add-ins/
---

Las extensiones web extienden las aplicaciones de Office e interactúan con el contenido en los documentos de Office. Las extensiones web añaden funcionalidad adicional al cliente de Office para mejorar la experiencia del usuario y la productividad.

Aspose.Cells también proporciona la capacidad de trabajar con extensiones web.

## **Agregar Extensión Web**

Puedes agregar Extensiones Web (Complementos de Office) en Excel haciendo clic en la pestaña **Insertar** y luego en el enlace **Tienda**/**Obtener complementos**. En la caja de Complementos, busca el complemento que deseas y agrégalo.

Aspose.Cells también ofrece la función de agregar Extensiones Web utilizando las clases [**WebExtension**](https://reference.aspose.com/cells/javascript-cpp/webextension) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/javascript-cpp/webextensiontaskpane). La siguiente muestra de código demuestra cómo usar las clases [**WebExtension**](https://reference.aspose.com/cells/javascript-cpp/webextension) y [**WebExtensionTaskPane**](https://reference.aspose.com/cells/javascript-cpp/webextensiontaskpane) para agregar una extensión web a un archivo Excel. Consulta el [archivo Excel de salida](89849869.xlsx) generado por el código como referencia.

### **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Add Web Extension Example</title>
    </head>
    <body>
        <h1>Add Web Extension Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, WebExtensionStoreType, Utils } = AsposeCells;

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

            // Create a new workbook or load from selected file
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access web extensions and task panes collections from worksheets
            const extensions = workbook.worksheets.webExtensions;
            const taskPanes = workbook.worksheets.webExtensionTaskPanes;

            // Add new web extension and task pane
            const extensionIndex = extensions.add();
            const taskPaneIndex = taskPanes.add();

            // Configure the extension reference
            const extension = extensions.get(extensionIndex);
            extension.reference.id = "wa104379955";
            extension.reference.storeName = "en-US";
            extension.reference.storeType = WebExtensionStoreType.OMEX;

            // Configure the task pane
            const taskPane = taskPanes.get(taskPaneIndex);
            taskPane.isVisible = true;
            taskPane.dockState = "right";
            taskPane.webExtension = extension;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddWebExtension_Out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Web extension and task pane added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Acceder a la Información de la Extensión Web**

Aspose.Cells permite acceder a la información de las Extensiones Web en un archivo Excel. La siguiente muestra de código demuestra cómo acceder a la información de la extensión web cargando el [archivo Excel de ejemplo](89849870.xlsx). Consulta la salida de la consola generada por el código.

### **Código de muestra**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Web Extensions Task Panes Example</title>
    </head>
    <body>
        <h1>Web Extensions Task Panes Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing web extension task panes collection
            const taskPanes = workbook.worksheets.webExtensionTaskPanes;

            const lines = [];
            for (let i = 0; i < taskPanes.count; i++) {
                const taskPane = taskPanes.get(i);
                lines.push("Width: " + taskPane.width);
                lines.push("IsVisible: " + taskPane.isVisible);
                lines.push("IsLocked: " + taskPane.isLocked);
                lines.push("DockState: " + taskPane.dockState);

                const webExt = taskPane.webExtension;
                const reference = webExt.reference;
                lines.push("StoreName: " + reference.storeName);
                lines.push("StoreType: " + reference.storeType);
                lines.push("WebExtension.Id: " + webExt.id);
                lines.push("---------------------------------");
            }

            document.getElementById('result').innerHTML = '<pre>' + lines.join("\n") + '</pre>';
        });
    </script>
</html>
```

### **Salida de la consola**

{{< highlight javascript >}}

Width: 350

IsVisible: True

IsLocked: False

DockState: right

StoreName: en-US

StoreType: OMEX

WebExtension.Id: 95D7ECE8-1355-492B-B6BF-27D25D0B0EEF

{{< /highlight >}}
