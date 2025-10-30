---
title: Få varningar vid laddning av Excel fil med JavaScript via C++
linktitle: Få varningar när Excel filen laddas
type: docs
weight: 110
url: /sv/javascript-cpp/get-warnings-while-loading-excel-file/
description: Lär dig att fånga varningar vid inläsning av en Excel fil med Aspose.Cells for JavaScript via C++. Hantera korrupta men laddbara arbetsböcker effektivt.
---

## **Möjliga användningsscenario**

Ibland försöker användaren ladda en arbetsbok som är något korrupt men ändå kan läsas in. I sådana fall ger Aspose.Cells varningar vid inläsning av arbetsboken. Du kan fånga dessa varningar genom att implementera [**IWarningCallback**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback)-gränssnittet och sätta [**LoadOptions.warningCallback**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#warningCallback--)-egenskapen.

## **Få varningar vid inläsning av Excel-fil**

Följande exempel förklarar hur man får varningar vid inläsning av en Excel-fil. Koden laddar [exempel Excel-fil](sampleDuplicateDefinedName.xlsx) som genererar en [**DuplicateDefinedName**](https://reference.aspose.com/cells/javascript-cpp/warningtype)-varning vid inläsning. Denna varning fångas sedan av [**IWarningCallback.warning(WarningInfo)**](https://reference.aspose.com/cells/javascript-cpp/iwarningcallback/#warning-warninginfo-)-metoden som skriver varningsmeddelanden till konsolen. Koden sparar därefter arbetsboken som [utgångs Excel-fil](outputDuplicateDefinedName.xlsx). Om du öppnar exempel-Excel-filen i Microsoft Excel visas denna varning, som visas i skärmbilden. Vänligen kontrollera även kodens konsolutdata nedan för mer förståelse.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Exempelkod**

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

## **Konsoloutput**



{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
