---
title: Получить предупреждения о замене шрифта при рендеринге файла Excel
type: docs
weight: 120
url: /ru/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

Иногда, при рендеринге файлов Microsoft Excel в PDF, Aspose.Cells заменяет шрифты. Aspose.Cells предоставляет функцию, которая позволяет разработчикам узнать, что определенный шрифт был заменен, и выдает предупреждение. Это полезная функция, которая может помочь вам определить, почему PDF-файл, полученный с помощью Aspose.Cells, отличается от фактического файла Excel, и вы сможете принять соответствующие меры. Например, вы можете установить недостающие шрифты, чтобы результаты рендеринга выглядели так же.

Если вы хотите получить предупреждения о замене шрифта при рендеринге файла Excel в PDF, реализуйте интерфейс IWarningCallback и установите метод PdfSaveOptions.setWarningCallback() с вашим реализованным интерфейсом.

{{% /alert %}}

На скриншоте ниже показан исходный файл Excel, используемый в следующем коде. В нем есть текст в ячейках A6 и A7 с шрифтами, которые не отображаются хорошо в Microsoft Excel.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells будет заменять шрифты в ячейках A6 и A7 на подходящие шрифты, как показано ниже.

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **Скачать исходный файл и PDF-файл**

Вы можете скачать исходный файл Excel и PDF-файл по следующим ссылкам

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

Следующий код реализует [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) и устанавливает метод [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) с реализованным интерфейсом. Теперь, когда какой-либо шрифт будет заменен в любой ячейке, Aspose.Cells выдаст предупреждение в методе WarningCallback.warning().

{{< highlight java >}}

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

После преобразования исходного файла на консоль отображаются следующие предупреждения:

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

Если ваша таблица содержит формулы, лучше вызвать метод Workbook.calculateFormula прямо перед рендерингом таблицы в формат PDF. Это обеспечит пересчет зависимых от формул значений и правильное рендеринг значений в PDF. 

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
