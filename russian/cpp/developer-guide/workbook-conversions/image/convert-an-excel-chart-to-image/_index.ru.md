---
title: Преобразовать диаграмму Excel в изображение с помощью C++
linktitle: Конвертировать диаграмму Excel в изображение
type: docs
weight: 20
url: /ru/cpp/convert-an-excel-chart-to-image/
description: Узнайте, как преобразовать диаграммы Excel в изображения с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Диаграммы выглядят привлекательно и позволяют легко видеть сравнения, модели и тенденции в данных. Например, вместо анализа столбцов чисел в листе, диаграмма показывает сразу, падают ли или растут продажи, или как фактические продажи сравниваются с прогнозируемыми. Людям часто нужно представлять статистическую и графическую информацию простым для понимания и удобным в поддержке способом. Изображение помогает.

Иногда диаграммы нужны в приложениях или на веб-страницах. Или они могут потребоваться для документа Word, PDF-файла, презентации PowerPoint или другого приложения. В каждом случае вы хотите отображать диаграмму как изображение, чтобы использовать его в другом месте.

{{% /alert %}}

## **Конвертация диаграмм в изображения**

В приведенных здесь примерах преобразуются круговая диаграмма и столбчатая диаграмма в изображения.

### **Конвертация круговой диаграммы в файл изображения**

Сначала создайте круговую диаграмму в Microsoft Excel, а затем конвертируйте ее в файл изображения с помощью Aspose.Cells. Код в этом примере создает изображение EMF на основе круговой диаграммы в шаблонном файле Microsoft Excel.

|**Результат: изображение круговой диаграммы**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_1.png)|

1. Создайте круговую диаграмму в Microsoft Excel:
   1. Откройте новую книгу в Microsoft Excel.
   1. Введите некоторые данные в лист.
   1. Создайте круговую диаграмму на основе данных.
   1. Сохраните файл.

|**Исходный файл.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_2.png)|

1. Скачайте и установите Aspose.Cells:
   1. [Скачать Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
   1. Установите его на вашем компьютере для разработки.

Все компоненты [Aspose](http://www.aspose.com/) работают в режиме оценки при первой установке. Режим оценки не имеет временных ограничений и вставляет в выходные документы только водяной знак.

1. Создайте проект:
   1. Запустите среду разработки для C++ (например, Visual Studio).
   1. Создайте новое консольное приложение.
   1. Добавьте ссылку на Aspose.Cells. Этот проект использует Aspose.Cells, поэтому добавьте ссылку на библиотеку Aspose.Cells.
   1. Напишите код, который находит и конвертирует диаграмму. Приведен ниже код, используемый компонентом для выполнения задачи. Используется очень немного строк кода.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the pie chart.
    Workbook workbook(srcDir + u"PieChart.xlsx");

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Chart chart = workbook.GetWorksheets().Get(0).GetCharts().Get(0);

    // Convert the chart to an image file.
    chart.ToImage(srcDir + u"PieChart.out.emf", Aspose::Cells::Drawing::ImageType::Emf);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Конвертация столбчатой диаграммы в файл изображения**

Сначала создайте столбцовую диаграмму в Microsoft Excel и преобразуйте ее в файл изображения, как указано выше. После выполнения этого кода создается JPEG-файл на основе столбчатой диаграммы из шаблона файла Excel.

|**Выходной файл: изображение столбчатой диаграммы.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_3.png)|

1. Создайте столбчатую диаграмму в Microsoft Excel:
   1. Откройте новую книгу в Microsoft Excel.
   1. Введите некоторые данные в лист.
   1. Создайте столбчатую диаграмму на основе данных.
   1. Сохраните файл.

|**Входной файл.**|
| :- |
|![todo:image_alt_text](convert-an-excel-chart-to-image_4.png)|

1. Создайте проект с ссылками, как описано выше.
1. Динамически преобразуйте диаграмму в изображение. Ниже приведен используемый компонентом код для выполнения этой задачи. Код аналогичен предыдущему:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the existing excel file which contains the column chart.
    U16String inputFilePath = srcDir + u"ColumnChart.xlsx";
    Workbook workbook(inputFilePath);

    // Get the designer chart (first chart) in the first worksheet of the workbook.
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Chart chart = worksheet.GetCharts().Get(0);

    // Convert the chart to an image file.
    U16String outputImagePath = srcDir + u"ColumnChart.out.jpeg";
    chart.ToImage(outputImagePath, ImageType::Jpeg);

    std::cout << "Chart converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
