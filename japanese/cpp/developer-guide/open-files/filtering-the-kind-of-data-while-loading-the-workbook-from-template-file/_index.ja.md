---
title: C++を使ったテンプレートファイルからワークブックを読み込む際のデータ種類のフィルタリング
linktitle: ワークブック読み込み時のデータフィルタリング
type: docs
weight: 400
url: /ja/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Aspose.Cellsを使ったテンプレートファイルからの特定データタイプのフィルタリング方法を学習します。
---

{{% alert color="primary" %}}

Excelファイル結合の効率的な方法

{{% /alert %}}

[指定されたリンク](5115552.xlsx)からダウンロードできるテンプレートファイルを使用して、ワークブックをロードする際にシェイプオブジェクトのみをロードするサンプルコードを以下に示します。以下のスクリーンショットには[テンプレートファイル](5115552.xlsx)の内容と、赤色および黄色の背景のデータがロードされないことを説明したものが表示されています。これは[**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/)プロパティが[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)に設定されているためです。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

[指定されたリンク](5115555.pdf)からダウンロードできる出力PDFです。ここでは、赤色および黄色の背景のデータが存在しない一方、すべての形状が存在することが分かります。

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
