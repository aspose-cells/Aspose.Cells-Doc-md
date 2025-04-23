---
title: Преобразование числовых данных в текстовом виде в число с помощью C++
linktitle: Преобразовать текстовые числовые данные в число
type: docs
weight: 900
url: /ru/cpp/convert-text-numeric-data-to-number/
description: Узнайте, как преобразовать числа, сохраненные как текст в Excel, в числа с помощью API Aspose.Cells for C++.
keywords: преобразование текста в число в Excel, преобразование текста в число в C++, преобразование числовых данных в текст, преобразование числовых данных в текст C++, преобразование числового текста в число, преобразование числового текста в число C++, преобразование числового текста в число с C++, преобразование числового текста в число в Excel с C++, преобразование числового текста в число в Excel с C++, преобразование числовой строки в число в Excel с C++, преобразование числовых данных Excel в число, преобразование числовой строки в число C++
---

## **Возможные сценарии использования**
Иногда вы хотите преобразовать числовые данные, введенные как текст, в числа. Вы можете вводить числа как текст в Microsoft Excel, поставив апостроф перед числом, например **'12345**. Затем Excel обрабатывает число как строку. Aspose.Cells позволяет вам преобразовывать строки в числа.

## Как преобразовать числа, хранящиеся как текст, в числа в Excel
Вы можете преобразовать числа, хранящиеся как текст, в числа, следуя нескольким простым шагам.
1. Выберите любую одиночную ячейку или диапазон ячеек, у которых есть индикатор ошибки в верхнем левом углу.
1. Рядом с выбранной ячейкой или диапазоном ячеек нажмите кнопку ошибки, которая появляется. В меню щелкните Преобразовать в число. 
<br>
<img src="4.png" width=70% />
1. Если кнопка предупреждения недоступна, выберите столбец с этой проблемой. Если вы не хотите преобразовать весь столбец, вы можете выбрать одну или несколько ячеек. Убедитесь, что выбранные вами ячейки находятся в одном столбце, иначе этот процесс не сработает. Кнопка Текст в столбцах обычно используется для разделения столбца, но ее также можно использовать для преобразования одного столбца текста в числа. На вкладке Данные щелкните Текст в столбцах.
<br>
<img src="1.png" width=70% />
1. Щелкните кнопку Завершить во всплывающем окне.
<br>
<img src="2.png" width=70% />
1. Числа, сохраненные как текст, преобразуются в числа.
<br>
<img src="3.png" width=70% />

## Как преобразовать числа, сохраненные как текст, в числа с помощью Aspose.Cells for C++
Aspose.Cells предоставляет метод [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/), который может быть использован для преобразования всех строковых или текстовых числовых данных в числа.

На следующем снимке экрана показаны строковые числа в ячейках **A1:A17**. Строковые числа выровнены влево.
<br>
<img src="5.png" width=70% />

Эти строковые числа были преобразованы в числа с использованием [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/convertstringtonumericvalue/) на следующем скриншоте. Как вы можете видеть, они теперь выровнены по правому краю.
<br>
<img src="6.png" width=70% />

## Код C++ для преобразования строковых числовых данных в реальные числа

Следующий образец кода показывает, как преобразовать все строковые числовые данные в фактические числа во всех листах книги.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate workbook object with an Excel file
    U16String inputFilePath = srcDir + u"SampleBook.xlsx";
    Workbook workbook(inputFilePath);

    // Iterate through all worksheets and convert string values to numeric
    for (int32_t i = 0; i < workbook.GetWorksheets().GetCount(); i++)
    {
        workbook.GetWorksheets().Get(i).GetCells().ConvertStringToNumericValue();
    }

    // Save the Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
