---
title: Gestionar códigos VBA del libro de trabajo habilitado para macros de Excel
linktitle: Proyecto de Macros
type: docs
weight: 200
url: /es/javascript-cpp/manage-vba-project/
description: Agregar módulo VBA y modificar VBA o Macro con Aspose.Cells for JavaScript via C++.
---

## **Agregar un módulo VBA en JavaScript via C++**
{{% alert color="primary" %}}

Aspose.Cells permite agregar un nuevo módulo VBA y código Macro usando Aspose.Cells for JavaScript via C++. Por favor, utilice el método [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-) para agregar el nuevo módulo VBA dentro del libro de trabajo

{{% /alert %}}

El siguiente código de ejemplo crea un nuevo libro de trabajo y añade un nuevo módulo VBA y Código Macro y guarda la salida en formato XLSM. Una vez que abras el archivo XLSM en Microsoft Excel y hagas clic en **Desarrollador > Visual Basic**, verás un módulo llamado "TestModule" y en su interior, el siguiente código macro.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module</title>
    </head>
    <body>
        <h1>Add VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
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
            // Create new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add VBA Module
            const idx = workbook.vbaProject.modules.add(worksheet);

            // Access the VBA Module, set its name and codes
            const module = workbook.vbaProject.modules.get(idx);
            module.name = "TestModule";
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Save the workbook as XLSM and prepare download
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Modificar VBA o Macro en JavaScript via C++**

{{% alert color="primary" %}} 

Puedes modificar el código VBA o Macro usando Aspose.Cells for JavaScript via C++. Aspose.Cells ha añadido los siguientes módulos y clases para leer y modificar el proyecto VBA en el archivo de Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Este artículo te mostrará cómo cambiar el código de VBA o macro dentro del archivo de Excel fuente utilizando Aspose.Cells.

{{% /alert %}} 

El siguiente código de ejemplo carga el archivo de Excel fuente que contiene el siguiente código VBA o Macro:

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Después de la ejecución del código de ejemplo de Aspose.Cells, el código de VBA o macro será modificado de la siguiente manera

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Puedes descargar el [archivo de Excel fuente](5112508.xlsm) y el [archivo de Excel de salida](5112511.xlsm) desde los enlaces proporcionados.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change VBA Module Code Example</title>
    </head>
    <body>
        <h1>Change VBA Module Code Example</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access VBA project modules
            const modules = workbook.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const module = modules.get(i);
                let code = module.codes;
                if (code && code.includes("This is test message.")) {
                    code = code.replace("This is test message.", "This is Aspose.Cells message.");
                    module.codes = code;
                }
            }

            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA module code updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Temas avanzados**
- [Agregar una referencia de librería al proyecto de VBA en el libro de trabajo](/cells/es/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Asignar Macro a un control de formulario](/cells/es/javascript-cpp/assign-macro-to-form-control/)
- [Comprobar si la firma digital del código VBA es válida](/cells/es/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Comprobar si el código VBA está firmado](/cells/es/javascript-cpp/check-if-vba-code-is-signed/)
- [Comprobar si el proyecto de VBA en un libro de Excel está firmado](/cells/es/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Comprobar si el proyecto de VBA está protegido y bloqueado para ver](/cells/es/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copiar el diseñador de almacenamiento de formularios de usuario Macro de VBA de la plantilla al libro de Excel de destino](/cells/es/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firmar digitalmente un proyecto de código VBA con certificado](/cells/es/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportar certificado de VBA a archivo o flujo de datos](/cells/es/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtrar proyecto de VBA al cargar un libro de Excel](/cells/es/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [Descubrir si el proyecto de VBA está protegido](/cells/es/javascript-cpp/find-out-if-vba-project-is-protected/)
- [Proteger con contraseña el proyecto de VBA del libro de Excel](/cells/es/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
