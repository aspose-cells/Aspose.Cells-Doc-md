---
title: Inställning av sidhuvuden och sidfötter med JavaScript via C++
linktitle:  Inställa sidhuvuden och sidfötter 
type: docs
weight: 30
url: /sv/javascript-cpp/setting-headers-and-footers/
description: Denna artikel förklarar hur man programmeringsmässigt infogar en bild i sidhuvudet och sidfoten i Excel kalkylblad med hjälp av Aspose.Cells for JavaScript via C++. 
keywords: infoga bild i excel sidhuvud sidfot JavaScript via C++, sätt excel sidhuvud sidfot script kommandon JavaScript via C++
---

{{% alert color="primary" %}}

Sidhuvuden och sidfötter är textrader som visas under övre marginalen eller ovanför den nedre marginalen. Det är möjligt att lägga till sidhuvuden och sidfötter i kalkylbladen också. Sidhuvuden och sidfötter kan användas för att visa användbar information som sidnummer, författarnamn, ämnesnamn eller datum och tid. Sidhuvuden och sidfötter hanteras med sidlayoutinställningarna.

{{% /alert %}}

## **Ställa in sidhuvuden och sidfötter**

Aspose.Cells for JavaScript via C++ tillåter dig att lägga till sidhuvuden och sidfötter till kalkylblad vid körning men vi rekommenderar att manuellt ställa in sidhuvuden och sidfötter i en fördesignad fil för utskrift. Du kan använda Microsoft Excel som ett GUI-verktyg för att ställa in sidhuvuden och sidfötter för att spara arbete och utvecklingstid. Aspose.Cells kan importera filen och spara inställningarna.

För att lägga till sidhuvuden och sidfötter vid körning tillhandahåller Aspose.Cells speciella API-anrop och skriptkommandon för att formatera sidhuvuden och sidfötter.

### **Skriptkommandon**

Skriptkommandon är speciella kommandon som tillåter dig att ställa in sidhuvud- och sidfotformatering.

|**Skriptkommandon**|**Beskrivning**|
| :- | :- |
|&P|Det nuvarande sidnumret|
|&G|En bild|
|&N|Det totala antalet sidor|
|&D|Aktuellt datum|
|&T|Aktuell tid|
|&A|Arbetsbladets namn|
|&F|Filnamnet utan dess sökväg|
|&&Text| Visar &Text. Till exempel: &&WO kommer att visas som &WO|
|&"\<FontName>"|Representerar ett typsnittsnamn. Till exempel: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Representerar typsnittsnamn med stil. Till exempel: &"Arial,Fetstil"|
|&\<FontSize>|Representerar teckensnittsstorlek. Till exempel: “&14abc”. Men om detta kommando följs av ett vanligt nummer som ska skrivas ut i sidhuvudet, ska detta separeras med ett mellanslag från teckensnittsstorleken. Till exempel: “&14 123”|

### **Ställ in headers och footers**

Klass [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) erbjuder två metoder, [**header(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#header-number-string-) och [**footer(number, string)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footer-number-string-), som används för att lägga till en rubrik och en sidfot till ett kalkylblad. Dessa metoder tar endast två parametrar:

- **Avsnitt** – avsnittet där sidhuvudet eller sidfoten ska placeras. Det finns tre avsnitt: vänster, mitten och höger, representerade av 0, 1 och 2 respektive.
- **Skript** – skriptet som ska användas för sidhuvudet eller sidfoten. Detta skript innehåller skriptkommandon för att formatera sidhuvuden eller sidfötter.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Set Headers and Footers Example</h1>
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
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Obtaining the reference of the PageSetup of the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const pageSetup = worksheet.pageSetup;

            // Setting worksheet name at the left section of the header
            pageSetup.header = pageSetup.header || [];
            pageSetup.header[0] = "&A";

            // Setting current date and current time at the central section of the header
            // and changing the font of the header
            pageSetup.header[1] = "&\"Times New Roman,Bold\"&D-&T";

            // Setting current file name at the right section of the header and changing the
            // font of the header
            pageSetup.header[2] = "&\"Times New Roman,Bold\"&12&F";

            // Setting a string at the left section of the footer and changing the font
            // of a part of this string ("123")
            pageSetup.footer = pageSetup.footer || [];
            pageSetup.footer[0] = "Hello World! &\"Courier New\"&14 123";

            // Setting the current page number at the central section of the footer
            pageSetup.footer[1] = "&P";

            // Setting page count at the right section of footer
            pageSetup.footer[2] = "&N";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SetHeadersAndFooters_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Headers and footers set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Infoga en bild i en sidhuvud eller sidfot**

Klass [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup) har två ytterligare metoder, [**headerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#headerPicture-number-numberarray-) och [**footerPicture(number, number[])**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#footerPicture-number-numberarray-), som används för att lägga till bilder i rubriken och sidfoten. Dessa metoder tar parametrarna:

- **Avsnitt** – avsnittet för sidhuvudet eller sidfoten där bilden ska placeras. Det finns tre avsnitt, vänster, mitten och höger, representerade av värdena 0, 1 och 2 respektive.
- **Byte-arrayer** – de grafiska data (de binära data ska skrivas in i bufferten i en byte-array).

Efter att ha utfört koden nedan och öppnat filen, kontrollera arbetsbladets sidhuvud genom:

1. På **Arkiv**-menyn väljer du **Sidlayout**. En dialogruta visas.
1. Välj fliken **Sidhuvud/Sidfot**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Image in Header/Footer Example</title>
    </head>
    <body>
        <h1>Insert Image in Header/Footer Example</h1>
        <p>Select an existing Excel file to modify (optional). If none is selected, a new workbook will be used.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert into the header:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Insert Image into Header</button>
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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the header.</p>';
                return;
            }

            // Read image bytes
            const imageFile = imageInput.files[0];
            const imageBuffer = await imageFile.arrayBuffer();
            const binaryData = new Uint8Array(imageBuffer);

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const excelFile = fileInput.files[0];
                const excelBuffer = await excelFile.arrayBuffer();
                workbook = new Workbook(new Uint8Array(excelBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet's page setup
            const pageSetup = workbook.worksheets.get(0).pageSetup;

            // Set the header picture and header scripts (converted from setters to properties)
            pageSetup.headerPicture = binaryData;
            pageSetup.header = "&G";
            pageSetup.header = "&A";

            // Save the workbook as Excel97-2003 (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertImageInHeaderFooter_out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image inserted into header successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
