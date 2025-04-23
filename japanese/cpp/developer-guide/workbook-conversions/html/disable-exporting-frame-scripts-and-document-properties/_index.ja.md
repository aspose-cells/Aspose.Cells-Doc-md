---
title: フレームスクリプトとドキュメントプロパティのエクスポートをＣ++で無効にする
type: docs
weight: 310
url: /ja/cpp/disable-exporting-frame-scripts-and-document-properties/
description: Aspose.Cellsを使用してフレームスクリプトとドキュメントプロパティのエクスポートを無効にします。
---

{{% alert color="primary" %}}

Aspose.CellsはワークブックをHTMLに変換する際にフレームスクリプトとドキュメントプロパティをエクスポートします。バージョン8.6.0のAspose.Cells for C++では、これらのエクスポートをオプションで無効にできる設定を追加しています。HtmlSaveOptions.ExportFrameScriptsAndPropertiesプロパティを使用してください。

{{% /alert %}}

## **フレームスクリプトとドキュメントプロパティのエクスポートを無効にする**

以下のサンプルコードを使用すると、フレームスクリプトとドキュメントプロパティのエクスポートを無効にできます。ワークブックをHTMLに変換すると、出力ファイルにフレームスクリプトとドキュメントプロパティは含まれません。

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

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
