---
title: Получить предупреждения о заменах шрифтов при рендеринге файла Excel в C++
linktitle: Получить предупреждения о замещениях шрифтов
type: docs
weight: 230
url: /ru/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Узнайте, как получать предупреждения о замещениях шрифтов при рендеринге файлов Excel в PDF с помощью Aspose.Cells и C++.
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

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GetWarningsForFontSubstitution : public IWarningCallback
{
public:
    void Warning(WarningInfo& info) override
    {
        if (info.GetType() == ExceptionType::FontSubstitution)
        {
            std::cout << "WARNING INFO: " << info.GetDescription().ToUtf8() << std::endl;
        }
    }

    static void Run()
    {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");
        Workbook workbook(srcDir + u"source.xlsx");
        PdfSaveOptions options;
        auto callback = std::make_shared<GetWarningsForFontSubstitution>();
        options.SetWarningCallback(callback.get());
        workbook.Save(outDir + u"output_out.pdf", options);
        std::cout << "PDF saved successfully with font substitution warnings!" << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();
    GetWarningsForFontSubstitution::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод**
После преобразования исходного файла Excel в PDF, предупреждения выводятся в отладочной консоли следующим образом:

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

Если в вашей таблице есть формулы, лучше вызвать метод `Workbook.CalculateFormula` прямо перед рендерингом таблицы в формат PDF. Это обеспечит пересчет значений, зависящих от формул, и правильное отображение значений в PDF.

{{% /alert %}}
