---
title: Actualiza el control ComboBox ActiveX con JavaScript a través de C++
linktitle: Actualizar el control de cuadro combinado ActiveX
type: docs
weight: 170
url: /es/javascript-cpp/update-activex-combobox-control/
description: Aprende cómo leer y escribir valores del control ComboBox ActiveX usando Aspose.Cells for JavaScript a través de C++. 
---

## **Escenarios de uso posibles**
Puedes leer o escribir los valores del control ComboBox ActiveX usando Aspose.Cells for JavaScript a través de C++. Accede al Control ActiveX mediante la propiedad [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) y verifica su tipo mediante la propiedad [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--), que debe devolver el valor [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/), y luego castea su tipo a un objeto [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) para leer o modificar sus diversas propiedades.

Descargue el [archivo de Excel de ejemplo](5115124.xlsx) utilizado en el siguiente código de ejemplo.
## **Actualizar control ActiveX ComboBox**
La siguiente captura de pantalla muestra el efecto del código de ejemplo en el [archivo de Excel de ejemplo](5115124.xlsx). Como puede ver, el valor del Control Combo Box ActiveX se ha actualizado a "Este es un control de combo box".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Código de muestra**
El siguiente código de ejemplo actualiza el valor del Control Combo Box ActiveX presente dentro del [archivo de Excel de ejemplo](5115124.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update ActiveX ComboBox</title>
    </head>
    <body>
        <h1>Update ActiveX ComboBox in Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and first shape
            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            // Access ActiveX ComboBox Control and update its value
            if (shape.activeXControl != null) {
                const c = shape.activeXControl;

                if (c instanceof AsposeCells.ComboBoxActiveXControl) {
                    // Type cast ActiveXControl into ComboBoxActiveXControl and change its value
                    const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
                    comboBoxActiveX.value = "This is combo box control with updated value.";
                }
            }

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
