---
title: Warnungen beim Laden der Excel Datei mit JavaScript über C++ erhalten
linktitle: Warnungen beim Laden einer Excel Datei erhalten
type: docs
weight: 110
url: /de/javascript-cpp/get-warnings-while-loading-excel-file/
description: Lernen, wie man Warnungen beim Laden einer Excel Datei mit Aspose.Cells for JavaScript über C++ erfasst. Behandeln Sie beschädigte, aber ladbare Arbeitsmappen effektiv.
---

## **Mögliche Verwendungsszenarien**

Manchmal versucht der Benutzer, eine Arbeitsmappe zu laden, die irgendwie beschädigt, aber dennoch ladbar ist. In solchen Fällen gibt Aspose.Cells Warnungen beim Laden der Arbeitsmappe aus. Sie können diese Warnungen abfangen, indem Sie die Schnittstelle [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback) implementieren und die Eigenschaft [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--) setzen.

## **Warnungen beim Laden von Excel-Dateien erhalten**

Der folgende Beispielcode erklärt, wie man Warnungen beim Laden einer Excel-Datei erhält. Der Code lädt die [Beispiel-Excel-Datei](sampleDuplicateDefinedName.xlsx), bei der beim Laden eine [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype)-Warnung ausgelöst wird. Diese Warnung wird dann von der Methode [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-) abgefangen, die die Warnmeldungen auf der Konsole ausgibt. Der Code speichert anschließend die Arbeitsmappe als [Ausgabe-Excel-Datei](outputDuplicateDefinedName.xlsx). Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen, wird diese Warnung ebenfalls angezeigt, wie in diesem Screenshot. Bitte überprüfen Sie auch die Konsolenausgabe des unten angegebenen Codes für ein besseres Verständnis.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Beispielcode**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Warning Callback Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Warning Callback Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, WarningType } = AsposeCells;

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

        // Implement IWarningCallback interface to catch warnings while loading workbook
        class WarningCallback extends AsposeCells.IWarningCallback {
            warning(warningInfo) {
                if (warningInfo.type === AsposeCells.WarningType.DuplicateDefinedName) {
                    console.log("Duplicate Defined Name Warning: " + warningInfo.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options and set the WarningCallback property 
            // to catch warnings while loading workbook
            const options = new LoadOptions();
            options.warningCallback = new WarningCallback();

            // Load the source excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save the workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDuplicateDefinedName.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook processed successfully. Check console for warnings.</p>';
        });
    </script>
</html>
```

## **Konsolenausgabe**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
