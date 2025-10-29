---
title: Ajouter des contrôles ActiveX en utilisant Aspose.Cells for JavaScript via C++
linktitle: Ajouter des contrôles ActiveX à l aide d Aspose.Cells
type: docs
weight: 260
url: /fr/javascript-cpp/add-activex-controls-using-aspose-cells/
description: Apprenez à ajouter des contrôles ActiveX dans une feuille de calcul en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Vous pouvez ajouter des contrôles ActiveX avec Aspose.Cells en utilisant la méthode [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-). Cette méthode prend un paramètre [**ControlType**](https://reference.aspose.com/cells/javascript-cpp/controltype/) qui indique quel type de contrôle ActiveX doit être ajouté dans une feuille de calcul. Elle a les valeurs suivantes.

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

Une fois que vous avez ajouté le contrôle ActiveX dans la collection de formes, vous pouvez accéder à l'objet contrôle ActiveX via la propriété [**Shape.activeXControl**](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) puis définir ses diverses propriétés.

{{% /alert %}}

Le code d'exemple suivant ajoute le contrôle ActiveX du bouton bascule à l'aide d'Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add ActiveX Control</title>
    </head>
    <body>
        <h1>Add ActiveX Control Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ControlType, Utils } = AsposeCells;

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
                // Create workbook object (empty workbook)
                const wb = new Workbook();

                // Access first worksheet
                const sheet = wb.worksheets.get(0);

                // Add Toggle Button ActiveX Control inside the Shape Collection
                const s = sheet.shapes.addActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

                // Access the ActiveX control object and set its linked cell property
                const c = s.activeXControl;
                c.linkedCell = "A1";

                // Save the workbook in xlsx format and provide download link
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'AddActiveXControls_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">ActiveX control added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
