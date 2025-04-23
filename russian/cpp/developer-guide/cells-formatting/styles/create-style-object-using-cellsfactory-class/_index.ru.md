---  
title: Создание объекта стиля с помощью класса CellsFactory на C++  
description: Aspose.Cells — это библиотека на C++ для работы с файлами электронных таблиц, которая предоставляет объект стиля для оформления ячеек. В этой статье будет рассказано, как создать объект стиля ячейки с помощью класса CellsFactory в библиотеке Aspose.Cells, чтобы пользователи могли настраивать внешний вид ячеек по необходимости.  
keywords: Aspose.Cells, библиотека C++, электронная таблица, объект стиля, стиль ячейки, настройка  
type: docs  
weight: 70  
url: /ru/cpp/create-style-object-using-cellsfactory-class/  
---  

## **Создайте объект стиля с использованием класса CellsFactory.**  
Следующий пример кода создает объект [Style](https://reference.aspose.com/cells/cpp/aspose.cells/style) с помощью [CellsFactory](https://reference.aspose.com/cells/cpp/aspose.cells/cellsfactory), а затем устанавливает Объект Стиля по умолчанию для рабочей книги. Загрузите [выходной файл excel](5115153.xlsx), чтобы ознакомиться с результатами этого кода.  

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

    // Create a Style object using CellsFactory class
    CellsFactory cf;
    Style st = cf.CreateStyle();

    // Set the Style fill color to Yellow
    st.SetPattern(BackgroundType::Solid);
    st.SetForegroundColor(Color::Yellow());

    // Create a workbook and set its default style using the created Style object
    Workbook wb;
    wb.SetDefaultStyle(st);

    // Save the workbook
    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
