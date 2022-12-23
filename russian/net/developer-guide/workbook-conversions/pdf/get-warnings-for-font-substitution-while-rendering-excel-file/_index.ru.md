---
title: Получение предупреждений о замене шрифта при рендеринге файла Excel
type: docs
weight: 230
url: /ru/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

Иногда при рендеринге файла Excel Microsoft в PDF Aspose.Cells заменяет шрифты. Aspose.Cells предоставляет функцию, которая позволяет разработчикам узнать, какой конкретный шрифт был заменен, с помощью предупреждения. Это полезная функция, которая может помочь вам определить, почему Aspose.Cells визуализированный файл PDF отличается от исходного файла Excel Microsoft, чтобы вы могли предпринять соответствующие действия. Например, установка отсутствующих шрифтов, чтобы результаты рендеринга выглядели одинаково.

{{% /alert %}} 

Чтобы получать предупреждения о замене шрифта при отображении файлов Excel на PDF, реализуйте интерфейс IWarningCallback и задайте свойство PdfSaveOptions.WarningCallback с реализованным интерфейсом.

На снимке экрана ниже показан исходный файл Excel, который мы будем использовать в следующем коде. В ячейках A6 и A7 есть некоторый текст со шрифтами, которые не отображаются нормально в Microsoft Excel.

|**Не все шрифты отображаются правильно**|
|:- |
|![дело:изображение_альтернативный_текст](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells заменит шрифты в ячейках A6 и A7 подходящими шрифтами, как показано ниже.

|**Заменяемые шрифты**|
|:- |
|![дело:изображение_альтернативный_текст](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **Скачать исходный файл и вывод PDF**
Вы можете скачать исходный файл Excel и вывод PDF по следующим ссылкам.

- [источник.xlsx](5112611.xlsx)
- [вывод.pdf](5112616.pdf)
## **Код**
Следующий код реализует IWarningCallback и устанавливает свойство PdfSaveOptions.WarningCallback с реализованным интерфейсом. Теперь всякий раз, когда какой-либо шрифт будет заменен в любой ячейке, Aspose.Cells вызовет предупреждение внутри метода WarningCallback.Warning().



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **Вывод**
После преобразования исходного файла Excel в PDF предупреждения выводятся в консоль отладки следующим образом:

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

Если ваша электронная таблица содержит формулы, лучше всего вызывать метод Workbook.CalculateFormula непосредственно перед визуализацией электронной таблицы в формате PDF. Это обеспечит пересчет значений, зависящих от формулы, и отображение правильных значений в файле PDF.

{{% /alert %}}
