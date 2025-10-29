---
title: Formes dans les graphiques avec JavaScript via C++
linktitle: Formes dans les graphiques
description: Apprenez à utiliser Aspose.Cells for JavaScript via C++ pour ajouter des contrôles et personnaliser des graphiques dans Microsoft Excel. Ce guide montre comment manipuler les éléments du graphique, ajuster la mise en forme et améliorer l apparence globale et la convivialité de vos graphiques.
keywords: Aspose.Cells for JavaScript via C++, Contrôles de graphique, Personnalisation du graphique, Microsoft Excel, Éléments du graphique, Mise en forme.
type: docs
weight: 70
url: /fr/javascript-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Parfois, vous avez besoin d'insérer des objets de dessin comme des étiquettes, des boîtes de texte, des images, etc. dans un graphique. Aspose.Cells peut ajouter les contrôles à un graphique à l'exécution.
{{% /alert %}}

## **Ajout de contrôle d'étiquette au graphique**

Les étiquettes fournissent un moyen de fournir des informations aux utilisateurs sur le contenu d'une feuille de calcul. Aspose.Cells vous permet d'ajouter et de manipuler des étiquettes même dans les graphiques.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) fournit une méthode nommée [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLabelInChart-number-number-number-number-), utilisée pour ajouter un contrôle d'étiquette à un graphique. Voici une liste des paramètres utilisés pour la méthode :

- **haut** – le décalage vertical de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **gauche** – le décalage horizontal de l'étiquette depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **hauteur** – la hauteur de l'étiquette, en unités de 1/4000 de la zone du graphique.
- **largeur** – la largeur de l'étiquette, en unités de 1/4000 de la zone du graphique.

La méthode retourne un objet [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/). La classe [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/) représente une étiquette dans le graphique. Elle a quelques membres importants :

- [**text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--) (propriété) - spécifie la chaîne de légende d'une étiquette.
- [**fill**](https://reference.aspose.com/cells/javascript-cpp/shape/#fill--) (propriété) - spécifie les attributs de couleur de remplissage.

L'exemple suivant montre comment ajouter une étiquette au graphique. L'exemple utilise un fichier de concepteur (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une étiquette dans le graphique. Ci-dessous se trouve le code d'origine pour ajouter une étiquette au graphique. La sortie suivante est générée lors de l'exécution du code.

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

## **Ajout d'un contrôle TextBox au graphique**

Une manière de mettre en évidence des informations importantes dans un rapport est d'utiliser une zone de texte. Par exemple, saisissez du texte pour mettre en valeur le nom de l'entreprise ou pour indiquer la région géographique avec le plus de ventes. La classe [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) fournit une méthode appelée [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-), qui est utilisée pour ajouter un contrôle de zone de texte à un graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de la zone de texte depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **height** - la hauteur de la zone de texte, en unités de 1/4000 de la zone du graphique.
- **width** - la largeur de la zone de texte, en unités de 1/4000 de la zone du graphique.

La méthode renvoie un objet [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/). La classe [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) représente une zone de texte dans le graphique.

L'exemple suivant montre comment ajouter une zone de texte à un graphique. L'exemple utilise le fichier de concepteur précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une zone de texte dans le graphique pour afficher le titre du graphique. Ci-dessous se trouve le code d'origine pour ajouter une zone de texte au graphique.

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

## **Ajout d'une image au graphique**

Aspose.Cells vous permet d'insérer des images dans un graphique. Par exemple, ajoutez une image pour mettre en avant ou donner plus de sens à un graphique ou à son contenu, ou insérez un fichier image de marque.

La classe [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) fournit une méthode nommée [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-), qui est utilisée pour ajouter un objet image au graphique. Voici la liste des paramètres utilisés pour la méthode :

- **top** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **left** - le décalage vertical de l'image depuis le coin supérieur gauche en unités de 1/4000 de la zone du graphique.
- **stream** - un objet flux qui contient les données de l'image.
- **widthScale** - l'échelle de la largeur de l'image, une valeur en pourcentage.
- **heightScale** - l'échelle de la hauteur de l'image, une valeur en pourcentage.

La méthode renvoie un objet [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/). La classe [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) représente un objet image dans le graphique.

L'exemple suivant montre comment ajouter une image au graphique. L'exemple utilise le fichier de conception précédent (**exp_piechart.xls**) qui contient un graphique. Nous utilisons ce fichier pour insérer une image dans le graphique. Ci-dessous se trouve le code d'origine pour ajouter une image au graphique.

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

## **Ajout d'une case à cocher dans le graphique**

Aspose.Cells vous permet d'insérer des cases à cocher dans une feuille de graphique en utilisant l'énumération [**MsoDrawingType**](https://reference.aspose.com/cells/javascript-cpp/msodrawingtype/). L'exemple suivant montre comment ajouter une case à cocher à une feuille de graphique.

L'image suivante montre la feuille de graphique avec la case à cocher dans le fichier de sortie.

![todo:image_alt_text](controls-in-charts_1.jpg)

Le [fichier de sortie](101089316.xlsx) généré par le snippet de code suivant est joint à titre de référence.

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

## **Sujets avancés**
- [Ajouter un filigrane WordArt au graphique](/cells/fr/javascript-cpp/add-wordart-watermark-to-chart/)
