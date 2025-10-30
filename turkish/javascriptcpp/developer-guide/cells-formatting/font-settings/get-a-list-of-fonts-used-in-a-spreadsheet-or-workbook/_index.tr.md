---
title: Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın
linktitle: Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın
description: C++ ile Aspose.Cells for JavaScript kullanarak bir elektronik tabloda kullanılan fontların listesini nasıl alınacağını öğrenin. Bu makale, belge içindeki font bilgilerini nasıl alacağınızı gösterecektir.
keywords: Aspose.Cells, JavaScript C++ ile, Elektronik Tablo, Çalışma Kitabı, Font, Liste
type: docs
weight: 20
url: /tr/javascript-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Olası Kullanım Senaryoları**

Bazen, bir belgenin düzenlenmesi için kullanılan yazı tiplerini bilmek önemli olabilir. Elektronik tablonuzu PDF veya resim formatına dönüştürdüğünüzde, Aspose.Cells tüm gerekli yazı tiplerinin sisteminize yüklü olmasını veya **yazı tipleri dizininde** bulunmasını gerektirir. Aspose.Cells, gereken yazı tipini bulamazsa, gerçek yazı tipinizi başka uygun bir yazı tipi ile değiştirmeye çalışır. Bu, sadece istenmeyen şekilde PDF veya görüntülerin işlenmesine neden olmakla kalmaz, aynı zamanda uygun yazı tiplerini bulma süresi de alır.

Bu gibi durumlarla başa çıkmak için, çalışma kitabınızda hangi yazı tiplerinin kullanıldığını bilmeniz gerekir; Windows ortamında bu yazı tiplerini sisteminize kurabilir veya Windows ya da Linux ortamında yazı tipi dizinine yerleştirebilirsiniz.

C++ ile Aspose.Cells for JavaScript, çalışma kitabınızda veya elektronik tabloda kullanılan tüm fontların listesini döndüren [**Workbook.fonts**](https://reference.aspose.com/cells/javascript-cpp/workbook/#fonts--) metodunu sağlar.

## **Bir Elektronik Tablo veya Çalışma Kitabında Kullanılan Yazı Tiplerinin Listesini Alın**

Aşağıdaki örnek kod, kaynak excel dosyasını yükler ve içinde kullanılan yazı tiplerinin listesini alır. İçinde bazı yanıltıcı yazı tiplerinin bulunduğu sahte bir çalışma sayfası vardır. Kod, çalışma kitabındaki tüm yazı tiplerini yazdırdığında, o sahte yazı tiplerini de yazdırır. Aşağıdaki ekran görüntüsü, [örnek excel dosyasını](25395211.xlsx) ve sahte yazı tiplerinin nasıl listelendiğini gösterir.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Get Fonts Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Get Fonts from Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Get Fonts</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get all the fonts inside the workbook (converted from getFonts())
            const fonts = workbook.fonts;

            // Print all the fonts into the result div
            if (!fonts || fonts.length === 0) {
                document.getElementById('result').innerHTML = '<p>No fonts found in the workbook.</p>';
                return;
            }

            let html = '<h2>Fonts in Workbook</h2><ul>';
            for (let i = 0; i < fonts.length; i++) {
                html += `<li>${fonts[i].toString()}</li>`;
            }
            html += '</ul>';
            document.getElementById('result').innerHTML = html;
        });
    </script>
</html>
```


## **Konsol Çıktısı**



{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
