---
title: Получить предупреждения о замещении шрифтов при рендеринге файла Excel с помощью JavaScript через C++
linktitle: Получить предупреждения о замене шрифта при рендеринге файла Excel
type: docs
weight: 230
url: /ru/javascript-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Узнайте, как получать предупреждения о замещении шрифтов при рендеринге файлов Excel в PDF с помощью Aspose.Cells for JavaScript через C++.
---

{{% alert color="primary" %}}  

Иногда, когда рендерится файл Microsoft Excel в PDF, Aspose.Cells заменяет шрифты. Aspose.Cells предоставляет функцию, которая позволяет разработчикам узнать, какой конкретный шрифт был заменен, запуская предупреждение. Это полезная функция, которая поможет вам определить, почему рендеринг PDF, выполненный Aspose.Cells, выглядит иначе, чем оригинальный файл Microsoft Excel, чтобы вы могли предпринять соответствующие действия. Например установить недостающие шрифты, и таким образом достичь одинакового внешнего вида.

{{% /alert %}}  

Чтобы получать предупреждения о замене шрифтов при рендеринге Excel в PDF, реализуйте интерфейс IWarningCallback и установите свойство PdfSaveOptions.warningCallback вашим реализованным интерфейсом.

Скриншот ниже показывает исходный файл Excel, который мы будем использовать в следующем коде. В нем есть текст в ячейках A6 и A7 шрифтом, который неправильно отображается в Microsoft Excel.

|**Не все шрифты отображаются правильно**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells будет заменять шрифты в ячейках A6 и A7 на подходящие шрифты, как показано ниже.

|**Замененные шрифты**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Скачать исходный файл и PDF-файл**  
Вы можете скачать исходный файл Excel и PDF-файл по следующим ссылкам

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Код**  
Следующий код реализует IWarningCallback и устанавливает свойство PdfSaveOptions.warningCallback реализованным интерфейсом. Теперь, когда любой шрифт будет заменен в любой ячейке, Aspose.Cells вызовет предупреждение внутри метода WarningCallback.Warning().

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - GetWarningsForFontSubstitution</title>
    </head>
    <body>
        <h1>GetWarningsForFontSubstitution Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

        class GetWarningsForFontSubstitution {
            static warning(info) {
                if (info.type === AsposeCells.WarningType.FontSubstitution) {
                    console.log("WARNING INFO: " + info.description);
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare PDF save options and assign warning callback
            const options = new PdfSaveOptions();
            options.warningCallback = GetWarningsForFontSubstitution;

            // Save workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  
## **Вывод**  
После преобразования исходного файла Excel в PDF, предупреждения выводятся в отладочной консоли следующим образом:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Если ваша таблица содержит формулы, лучше вызвать метод Workbook.calculateFormula прямо перед рендерингом таблицы в формат PDF. Это обеспечит пересчет зависимых от формул значений и правильное рендеринг значений в PDF.

{{% /alert %}}
