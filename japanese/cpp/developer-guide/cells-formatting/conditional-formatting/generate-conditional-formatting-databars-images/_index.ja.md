---
title: C++でデータバー画像を生成
linktitle: 条件付き書式のデータバー画像を生成
description: Aspose.Cellsはスプレッドシートファイルの操作に使えるC++ライブラリです。条件付き書式データバーや画像の生成をサポートしており、セルの値に基づいてスプレッドシートの表示をカスタマイズできます。この資料では、Aspose.Cellsライブラリを使用して条件付き書式のデータバーや画像を生成する方法を紹介します。
keywords: Aspose.Cells、条件付き書式、データバー、画像、スプレッドシート
type: docs
weight: 40
url: /ja/cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

時折、条件付き書式のデータバーの画像を生成する必要があります。Aspose.Cellsの [**DataBar.ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/) メソッドを使用して、これらの画像を生成できます。この記事では、Aspose.Cellsを使用してデータバーの画像を生成する方法について説明します。

{{% /alert %}}

以下のサンプルコードは、セルC1のDataBar画像を生成します。まず、そのセルの書式条件オブジェクトにアクセスし、そのオブジェクトから[**DataBar**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/)オブジェクトを取得、その[**ToImage()**](https://reference.aspose.com/cells/cpp/aspose.cells/databar/toimage/)メソッドを使用してセルの画像を生成します。最後に、その画像をディスクに保存します。

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"sampleGenerateDatabarImage.xlsx");
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cell cell = worksheet.GetCells().Get(u"C1");

    int idx = worksheet.GetConditionalFormattings().Add();
    FormatConditionCollection fcc = worksheet.GetConditionalFormattings().Get(idx);
    fcc.AddCondition(FormatConditionType::DataBar);
    fcc.AddArea(CellArea::CreateCellArea(u"C1", u"C4"));

    DataBar dbar = fcc.Get(0).GetDataBar();

    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Png);

    Vector<uint8_t> imgBytes = dbar.ToImage(cell, opts);

    std::ofstream outFile((outDir + u"outputGenerateDatabarImage.png").ToUtf8(), std::ios::binary);
    outFile.write(reinterpret_cast<const char*>(imgBytes.GetData()), imgBytes.GetLength());
    outFile.close();

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
