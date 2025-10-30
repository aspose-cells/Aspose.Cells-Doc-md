---
title: Hücre Değerinin veya Aralığının Tek Tek Tırnak Önekini Koru
type: docs
weight: 310
url: /tr/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Hücre veya Aralıktaki Tek Tırnak Önekiyi Koruma konusunda Aspose.Cells for JavaScript C++ API sini kullanmayı öğrenin.
keywords: Hücre veya Aralık Tek Tırnak Önekiyi Koruma JavaScript C++, önde gelen ünlem veya tek tırnak karakterini gizleme JavaScript C++, önde gelen ünlem veya tek tırnak karakterini gösterme JavaScript C++ ile
---

## **Olası Kullanım Senaryoları**

Önde gelen tek tırnak ya da tek tırnak işaretli bir hücreye bir değer koyduğunuzda, Microsoft Excel bunu gizler, ancak hücreyi seçtiğinizde, önde gelen tek tırnak ya da tek tırnak işaretini aşağıdaki ekran görüntüsünde gösterildiği gibi bir formül çubuğunda görüntüler.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for JavaScript C++ ayrıca, Microsoft Excel gibi önde gelen ünlem veya tek tırnakı gizler, ancak bu hücrenin [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) değerini **true** olarak ayarlar. Hücrenin boş bir stili ayarlarsanız, o zaman [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) tekrar **false** olur. Bu sorunla başa çıkmak için Aspose.Cells for JavaScript C++ [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) özelliğini sağlar. Bu özellik **false** olarak ayarlandığında, [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) hiç güncellenmez ve eski değeri korunur. Bu, eğer [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--)'ün eski değeri **true** ise, **true** olarak kalacaktır ve eski değeri **false** ise, **false** kalacaktır.

## **Hücre Değerinin veya Aralığın Ön Eklemesini Koruma**

Aşağıdaki örnek kod yukarıda anlatılan [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) kullanımını açıklar. Lütfen kod içindeki yorumları okuyun ve aşağıdaki kodun konsol çıktısına bakarak daha fazla yardım alın.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells QuotePrefix Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>QuotePrefix Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const outputLines = [];

            // Create workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell A1
            const cell = ws.cells.get("A1");

            // Put some text in cell, it does not have Single Quote at the beginning
            cell.value = "Text";

            // Access style of cell A1
            let st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Put some text in cell, it has Single Quote at the beginning
            cell.value = "'Text";

            // Access style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Print information about StyleFlag.QuotePrefix property
            outputLines.push("");
            outputLines.push("When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.");
            outputLines.push("Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.");
            outputLines.push("");

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as false
            // It means, we do not want to update the Style.QuotePrefix property of cell A1's style.
            let flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = false;

            // Create a range consisting of single cell A1
            const rng = ws.cells.createRange("A1");

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print True, because we have not updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as true
            // It means, we want to update the Style.QuotePrefix property of cell A1's style.
            flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = true;

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print False, because we have updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Update result div
            resultDiv.innerHTML = "<pre>" + outputLines.join("\n") + "</pre>";

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```



## **Konsol Çıktısı**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
