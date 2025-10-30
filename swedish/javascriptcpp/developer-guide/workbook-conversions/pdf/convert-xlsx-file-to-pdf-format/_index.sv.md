---
title: Konvertera XLSX fil till PDF format med JavaScript via C++
linktitle: Konvertera XLSX fil till PDF format
type: docs
weight: 30
url: /sv/javascript-cpp/convert-xlsx-file-to-pdf-format/
description: Denna guide förklarar hur man konverterar en Excel fil (XLSX) till PDF format med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

PDF (Portable Document Format) representerar dokument oberoende av den programvara, hårdvara och operativsystem som används för att skapa dessa dokument. En PDF-fil kan vara dokument med vilken kombination av text, grafik och bilder som helst på ett enhets- och upplösningsoberoende sätt. PDF-filer är ofta komprimerade, så de tar upp mindre utrymme än den ursprungliga filen.

Ibland behöver du konvertera en Microsoft Excel-fil till PDF. För detta krävs en snabb, säker, noggrann och tillförlitlig lösning som låter dig distribuera PDF-dokument globalt. Det finns många konverteringsverktyg som kan utföra denna uppgift. Men du måste försäkra dig om att layouten för den ursprungliga Excel-dokumentet behålls i utdata PDF-filen. Bilder, diagram, former, datainmatning, teckensnitt, attribut, färger, sidinställningar, textsättning, ramar, diagram etc. ska renderas exakt och precist. [Aspose.Cells](https://products.aspose.com/cells/javascript-cpp/) säkerställer hög trovärdighetskonvertering.

Detta dokument är utformat för att ge en heltäckande förståelse för hur ett Microsoft Excel-dokument (som innehåller bilder, diagram, formatering etc.) kan konverteras till PDF. I detta visar det hur man skapar en enkel konsolapplikation i JavaScript via C++ som konverterar en Excel-fil till PDF med Aspose.Cells API. Konverteringen utförs med hög precision och noggrannhet.

{{% /alert %}}

## **Konvertera Excel till PDF**

Detta exempel använder en Excel-fil (SampleInput.xlsx) som mall. Arbetsboken innehåller arbetsblad med diagram och bilder. Varje arbetsblad innehåller olika typer av format med typsnitt, attribut, färger, skuggningseffekter och kantlinjer. Det finns ett kolumndiagram på det första arbetsbladet och en bild på det sista.

### **Den förkonfigurerade Excelfilen**

Mallen har tre blad, inklusive diagram och bilder som media. Det första bladet har diagram och det sista bladet har en bild som visas nedan i skärmbilderna.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|

### **Konverteringsprocess**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object with the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the PDF file
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Om kalkylbladet innehåller formler är det bäst att anropa [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) just innan du konverterar kalkylbladet till PDF. Doing so säkerställer att formelberoende värden omräknas, och att de rätta värdena visas i PDF.

{{% /alert %}}

### **Resultat**

När ovanstående kod har körts skapas en PDF-fil i mappen Files i din programkatalog.
Följande skärmbilder visar PDF-sidorna. Observera att sidhuvuden och sidfötter också behålls i den utmatade PDF-filen.

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|Det första kalkylbladet **(Försäljningsprognos)**|Det andra kalkylbladet **(Försäljningsrapport)**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|Det tredje kalkylbladet **(Dataregistrering)**|Det sista kalkylbladet **(Bild)**|
