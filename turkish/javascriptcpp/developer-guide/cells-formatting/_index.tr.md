---
title: JavaScript ile C++ üzerinden hücreleri biçimlendirme
description: Bir rehber, sayı biçimlendirme, tarih biçimlendirme, font stilleri ve diğer hücre stili seçenekleri dahil olmak üzere Aspose.Cells for JavaScript C++ ile hücreleri biçimlendirme ve stillendirmeyi öğrenin. Kılavuzumuz, çekici ve profesyonel görünümlü tablolar oluşturmanıza yardımcı olacaktır.
keywords: Aspose.Cells for JavaScript C++ ile hücre biçimlendirme, stil verme, sayı biçimlendirme, tarih biçimlendirme, font stili, hücre stili seçenekleri, elektronik tablo, oluşturma, profesyonel görünüm, satır ve sütunları biçimlendirme.
linktitle: Hücreleri Biçimlendirin
type: docs
weight: 120
url: /tr/javascript-cpp/cells-formatting/
---

## **Giriş**

{{% alert color="primary" %}}

Aspose.Cells, [Hücre](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) ve [**style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) metodlarını sağlar, bunlar hücrenin biçimlendirme stilini almak/vermek için kullanılır. Aspose.Cells ayrıca [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) sınıfını da sağlar.

{{% /alert %}}

## **Hücreleri biçimlendirme nasıl yapılır teknikleri**

Hücrelere arka plan veya ön plan renkleri, kenarlıklar, fontlar, yatay ve dikey hizalamalar, girinti düzeyi, yazı yönü, döndürme açısı ve çok daha fazlası için farklı türde biçimlendirme stilleri uygulayın.

### **Stil Metodları nasıl kullanılır**

Eğer geliştiriciler farklı hücrelere farklı biçimlendirme stilleri uygulamak istiyorsa, hücrenin [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) öğesini [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) metodu ile almak, stil özelliklerini belirlemek ve ardından biçimlendirmeyi [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) metodu ile uygulamak daha iyidir. Aşağıda, bu yaklaşımı göstermek için bir örnek verilmiştir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Styling Example</h1>
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

            // Instantiate or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello Aspose!";

            // Defining a Style object
            let style;

            // Get the style from A1 cell
            style = cell.style;

            // Setting the vertical alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text
            style.font.color = AsposeCells.Color.Green;

            // Setting to shrink according to the text contained in it
            style.shrinkToFit = true;

            // Setting the bottom border color to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Applying the style to A1 cell
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Farklı Hücreleri Biçimlendirmek İçin Stil Nesnesini Kullanma**

Eğer geliştiriciler aynı biçimlendirme stilini farklı hücrelere uygulamak istiyorsa, [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesini kullanabilirler. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesini kullanmak için aşağıdaki adımları takip edin:

1. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) metodunu çağırarak bir [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi ekleyin
2. Yeni eklenen [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesine erişin
3. İstenen biçimlendirme ayarlarını uygulamak için [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesinin ilgili özelliklerini/atribütlerini ayarlayın
4. Yapılandırılmış [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesini istediğiniz hücrelere atayın

Bu yaklaşım uygulamalarınızın verimliliğini büyük ölçüde artırabilir ve aynı zamanda bellek tasarrufu sağlayabilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Style Cells</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, BorderType, CellBorderType } = AsposeCells;

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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Add a new worksheet to the workbook
            const i = workbook.worksheets.add();

            // Obtain the newly added worksheet by index
            const worksheet = workbook.worksheets.get(i);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Set value of A1
            cell.value = "Hello Aspose!";

            // Create a new style
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = TextAlignmentType.Center;
            style.horizontalAlignment = TextAlignmentType.Center;

            // Set font color
            style.font.color = Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(BorderType.BottomBorder).color = Color.Red;
            style.borders.get(BorderType.BottomBorder).lineStyle = CellBorderType.Medium;

            // Apply style to A1
            cell.style = style;

            // Apply same style to B1, C1, D1
            worksheet.cells.get("B1").style = style;
            worksheet.cells.get("C1").style = style;
            worksheet.cells.get("D1").style = style;

            // Save workbook to XLS format and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and styled successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **Microsoft Excel 2007 Önceden Tanımlanmış Stilleri Nasıl Kullanılır**

Microsoft Excel 2007 için farklı biçimlendirme stilleri uygulamanız gerekiyorsa, Aspose.Cells API'sını kullanarak stilleri uygulayın. Aşağıdaki örnek, bir hücreye önceden tanımlanmış bir stil uygulamanın bu yaklaşımını gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Workbook and Set Cell Style Example</h1>
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
            // Instantiate a new Workbook.
            const workbook = new Workbook();

            // Create a style object.
            const style = workbook.createStyle();

            // Access the first worksheet in the workbook
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const cell = worksheet.cells.get("A1");

            // Input a value to A1 cell.
            cell.putValue("Test");

            // Apply the style to the cell.
            cell.style = style;

            // Saving the Excel 2007 file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```



## **Bir Hücredeki Seçili Karakterleri Biçimlendirme**

Yazı tipi ayarlarıyla ilgilenmek, hücre içindeki metni biçimlendirmeyi açıklar, ancak sadece hücre içeriğinin tümünü biçimlendirmeyi açıklar. Seçili karakterleri biçimlendirmek istiyorsanız ne yapacaksınız?

Aspose.Cells bu özelliği de destekler. Bu konu, bu özelliğin etkin kullanımını açıklar.

### **Seçili Karakterleri Biçimlendirmek**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonundaki her öğe, [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfı nesnesini temsil eder.

[**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfı, aşağıdaki parametreleri alan [**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) metodunu sağlar; böylece bir hücre içindeki karakter aralığını seçebilirsiniz:

- **Başlangıç İndeksi**, seçimin nereden başlayacağı karakterin indeksi.
- **Karakter Sayısı**, seçilecek karakterlerin sayısı.

[**characters(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-number-number-) metodu, geliştiricilerin aşağıdaki kod örneğinde gösterildiği gibi hücreyle aynı şekilde karakterleri biçimlendirmelerine izin veren [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) sınıfı örneği döndürür. Çıktı dosyasında, A1 hücresinde 'Visit' kelimesi varsayılan font ile biçimlendirilirken, 'Aspose!' kalın ve mavi olacaktır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
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

            // If a file is provided, open it; otherwise create a new workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Visit Aspose!";

            // Setting the font of selected characters to bold and color to blue
            const charRange = cell.characters(6, 7);
            charRange.font.isBold = true;
            charRange.font.color = AsposeCells.Color.Blue;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Bir hücredeki Zengin Metnin bir bölümünü biçimlendirmeyi ilginize aldıysanız, [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) ve [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) metodlarını kullanmayı düşünün. [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) metodu, metnin bölümlerine erişmek için kullanılır ve ardından [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) metodu ile değişiklikler yapılabilir. Ayrıca, **Get** metodu, font adı, font rengi, kalınlık vb. gibi çeşitli özellikleri ayarlamak için kullanılabilecek [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) nesnesi dizisi döndürür ve **Set** metodu bu değişiklikleri uygulamak için kullanılabilir.

{{% /alert %}}

## **Satırları ve Sütunları Nasıl Biçimlendirilir**

Bazı durumlarda, geliştiricilerin satırlara veya sütunlara aynı biçimlendirmeyi uygulamaları gerekebilir. Hücrelere tek tek biçimlendirme uygulamak genellikle daha uzun sürer ve iyi bir çözüm değildir.
Bu sorunu ele almak için, Aspose.Cells bu makalede detaylı bir şekilde tartışılan basit ve hızlı bir yol sağlar.

### **Satırları ve Sütunları Biçimlendirme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfını sağlar. [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfı, Excel dosyasındaki her çalışma sayfasına erişimi sağlayan [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) koleksiyonunu içerir. Bir çalışma sayfası, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı ile temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) sınıfı, [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonunu sağlar. [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonunda, bir [**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) nesnesini temsil eden öğeler bulunur.

### **Bir Satırı Nasıl Biçimlendirirsiniz**

[**rows**](https://reference.aspose.com/cells/javascript-cpp/cells/#rows--) koleksiyonundaki her öğe, bir [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) nesnesini temsil eder. [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) nesnesi, satırın biçimlendirmesini ayarlamak için kullanılan [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) metodunu sunar. Aynı biçimlendirmeyi bir satıra uygulamak için, [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesini kullanın. Aşağıdaki adımlar, nasıl kullanılacağını gösterir.

1. [**createStyle()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createStyle--) metodunu çağırarak [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfına [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesi ekleyin.
2. [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesinin özelliklerini ayarlayarak biçimlendirme ayarları uygulayın.
3. [**StyleFlag**](https://reference.aspose.com/cells/javascript-cpp/styleflag) nesnesinin ilgili özelliklerini YASAKLAYIN.
4. Yapılandırılmış [**Style**](https://reference.aspose.com/cells/javascript-cpp/style) nesnesini [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) nesnesine atayın.

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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Obtaining the reference of the first (default) worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Adding a new Style to the styles
            const style = workbook.createStyle();

            // Setting the vertical alignment of the text in the "A1" cell
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the horizontal alignment of the text in the "A1" cell
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Setting the font color of the text in the "A1" cell
            style.font.color = AsposeCells.Color.Green;

            // Shrinking the text to fit in the cell
            style.shrinkToFit = true;

            // Setting the bottom border color of the cell to red
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;

            // Setting the bottom border type of the cell to medium
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Creating StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Accessing a row from the Rows collection
            const row = worksheet.cells.rows.get(0);

            // Assigning the Style object to the Style property of the row
            row.applyStyle(style, styleFlag);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Bir Sutunu Nasıl Biçimlendirirsiniz**

[**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--) koleksiyonu ayrıca bir [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--) koleksiyonu da sağlar. [**columns**](https://reference.aspose.com/cells/javascript-cpp/cells/#columns--) koleksiyonundaki her öğe bir [**Column**](https://reference.aspose.com/cells/javascript-cpp/column) nesnesini temsil eder. Bir [**Row**](https://reference.aspose.com/cells/javascript-cpp/row) nesnesine benzer şekilde, [**Column**](https://reference.aspose.com/cells/javascript-cpp/column) nesnesi de sütunu biçimlendirmek için [**applyStyle(Style, StyleFlag)**](https://reference.aspose.com/cells/javascript-cpp/row/#applyStyle-style-styleflag-) metodunu sunar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Style and Column Apply Example</h1>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a new Style to the styles
            const style = workbook.createStyle();

            // Set vertical and horizontal alignment
            style.verticalAlignment = AsposeCells.TextAlignmentType.Center;
            style.horizontalAlignment = AsposeCells.TextAlignmentType.Center;

            // Set font color
            style.font.color = AsposeCells.Color.Green;

            // Shrink to fit
            style.shrinkToFit = true;

            // Set bottom border color and style
            style.borders.get(AsposeCells.BorderType.BottomBorder).color = AsposeCells.Color.Red;
            style.borders.get(AsposeCells.BorderType.BottomBorder).lineStyle = AsposeCells.CellBorderType.Medium;

            // Create and configure StyleFlag
            const styleFlag = new AsposeCells.StyleFlag();
            styleFlag.horizontalAlignment = true;
            styleFlag.verticalAlignment = true;
            styleFlag.shrinkToFit = true;
            styleFlag.borders = true;
            styleFlag.fontColor = true;

            // Access first column and apply style
            const column = worksheet.cells.getColumns().get(0);
            column.applyStyle(style, styleFlag);

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Style applied to column successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Hizalama Ayarları](/cells/tr/javascript-cpp/cells-alignment-settings/)
- [Kenarlık Ayarları](/cells/tr/javascript-cpp/cells-border-settings/)
- [Excel ve ODS dosyalarının Koşullu Biçimleri ayarlanması.](/cells/tr/javascript-cpp/conditional-formatting/)
- [Excel Temaları ve Renkleri](/cells/tr/javascript-cpp/excel-themes-and-colors/)
- [Doldurma Ayarları](/cells/tr/javascript-cpp/cells-fill-settings/)
- [Font Ayarları](/cells/tr/javascript-cpp/cells-font-settings/)
- [Bir İşkitapta Hücreleri Biçimlendirme](/cells/tr/javascript-cpp/format-worksheet-cells-in-a-workbook/)
- [1904 Tarih Sistemi Uygulama](/cells/tr/javascript-cpp/implement-1904-date-system/)
- [Hücreleri Birleştirme ve Ayırma](/cells/tr/javascript-cpp/merging-and-unmerging-cells/)
- [Sayı Ayarları](/cells/tr/javascript-cpp/cells-number-settings/)
- [Hücreler için Stili Getirme ve Ayarlama](/cells/tr/javascript-cpp/evaluating-cell-getstyle-and-setstyle-methods-against-cell-style-property/)
