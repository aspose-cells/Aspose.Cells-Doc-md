---
title: Задание пользовательских разделителей десятичных и групповых чисел для рабочей книги с помощью C++
linktitle: Задание пользовательских разделителей десятичных и групповых чисел
type: docs
weight: 110
url: /ru/cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Изменение разделителя десятичных и групповых чисел в MS Excel и с помощью кода C++, используя API Aspose.Cells for C++.
keywords: указать пользовательский разделитель десятичной части для excel, указать пользовательский разделитель десятичной части для excel c++, указать пользовательский групповой разделитель excel, указать пользовательский групповой разделитель excel c++, указать пользовательский разделитель decimal и group для excel, указать пользовательский разделитель decimal и group для excel c++, изменить разделитель decimal и group в excel, изменить разделитель decimal в excel, изменить разделитель group в excel, изменить разделитель decimal в excel c++, изменить разделитель group в excel c++
---

{{% alert color="primary" %}}

В Microsoft Excel вы можете указать пользовательские разделители десятичной точки и тысячи вместо использования системных разделителей из **Расширенных опций Excel**, как показано на скриншоте ниже.

Aspose.Cells предоставляет свойства [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumberdecimalseparator/) и [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) для установки пользовательских разделителей для форматирования/разбора чисел.

{{% /alert %}}

## **Указание пользовательских разделителей, используя Microsoft Excel**

На следующем скриншоте показаны **Расширенные параметры Excel** и выделена секция для указания **Пользовательских разделителей**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Указание пользовательских разделителей с использованием Aspose.Cells**

Приведенный ниже образец кода иллюстрирует, как указать пользовательские разделители с помощью API Aspose.Cells. Он указывает пользовательские разделители для десятичных и групповых чисел как точку и пробел соответственно.

### Код C++ для задания пользовательских разделителей чисел с десятичной точкой и группировкой

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Specify custom separators
    workbook.GetSettings().SetNumberDecimalSeparator(u'.');
    workbook.GetSettings().SetNumberGroupSeparator(u' ');

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set cell value
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(123456.789);

    // Set custom cell style
    Style style = cell.GetStyle();
    style.SetCustom(u"#,##0.000;[Red]#,##0.000", true);
    cell.SetStyle(style);

    // Auto-fit columns
    worksheet.AutoFitColumns();

    // Save workbook as PDF
    workbook.Save(outDir + u"CustomSeparator_out.pdf");

    std::cout << "Workbook saved successfully with custom separators!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
