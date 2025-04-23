---
title: ExcelをJSONに変換(C++)
linktitle: ExcelをJSONに変換します。
type: docs
weight: 300
url: /ja/cpp/convert-excel-to-json/
description: C++を使用してExcelファイルをJSONに変換する方法を学びます。
keywords: Office 2013、Office 2016、Office 2019、およびOffice 365なしでブックをJSONにエクスポートする
---

{{% alert color="primary" %}}

Aspose.CellsはワークブックをJson(JavaScript Object Notation)ファイルに変換することをサポートしています。

{{% /alert %}}

## **ExcelワークブックをJSONに変換**

ExcelブックをJSONに変換する方法に関する最良のソリューションがAspose.Cells for C++ライブラリにあります。APIはスプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)メソッドの第2引数に[**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/)を渡します。また、[**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/)クラスを使用して追加設定も可能です。

次のコード例は、ExcelワークブックをJSONにエクスポートする例です。[ソースファイル](sample.xlsx)の変換に使用したコード例も参考にしてください。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

次のコード例では、JsonSaveOptionsクラスを使用して追加設定を行い、ExcelワークブックをJSONにエクスポートします。[ソースファイル](sample.xlsx)をJSONファイルに変換する例も参照してください。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

