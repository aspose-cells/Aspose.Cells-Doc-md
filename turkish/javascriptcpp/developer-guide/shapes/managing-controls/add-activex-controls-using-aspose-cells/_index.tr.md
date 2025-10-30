---
title: C++ ile Aspose.Cells for JavaScript kullanarak ActiveX Kontrolleri Ekle
linktitle: Aspose.Cells Kullanarak AktifX Kontrolleri Ekleme
type: docs
weight: 260
url: /tr/javascript-cpp/add-activex-controls-using-aspose-cells/
description: C++ kullanarak Aspose.Cells for JavaScript ile çalışma sayfasına ActiveX kontrolleri nasıl eklenir öğrenin. 
---

{{% alert color="primary" %}}

 Aspose.Cells kullanarak [**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-) yöntemiyle ActiveX kontrolleri ekleyebilirsiniz. Bu yöntem, bir parametre [**ControlType**](https://reference.aspose.com/cells/javascript-cpp/controltype/) alır ve bu, hangi tür ActiveX kontrolünün bir çalışma sayfasına eklenmesi gerektiğini belirtir. Aşağıdaki değerleri içerir.

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

ActiveX kontrolü şekil koleksiyonuna eklendikten sonra, [**Shape.activeXControl**](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) özelliği aracılığıyla ActiveX kontrol nesnesine erişebilir ve ardından çeşitli özelliklerini ayarlayabilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, Aspose.Cells kullanarak Toggle Button AktifX Kontrolü ekler.

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
