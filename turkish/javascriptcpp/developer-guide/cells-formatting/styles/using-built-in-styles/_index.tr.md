---
title: Dahili Stiller Kullanma
linktitle: Dahili Stiller Kullanma
type: docs
weight: 80
url: /tr/javascript-cpp/using-built-in-styles/
description: Excel yerleşik stillerini C++ aracılığıyla kullanmak için JavaScript kodu.
keywords: JavaScript, Excel yerleşik stillerini kullanır, JavaScript ile çalışma kitabında stilleri programlı olarak uygular, çalışma kitabında stilleri programlı olarak uygular, JavaScript Excel de yerleşik stilleri uygular, JavaScript ile çalışma kitabında yerleşik stilleri uygular, JavaScript kodu çalışma kitabında yerleşik stilleri uygular, JavaScript kodu Excel çalışma kitabında yerleşik stilleri uygular
---

{{% alert color="primary" %}}  
Aspose.Cells, bir elektronik tablo belgesinde bir hücreyi biçimlendirmek için geniş bir koleksiyon sunar. Hazır stilleri çalışma kitabımızda kullanabilir ve aynı zamanda özel stiller oluşturabiliriz.  
{{% /alert %}}  

## **Dahili Stilleri Nasıl Kullanılır**  

[**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) yöntemi ve [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) numaralı numaralaması yerleşik stilleri kullanmayı kolaylaştırır. İşte tüm olası yerleşik stiller listesi:  

- YirmiYüzdeVurgu1
- YirmiYüzdeVurgu2
- YirmiYüzdeVurgu3
- YirmiYüzdeVurgu4
- YirmiYüzdeVurgu5
- YirmiYüzdeVurgu6
- KırkYüzdeVurgu1
- KırkYüzdeVurgu2
- KırkYüzdeVurgu3
- KırkYüzdeVurgu4
- KırkYüzdeVurgu5
- KırkYüzdeVurgu6
- AltmışYüzdeVurgu1
- AltmışYüzdeVurgu2
- AltmışYüzdeVurgu3
- AltmışYüzdeVurgu4
- AltmışYüzdeVurgu5
- AltmışYüzdeVurgu6
- Vurgu1
- Vurgu2
- Vurgu3
- Vurgu4
- Vurgu5
- Vurgu6
- Kötü
- Hesaplama
- KontrolHücre
- Virgül
- Virgül1
- Para Birimi
- Para Birimi1
- AçıklayıcıMetin
- İyi
- Başlık1
- Başlık2
- Başlık3
- Başlık4
- Kısayol
- TakipEdilenKöprüleşke
- Girdi
- BağlantılıHücre
- Nötr
- Normal
- Not
- Çıktı
- Yüzde
- Başlık
- Toplam
- UyarıMetni
- SatırDüzeyi
- SütunDüzeyi


## JavaScript kodu ile yerleşik stilleri kullanma  
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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();

            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;

            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);

            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';

            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```
