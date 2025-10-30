---
title: JavaScript ile C++ kullanarak Alanları Formatla
linktitle: Aralıkları Biçimlendir
type: docs
weight: 105
url: /tr/javascript-cpp/how-to-format-a-range/
description: Excel de bir hücre aralığını Aspose.Cells for JavaScript kullanarak nasıl biçimlendireceğinizi öğrenin, C++ ile.
---

## **Olası Kullanım Senaryoları**  
Bir aralığa stili uygulamanız gerektiğinde, aralık biçimlendirme kullanabilirsiniz.  

## **Excel'de bir Aralığı Nasıl Biçimlendirirsiniz**  

Excel'de bir aralığı biçimlendirmek için, Excel tarafından sağlanan yerleşik biçimlendirme seçeneklerini kullanabilirsiniz. İşte Excel'de bir aralığı doğrudan nasıl biçimlendireceğiniz:  

1. Excel'i açın ve biçimlendirmek istediğiniz aralığı içeren çalışma kitabını açın.  

2. Biçimlendirmek istediğiniz hücre aralığını seçin. Aralığı seçmek için tıklayıp sürükleyebilirsiniz veya Shift + Ok tuşları gibi klavye kısayollarını kullanarak seçimi genişletebilirsiniz.  

3. Aralık seçildikten sonra, seçilen aralık üzerine sağ tıklayın ve bağlam menüsünden "Hücreleri Biçimlendir" öğesini seçin. Alternatif olarak, Excel şeridindeki Ana sekmesine giderek, "Hücreler" grubundaki "Biçim" açılır menüsüne tıklayın ve "Hücreleri Biçimlendir" seçeneğini belirleyin.  

4. "Hücreleri Biçimlendir" iletişim kutusu görünecektir. Burada, seçilen aralığa uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin, yazı tipi stili, yazı tipi boyutu, yazı tipi rengi, sayı formatı, kenarlıklar, arka plan rengi vb. değiştirebilirsiniz. Farklı sekmeleri keşfetmek için iletişim kutusundaki farklı sekmelere bakın.  

5. İstenen biçimlendirme değişikliklerini yaptıktan sonra, seçilen aralığa biçimlendirmeyi uygulamak için "Tamam" düğmesine tıklayın.  

## **JavaScript Kullanarak Bir Aralık Nasıl Biçimlendirilir**  

C++ kullanarak Aspose.Cells for JavaScript ile bir aralık biçimlendirmek için aşağıdaki yöntemleri kullanabilirsiniz:  
1. [Range.applyStyle(style, flag)](https://reference.aspose.com/cells/javascript-cpp/range/#applyStyle-style-styleflag-)  
2. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  
3. [Range.style](https://reference.aspose.com/cells/javascript-cpp/range/#style-style-)  

## **Örnek Kod**  
Bu örnekte bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veri ekliyoruz, ilk çalışma sayfasına erişiyoruz ve iki aralık("A1:C3" ve "A4:C5") tanımlıyoruz. Daha sonra yeni stiller oluşturuyoruz, çeşitli biçimlendirme seçeneklerini belirliyoruz (örneğin, yazı tipi rengi, kalın), ve stili aralığa uyguluyoruz. Son olarak, çalışma kitabını yeni bir dosyaya kaydediyoruz.  
<br>  
![todo:image_alt_text](format-range.png)  

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

            // Create the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);

            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Access the worksheet (already have ws, but keep variable for clarity)
            const worksheet = workbook.worksheets.get(0);

            // Define the range
            const range = worksheet.cells.createRange("A1:C3");

            // Apply formatting to the range
            const style = workbook.createStyle();
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.font = true;
            range.applyStyle(style, flag);

            // Define the range
            const range2 = worksheet.cells.createRange("A4:C5");

            // Apply formatting to the range
            const style2 = workbook.createStyle();
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            range2.setStyle(style2);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
