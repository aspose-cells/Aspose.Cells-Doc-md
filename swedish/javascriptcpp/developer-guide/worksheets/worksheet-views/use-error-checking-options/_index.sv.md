---
title: Använd Felkontrollalternativ med JavaScript via C++
linktitle: Använda alternativ för felkontroll
type: docs
weight: 140
url: /sv/javascript-cpp/use-error-checking-options/
description: Lär dig hur man programmässigt använder felkontrollalternativ i Excel ark med Aspose.Cells for JavaScript via C++.
keywords: lagra nummer som text i excel med JavaScript via C++, felkontrollera excel alternativ JavaScript via C++
---

{{% alert color="primary" %}}  
Microsoft Excel tillåter användare att definiera felkontrolloptioner och regler. Användare ser ofta felkontroller när de skapar formler, en liten triangel i det övre högra hörnet av en cell markeras när det är ett problem med en cell. Excel tillhandahåller information som hjälper användare att korrigera vanliga problem.  
{{% /alert %}}  

## **Typer av fel**  

Fel som innebär att formeln inte kan returnera ett resultat – till exempel att dela ett tal med noll – kräver omedelbar uppmärksamhet och ett felvärde visas i cellen. Klicka på den gröna triangeln visar ett utropstecken; klicka på detta öppnar en lista med alternativ.  

Felet kan lösas med hjälp av alternativen eller ignoreras. Att ignorera ett fel innebär att detta fel inte kommer att visas vid framtida felkontroller.  

Aspose.Cells tillhandahåller funktioner för felkontrollalternativ. Klassen [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) hanterar olika typer av felkontroller, till exempel nummer lagrade som text, formelberäkningsfel och valideringsfel. Använd enumerationen [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype) för att ställa in önskad felkontroll.  

## **Nummer som lagras som text**  

Ibland kan nummer formateras och lagras i celler som text. Det kan orsaka problem med beräkningar eller producera förvirrande sorteringsordningar. Nummer som är formaterade som text är vänsterjusterade istället för högerjusterade i cellen. Om en formel som ska utföra en matematisk operation på celler inte returnerar ett värde, kontrollera justeringen i cellerna som formeln hänvisar till - vissa eller alla dessa celler kan vara nummer formaterade som text.  

Du kan använda felkontrolloptionerna för att snabbt konvertera nummer som lagras som text till verkliga nummer.  

1. På **Verktyg**-menyn klickar du på **Alternativ**.  
1. Markera fliken för Felkontroll.  
   **Alternativ för siffror sparade som text** alternativet är markerat som standard.  
1. Inaktivera det.  

Följande exempelkod visar hur man inaktiverar felkontrollen för siffror sparade som text för en arbetsbok i mallen XLS med hjälp av Aspose.Cells API.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
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

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
