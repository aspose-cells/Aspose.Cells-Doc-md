---
title: Получение предупреждений при загрузке файла Excel с помощью C++
linktitle: Получать предупреждения при загрузке файла Excel
type: docs
weight: 110
url: /ru/cpp/get-warnings-while-loading-excel-file/
description: Узнайте, как ловить и обрабатывать предупреждения при загрузке файлов Excel с использованием Aspose.Cells for C++.
---

## **Возможные сценарии использования**

Иногда пользователь пытается загрузить книгу, которая немного повреждена, но всё ещё поддаётся загрузке. В таких случаях Aspose.Cells выводит предупреждения при загрузке книги. Вы можете поймать эти предупреждения, реализовав интерфейс [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/) и установив свойство [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/).

## **Получение предупреждений при загрузке файла Excel**

Следующий пример кода показывает, как получать предупреждения при загрузке файла Excel. Код загружает [образец файла Excel](sampleDuplicateDefinedName.xlsx), на который при загрузке выводится предупреждение [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/). Это предупреждение перехватывается методом [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/), который выводит сообщения в консоль. Затем книга сохраняется как [выходной файл Excel](outputDuplicateDefinedName.xlsx). Если открыть исходный файл в Microsoft Excel, тоже появится это предупреждение, как показано на скриншоте ниже. Также проверьте вывод в консоли из кода для более полного понимания.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class WarningCallback : public IWarningCallback {
public:
    void Warning(WarningInfo& warningInfo) override {
        if (warningInfo.GetType() == ExceptionType::DefinedName) {
            std::cout << "Defined Name Warning: " << warningInfo.GetDescription().ToUtf8() << std::endl;
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    LoadOptions options;
    WarningCallback callback;
    options.SetWarningCallback(&callback);

    U16String inputFilePath = srcDir + u"sampleDuplicateDefinedName.xlsx";
    Workbook book(inputFilePath, options);

    U16String outputFilePath = outDir + u"outputDuplicateDefinedName.xlsx";
    book.Save(outputFilePath);

    std::cout << "Workbook saved successfully with warning handling!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Вывод в консоль**

Ниже приведен вывод консольного вывода вышеуказанного кода при выполнении с предоставленным [образцом файла Excel](sampleDuplicateDefinedName.xlsx).

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
