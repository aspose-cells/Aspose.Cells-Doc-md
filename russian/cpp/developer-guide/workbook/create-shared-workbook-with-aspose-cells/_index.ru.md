---  
title: Создайте совместную рабочую книгу с помощью Aspose.Cells и C++  
linktitle: Создание общей книги с Aspose.Cells  
type: docs  
weight: 40  
url: /ru/cpp/create-shared-workbook-with-aspose-cells/  
description: Узнайте, как создать общую рабочую книгу с помощью Aspose.Cells и C++.  
---  

## **Возможные сценарии использования**  

Microsoft Excel позволяет делиться книгой, как показано на следующем скриншоте. Когда вы делитесь рабочей книгой, более одного пользователя могут ее редактировать в сети. Aspose.Cells позволяет создавать совместную книгу с помощью свойства [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Создание общей книги с Aspose.Cells**  

Следующий пример кода создает совместную книгу, устанавливая свойство [**Workbook.GetShared()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshared/) в значение **true**. Открыв [выходной файл Excel](55541786.xlsx) в Microsoft Excel, вы увидите указание **Shared** рядом с именем файла, как показано на скриншоте.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **Образец кода**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create Workbook object
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>();

    // Share the Workbook
    wb->GetSettings().SetShared(true);

    // Save the Shared Workbook
    wb->Save(u"outputSharedWorkbook.xlsx");

    std::cout << "Shared workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
