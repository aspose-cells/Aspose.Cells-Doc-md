---
title: Сводная таблица и исходные данные с помощью C++
linktitle: Сводная таблица и исходные данные
type: docs
weight: 30
url: /ru/cpp/pivot-table-and-source-data/
description: Узнайте, как динамически изменять исходные данные сводной таблицы с помощью Aspose.Cells и C++.
---

## **Исходные данные сводной таблицы**

Иногда возникают ситуации, когда вы хотите создать отчеты Microsoft Excel с сводными таблицами, использующими данные из разных источников данных (например, базы данных), которые неизвестны на этапе проектирования. В этой статье представлен подход к динамическому изменению источника данных сводной таблицы.

### **Изменение исходного источника данных сводной таблицы**

1. Создание нового файла шаблона дизайнера.
   1. Создайте новый файл шаблона дизайнера, как показано на скриншоте ниже.
   1. Затем определите именованный диапазон **DataSource**, который ссылается на этот диапазон ячеек.

      **Создание файла шаблона дизайнера и определение именованного диапазона DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Создание сводной таблицы на основе этого именованного диапазона.
   1. В Microsoft Excel выберите **Данные**, затем **Сводная таблица** и **Отчет сводной таблицы и диаграмма**.
   1. Создайте сводную таблицу на основе созданного в первом шаге именованного диапазона.

      **Создание сводной таблицы на основе именованного диапазона DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Перетащите соответствующее поле на строку и столбец сводной таблицы, затем создайте результирующую сводную таблицу, как показано на скриншоте ниже.

   **Создание сводной таблицы на основе соответствующего поля** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Щелкните правой кнопкой мыши на сводной таблице и выберите **Параметры таблицы**.
   1. Установите **Обновлять при открытии** в настройках **Параметры данных**.

      **Настройка параметров сводной таблицы** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Теперь вы можете сохранить этот файл как файл вашего дизайнерского шаблона.

1. Пополнение новыми данными и изменение исходных данных сводной таблицы.
   1. После создания дизайнерского шаблона используйте следующий код для изменения исходных данных сводной таблицы.

Исполнение приведенного ниже примера кода изменяет исходные данные сводной таблицы.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Populating new data to the worksheet cells
    worksheet.GetCells().Get(u"A9").PutValue(u"Golf");
    worksheet.GetCells().Get(u"B9").PutValue(u"Qtr4");
    worksheet.GetCells().Get(u"C9").PutValue(7000);

    // Changing named range "DataSource"
    Range range = worksheet.GetCells().CreateRange(0, 0, 9, 3);
    range.SetName(u"DataSource");

    // Saving the modified Excel file
    U16String outputFilePath = srcDir + u"output.xls";
    workbook.Save(outputFilePath);

    Aspose::Cells::Cleanup();

    std::cout << "File saved successfully!" << std::endl;

    return 0;
}
```
