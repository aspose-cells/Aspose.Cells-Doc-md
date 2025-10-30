---
title: Grafiklerde JavaScript ile C++ kullanımıyla şekiller
linktitle: Grafiklerde Şekiller
description: C++ kullanarak Aspose.Cells for JavaScript ile Microsoft Excel de grafiklere kontroller ekleme ve özelleştirme yollarını öğrenin. Bu rehber, grafik elementleriyle nasıl oynanacağını, biçimlendirmeyi ayarlamayı ve grafiklerinizin genel görünümünü ve kullanılabilirliğini artırmayı gösterir.
keywords: C++ kullanarak Aspose.Cells for JavaScript, Grafik Kontrolleri, Grafik Özelleştirme, Microsoft Excel, Grafik Öğeleri, Biçimlendirme.
type: docs
weight: 70
url: /tr/javascript-cpp/controls-in-charts/
---

{{% alert color="primary" %}}
Bazen bir grafik içine etiketler, metin kutuları, resimler ve benzeri çizim nesneleri eklemeniz gerekebilir. Aspose.Cells, çalışma zamanında bir grafiğe denetim ekleyebilir.
{{% /alert %}}

## **Grafiğe Etiket Denetimi Ekleme**

Etiketler, bir elektronik tablonun içeriği hakkında kullanıcılara bilgi vermenin bir yolunu sağlar. Aspose.Cells, etiketleri hatta grafiklere bile eklemenize ve bunları manipüle etmenize olanak sağlar.

[**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) sınıfı, bir [**addLabelInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLabelInChart-number-number-number-number-) yöntemi adında bir yöntem sağlar. Bu yöntem, bir etiket denetimini grafiğe eklemek için kullanılır. Yöntem için kullanılan parametrelerin bir listesi aşağıda verilmiştir:

- **üst** – etiketin sol üst köşesinden dikey ofset (1/4000 biriminde grafik alanı).
- **sol** – etiketin sol üst köşesinden yatay ofset (1/4000 biriminde grafik alanı).
- **yükseklik** – etiketin yüksekliği, grafik alanının 1/4000 biriminde.
- **genişlik** – etiketin genişliği, grafik alanının 1/4000 biriminde.

Yöntem, [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/) nesnesi döndürür. [**Label**](https://reference.aspose.com/cells/javascript-cpp/label/) sınıfı, grafikteki bir etiketi temsil eder. Bazı önemli üyelere sahiptir:

- [**text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--) (özellik) – bir etiketin başlık dizgisini belirtir.
- [**fill**](https://reference.aspose.com/cells/javascript-cpp/shape/#fill--) (özellik) – doldurma rengi özelliklerini belirtir.

Aşağıdaki örnek, bir etiketin grafiğe nasıl ekleneceğini göstermektedir. Örnek, içinde bir grafik bulunan bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafikte bir etiket eklemek için kullanırız. Aşağıda, grafiğe bir etiket eklemek için orijinal kod verilmiştir. Kodu yürüttüğünüzde aşağıdaki çıktı üretilir.

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

## **Grafiğe TextBox Kontrolü Ekleme**

Bir raporda önemli bilgileri vurgulamanın bir yolu, bir metin kutusu kullanmaktır. Örneğin, şirket adını vurgulamak veya en yüksek satış yapılan coğrafi bölgeyi belirtmek için metin girin. [**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) sınıfı, grafiğe bir metin kutusu denetimi eklemek için kullanılan [**addTextBoxInChart(number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addTextBoxInChart-number-number-number-number-) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – metin kutusunun grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **height** – metin kutusunun yüksekliği, grafik alanının 1/4000 biriminde.
- **width** – metin kutusunun genişliği, grafik alanının 1/4000 biriminde.

Yöntem, bir [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) nesnesi döndürür. [**TextBox**](https://reference.aspose.com/cells/javascript-cpp/textbox/) sınıfı, grafiğe bir metin kutusu temsil eder.

Aşağıdaki örnek, bir metin kutusunun grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe metin kutusu eklemek için kullanırız. Aşağıda, grafiğe metin kutusu eklemek için orijinal kod bulunmaktadır.

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

## **Grafiğe Resim Ekleme**

Aspose.Cells, bir grafiğe resim eklemenize olanak tanır. Örneğin, bir resim ekleyerek bir grafiği vurgulamak veya anlamını artırmak veya bir marka resim dosyası eklemek.

[**ShapeCollection**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/) sınıfı, grafiğe bir resim nesnesi eklemek için kullanılan [**addPictureInChart(number, number, Uint8Array, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addPictureInChart-number-number-uint8array-number-number-) adında bir yöntem sağlar. Aşağıdaki parametre listesi, yöntem için kullanılan parametreleri gösterir:

- **top** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **left** – resmin, grafik alanının sol üst köşesinden dikey ofseti, 1/4000 birimde.
- **stream** – resim verisini içeren bir akım nesnesi.
- **widthScale** – resmin genişlik ölçeği, yüzde değeri.
- **heightScale** – resmin yükseklik ölçeği, yüzde değeri.

Yöntem, bir [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) nesnesi döndürür. [**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture/) sınıfı, grafiğe bir resim nesnesi temsil eder.

Aşağıdaki örnek, bir resmin grafiğe nasıl ekleneceğini gösterir. Örnek, içinde bir grafik bulunan önceki bir tasarımcı dosyası (**exp_piechart.xls**) kullanır. Bu dosyayı, grafiğe bir resim eklemek için kullanırız. Aşağıda, grafiğe resim eklemek için orijinal kod bulunmaktadır.

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

## **Grafiğe Onay Kutusu Ekleme**

Aspose.Cells, bir [**MsoDrawingType**](https://reference.aspose.com/cells/javascript-cpp/msodrawingtype/) numarasını kullanarak bir grafik tablosuna onay kutuları eklemenize olanak tanır. Aşağıdaki örnek, bir grafik tablosuna onay kutusu eklemeyi göstermektedir.

Aşağıdaki resim, çıktı dosyasındaki grafik tablosunu içeren onay kutusu göstermektedir.

![todo:image_alt_text](controls-in-charts_1.jpg)

Aşağıdaki kod parçası tarafından oluşturulan [çıktı dosyası](101089316.xlsx), referansınız için ekte bulunmaktadır.

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

## **Gelişmiş Konular**
- [Grafiklere WordArt Filigranı Ekleme](/cells/tr/javascript-cpp/add-wordart-watermark-to-chart/)
