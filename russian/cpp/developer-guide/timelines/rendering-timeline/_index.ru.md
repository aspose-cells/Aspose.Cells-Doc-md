---
title: Отрисовка временной шкалы с помощью C++
type: docs
weight: 40
url: /ru/cpp/rendering-timeline/
description: Управляйте временными шкалами Excel файлов с помощью Aspose.Cells и C++.
keywords: Преобразование временной шкалы без использования Office 2013, Office 2016, Office 2019 и Office 365
---

## **Возможные сценарии использования**
Aspose.Cells поддерживает визуализацию временной шкалы без использования office 2013, office 2016, office 2019 и office 365. Если вы конвертируете свой лист в изображение или сохраняете свою книгу в форматах PDF или HTML, то вы увидите, что временные шкалы визуализированы правильно.

## **Визуализация временной шкалы**
В следующем образце кода загружается [образец Excel-файла](input.xlsx), содержащий существующую временную шкалу. Получите объект формы по имени временной шкалы, а затем визуализируйте его в виде изображения через метод Shape.ToImage(). Полученное изображение - это [выходное изображение](out.png), которое показывает визуализированную временную шкалу. Как видите, временная шкала была правильно визуализирована и выглядит так же, как в образцовом Excel-файле.

![todo:image_alt_text](out.png)
### **Образец кода**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing timeline.
    Workbook workbook(u"input.xlsx");

    // Access second worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(1);

    // Access the first Timeline inside the worksheet.
    Timeline timeline = sheet.GetTimelines().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    // Get timeline shape object by timeline's name
    Shape timeLineShape = sheet.GetShapes().Get(timeline.GetName());

    // Save the timeline as an image
    timeLineShape.ToImage(u"out.png", options);

    std::cout << "Timeline image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
