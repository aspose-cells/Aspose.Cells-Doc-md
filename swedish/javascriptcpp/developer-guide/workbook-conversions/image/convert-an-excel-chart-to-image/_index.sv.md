---
title: Konvertera ett Excel diagram till bild med JavaScript via C++
linktitle: Konvertera en Excel diagram till bild
type: docs
weight: 20
url: /sv/javascript-cpp/convert-an-excel-chart-to-image/
description: Lär dig hur man konverterar Excel diagram till bilder med Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}  

Diagram är visuellt tilltalande och gör det enkelt för användare att se jämförelser, mönster och trender i data. Till exempel visar ett diagram på ett överskådligt sätt om försäljningen ökar eller minskar, eller hur faktisk försäljning jämförs med projicerad försäljning. Människor ombeds ofta att presentera statistisk och grafisk information på ett lättförståeligt och lätt underhållet sätt. En bild hjälper till.  

Ibland behövs diagram i en applikation eller webbsidor. Eller det kan behövas för ett Word-dokument, en PDF-fil, en PowerPoint-presentation eller någon annan applikation. I varje fall vill du rendera diagrammet som en bild så att du kan använda det någon annanstans.  

{{% /alert %}}  

## **Konvertera diagram till bilder**  

I exemplen här konverteras en pajdiagram och ett kolumndiagram till bilder.  

### **Konvertera ett cirkeldiagram till en bildfil**  

Först, skapa ett cirkeldiagram i Microsoft Excel och konvertera det sedan till en bildfil med Aspose.Cells for JavaScript via C++. Koden i detta exempel skapar en EMF-bild baserad på cirkeldiagrammet i mallfilen för Microsoft Excel.  

|**Utgång: cirkeldiagramsbild**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|  

1. Skapa ett cirkeldiagram i Microsoft Excel:  
   1. Öppna en ny arbetsbok i Microsoft Excel.  
   1. Ange några data i ett kalkylblad.  
   1. Skapa ett cirkeldiagram baserat på data.  
   1. Spara filen.  

|**Ingångsfilen.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|  

1. Ladda ner och installera Aspose.Cells:  
   1. [Ladda ner Aspose.Cells for JavaScript via C++](https://downloads.aspose.com/cells/javascript-cpp).  
   1. Installera det på din utvecklingsdator.  

Alla [Aspose](http://www.aspose.com/) komponenter fungerar i utvärderingsläge när de först installeras. Utvärderingsläget har ingen tidsbegränsning och det lägger bara vattenstämplar i utdata dokument.  

1. Skapa ett projekt:  
   1. Starta din föredragna IDE.  
   1. Skapa en ny konsolapplikation. Detta exempel använder en JavaScript-applikation, men du kan skapa den med valfri JavaScript-miljö.  
   1. Lägg till en referens. Detta projekt använder Aspose.Cells så lägg till en referens till Aspose.Cells for JavaScript via C++.  
   1. Skriv koden som hittar och konverterar diagrammet. Nedan är koden som används av komponenten för att utföra uppgiften. Mycket få rader kod används.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Chart to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (EMF) and prepare download link
            const imageData = chart.toImage(AsposeCells.ImageType.Emf);
            const blob = new Blob([imageData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'PieChart.out.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to EMF successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

### **Konvertera ett kolumndiagram till en bildfil**  

Först, skapa ett kolumndiagram i Microsoft Excel och konvertera det till en bildfil, som ovan. Efter att ha kört exempel koden, skapas en JPEG-fil baserad på kolumndiagrammet i mall-Excel-filen.  

|**Utmatningsfil: en kolumndiagramsbild.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|  

1. Skapa ett kolumndiagram i Microsoft Excel:  
   1. Öppna en ny arbetsbok i Microsoft Excel.  
   1. Ange några data i ett kalkylblad.  
   1. Skapa ett kolumndiagram baserat på datan.  
   1. Spara filen.  

|**Ingångsfil.**|  
| :- |  
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|  

1. Bygg ett projekt, med referenser, enligt beskrivningen ovan.  
1. Konvertera diagrammet till en bild dynamiskt. Följande är koden som används av komponenten för att utföra uppgiften. Koden är liknande den tidigare:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Chart to Image</title>
    </head>
    <body>
        <h1>Convert Chart to Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageType, Utils } = AsposeCells;

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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart (first chart) in the first worksheet of the workbook.
            const chart = workbook.worksheets.get(0).charts.get(0);

            // Convert the chart to an image (JPEG)
            const imageData = await chart.toImage(ImageType.Jpeg);

            // Create a Blob and provide a download link
            const blob = new Blob([imageData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ColumnChart.out.jpeg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Chart Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Chart converted to image successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```
