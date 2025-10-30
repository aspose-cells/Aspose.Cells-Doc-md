---
title: Bir hücrenin biçimini değiştirme
linktitle: Bir hücrenin biçimini değiştirme
description: JavaScript via C++ kullanarak Aspose.Cells kütüphanesi ile hücrelerin biçimlendirmesini değiştirme, font, renk, kenar vb. Bu özellikleri ayarlayarak hücrelerin görünümünü daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells, hücre biçimlendirme, JavaScript via C++, font, renk, kenar
type: docs
weight: 20
url: /tr/javascript-cpp/how-to-change-format-of-cell/
---

## **Olası Kullanım Senaryoları**
Belirli verileri vurgulamak istediğinizde, hücrelerin stiline değişiklik yapabilirsiniz.

## **Excel'de bir hücrenin biçimini nasıl değiştirilir**

Excel'de bir tek hücrenin biçimini değiştirmek için şu adımları izleyin:

1. Excel'i açın ve biçimini değiştirmek istediğiniz hücreyi içeren çalışma kitabını açın.

2. Biçimini değiştirmek istediğiniz hücreyi bulun.

3. Hücreye sağ tıklayın ve bağlam menüsünden "Hücre Biçimlendir" seçeneğini seçin. Alternatif olarak, hücreyi seçebilir ve Excel şeridindeki Anahtar sekmesine giderek "Hücreler" grubundaki "Biçim" açılır menüsüne tıklayıp "Hücre Biçimleri"ni seçebilirsiniz.

4. "Hücre Biçimleri" iletişim kutusu görünecektir. Burada, seçilen hücreye uygulanacak çeşitli biçimlendirme seçeneklerini seçebilirsiniz. Örneğin, yazı tipi stilini, yazı tipi boyutunu, yazı tipi rengini, sayı biçimini, sınırları, arka plan rengini vs. değiştirebilirsiniz. Farklı sekmele
rin iletişim kutusunda çeşitli biçimlendirme seçeneklerine erişmek için keşfedin.

5. İstenen biçimlendirme değişiklikleri yapıldıktan sonra, seçilen hücreye biçimlendirmeyi uygulamak için "Tamam" düğmesine tıklayın.


## **JavaScript kullanarak bir hücrenin biçimini nasıl değiştirilir**

Aspose.Cells kullanarak hücre biçimlendirmesini değiştirmek için aşağıdaki yöntemleri kullanabilirsiniz:
1. [Hücre.stil(Style)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-)
2. [Hücre.stil(Style, explicitFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-boolean-)
3. [Hücre.stil(Style, StyleFlag)](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-styleflag-)


## **Örnek Kod**
Bu örnekte, bir Excel çalışma kitabı oluşturuyoruz, bazı örnek veriler ekliyoruz, ilk çalışma sayfasına erişiyor ve iki hücreyi ("A2" ve "B3") alıyoruz. Ardından, hücre stilini alıyoruz, çeşitli biçimlendirme seçenekleri ayarlıyoruz (örneğin, yazı tipi rengi, kalın) ve biçimi hücreye uyguluyoruz. Son olarak, çalışma kitabını yeni bir dosyaya kaydediyoruz.
![todo:image_alt_text](change-format.png)

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

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells
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

            // Access the worksheet
            const worksheet = workbook.worksheets.get(0);

            const a2 = worksheet.cells.get("A2");

            // Get style of A2
            const style = a2.style;

            // Change the format
            style.font.color = AsposeCells.Color.Red;
            style.font.isBold = true;

            const flag = new AsposeCells.StyleFlag();
            flag.fontColor = true;
            // Apply style (assignment per conversion rules)
            a2.style = style;

            const b3 = worksheet.cells.get("B3");
            // Get style of B3
            const style2 = b3.style;

            // Change the format
            style2.font.color = AsposeCells.Color.Blue;
            style2.font.isItalic = true;
            b3.style = style2;

            // Saving the modified workbook and offering it for download
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
