--- 
title: Экспорт комментариев при сохранении файла Excel в HTML с помощью C++ 
linktitle: Экспорт комментариев при сохранении файла Excel в HTML 
type: docs 
weight: 40 
url: /ru/cpp/export-comments-while-saving-excel-file-to/ 
description: Узнайте, как экспортировать комментарии при сохранении файлов Excel в HTML с помощью Aspose.Cells на C++. 
--- 

## **Возможные сценарии использования**

При сохранении файла Excel в HTML комментарии не экспортируются. Однако Aspose.Cells предоставляет эту возможность с помощью свойства [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). Установив его значение **true**, комментарии, присутствующие в вашем файле Excel, также будут отображаться в HTML.

## **Экспортировать комментарии при сохранении файла Excel в HTML**

Следующий пример кода объясняет использование свойства [**HtmlSaveOptions.IsExportComments**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/isexportcomments/). Скриншот показывает, как влияет установка его значения в **true** на отображение комментариев в HTML. Пожалуйста, скачайте пример файла Excel и сгенерированный HTML для ознакомления.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load sample Excel file
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = sourceDir + u"sampleExportCommentsHTML.xlsx";
    Workbook workbook(inputFilePath);

    // Export comments - set IsExportComments property to true
    HtmlSaveOptions opts;
    opts.SetIsExportComments(true);

    // Save the Excel file to HTML
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outputDir + u"outputExportCommentsHTML.html", opts);

    std::cout << "Excel file exported to HTML with comments successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
