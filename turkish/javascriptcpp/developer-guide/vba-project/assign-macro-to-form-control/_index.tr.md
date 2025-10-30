---
title: JavaScript ile C++ kullanarak Form Kontrolüne Makro Ata
linktitle: Form Kontrolüne Makro Atama
type: docs
weight: 60
url: /tr/javascript-cpp/assign-macro-to-form-control/
description: JavaScript ile C++ kullanarak bir Form Kontrolüne (örneğin düğme) Makro Kodunu nasıl atayacağınızı öğrenin. 
keywords: JavaScript ile C++ kullanarak Form Kontrolüne Makro Ata, Form Kontrolü için Makro Kodu JavaScript ile C++, XLSM JavaScript ile Entegre Edilmiş Makro
---

{{% alert color="primary" %}}

Aspose.Cells, Düğme gibi Bir Form Kontrolüne bir Makro Kodu atamanıza izin verir. Lütfen çalışma kitabının içindeki Form Kontrolüne yeni bir Makro Kodu atamak için [**Shape.macroName**](https://reference.aspose.com/cells/javascript-cpp/shape/#macroName--) özelliğini kullanın.

{{% /alert %}}

Aşağıdaki örnek kod yeni bir çalışma kitabı oluşturur, bir Makro Kodunu Bir Form Düğmesine atar ve sonucu XLSM formatında kaydeder. Microsoft Excel'de çıktı XLSM dosyasını açtığınızda, aşağıdaki makro kodunu göreceksiniz.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **JavaScript kullanarak Form Kontrolüne Makro Ata**



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module and Button</title>
    </head>
    <body>
        <h1>Add VBA Module and Button Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            if (fileInput.files.length && fileInput.files[0]) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                var workbook = new Workbook();
            }

            // Accessing the first worksheet in the workbook
            const sheet = workbook.worksheets.get(0);

            // Adding a VBA module to the workbook tied to the sheet
            const moduleIdx = workbook.vbaProject.modules.add(sheet);
            const module = workbook.vbaProject.modules.get(moduleIdx);
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Adding a button shape to the sheet
            const button = sheet.shapes.addButton(2, 0, 2, 0, 28, 80);
            button.placement = AsposeCells.PlacementType.FreeFloating;
            button.font.name = "Tahoma";
            button.font.isBold = true;
            button.font.color = AsposeCells.Color.Blue;
            button.text = "Aspose";

            // Assigning the macro name to the button
            button.macroName = sheet.name + ".ShowMessage";

            // Saving the modified workbook as an XLSM file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: 'application/vnd.ms-excel.sheet.macroEnabled.12' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified XLSM File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module and button added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
