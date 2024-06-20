---
title: Получить предупреждения о замене шрифта при рендеринге файла Excel
type: docs
weight: 230
url: /ru/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

Иногда, когда рендерится файл Microsoft Excel в PDF, Aspose.Cells заменяет шрифты. Aspose.Cells предоставляет функцию, которая позволяет разработчикам узнать, какой конкретный шрифт был заменен, запуская предупреждение. Это полезная функция, которая поможет вам определить, почему рендеринг PDF, выполненный Aspose.Cells, выглядит иначе, чем оригинальный файл Microsoft Excel, чтобы вы могли предпринять соответствующие действия. Например установить недостающие шрифты, и таким образом достичь одинакового внешнего вида.

{{% /alert %}} 

Для получения предупреждений о замене шрифтов при рендеринге файлов Excel в PDF реализуйте интерфейс IWarningCallback и установите свойство PdfSaveOptions.WarningCallback соответствующим образом.

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
Следующий код реализует интерфейс IWarningCallback и устанавливает свойство PdfSaveOptions.WarningCallback соответствующим образом. Теперь, когда любой шрифт будет заменен в любой ячейке, Aspose.Cells будет запускать предупреждение в методе WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Вывод**
После преобразования исходного файла Excel в PDF, предупреждения выводятся в отладочной консоли следующим образом:

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Если ваш электронный таблицы содержит формулы, лучше вызвать метод CalculateFormula книги прямо перед рендерингом электронной таблицы в формат PDF. Это гарантирует пересчет значений, зависящих от формул, и правильный вывод значений в PDF.

{{% /alert %}}
