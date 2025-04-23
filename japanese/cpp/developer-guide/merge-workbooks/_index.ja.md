---
title: 複数のワークブックを1つに結合する（C++）
linktitle: ワークブック結合ツール
type: docs
weight: 66
url: /ja/cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aspose.Cellsを使って複数のワークブックを1つに結合する方法を学びます（C++）。
---

{{% alert color="primary" %}}

時には、画像やチャート、データなど様々な内容を持つワークブックを1つに結合する必要があります。Aspose.Cellsはこの機能をサポートしています。この記事では、Visual Studioでコンソールアプリケーションを作成し、数行のコードでワークブックを結合する方法を示します。

{{% /alert %}}

## **画像とグラフを使用したワークブックの結合**

例のコードは、Aspose.Cellsを使用して2つのワークブックを1つのワークブックに結合します。コードはソースワークブックを読み込み、[**Workbook::Combine()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/combine/)メソッドを使用してそれらを結合し、出力ワークブックを保存します。

### **ソースワークブック**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **出力ワークブック**

- [combined.xlsx](5473095.xlsx)

### **スクリーンショット**

以下は、ソースおよび出力ワークブックのスクリーンショットです。

{{% alert color="primary" %}}

ソースワークブックを好きなものを使用できます。これらの画像は、イメージ説明のためのものです。

{{% /alert %}}

**チャートワークブックの最初のワークシート - 積み重ね** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**チャートワークブックの2番目のワークシート - 折れ線** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**画像ワークブックの最初のワークシート - 画像** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**結合されたワークブックの3つのワークシート - 積み重ね、折れ線、画像** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

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

    // Path of the first source excel file
    U16String sourceFile1 = srcDir + u"SampleChart.xlsx";

    // Path of the second source excel file
    U16String sourceFile2 = srcDir + u"SampleImage.xlsx";

    // Open the first excel file.
    Workbook sourceBook1(sourceFile1);

    // Open the second excel file.
    Workbook sourceBook2(sourceFile2);

    // Combining the two workbooks
    sourceBook1.Combine(sourceBook2);

    // Define the output file path
    U16String outputFilePath = srcDir + u"Combined.out.xlsx";

    // Save the target book file.
    sourceBook1.Save(outputFilePath);

    std::cout << "Workbooks combined and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高度なトピック**
- [複数のワークシートを単一のワークシートに結合する](/cells/ja/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [ファイルの結合](/cells/ja/cpp/merge-files/)
