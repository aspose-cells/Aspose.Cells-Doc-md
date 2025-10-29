---
title: Получать предупреждения о замене шрифтов при рендеринге Excel файла с помощью Golang через C++
linktitle: Получить предупреждения о замещениях шрифтов
type: docs
weight: 230
url: /ru/go-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Узнайте, как получать предупреждения о замене шрифтов при рендеринге Excel файлов в PDF с помощью Aspose.Cells и Golang через C++.
---

{{% alert color="primary" %}}

Иногда, когда рендерится файл Microsoft Excel в PDF, Aspose.Cells заменяет шрифты. Aspose.Cells предоставляет функцию, которая позволяет разработчикам узнать, какой конкретный шрифт был заменен, запуская предупреждение. Это полезная функция, которая поможет вам определить, почему рендеринг PDF, выполненный Aspose.Cells, выглядит иначе, чем оригинальный файл Microsoft Excel, чтобы вы могли предпринять соответствующие действия. Например установить недостающие шрифты, и таким образом достичь одинакового внешнего вида.

{{% /alert %}}

Для получения предупреждений о замещениях шрифтов при преобразовании Excel в PDF реализуйте интерфейс `IWarningCallback` и установите свойство `PdfSaveOptions.WarningCallback` вашим реализованным интерфейсом.

Скриншот ниже показывает исходный файл Excel, который мы будем использовать в следующем коде. В нем есть текст в ячейках A6 и A7 шрифтом, который неправильно отображается в Microsoft Excel.

|**Не все шрифты отображаются правильно**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cells будет заменять шрифты в ячейках A6 и A7 на подходящие шрифты, как показано ниже.

|**Замененные шрифты**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **Скачать исходный файл и PDF-файл**
Вы можете скачать исходный файл Excel и итоговый PDF по следующим ссылкам:

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **Код**
Следующий код реализует `IWarningCallback` и устанавливает свойство `PdfSaveOptions.WarningCallback` в реализованный интерфейс. Теперь, если любой шрифт будет заменен в любой ячейке, Aspose.Cells вызовет предупреждение внутри метода `WarningCallback.Warning()`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWarningsForFontSubstitutionWhileRenderingExcelFile.go" >}}
## **Вывод**
После преобразования исходного файла Excel в PDF, предупреждения выводятся в отладочной консоли следующим образом:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Если в вашей таблице есть формулы, лучше вызвать метод `Workbook.CalculateFormula` прямо перед рендерингом таблицы в формат PDF. Это обеспечит пересчет значений, зависящих от формул, и правильное отображение значений в PDF.

{{% /alert %}}
