---
title: 使用 C++ 获取加载Excel文件时的警告
linktitle: 加载Excel文件时获取警告
type: docs
weight: 110
url: /zh/cpp/get-warnings-while-loading-excel-file/
description: 学习如何在使用 Aspose.Cells for C++ 加载Excel文件时捕获和处理警告。
---

## **可能的使用场景**

有时用户尝试加载一个可能已损坏但仍可加载的工作簿。在这种情况下，Aspose.Cells 在加载工作簿时会发出警告。您可以通过实现 [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/) 接口并设置 [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/) 属性来捕获这些警告。

## **加载 Excel 文件时获取警告**

以下示例代码说明如何在加载Excel文件时获取警告。代码加载了一个示例Excel文件（sampleDuplicateDefinedName.xlsx），在加载时会发出 [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/) 警告。该警告由 [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/) 方法捕获，并在控制台打印。之后，将工作簿保存为 [输出Excel文件](outputDuplicateDefinedName.xlsx)。如果用Microsoft Excel打开该示例文件，也会显示相同的警告，如下截图所示。请同时查看下面的控制台输出以获取更多信息。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **示例代码**

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

## **控制台输出**

执行上述代码时，以下是控制台输出的代码，提供了 [示例excel文件](sampleDuplicateDefinedName.xlsx)。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
