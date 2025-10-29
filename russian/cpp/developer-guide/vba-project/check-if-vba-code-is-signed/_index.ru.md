---  
title: Проверьте, подписан ли VBA код с помощью C++  
linktitle: Проверить, подписан ли код VBA  
type: docs  
weight: 100  
url: /ru/cpp/check-if-vba-code-is-signed/  
description: Узнайте, как проверить, подписан ли VBA код в файлах Excel с помощью Aspose.Cells и C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells позволяет проверить, подписан ли проект VBA-кода или нет. Пожалуйста, используйте свойство [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/) для проверки подписи VBA-проекта.  

{{% /alert %}}  

Следующий код объясняет, как проверить, подписан ли VBA-код, с помощью свойства [**VbaProject::IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned/). Вы можете использовать любой файл Excel для тестирования этого кода. Для тестирования можно использовать [этот файл в коде](5115032.xlsm).  

## **Проверьте, подписан ли VBA-код в C++**  

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Check if the VBA code project is signed
    std::wcout << U"Is VBA Code Project Signed: " << workbook.GetVbaProject().IsSigned() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```  

## Вывод в консоль  

Ниже представлен вывод в консоль вышеупомянутого кода с использованием [образцового файла Excel](5115032.xlsm), предоставленного по ссылке.  

{{< highlight java >}}  

Is VBA Code Project Signed: True  

{{< /highlight >}}  
{{< app/cells/assistant language="cpp" >}}
