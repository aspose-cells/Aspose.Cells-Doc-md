---
title: Ändra typsnittet på endast de specifika Unicode tecknen när du sparar till PDF med JavaScript via C++
linktitle: Byt typsnitt på specifika Unicode tecken vid sparande till PDF
type: docs
weight: 260
url: /sv/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: Lär dig hur man ändrar typsnittet för specifika Unicode tecken när du sparar till PDF med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}} 

Vissa Unicode-tecken visas inte med det användarvalda typsnittet. Ett sådant Unicode-tecken är **Icke-linjär bindestreck** (U+2011) och dess Unicode-nummer är 8209. Detta tecken kan inte visas med **Times New Roman**, men det kan visas med andra typsnitt som **Arial Unicode MS**.

 När ett sådant tecken förekommer inuti ett ord eller en mening som är i ett specifikt typsnitt som Times New Roman, ändrar Aspose.Cells teckensnittet för hela ordet eller meningen till ett typsnitt som kan visa detta tecken, t.ex. Arial Unicode till MS.

 Detta är dock oönskat beteende för vissa användare och de vill bara ändra typsnittet för det specifika tecknet istället för att ändra hela ordet eller meningen.

 För att hantera detta problem, tillhandahåller Aspose.Cells egenskapen `PdfSaveOptions.isFontSubstitutionCharGranularity` som bör ställas in på true så att bara typsnittet för specifika tecken som inte kan visas byts till ett visningsbart typsnitt, medan resten av ordet eller meningen förblir i det ursprungliga typsnittet.

{{% /alert %}} 

## **Exempel**
Följande skärmbild jämför de två utdata-PDF:erna som genererats av koden nedan.

 En genereras utan att ställa in `PdfSaveOptions.isFontSubstitutionCharGranularity` egenskapen och den andra genererades efter att ha ställt in egenskapen `PdfSaveOptions.isFontSubstitutionCharGranularity` till true.

 Som du kan se i den första PDF:en har hela meningen ändrats från Times New Roman till Arial Unicode MS på grund av icke-brytande bindestrecket. I den andra PDF:en har endast tecknet icke-brytande bindestrecket ändrats.

|**Första PDF-filen**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**Andra PDF-filen**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **Exempelkod**


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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result PDF 1</a>
        <a id="downloadLink2" style="display: none;">Download Result PDF 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p>Running example...</p>';

            // Create workbook object
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            let style = cell1.style;
            style.font.name = "Times New Roman";
            cell1.style = style;
            cell2.style = style;

            // Put the values inside the cell
            cell1.value = "Hello without Non-Breaking Hyphen";
            cell2.value = "Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen";

            // Autofit the columns
            worksheet.autoFitColumns();

            // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'SampleOutput_out.pdf';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download SampleOutput_out.pdf';

            // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
            const opts = new PdfSaveOptions();
            opts.isFontSubstitutionCharGranularity = true;
            const outputData2 = workbook.save(SaveFormat.Pdf, opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SampleOutput2_out.pdf';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download SampleOutput2_out.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated PDFs.</p>';
        });
    </script>
</html>
```
