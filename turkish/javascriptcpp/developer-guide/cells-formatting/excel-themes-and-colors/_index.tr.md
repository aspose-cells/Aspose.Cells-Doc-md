---
title: Excel Temaları ve Renkler
linktitle: Excel Temaları ve Renkler  
type: docs  
weight: 100  
url: /tr/javascript-cpp/excel-themes-and-colors/  
description: Aspose.Cells for JavaScript via C++ kullanarak özel renk düzenleri nasıl kullanılır öğrenin.  
keywords: JavaScript ile Renk Düzenleri Oluşturma ve Uygulama, JavaScript programlı olarak Özel Renk Düzeni Oluşturma, Programlı olarak nasıl Özel Renk Düzeni Uygulanır JavaScript, JavaScript ile Excel’de Renk Düzeni nasıl kullanılır  
---

## **Excel'de Tema Uygulama ve Oluşturma**  
Belge temaları, Excel belgelerinin renklerini, yazı tiplerini ve grafik biçimlendirme efektlerini kolayca koordine etmenizi ve bunları hızlı bir şekilde güncellemenizi sağlar.  
Temalar, kitapçıkta kullanılan isimlendirilmiş stiller, grafik efektleri ve diğer nesnelerle birleşik bir görünüm sağlar. Örneğin, Accent1 stili Office ve Apex temalarında farklı görünür. Sıkça, bir belge teması uygular ve ardından istediğiniz gibi değiştirirsiniz.  

### **Excel'de Bir Renk Şeması Nasıl Uygulanır**  
1. Excel'i açın ve Excel menü şeridinde "Sayfa Düzeni" sekmesine gidin.  
1. "Temalar" bölümündeki "Renkler" düğmesine tıklayın.  
<br>  
<img src="color.png" width=70% />  
1. Gereksinimlerinize uygun bir renk paleti seçin veya canlı bir önizleme görmek için şema üzerinde gezdirin.  

### **Excel'de Özel Renk Şeması Nasıl Oluşturulur**  
Belgenize taze, benzersiz bir görünüm vermek veya kuruluşunuzun marka standartlarına uygun olmak için kendi renk setinizi oluşturabilirsiniz.  

1. Excel'i açın ve Excel menü şeridinde "Sayfa Düzeni" sekmesine gidin.  
1. "Temalar" bölümündeki "Renkler" düğmesine tıklayın.  
1. "Renkleri Özelleştir..." düğmesine tıklayın.  
<br>  
<img src="color2.png" width=70% />  

1. "Yeni Tema Renkleri Oluştur" iletişim kutusunda, her bir öğe için renk seçmek için yanlarındaki renk açılır listelerine tıklayabilirsiniz. Renkleri paletten seçebilir veya "Daha Fazla Renkler" seçeneğini kullanarak özel renkler tanımlayabilirsiniz.  
<br>  
<img src="color3.png" width=70% />  
1. Tüm istenen renkleri seçtikten sonra, özel renk şemanıza bir ad sağlamak için "Ad" alanına bir ad girin.  

1. Özel renk şemanızı kaydetmek için "Kaydet" düğmesine tıklayın. Özel renk şemanız artık gelecekte kullanılmak üzere "Renkler" açılır menüsünde mevcut olacaktır.  

## **Aspose.Cells'te Renk Şeması Oluşturma ve Uygulama**  
Aspose.Cells, temaları ve renkleri özelleştirmek için özellikler sağlar.  

### **Aspose.Cells'te Özel Renk Teması Nasıl Oluşturulur**  
Eğer dosyada tema renkleri kullanıldıysa, her hücreyi ayrı ayrı değiştirmemize gerek kalmaz; temanın renklerini değiştiririz.  

Aşağıdaki örnek, istediğiniz renklerle özel temaları nasıl uygulayacağınızı gösterir. Microsoft Excel 2007'de manuel olarak oluşturulmuş bir örnek şablon dosyası kullanıyoruz.  

Aşağıdaki örnek, bir şablon XLSX dosyasını yükler, farklı tema renk türleri için renkleri tanımlar, özelleştirilmiş renkleri uygular ve Excel dosyasını kaydeder.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Custom Theme Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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

            // Define Color array (of 12 colors) for Theme.
            const carr = [
                new Color("AntiqueWhite"), // Background1
                new Color("Brown"), // Text1
                new Color("AliceBlue"), // Background2
                new Color("Yellow"), // Text2
                new Color("YellowGreen"), // Accent1
                new Color("Red"), // Accent2
                new Color("Pink"), // Accent3
                new Color("Purple"), // Accent4
                new Color("PaleGreen"), // Accent5
                new Color("Orange"), // Accent6
                new Color("Green"), // Hyperlink
                new Color("Gray") // Followed Hyperlink
            ];

            // Set the custom theme with specified colors.
            workbook.customTheme("CustomeTheme1", carr);

            // Save as the excel file.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom theme applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



### **Aspose.Cells'te Tema Renklerinin Uygulanması**  
Aşağıdaki örnek, bir hücrenin ön plan ve yazı tipi renklerini varsayılan tema renk türlerine göre uygular. Ayrıca, Excel dosyasını diske kaydeder.  


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
            // Instantiate a Workbook.
            const workbook = new Workbook();

            // Get cells collection in the first (default) worksheet.
            const cells = workbook.worksheets.get(0).cells;

            // Get the D3 cell.
            const c = cells.get("D3");

            // Get the style of the cell.
            const s = c.style;

            // Set foreground color for the cell from the default theme Accent2 color.
            s.foregroundThemeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent2, 0.5);

            // Set the pattern type.
            s.pattern = AsposeCells.BackgroundType.Solid;

            // Get the font for the style.
            const f = s.font;

            // Set the theme color.
            f.themeColor = new AsposeCells.ThemeColor(AsposeCells.ThemeColorType.Accent4, 0.1);

            // Apply style.
            c.style = s;

            // Put a value.
            c.value = "Testing1";

            // Save the excel file and provide download link.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to save the file.</p>';
        });
    </script>
</html>
```


### **Aspose.Cells'te Tema Renklerinin Alınması ve Ayarlanması**  
Aşağıda temalı renkleri uygulayan ve ayarlayan birkaç yöntem ve özellik bulunmaktadır.  

- [**Style.foregroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#foregroundThemeColor-themecolor-): Ön plan rengini ayarlamak için kullanılır.  
- [**Style.backgroundThemeColor**](https://reference.aspose.com/cells/javascript-cpp/style/#backgroundThemeColor-themecolor-): Arka plan rengini ayarlamak için kullanılır.  
- [**Font.themeColor**](https://reference.aspose.com/cells/javascript-cpp/font/#themeColor-themecolor-): Yazı tipi rengini ayarlamak için kullanılır.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-): Tema rengini almak için kullanılır.  
- [**Workbook.themeColor**](https://reference.aspose.com/cells/javascript-cpp/workbook/#themeColor-themecolortype-color-): Tema rengini ayarlamak için kullanılır.  

Aşağıdaki örnek, temalı renkleri almanın ve ayarlamanın nasıl yapılacağını gösterir.  

Aşağıdaki örnek, şablon XLSX dosyasını kullanır, farklı tema renkleri için renkleri alır, renkleri değiştirir ve Microsoft Excel dosyasını kaydeder.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Theme Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color, ThemeColorType } = AsposeCells;

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

            // Instantiating a Workbook object and opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Background1 theme color.
            let c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1: ", c);

            // Get the Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2: ", c);

            // Change the Background1 theme color.
            workbook.themeColor(ThemeColorType.Background1, Color.Red);

            // Get the updated Background1 theme color.
            c = workbook.themeColor(ThemeColorType.Background1);
            console.log("theme color Background1 changed to: ", c);

            // Change the Accent2 theme color.
            workbook.themeColor(ThemeColorType.Accent2, Color.Blue);

            // Get the updated Accent2 theme color.
            c = workbook.themeColor(ThemeColorType.Accent2);
            console.log("theme color Accent2 changed to: ", c);

            // Saving the updated file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Updated Excel File';

            // Display results
            let resultHtml = '';
            resultHtml += `<p>theme color Background1: ${JSON.stringify(workbook.themeColor(ThemeColorType.Background1))}</p>`;
            resultHtml += `<p>theme color Accent2: ${JSON.stringify(workbook.themeColor(ThemeColorType.Accent2))}</p>`;
            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! See console for detailed logs.</p>' + resultHtml;
        });
    </script>
</html>
```


## **Gelişmiş Konular**  
- [Excel Dosyasından Tema Verisi Çıkarın](/cells/tr/javascript-cpp/extract-theme-data-from-excel-file/)
