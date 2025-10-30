---
title: JavaScript ile C++ aracılığıyla Adlandırılmış Aralıkları Formatla ve Değiştir
linktitle: Biçimlendirme ve Adlandırılmış Aralıkları Düzenleme
type: docs
weight: 85
url: /tr/javascript-cpp/format-and-modify-named-ranges/
description: Aspose.Cells for JavaScript via C++ kullanarak adlandırılmış aralıkları nasıl biçimlendireceğinizi ve değiştireceğinizi öğrenin. 
---

## **Aralıkları Biçimlendirme**

### **Bir Adlandırılmış Aralığa Arkaplan Rengi ve Yazı Tipi Ayarlarını Tanımlama**

Biçimlendirme uygulamak için, stil ayarlarını belirten bir [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi tanımlayın ve bunu [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) nesnesine uygulayın.

Aşağıdaki örnek, bir aralığa katı doldurmalı rengi (gölge rengi) ve yazı tipi ayarlarını nasıl ayarlayacağınızı göstermektedir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Range Styles Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, BackgroundType, StyleFlag, Utils } = AsposeCells;

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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Get the first worksheet in the book.
            const WS = workbook.worksheets.get(0);

            // Create a range of cells.
            const range = WS.cells.createRange(1, 1, 1, 18);

            // Name the range.
            range.name = "MyRange";

            // Declare a style object.
            let stl;

            // Create/add the style object.
            stl = workbook.createStyle();

            // Specify some Font settings.
            stl.font.name = "Arial";
            stl.font.isBold = true;

            // Set the font text color
            stl.font.color = Color.Red;

            // To Set the fill color of the range, you may use ForegroundColor with
            // Solid Pattern setting.
            stl.foregroundColor = Color.Yellow;
            stl.pattern = BackgroundType.Solid;

            // Create a StyleFlag object.
            let flg = new StyleFlag();
            // Make the corresponding attributes ON.
            flg.font = true;
            flg.cellShading = true;

            // Apply the style to the range.
            range.applyStyle(stl, flg);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rangestyles.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the generated file.</p>';
        });
    </script>
</html>
```

### **Bir Adlandırılmış Aralığa Sınırlar Ekleme**

Bir tek hücre yerine, hücre aralığına sınır ekleme mümkündür. [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) nesnesi, hücre aralığına sınır eklemek için aşağıdaki parametreleri alan bir [**outlineBorder(BorderType, CellBorderType, CellsColor)**](https://reference.aspose.com/cells/javascript-cpp/range/#outlineBorder-bordertype-cellbordertype-cellscolor-) metodu sağlar.

- Kenar tipi, kenar türü, [**BorderType**](https://reference.aspose.com/cells/javascript-cpp/bordertype) sıralamasından seçilir.
- Çizgi stili, çizgi stili, [**CellBorderType**](https://reference.aspose.com/cells/javascript-cpp/cellbordertype) sıralamasından seçilir.
- Renk, çizgi rengi, Color sıralamasından seçilir.

Aşağıdaki örnek, bir aralığa kenarlık eklemeyi gösterir.

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
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color, Utils } = AsposeCells;

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
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Clears the worksheets
            workbook.worksheets.clear();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello World From Aspose");

            // Creating a range of cells starting from "A1" cell to 3rd column in a row
            const range = worksheet.cells.createRange(0, 0, 1, 3);

            // Adding a thick top border with blue line
            range.setOutlineBorder(BorderType.TopBorder, CellBorderType.Thick, Color.Blue);

            // Adding a thick bottom border with blue line
            range.setOutlineBorder(BorderType.BottomBorder, CellBorderType.Thick, Color.Blue);

            // Adding a thick left border with blue line
            range.setOutlineBorder(BorderType.LeftBorder, CellBorderType.Thick, Color.Blue);

            // Adding a thick right border with blue line
            range.setOutlineBorder(BorderType.RightBorder, CellBorderType.Thick, Color.Blue);

            // Saving the Excel file (Excel97-2003 format)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

Aşağıdaki örnek, aralıktaki her hücreye sınırların nasıl ayarlanacağını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Style to Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, BorderType, CellBorderType, Color } = AsposeCells;

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

            // Instantiating a Workbook object opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the cells in the first worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Create a range of cells.
            const range = cells.createRange("A6", "P216");

            // Declare style.
            let stl;

            // Create the style adding to the style collection.
            stl = workbook.createStyle();

            // Specify the font settings.
            stl.font.name = "Arial";
            stl.font.isBold = true;
            stl.font.color = Color.Blue;

            // Set the borders
            const borders = stl.borders;
            borders.get(BorderType.TopBorder).lineStyle = CellBorderType.Thin;
            borders.get(BorderType.TopBorder).color = Color.Blue;
            borders.get(BorderType.LeftBorder).lineStyle = CellBorderType.Thin;
            borders.get(BorderType.LeftBorder).color = Color.Blue;
            borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Thin;
            borders.get(BorderType.BottomBorder).color = Color.Blue;
            borders.get(BorderType.RightBorder).lineStyle = CellBorderType.Thin;
            borders.get(BorderType.RightBorder).color = Color.Blue;

            // Create StyleFlag object.
            const flg = new StyleFlag();
            // Make the corresponding formatting attributes ON.
            flg.font = true;
            flg.borders = true;

            // Apply the style with format settings to the range.
            range.applyStyle(stl, flg);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Style applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **İsimlendirilmiş Bir Aralığı Yeniden Adlandır**

Aspose.Cells, ihtiyaçlarınıza göre isimlendirilmiş aralığın adını değiştirme imkanı sağlar. İsimlendirilmiş aralığı alıp [**Name.text**](https://reference.aspose.com/cells/javascript-cpp/name/#text--) özniteliği kullanarak yeniden adlandırabilirsiniz. Aşağıdaki örnek, bir isimlendirilmiş aralığı yeniden adlandırmanın nasıl yapılacağını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Renaming Range</title>
    </head>
    <body>
        <h1>Renaming Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Get the Cells of the sheet
            const cells = sheet.cells;

            // Get the named range "TestRange"
            const name = workbook.worksheets.names.get("TestRange");

            // Rename it
            name.text = "NewRange";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenamingRange.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Named range renamed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Aralıkların Birleşimi**

Aspose.Cells, aralıklar arasında birleşim yapmak için [**Range.unionRang(Range)**](https://reference.aspose.com/cells/javascript-cpp/range/#unionRang-range-) metodunu sağlar; bu metod bir [*dizi*] nesnesi döndürür. Aşağıdaki örnek, aralıklar arasında birleşim yapmayı gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Named Ranges Union and Styling Example</h1>
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

            // Instantiate a workbook object and open the uploaded excel file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named ranges.
            const ranges = workbook.worksheets.namedRanges;

            // Create a style object.
            const style = workbook.createStyle();

            // Set the shading color with solid pattern type.
            style.foregroundColor = AsposeCells.Color.Yellow;
            style.pattern = AsposeCells.BackgroundType.Solid;

            // Create a styleflag object.
            const flag = new AsposeCells.StyleFlag();

            // Apply the cellshading.
            flag.cellShading = true;

            // Creates an array list.
            let al = [];

            // Get the array list collection apply the union operation.
            al = ranges[0].unionRanges([ranges[1]]);

            // Define a range object.
            let rng;
            let frow, fcol, erow, ecol;

            for (let i = 0; i < al.length; i++)
            {
                // Get a range.
                rng = al[i];
                frow = rng.firstRow;
                fcol = rng.firstColumn;
                erow = rng.rowCount;
                ecol = rng.columnCount;

                // Apply the style to the range.
                rng.applyStyle(style, flag);
            }

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rngUnion.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Aralıkların Kesişimi**

Aspose.Cells, iki aralığın kesişmesini sağlamak için [**Range.intersect(Range)**](https://reference.aspose.com/cells/javascript-cpp/range/#intersect-range-) metodunu sağlar. Metod, bir [**Range**](https://reference.aspose.com/cells/javascript-cpp/range) nesnesi döndürür. Bir aralığın diğerini kesip kesmediğini kontrol etmek için [**Range.intersect(Range)**](https://reference.aspose.com/cells/javascript-cpp/range/#intersect-range-) metodunu kullanın; bu metod Boolean değer döndürür. Aşağıdaki örnek, aralıkların kesişmesini gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Named Range Intersection Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, BackgroundType, StyleFlag, Utils } = AsposeCells;

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

            // Instantiate a workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the named ranges.
            const ranges = workbook.worksheets.namedRanges;

            // Check whether the first range intersect the second range.
            const isIntersect = ranges.get(0).isIntersect(ranges.get(1));

            // Create a style object.
            const style = workbook.createStyle();

            // Set the shading color with solid pattern type.
            style.foregroundColor = Color.Yellow;
            style.pattern = BackgroundType.Solid;

            // Create a styleflag object.
            const flag = new StyleFlag();

            // Apply the cell shading.
            flag.cellShading = true;

            // If first range intersects second range.
            if (isIntersect) {
                // Create a range by getting the intersection.
                const intersection = ranges.get(0).intersect(ranges.get(1));

                // Name the range.
                intersection.name = "Intersection";

                // Apply the style to the range.
                intersection.applyStyle(style, flag);
            }

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'rngIntersection.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **İsimlendirilmiş Aralıklarda Hücreleri Birleştirme**

Aspose.Cells, aralıktaki hücreleri birleştirmek için [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) metodunu sağlar. Aşağıdaki örnek, isimlendirilmiş bir aralıktaki hücreleri nasıl birleştireceğinizi gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merging Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, StyleFlag, TextAlignmentType, Utils } = AsposeCells;

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

            // Instantiate a new Workbook.
            const wb1 = new Workbook();

            // Get the first worksheet in the workbook.
            const worksheet1 = wb1.worksheets.get(0);

            // Create a range.
            const mrange = worksheet1.cells.createRange("A18", "J18");

            // Name the range.
            mrange.name = "Details";

            // Merge the cells of the range.
            mrange.merge();

            // Get the range.
            const range1 = wb1.worksheets.rangeByName("Details");      

            // Define a style object.
            const style = wb1.createStyle();

            // Set the alignment.
            style.horizontalAlignment = TextAlignmentType.Center;

            // Create a StyleFlag object.
            const flag = new StyleFlag();
            // Make the relative style attribute ON.
            flag.horizontalAlignment = true;

            // Apply the style to the range.
            range1.applyStyle(style, flag);

            // Input data into range.
            range1.get(0, 0).putValue("Aspose");

            // Save the excel file.
            const outputData = wb1.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'mergingrange.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultEl.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Adlandırılmış Bir Aralığı Kaldır**

Aspose.Cells, aralığın ismini silmek için [**NameCollection.removeAt(number)**](https://reference.aspose.com/cells/javascript-cpp/namecollection/#removeAt-number-) metodunu sağlar. Aralığın içeriğini temizlemek için [**Cells.clearRange(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/cells/#clearRange-cellarea-) metodunu kullanın. Aşağıdaki örnek, bir isimlendirilmiş aralığı ve içeriğini nasıl kaldıracağınızı gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Copy Ranges Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, BorderType, CellBorderType, Color, Utils } = AsposeCells;

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
            // Creating a new Workbook (blank)
            const workbook = new Workbook();

            // Get all the worksheets in the book.
            const worksheets = workbook.worksheets;

            // Get the first worksheet in the worksheets collection.
            const worksheet = worksheets.get(0);

            // Create a range of cells.
            const range1 = worksheet.cells.createRange("E12", "I12");

            // Name the range.
            range1.name = "MyRange";

            // Set the outline border to the range.
            range1.outlineBorder = { position: BorderType.TopBorder, type: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { position: BorderType.BottomBorder, type: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { position: BorderType.LeftBorder, type: CellBorderType.Medium, color: new Color(0, 0, 128) };
            range1.outlineBorder = { position: BorderType.RightBorder, type: CellBorderType.Medium, color: new Color(0, 0, 128) };

            // Input some data with some formattings into a few cells in the range.
            range1.get(0, 0).putValue("Test");
            range1.get(0, 4).putValue("123");

            // Create another range of cells.
            const range2 = worksheet.cells.createRange("B3", "F3");

            // Name the range.
            range2.name = "testrange";

            // Copy the first range into second range.
            range2.copy(range1);

            // Remove the previous named range (range1) with its contents.
            worksheet.cells.clearRange(11, 4, 11, 8);
            worksheets.names.removeAt(0);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'copyranges.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
