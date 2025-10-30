---
title: Doldurma Ayarları
linktitle: Doldurma Ayarları
description: JavaScript via C++ kullanarak hücrelerin dolgu ayarları, arka plan ve stilini nasıl özelleştireceğinizi öğrenin.
keywords: Aspose.Cells, Hücreler, Dolgu Ayarları, Arka Plan, Stil, JavaScript via C++
type: docs
weight: 50
url: /tr/javascript-cpp/cells-fill-settings/
---

## **Renkler ve Arka Plan Desenleri**

Microsoft Excel, hücrelerin ön plan (çerçeve) ve arka plan (doldurma) renklerini ve arka plan desenlerini ayarlayabilir.

Aspose.Cells, bu özellikleri esnek bir şekilde destekler. Bu konuda, Aspose.Cells kullanarak bu özellikleri nasıl kullanacağımızı öğreneceğiz.

### **Renkler ve Arka Plan Desenlerini Ayarlama**

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar; bu, bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her sayfaya erişimi sağlayan [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/javascript-cpp/cells) koleksiyonundaki her öğe [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının bir nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) öğesi, bir hücrenin biçimlendirmesini almak ve ayarlamak için kullanılan [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) özelliğine sahiptir. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) sınıfı, hücrelerin ön plan ve arka plan renklerini ayarlamak için özellikler sağlar. Aspose.Cells, aşağıda verilen önceden tanımlı arka plan desenleri setini içeren [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) enumerasyonunu sağlar.

|**Arka Plan Desenleri**|**Açıklama**|
| :- | :- |
|DiagonalCrosshatch|Çapraz çizgili deseni temsil eder|
|DiagonalStripe|Çapraz şerit deseni temsil eder|
|Gray6|%6,25 gri deseni temsil eder|
|Gray12|%12,5 gri deseni temsil eder|
|Gray25|%25 gri deseni temsil eder|
|Gray50|%50 gri deseni temsil eder|
|Gray75|%75 gri deseni temsil eder|
|HorizontalStripe|Dikey şerit deseni temsil eder|
|None|Arka plan yok|
|ReverseDiagonalStripe|Çapraz ters şerit deseni temsil eder|
|Solid|Düz deseni temsil eder|
|ThickDiagonalCrosshatch|Kalın çapraz çizgili deseni temsil eder|
|ThinDiagonalCrosshatch|İnce çapraz çizgili deseni temsil eder|
|ThinDiagonalStripe|İnce çapraz şerit deseni temsil eder|
|ThinHorizontalCrosshatch|İnce yatay çapraz çizgili deseni temsil eder|
|ThinHorizontalStripe|İnce yatay şerit deseni temsil eder|
|ThinReverseDiagonalStripe|İnce ters çapraz şerit deseni temsil eder|
|ThinVerticalStripe|İnce dikey şerit deseni temsil eder|
|VerticalStripe|Dikey şerit deseni temsil eder|

Aşağıdaki örnekte, A1 hücresinin ön plan rengi ayarlanmış ancak A2, dikey çizgili bir arka plan deseni olan hem ön plan rengi hem de arka plan rengi olarak yapılandırılmıştır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Define a Style and get the A1 cell style
            let style = worksheet.cells.get("A1").style;

            // Setting the foreground color to yellow
            style.foregroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A1 cell
            worksheet.cells.get("A1").style = style;

            // Get the A2 cell style
            style = worksheet.cells.get("A2").style;

            // Setting the foreground color to blue
            style.foregroundColor = AsposeCells.Color.Blue;

            // Setting the background color to yellow
            style.backgroundColor = AsposeCells.Color.Yellow;

            // Setting the background pattern to vertical stripe
            style.pattern = AsposeCells.BackgroundType.VerticalStripe;

            // Apply the style to A2 cell
            worksheet.cells.get("A2").style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and ready for download.</p>';
        });
    </script>
</html>
```


### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

- Bir hücrenin ön plan veya arka plan rengini ayarlamak için [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesinin [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) veya [**backgroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundColor-color-) özelliklerini kullanın. Her ikisi de, sadece [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesinin [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) özelliği yapılandırıldığında etkili olur.
- [**foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor-color-) özelliği hücrenin ton rengini ayarlar. [**pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) özelliği, ön plan veya arka plan rengi için kullanılan arka plan deseni türünü belirtir. Aspose.Cells, önceden tanımlanmış arka plan desenleri türlerini içeren [**BackgroundType**](https://reference.aspose.com/cells/javascript-cpp/backgroundtype) adlı bir sıralama sağlar.
- {0} sıralaması içinden *BackgroundType.None* değerini seçerseniz, ön plan rengi uygulanmaz. Aynı şekilde, arka plan rengi de {BackgroundType.None} veya {BackgroundType.Solid} değerleri seçilirse uygulanmaz.
- Hücrenin gölgelendirme/dolgu rengini alırken, [**style.pattern**](https://reference.aspose.com/cells/javascript-cpp/style/#pattern-backgroundtype-) *BackgroundType.None* ise, [**style.foregroundColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundColor--) *Color.Empty* değerini döndürecektir.

{{% /alert %}}

### **Gradyan Dolgu Efektleri Uygulama**

Arka plan degrade dolgu efektlerinizi hücreye uygulamak için, uygun şekilde [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesinin [**twoColorGradient**](https://reference.aspose.com/cells/javascript-cpp/style/#twoColorGradient-color-color-gradientstyletype-number-) özelliğini kullanın.

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
        const { Workbook, SaveFormat, Color, GradientStyleType, TextAlignmentType } = AsposeCells;

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
                workbook = new Workbook();
            }

            const worksheet = workbook.worksheets.get(0);

            worksheet.cells.get(2, 1).putValue("test");

            const style = worksheet.cells.get("B3").style;

            style.isGradient = true;
            style.twoColorGradient = [ new Color(255, 255, 255), new Color(79, 129, 189), GradientStyleType.Horizontal, 1 ];
            style.font.color = Color.Red;
            style.horizontalAlignment = TextAlignmentType.Center;
            style.verticalAlignment = TextAlignmentType.Center;

            worksheet.cells.get("B3").style = style;

            worksheet.cells.rowHeightPixel = [2, 53];

            worksheet.cells.merge(2, 1, 1, 2);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


## **Renkler ve Palet**

Bir palet, bir görüntü oluşturmak için kullanılabilen renk sayısıdır. Bir sunumda standart bir palet kullanımı, kullanıcının tutarlı bir görünüm oluşturmasına olanak tanır. Her Microsoft Excel (97-2003) dosyasının bir hücrelere, fontlara, ızgaralara, grafik nesnelerine, doldurmalara ve çizgilere uygulanabilen 56 renklik bir paleti vardır.

Aspose.Cells ile sadece paletin mevcut renklerini değil aynı zamanda özel renkleri de kullanmak mümkündür. Özel bir rengi kullanmadan önce, önce paletine ekleyin.

Bu konu, paletine özel renkler eklemenin nasıl yapıldığını tartışmaktadır.

### **Paletine Özel Renkler Eklemek**

Aspose.Cells, Microsoft Excel'in 56 renkli paletini destekler. Paletine tanımlanmamış özel bir renk kullanmak için, rengi paletine ekleyin.

Aspose.Cells, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) adlı bir sınıf sağlar; bu, bir Microsoft Excel dosyasını temsil eder. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, aşağıdaki parametreleri kullanarak paleti değiştirmek için özel bir renk eklemek amacıyla [**changePalette**](https://reference.aspose.com/cells/javascript-cpp/workbook/#changePalette-color-number-) metodunu sağlar:

- Özel Renk, paletine eklenecek özel renk.
- İndeks, özel rengin paletindeki rengin yerini belirtir. 0-55 arasında olmalıdır.

Aşağıdaki örnek, (Orkide) özel bir rengi paletine ekleyip bunu bir font üzerine uygulamadan önce paletine ekler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Checks if a color is in the palette for the spreadsheet.
            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding Orchid color to the palette at 55th index
            workbook.changePalette(AsposeCells.Color.Orchid, 55);

            console.log(workbook.isColorInPalette(AsposeCells.Color.Orchid));

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.putValue("Hello Aspose!");

            // Defining new Style object
            const styleObject = workbook.createStyle();
            // Setting the Orchid (custom) color to the font
            styleObject.font.color = workbook.colors[55];

            // Applying the style to the cell
            cell.style = styleObject;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}

Palet sadece 56 renk tutar. Bir özel rengi paletine eklediğinizde, palet değişir ve önceki rengiyle biçimlendirilen dosyadaki her eleman değişir. Bu nedenle, paleti değiştirirken lütfen çok dikkatli olun. Dahası, bu sadece XLS (Excel 97 - 2003) dosya biçiminde bir kısıtlama olarak mevcuttur, XLSX veya diğer gelişmiş MS Excel (2007/2010 veya 2013) dosya biçimleri için böyle bir kısıtlama yoktur.

{{% /alert %}}
