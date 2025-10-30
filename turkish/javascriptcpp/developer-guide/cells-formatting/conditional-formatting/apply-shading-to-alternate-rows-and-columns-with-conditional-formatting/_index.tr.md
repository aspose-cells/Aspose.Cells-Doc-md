---
title: Koşullu Biçimlendirme ile Sıradaki Satır ve Sütunlara Gölge Uygula
linktitle: Koşullu Biçimlendirme ile Sıradaki Satır ve Sütunlara Gölge Uygula
description: Aspose.Cells kütüphanesini C++ aracılığıyla JavaScript kullanarak, alternans satırlar ve sütunlar için gölgeli koşullu biçimlendirme uygulamada nasıl kullanılır, bu kriterleri ayarlayarak hücrelerin görünümünü ve şeklini daha iyi kontrol edebilirsiniz.
keywords: Aspose.Cells, Koşullu Biçimlendirme, JavaScript aracılığıyla C++, Alternatif Satırlar, Alternatif Sütunlar, Gölgelendirme
type: docs
weight: 30
url: /tr/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Aspose.Cells API'leri, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) nesnesi için koşullu biçimlendirme kurallarını ekleme ve manipulate etme imkanı sağlar. Bu kurallar, istenen biçimlendirmeyi elde etmek için çeşitli şekillerde uyarlanabilir. Bu makale, Aspose.Cells for JavaScript aracılığıyla C++ API'lerini kullanarak, koşullu biçimlendirme kuralları ve Excel'in yerleşik fonksiyonları ile alternatif satır ve sütunlara gölge ekleme yöntemini gösterecektir.

{{% /alert %}}

Bu makale, Excel'in yerleşik işlevleri ROW, COLUMN ve MOD'u kullanmaktadır. İleride sunulan kod örneğini daha iyi anlayabilmek için bu işlevlerin bazı ayrıntıları aşağıda verilmiştir.

- **ROW()** fonksiyonu, bir hücre referansının satır numarasını döner. Referans parametresi belirtilmediyse, fonksiyonun girildiği hücrenin adresi referans alınır.
- **COLUMN()** fonksiyonu, bir hücre referansının sütun numarasını döner. Referans parametresi belirtilmediyse, fonksiyonun girildiği hücrenin adresi referans alınır.
- **MOD()** işlevi, bir sayının bir bölen tarafından bölündükten sonra kalanı döndürür. İşlevin ilk parametresi, kalanını bulmak istediğiniz sayısal değeri, ikinci parametre ise bu sayısal değeri bölmek için kullanılan parametreyi temsil eder. Bölen 0 ise, #DIV/0! hatası döndürür.

Bu hedefe ulaşmak için kod yazmaya başlıyoruz ve bunun için Aspose.Cells for JavaScript aracılığıyla C++ API'sinden yardım alıyoruz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


Aşağıdaki görüntü, Excel uygulamasında yüklenen sonuç elektronik tabloyu göstermektedir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Sıralı sütunlara gölge uygulamak için yapmanız gereken tek şey, **=MOD(ROW(),2)=0** formülünü **=MOD(COLUMN(),2)=0** olarak değiştirmektir; yani, satır dizinini almak yerine formülü sütun dizinine değiştirin.  
Bu durumda elde edilen elektronik tablo aşağıdaki gibi görünecektir.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
