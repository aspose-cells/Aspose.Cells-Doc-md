---
title: 用 C++ 将 JSON 转换为 CSV
linktitle: 将JSON转换为CSV
type: docs
weight: 210
url: /zh/cpp/convert-json-to-csv/
description: 学习如何使用 Aspose.Cells for C++ 结合简单和嵌套的 JSON 示例将 JSON 转换为 CSV。
---

## **将JSON转换为CSV**

 Aspose.Cells 支持将简单和嵌套的 JSON 转换为 CSV。为此，API 提供了 [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) 和 [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) 类。[**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) 类提供 JSON 排版的选项，例如 [**SetIgnoreTitle**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/setignoretitle/)（如果数组是对象的属性，则忽略标题）或 [**GetArrayAsTable()**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/getarrayastable/)（将数组作为表处理）。[**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) 类使用 [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) 类设置的排版选项处理 JSON。

 以下代码示例演示了如何使用 [**JsonLayoutOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonlayoutoptions/) 和 [**JsonUtility**](https://reference.aspose.com/cells/cpp/aspose.cells.utility/jsonutility/) 类加载 [源 JSON 文件](104398869.json)，并生成 [输出 CSV 文件](104398870.csv)。

### **示例代码**

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String jsonFilePath = srcDir + u"SampleJson.json";
    U16String jsonData;
    std::ifstream jsonFile(jsonFilePath.ToUtf8().c_str());
    if (jsonFile.is_open())
    {
        std::stringstream buffer;
        buffer << jsonFile.rdbuf();
        jsonData = U16String(buffer.str().c_str());
        jsonFile.close();
    }
    else
    {
        std::cerr << "Failed to open JSON file: " << jsonFilePath.ToUtf8().c_str() << std::endl;
        return -1;
    }

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    JsonLayoutOptions importOptions;
    importOptions.SetConvertNumericOrDate(true);
    importOptions.SetArrayAsTable(true);
    importOptions.SetIgnoreTitle(true);

    JsonUtility::ImportData(jsonData, cells, 0, 0, importOptions);

    U16String outputFilePath = outDir + u"SampleJson_out.csv";
    workbook.Save(outputFilePath);

    std::cout << "JSON data imported and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
