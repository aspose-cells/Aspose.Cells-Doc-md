---
title: Mettre à jour le contrôle ComboBox ActiveX avec JavaScript via C++
linktitle: Mettre à jour le contrôle ComboBox ActiveX
type: docs
weight: 170
url: /fr/javascript-cpp/update-activex-combobox-control/
description: Apprenez comment lire et écrire les valeurs du contrôle ComboBox ActiveX en utilisant Aspose.Cells for JavaScript via C++. 
---

## **Scénarios d'utilisation possibles**
Vous pouvez lire ou écrire les valeurs du contrôle ComboBox ActiveX en utilisant Aspose.Cells for JavaScript via C++. Accédez au contrôle ActiveX via la propriété [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) et vérifiez son type via la propriété [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--) , il doit retourner la valeur [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/) puis la caster en objet [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) et lire ou modifier ses différentes propriétés.

Veuillez télécharger le [fichier Excel exemple](5115124.xlsx) utilisé dans le code d'exemple suivant.
## **Mise à jour du contrôle ComboBox ActiveX**
La capture d'écran suivante montre l'effet du code d'exemple sur le [fichier Excel d'exemple](5115124.xlsx). Comme vous pouvez le constater, la valeur de la boîte combinée ActiveX a été mise à jour pour "Il s'agit d'un contrôle de boîte combinée".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Code d'exemple**
Le code d'exemple suivant met à jour la valeur du contrôle Boîte combi ActiveX présent dans le [fichier Excel d'exemple](5115124.xlsx).

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
