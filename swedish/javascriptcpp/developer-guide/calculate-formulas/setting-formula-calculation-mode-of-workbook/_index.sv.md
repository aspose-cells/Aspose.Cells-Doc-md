---
title: Inställning av Formelberäkningsläge för arbetsbok med JavaScript via C++
linktitle: Ställa in formelberäkningsläget för arbetsboken
description: Denna artikel introducerar hur man ställer in formelberäkningsläget för en arbetsbok i Microsoft Excel med Aspose.Cells for JavaScript via C++. Genom att ladda en befintlig Excel fil eller skapa en ny fil kan vi använda den egenskap som tillhandahålls av Aspose.Cells för att ställa in formelberäkningsläget och få resultatet. Slutligen sparar vi den modifierade Excel filen till disk.
keywords: Aspose.Cells, Excel, arbetsbok, formelberäkningsläge, inställningar, JavaScript via C++
type: docs
weight: 110
url: /sv/javascript-cpp/setting-formula-calculation-mode-of-workbook/
---

{{% alert color="primary" %}}  
Microsoft Excel tillåter dig att ställa in formelberäkningsläget, det vill säga hur formler beräknas. Det finns tre möjliga värden:  

- Automatisk - beräknas om varje gång något ändras och varje gång en arbetsbok öppnas.  
- Automatisk, utom för datatabeller - beräknas om varje gång något ändras, men exkluderar datatabeller.  
- Manuell - beräknas endast när användaren uttryckligen begär det genom att trycka på F9 eller CTRL+ALT+F9 eller när arbetsboken sparas.  
{{% /alert %}}  

För att ställa in formelberäkningsläge i Microsoft Excel:  

1. Välj **Formler** och sedan **Beräkningsalternativ**.  
1. Välj ett av alternativen.  

Aspose.Cells for JavaScript via C++ tillåter också att ställa in **Formelberäkningsläge** med [**FormulaSettings.calculationMode**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#calculationMode--) lägesegenskap. Du kan tilldela den enumen [**CalcModeType**](https://reference.aspose.com/cells/javascript-cpp/calcmodetype) som har ett av följande värden:  

- CalcModeType.Automatic  
- CalcModeType.AutomaticExceptTable  
- CalcModeType.Manual  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            // Creating a workbook
            const workbook = new Workbook();

            // Set the Formula Calculation Mode to Manual
            workbook.settings.formulaSettings.calculationMode = AsposeCells.CalcModeType.Manual;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
