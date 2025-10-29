---  
title: Получить предупреждения о замене шрифтов при рендеринге файла Excel через Node.js и C++  
linktitle: Получить предупреждения о замене шрифта при рендеринге файла Excel  
type: docs  
weight: 230  
url: /ru/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/  
description: Узнайте, как получать предупреждения о замене шрифтов при рендеринге Excel в PDF с помощью Aspose.Cells for Node.js via C++.  
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

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class GetWarningsForFontSubstitution {
static warning(info) {
if (info.getType() === AsposeCells.WarningType.FontSubstitution) {
console.log("WARNING INFO: " + info.getDescription());
}
}

static run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setWarningCallback(GetWarningsForFontSubstitution);
const outputFilePath = path.join(dataDir, "output_out.pdf");
workbook.save(outputFilePath, options);
}
}
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

{{< app/cells/assistant language="nodejs-cpp" >}}
