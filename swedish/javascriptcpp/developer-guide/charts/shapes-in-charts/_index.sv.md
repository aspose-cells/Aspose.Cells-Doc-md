---
title: Former i diagram med JavaScript via C++
linktitle: Former i diagram
description: Lär dig hur man använder Aspose.Cells for JavaScript via C++ för att lägga till kontroller och anpassa diagram i Microsoft Excel. Den här guiden visar hur man manipulerar diagramelement, justerar formatering och förbättrar det övergripande utseendet och användbarheten av dina diagram.
keywords: Aspose.Cells for JavaScript via C++, diagramkontroller, diagramanpassning, Microsoft Excel, diagramelement, formatering.
type: docs
weight: 70
url: /sv/javascript-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Ibland behöver du infoga ritobjekt som etiketter, textrutor, bilder och så vidare i ett diagram. Aspose.Cells kan lägga till kontroller i ett diagram vid körtid.
{{% /alert %}}

## **Lägga till etikettkontroll i diagrammet**

Etiketter ger ett sätt att ge information till användarna om innehållet i ett kalkylblad. Aspose.Cells låter dig lägga till och manipulera etiketter även i diagram.

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) tillhandahåller en metod med namnet [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLabelInChart-number-number-number-number-), som används för att lägga till en etikettkontroll i ett diagram. Nedan finns en lista över de parametrar som används för metoden:

- **överst** – vertikalt avstånd från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **vänster** – det horisontella avståndet från etiketten till det övre vänstra hörnet i enheter av 1/4000 av diagramområdet.
- **höjd** – etikettens höjd, i enheter av 1/4000 av diagramområdet.
- **bredd** – etikettens bredd, i enheter på 1/4000 av diagramområdet.

Metoden returnerar [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/)-objekt. Klassen [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/) representerar en etikett i diagrammet. Den har några viktiga medlemmar:

- [**text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--) (egenskap) – specificerar en etiketts bildtext.
- [**fill**](https://reference.aspose.com/cells/javascript-cpp/shape/#fill--) (egenskap) – specificerar färgfyllningsegenskaper.

Följande exempel visar hur man lägger till en etikett i diagrammet. Exemplet använder en designerfil (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en etikett i diagrammet. Nedan finns den ursprungliga koden för att lägga till en etikett i diagrammet. Följande utdata genereras när koden utförs.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Add Label In Chart Example</title>
    </head>
    <body>
        <h1>Add Label In Chart Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new label to the chart.
            const label = chart.shapes.addLabelInChart(100, 100, 350, 900);

            // Set the caption of the label.
            label.text = "A Label In Chart";

            // Set the Placement Type, the way the Label is attached to the cells.
            label.placement = AsposeCells.PlacementType.FreeFloating;

            // Save the excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Label added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Lägga till textbox-styrenhet i diagrammet**

Ett sätt att markera viktig information i en rapport är att använda en textruta. Till exempel, mata in text för att markera företagsnamnet eller för att ange den geografiska regionen med högst försäljning. Klassen [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) tillhandahåller en metod som heter [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), som används för att lägga till en textruta styrenhet i ett diagram. Följande är parametrarna som används för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – den vertikala avvikelsen för textrutan från det övre vänstra hörnet i enheter på 1/4000 av diagramområdet.
- **höjd** – textrutans höjd, i enheter om 1/4000 av diagramområdet.
- **bredd** – textrutans bredd, i enheter om 1/4000 av diagramområdet.

Metoden returnerar [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/)-objekt. Klassen [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) representerar en textruta i diagrammet.

Följande exempel visar hur man lägger till en textruta i ett diagram. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en textruta i diagrammet för att visa diagramtiteln. Nedan finns den ursprungliga koden för att lägga till en textruta i diagrammet.

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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the second sheet.
            const sheet = workbook.worksheets.get(1);
            const chart = sheet.charts.get(0);

            // Add a new textbox to the chart.
            const textbox0 = chart.shapes.addTextBoxInChart(100, 1100, 350, 2550);

            // Fill the text.
            textbox0.text = "Sales By Region";

            // Get the textbox text frame.
            // const textframe0 = textbox0.textFrame;

            // Set the textbox to adjust it according to its contents.
            // textframe0.autoSize = true;

            // Set the font color.
            textbox0.font.color = AsposeCells.Color.Maroon;

            // Set the font to bold.
            textbox0.font.isBold = true;

            // Set the font size.
            textbox0.font.size = 14;

            // Set font attribute to italic.
            textbox0.font.isItalic = true;

            // Get the fill format of the textbox.
            const fillformat = textbox0.fill;

            // Get the line format type of the textbox.
            const lineformat = textbox0.line;

            // Set the line weight.
            lineformat.weight = 2;

            // Set the dash style to solid.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Lägga till bild i diagrammet**

Aspose.Cells gör det möjligt att infoga bilder i ett diagram. Till exempel, lägg till en bild för att betona eller ge mer mening åt ett diagram eller dess innehåll, eller infoga en varumärkesbildfil.

Klassen [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) tillhandahåller en metod som heter [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), som används för att lägga till ett bildobjekt i diagrammet. Följande är parametrarna som används för metoden:

- **top** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **vänster** – det vertikala avståndet från den övre vänstra hörnet i enheter om 1/4000 av diagramområdet.
- **ström** – en strömobjekt som innehåller bilddata.
- **breddskala** – bildens breddskala, en procentuell värde.
- **höjdskala** – bildens höjdskala, en procentuell värde.

Metoden returnerar ett [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/)-objekt. Klassen [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) representerar en bildobjekt i diagrammet.

Följande exempel visar hur man lägger till en bild i diagrammet. Exemplet använder den tidigare designerfilen (**exp_piechart.xls**) som har ett diagram i den. Vi använder denna fil för att infoga en bild i diagrammet. Nedan finns den ursprungliga koden för att lägga till en bild i diagrammet.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Picture to Chart</title>
    </head>
    <body>
        <h1>Add Picture to Chart Example</h1>
        <p>Select an Excel file and an image to add to the first chart in the first worksheet.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="imageInput" accept="image/*" />
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
            const imageInput = document.getElementById('imageInput');
            if (!fileInput.files.length || !imageInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file and an image file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const imageFile = imageInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const imageBuffer = await imageFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the designer chart in the first sheet.
            const sheet = workbook.worksheets.get(0);
            const chart = sheet.charts.get(0);

            // Add a new picture to the chart.
            const pic0 = chart.shapes.addPictureInChart(50, 50, new Uint8Array(imageBuffer), 40, 40);

            // Get the lineformat type of the picture.
            const lineformat = pic0.line;

            // Set the dash style.
            lineformat.dashStyle = AsposeCells.MsoLineDashStyle.Solid;

            // Set the line weight.
            lineformat.weight = 4;

            // Save the modified Excel file and provide a download link.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'chart.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Picture added to chart successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Lägger till kryssruta i diagrammet**

Aspose.Cells tillåter dig att infoga kryssrutor i ett diagramblad genom att använda [**MsoDrawingType**](https://reference.aspose.com/cells/javascript-cpp/msodrawingtype/)-uppräkningen. Följande exempel demonstrerar hur man lägger till en kryssruta i ett diagramblad.

Följande bild visar diagrambladet med kryssrutan i utdatafilen.

![todo:image_alt_text](controls-in-charts_1.jpg)

Den [utdatafilen](101089316.xlsx) som genererats av följande kodsnutt bifogas för din referens.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Insert Checkbox in Chart Sheet Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Insert Checkbox in Chart Sheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            // This example creates a new workbook and inserts a chart sheet with a checkbox in the chart.
            // The file input is optional for this example (a new workbook is created regardless).

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a chart sheet to the workbook
            const index = workbook.worksheets.add(AsposeCells.SheetType.Chart);

            // Access the newly added chart sheet
            const sheet = workbook.worksheets.get(index);

            // Add a floating column chart to the chart sheet
            sheet.charts.addFloatingChart(AsposeCells.ChartType.Column, 0, 0, 1024, 960);

            // Add nSeries to the chart (single series with values 1,2,3)
            sheet.charts.get(0).nSeries.add("{1,2,3}", false);

            // Add checkbox to the chart
            sheet.charts.get(0).shapes.addShapeInChart(AsposeCells.MsoDrawingType.CheckBox, AsposeCells.PlacementType.Move, 400, 400, 1000, 600);

            // Set text of the checkbox shape
            sheet.charts.get(0).shapes.get(0).text = "CheckBox 1";

            // Save the workbook to XLSX format and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'InsertCheckboxInChartSheet_out.xlsx';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Chart sheet with checkbox created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Fortsatta ämnen**
- [Lägg till WordArt-vattenstämpel på diagram](/cells/sv/javascript-cpp/add-wordart-watermark-to-chart/)
