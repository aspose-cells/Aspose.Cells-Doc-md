---
title: Получение предупреждений о замене шрифта при рендеринге файла Excel
type: docs
weight: 120
url: /ru/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

Иногда при рендеринге Microsoft файлов Excel в PDF Aspose.Cells заменяет шрифты. Aspose.Cells предоставляет функцию, которая позволяет разработчикам узнать, что конкретный шрифт был заменен, выдав предупреждение. Это полезная функция, которая может помочь вам определить, почему Aspose.Cells визуализированный PDF отличается от фактического файла Excel, и вы можете предпринять соответствующие действия. Например, вы можете установить отсутствующие шрифты, чтобы результаты рендеринга выглядели одинаково.

Если вы хотите получать предупреждения о замене шрифта при рендеринге файла Excel на PDF, реализуйте интерфейс IWarningCallback и задайте метод PdfSaveOptions.setWarningCallback() с вашим реализованным интерфейсом.

{{% /alert %}}

На снимке экрана ниже показан исходный файл Excel, используемый в следующем коде. В ячейках A6 и A7 есть некоторый текст со шрифтами, которые плохо отображаются в Microsoft Excel.

![дело:изображение_альтернативный_текст](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells заменит шрифты в ячейках A6 и A7 подходящими шрифтами, как показано ниже.

![дело:изображение_альтернативный_текст](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Скачать исходный файл и вывод PDF**

Вы можете скачать исходный файл Excel и вывод PDF по следующим ссылкам.

- [источник.xlsx](5472700.xlsx)
- [вывод.pdf](5472699.pdf)

 Следующий код реализует[**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) и установите[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) метод с реализованным интерфейсом. Теперь всякий раз, когда какой-либо шрифт будет заменен в любой ячейке, Aspose.Cells вызовет предупреждение внутри метода WarningCallback.warning().

{{< highlight "java" >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **Вывод предупреждений**

После преобразования исходного файла в консоль отладки выводятся следующие предупреждения:

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

 Если ваша электронная таблица содержит формулы, лучше всего вызывать метод Workbook.calculateFormula непосредственно перед визуализацией электронной таблицы в формате PDF. Это обеспечит пересчет значений, зависящих от формулы, и отображение правильных значений в файле PDF.

{{% /alert %}}
