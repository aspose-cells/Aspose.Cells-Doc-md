---
title: İngilizce veya başka bir dilde Hatalar ve Boolean Değeri uygulamak için JavaScript ile C++ kullanın
linktitle: Rusça veya başka bir dilde Hataları ve Boolean Değerleri Uygulayın
type: docs
weight: 40
url: /tr/javascript-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Farklı dillerde Hatalar ve Boolean değerlerini Aspose.Cells for JavaScript C++ ile nasıl uygulayacağınızı öğrenin. 
---

## **Olası Kullanım Senaryoları**

Eğer Microsoft Excel'i Rusça Yerel veya Dil veya başka herhangi bir Yerel veya Dilde kullanıyorsanız, Hatalar ve Boolean değerleri o Yerel veya Dil'e göre görüntülenir. Bunu Aspose.Cells for JavaScript C++ kullanarak [**WorkbookSettings.globalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#globalizationSettings--) özelliği ile benzer bir davranış yakalayabilirsiniz. [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings) sınıfının aşağıdaki metodlarını geçersiz kılmanız gerekir.

- [**GlobalizationSettings.errorValueString(string)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#errorValueString-string-)
- [**GlobalizationSettings.booleanValueString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#booleanValueString-boolean-)

## **Rusça veya Başka Bir Dilde Hataları ve Boolean Değerleri Uygulayın**

Aşağıdaki örnek kod, Rusça veya başka bir dilde Hataları ve Boolean Değerleri nasıl uygulayacağınızı göstermektedir. Bu kodda kullanılan bu [Örnek Excel Dosyasını](73990159.xlsx) ve [Çıktı PDF](73990160.pdf) dosyasını kontrol edin. Ekran görüntüsü, Örnek Excel Dosyası ile Çıktı PDF arasındaki farkı göstermektedir.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Örnek Kod**

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
