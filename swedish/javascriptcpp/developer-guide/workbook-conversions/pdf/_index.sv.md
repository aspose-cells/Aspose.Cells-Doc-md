---
title: PDF med JavaScript via C++
linktitle: Pdf
type: docs
weight: 220
url: /sv/javascript-cpp/convert-excel-to-pdf/
description: Lär dig hur man konverterar Excel arbetsbok till PDF med Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}
Aspose.Cells stöder konvertering av Excel-arbetsbok till PDF. I det här exemplet kommer vi att se komplett konvertering av en Excel-arbetsbok till PDF.
{{% /alert %}}

## **Konvertering av Excelarbetsbok till PDF**

PDF-filer används i stor utsträckning för att utbyta dokument mellan organisationer, statliga sektorer och individer. Det är ett standarddokumentformat och mjukvaruutvecklare uppmanas ofta att hitta ett sätt att konvertera Microsoft Excel-filer till PDF-dokument.

Aspose.Cells stöder konvertering av Excel-filer till PDF och bibehåller hög visuell identitet vid konverteringen.

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ skriver direkt ut information om API och Versionsnummer i utdata dokument. Till exempel, vid rendering av dokument till PDF, fyller Aspose.Cells for JavaScript via C++ i fältet **PDF Producer** med värde, t.ex. 'Aspose.Cells v23.2'.

Observera att du kan ändra denna information i utdata-dokument genom [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#producer--) -egenskapen.
{{% /alert %}}

### **Direkt konvertering**

Aspose.Cells for JavaScript via C++ stödjer konvertering från kalkylblad till PDF oberoende av annan programvara. Spara helt enkelt en Excel-fil som PDF med hjälp av klassens [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) metod. Metoden [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) ger medlemmen i enumerationen [**SaveFormat.Pdf**](https://reference.aspose.com/cells/javascript-cpp/saveformat) som konverterar de inbyggda Excel-filformaten till PDF.

Följ stegen nedan för att direkt konvertera Excel-kalkylbladen till PDF-format:

1. Skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) -klassen genom att anropa dess tomma konstruktor.
1. Du kan öppna/ladda en befintlig mallfil eller hoppa över detta steg om du skapar arbetsboken från grunden.
1. Gör något arbete (infodata, tillämpa formatering, ange formler, infoga bilder eller andra ritobjekt, etc.) på kalkylbladet med hjälp av Aspose.Cells APIs.
1. När kalkylbladskoden är klar, anropa [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) klassens [**save(string, SaveFormat)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#save-string-saveformat-) metod för att spara kalkylbladet.

Filtypen ska vara PDF, så välj *Pdf* (ett fördefinierat värde) från [**SaveFormat**](https://reference.aspose.com/cells/javascript-cpp/saveformat) -uppräkningen för att generera det slutliga PDF-dokumentet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Instantiate the Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save the document in PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion to PDF completed! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Avancerad konvertering**

Du kan också välja att använda [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)-klassen för att ange olika egenskaper för konverteringen. Genom att ange olika egenskaper för [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)-klassen får du kontroll över utskrifts-, font-, säkerhets- och komprimeringsinställningar för utdata-PDF:en. 

Den viktigaste egenskapen är [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) som möjliggör att du ställer in efterlevnadsnivån för PDF-standarden. För närvarande kan du spara i PDF 1.4, PDF 1.5, PDF 1.6, PDF 1.7, PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab och PDF/A-3u-format. Observera att med PDF/A-formatet är filstorleken större än en vanlig PDF-filstorlek.

#### **Spara arbetsboken som PDF/A-kompatibla filer**

Den nedanstående kodsnutten visar hur man använder [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) -klassen för att spara Excel-filer i PDF/A-kompatibilt PDF-format.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create PDF/A from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCompliance } = AsposeCells;

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
            // Instantiate new workbook
            const workbook = new Workbook();

            // Insert a value into the A1 cell in the first worksheet
            workbook.worksheets.get(0).cells.get(0, 0).value = "Testing PDF/A";

            // Define PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set the compliance type
            pdfSaveOptions.compliance = PdfCompliance.PdfA1b;

            // Save the file to PDF with options
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF/A File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF/A created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
Observera att egenskapen [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) lades till med version Aspose.Cells for JavaScript via C++ 5.3.0.
{{% /alert %}}

#### **Ange PDF-skapandetid**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) -klassen kan du få eller ställa in PDF-skapandetid. Följande kod visar användningen av [**PdfSaveOptions.createdTime**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#createdTime--) -egenskapen för att ange skapandetiden för PDF-filen.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, PdfSaveOptions, SaveFormat, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const options = new PdfSaveOptions();
            options.createdTime = new Date();

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

#### **Ange alternativet för att kopiera innehållet för tillgänglighet**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) -klassen kan du få eller ställa in PDF [**PdfSecurityOptions.accessibilityExtractContent**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/#accessibilityExtractContent--) -alternativet för att kontrollera tillgången till innehållet i den konverterade PDF:en.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Convert to PDF with Security Options</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Security Options</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOpt = new PdfSaveOptions();

            // Create an instance of PdfSecurityOptions
            const securityOptions = new PdfSecurityOptions();

            // Set AccessibilityExtractContent to false (converted from setAccessibilityExtractContent(false))
            securityOptions.accessibilityExtractContent = false;

            // Set the security option in the PdfSaveOptions (converted from setSecurityOptions)
            pdfSaveOpt.securityOptions = securityOptions;

            // Save the workbook to PDF format while passing the PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOpt);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outFile.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

#### **Exportera anpassade egenskaper till PDF**

Med [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)-klassen kan du exportera de anpassade egenskaperna i källarbetsboken till PDF. [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/javascript-cpp/pdfcustompropertiesexport/)-enumeratorn används för att ange sättet som egenskaper exporteras på. Dessa egenskaper kan observeras i Adobe Acrobat Reader genom att klicka på Fil och sedan alternativet Egenskaper enligt följande bild. Mallfilen "sourceWithCustProps.xlsx" kan laddas ned [här](sourceWithCustProps.xlsx) för testning och utdatapdf-filen "outSourceWithCustProps" är tillgänglig [här](outSourceWithCustProps.pdf) för analys.

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF with Custom Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfCustomPropertiesExport } = AsposeCells;

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

            // Instantiating a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create an instance of PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
            pdfSaveOptions.customPropertiesExport = PdfCustomPropertiesExport.Standard;

            // Save the workbook to PDF format while passing the object of PdfSaveOptions
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);

            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outSourceWithCustProps.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

### **Konverteringsattribut**

Vi arbetar med att förbättra konverteringsfunktionerna med varje ny version. Aspose.Cells Excel till PDF-konvertering har fortfarande ett par begränsningar. MapChart stöds inte vid konvertering till PDF-format. Även vissa ritningsobjekt stöds inte väl.

Tabellen nedan listar alla funktioner som är fullt eller delvis stödda vid export till PDF med Aspose.Cells. Denna tabell är inte slutgiltig och täcker inte alla kalkylbladsattribut, men den identifierar de funktioner som inte stöds eller endast delvis stöds för konvertering till PDF.

|**Dokumentelement**|**Attribut**|**Stöds**|**Noter**|
| :- | :- | :- | :- |
|Justering| |Ja| |
|Bakgrundsin...  |Ja| 
|Gräns|Färg|Ja| 
|Gräns|Linjestil|Ja| 
|Gräns|Linjebredd|Ja| 
|Cell Data| |Ja| 
|Kommentarer| |Ja| 
|Villkorlig formatering| |Ja| 
|Dokumentegenskaper| |Ja| 
|Ritobjekt| |Delvis|Skuggor och 3D-effekter för ritobjekt stöds inte bra; WordArt och SmartArt stöds delvis.
|Teckensnitt|Storlek|Ja| 
|Teckensnitt|Färg|Ja| 
|Teckensnitt|Stil|Ja| 
|Teckensnitt|Understrykning|Ja| 
|Teckensnitt|Effekter|Ja| 
|Bilder| |Ja| 
|Hypertextlänk| |Ja| 
|Diagram| |Delvis|Kartdiagram stöds inte.|
|Sammanfogade celler| |Ja| |
|Sidbrytning| |Ja| |
|Sidoppsett|Sidhuvud/-fot|Ja| |
|Sidoppsett|Marginaler|Ja| |
|Sidoppsett|Sidorientering|Ja| |
|Sidoppsett|Sidstorlek|Ja| |
|Sidoppsett|Utskriftsområde|Ja| |
|Sidoppsett|Utskriftsrubriker|Ja| |
|Sidoppsett|Skalning|Ja| |
|Radhöjd/Kolumnbredd| |Ja| |
|RTL (Höger-till-vänster) språk| |Ja| |

{{% alert color="primary" %}}
Om ditt kalkylblad innehåller formler, är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) strax innan du renderar kalkylbladet till PDF-format. Genom att göra det säkerställs att formelberoende värden beräknas om och de korrekta värdena renderas i PDF-filen.
{{% /alert %}}

## **Fortsatta ämnen**
- [Lägg till bokmärken i PDF med namngivna destinationer](/cells/sv/javascript-cpp/add-pdf-bookmarks-with-named-destinations/)
- [Undvik tom sida i utmatnings-PDF när det inte finns något att skriva ut](/cells/sv/javascript-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [Ändra typsnitt på bara specifika Unicode-tecken vid sparande till PDF](/cells/sv/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [Konvertera XLSX-fil till PDF-format](/cells/sv/javascript-cpp/convert-xlsx-file-to-pdf-format/)
- [Konvertera Excel-fil till PDF-format kompatibelt med PDFA-1a](/cells/sv/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [Konvertera XLS-fil med bilder eller diagram till PDF](/cells/sv/javascript-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [Skapa PdfBookmarkEntry för diagramblad](/cells/sv/javascript-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [Anpassa alla arbetsbokskolumner på en enda PDF-sida](/cells/sv/javascript-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [Hämta DrawObject och gräns vid rendering till PDF med hjälp av DrawObjectEventHandler-klassen](/cells/sv/javascript-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [Hämta varningar för teckensnittsbyte vid konvertering av Excel-fil](/cells/sv/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [Ignorera fel vid rendering av Excel till PDF](/cells/sv/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [Begränsa antalet genererade sidor - Excel till PDF-konvertering](/cells/sv/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [Skriv ut kommentarer vid sparande till PDF](/cells/sv/javascript-cpp/print-comments-while-saving-to-pdf/)
- [Rendera Office-tillägg vid konvertering av Excel till PDF](/cells/sv/javascript-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [Rendera en PDF-sida per Excel-ark - Konvertering från Excel till PDF](/cells/sv/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [Rendera Unicode-supplementära tecken i utgående PDF med Aspose.Cells](/cells/sv/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [Resamplings tillagda bilder - Konvertering från Excel till PDF](/cells/sv/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [Spara varje arbetsblad i en separat PDF-fil](/cells/sv/javascript-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [Spara Excel som PDF med standard- eller minsta storlek](/cells/sv/javascript-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [Spara angivna arbetsblad som PDF](/cells/sv/javascript-cpp/save-specified-worksheets-to-pdf/)
- [Säkra PDF-dokument](/cells/sv/javascript-cpp/secure-pdf-documents/)
- [Ange hur textsträngar ska korsas i utgående PDF och bild](/cells/sv/javascript-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
