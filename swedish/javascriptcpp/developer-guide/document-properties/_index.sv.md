---
title: Hantera dokumentegenskaper med JavaScript via C++
linktitle: Dokumentegenskaper
type: docs
weight: 80
url: /sv/javascript-cpp/managing-document-properties/
description: Lär dig hur du hanterar dokumentegenskaper genom Aspose.Cells for JavaScript via C++ API er.
keywords: Hur man hanterar dokumentegenskaper i JavaScript via C++, hämta eller ställ in dokumentegenskaper med JavaScript via C++, lägg till eller ta bort dokumentegenskaper via JavaScript via C++, infoga eller ta bort dokumentegenskaper med JavaScript via C++, hur man får tillgång till dokumentegenskaper med Aspose.Cells for JavaScript via C++ API er.
---

## **Introduktion**

Microsoft Excel ger möjligheten att lägga till egenskaper i kalkylbladfiler. Dessa dokumentegenskaper förser användbar information och är uppdelade i 2 kategorier enligt detaljerna nedan.

- Systemdefinierade (inbyggda) egenskaper: Inbyggda egenskaper innehåller allmän information om dokumentet som dokumenttitel, författarnamn, dokumentstatistik och så vidare.
- Användardefinierade (anpassade) egenskaper: Anpassade egenskaper som definieras av användaren i form av namn-värdepar.

{{% alert color="primary" %}}

Det viktigaste att veta om inbyggda och anpassade egenskaper är att inbyggda egenskaper kan kommas åt och ändras, men inte skapas eller tas bort. Däremot kan anpassade egenskaper skapas och hanteras.

{{% /alert %}}

## **Hur man hanterar dokumentegenskaper med Microsoft Excel**

Microsoft Excel gör det möjligt att hantera dokumentegenskaper för Excel-filer på ett WYSIWYG-sätt. Följ stegen nedan för att öppna **Egenskaper**-dialogrutan i Excel 2016.

1. Välj **Info** i **Fil**-menyn.

|**Val av Info-meny**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
2. Klicka på **Egenskaper** och välj "Avancerade egenskaper".

|**Klicka på Avancerad Val av egenskaper**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
3. Hantera filens dokumentegenskaper.

|**Dialogruta Egenskaper**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
I dialogrutan Egenskaper finns olika flikar, som Allmänt, Sammanfattning, Statistik, Innehåll och Anpassade. Varje flik hjälper till att konfigurera olika typer av information relaterad till filen. Anpassad flik används för att hantera anpassade egenskaper.

## **Hur man arbetar med dokumentegenskaper med Aspose.Cells**

Utvecklare kan dynamiskt hantera dokumentegenskaper med hjälp av Aspose.Cells API:er. Denna funktion hjälper utvecklarna att lagra användbar information tillsammans med filen, som när filen mottogs, bearbetades, tidsstämplades och så vidare.

{{% alert color="primary" %}}

Aspose.Cells for JavaScript via C++ skriver direkt information om API och versionsnummer i utdata dokument. Till exempel, vid rendering av dokument till PDF, fyller Aspose.Cells for JavaScript via C++ i **Application**-fältet med värdet 'Aspose.Cells' och **PDF Producer**-fältet med värdet, t.ex. 'Aspose.Cells v17.9'.

 Observera att du inte kan instruera Aspose.Cells for JavaScript via C++ att ändra eller ta bort denna information från utdata-dokument.

{{% /alert %}}

### **Hur man får åtkomst till dokumentegenskaper**

Aspose.Cells API:er stödjer båda typerna av dokumentegenskaper, inbyggda och anpassade. Aspose.Cells' [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klass representerar en Excel-fil och, precis som en Excel-fil, kan [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)-klassen innehålla flera kalkblad, var och ett representerat av [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)-klassen medan samlingen av kalkblad representeras av [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection)-klassen.

Använd [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) för att komma åt filens dokumentegenskaper som beskrivs nedan.

- För att komma åt inbyggda dokumentegenskaper, använd [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--).
- För att komma åt anpassade dokumentegenskaper, använd [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--).

Både [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) och [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--) returnerar instansen av [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/). Denna samling innehåller [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) objekt, var och ett som representerar en enkel inbyggd eller anpassad dokumentegenskap.

Det är upp till applikationskravet hur man får åtkomst till en egenskap, dvs. genom att använda index eller namn på egenskapen från [**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/) som visas i exemplet nedan.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)-klassen gör det möjligt att hämta namn, värde och typ för dokumentegenskapen:

- För att få egenskapens namn, använd [**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--).
- För att hämta egenskapens värde, använd [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) returnerar värdet som ett objekt.
- För att hämta egenskapstypen, använd [**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--). Detta returnerar ett av [**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/)-enumerationsvärdena. Efter att du har fått egenskapstypen, använd någon av **DocumentProperty.ToXXX**-metoderna för att erhålla värdet av lämplig typ istället för att använda [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). **DocumentProperty.ToXXX**-metoderna beskrivs i tabellen nedan.

{{% alert color="primary" %}}

 [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) -klassen ger också ett set av metoder som returnerar värden av andra datatyper.

{{% /alert %}}

|**Medlemsnamn**|**Beskrivning**|**ToXXX-metod**|
| :- | :- | :- |
|Boolean| Egenskapens datatyp är Boolean|ToBool|
|Date| Egenskapens datatyp är DateTime. Observera att Microsoft Excel endast lagrar <br>datumdelen, ingen tid kan lagras i en anpassad egenskap av denna typ|ToDateTime|
|Float| Egenskapens datatyp är Dubbel|ToDouble|
|Number| Egenskapens datatyp är Int32|ToInt|
|String|Typen av egenskapsdata är string|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **Hur man lägger till eller tar bort anpassade dokumentegenskaper**

Som vi tidigare har beskrivit i början av detta ämne kan utvecklare inte lägga till eller ta bort inbyggda egenskaper eftersom dessa egenskaper är systemdefinierade men det är möjligt att lägga till eller ta bort anpassade egenskaper eftersom dessa är användardefinierade.

### **Hur man lägger till anpassade egenskaper**

Aspose.Cells API:er har exponerat [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-)-metoden för [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/)-klassen för att lägga till anpassade egenskaper till samlingen. [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-)-metoden lägger till egenskapen i excel-filen och returnerar en referens till den nya dokumentegenskapen som ett [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)-objekt.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **Hur man konfigurerar egendom med länk till innehåll**

För att skapa en anpassad egenskap kopplad till innehållet i ett givet område, kalla på [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-)-metoden och passera egenskapens namn och källa. Du kan kontrollera om en egenskap är konfigurerad som kopplad till innehåll med hjälp av [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--)-egenskapen. Dessutom är det också möjligt att få källområdet med hjälp av [**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--)-egenskapen i [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/)-klassen.

Vi använder en enkel mall Microsoft Excel-fil i exemplet. Arbetsboken har en definierad namngiven område märkt **MyRange** som hänvisar till en cellvärde.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
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
            const fileInput = document.getElementById('fileInput');
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **Hur man tar bort anpassade egenskaper**

För att ta bort anpassade egenskaper med Aspose.Cells, kalla på [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-)-metoden och passera namnet på dokumentegenskapen som ska tas bort.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen](/cells/sv/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper](/cells/sv/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Ange språket för Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
