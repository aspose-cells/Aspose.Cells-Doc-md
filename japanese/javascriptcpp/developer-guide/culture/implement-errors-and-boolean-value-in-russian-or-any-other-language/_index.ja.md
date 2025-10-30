---
title: ロシア語またはその他の言語でエラーとブール値をJavaScript経由でC++で実装する方法を学びます。
linktitle: ロシア語または他の言語でエラーおよび真偽値を実装する
type: docs
weight: 40
url: /ja/javascript-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aspose.Cells for JavaScriptを使用して、異なる言語でエラーとブール値を実装する方法を学びます。 
---

## **可能な使用シナリオ**

Microsoft Excelをロシアロケールまたは言語、その他のロケールや言語で使用している場合、そのロケールや言語に従ったエラーとブール値が表示されます。これと同様の動作は、Aspose.Cells for JavaScriptをC++で使用して[**WorkbookSettings.globalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#globalizationSettings--)プロパティを利用することで実現できます。これには、[**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings)クラスの以下のメソッドをオーバーライドする必要があります。

- [**GlobalizationSettings.errorValueString(string)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#errorValueString-string-)
- [**GlobalizationSettings.booleanValueString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#booleanValueString-boolean-)

## **ロシア語または他の言語でエラーおよび真偽値を実装する**

下記のサンプルコードは、ロシア語または他の言語でのエラーおよび真偽値の実装方法を説明しています。このコードで使用される [サンプルExcelファイル](73990159.xlsx) およびその [出力PDF](73990160.pdf) を確認してください。スクリーンショットは、サンプルExcelファイルと出力PDFの違いを参照用に示しています。

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Russian Globalization Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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

        // Russian Globalization
        class RussianGlobalization extends AsposeCells.GlobalizationSettings {
            errorValueString(err) {
                switch (err.toUpperCase()) {
                    case "#NAME?":
                        return "#RussianName-имя?";
                }
                return "RussianError-ошибка";
            }

            booleanValueString(bv) {
                return bv ? "RussianTrue-правда" : "RussianFalse-ложный";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set GlobalizationSettings in Russian Language
            workbook.settings.globalizationSettings = new RussianGlobalization();

            // Calculate the formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRussianGlobalization.pdf';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
