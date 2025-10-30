---
title: 共有数式の設定（C++）
linktitle: 共有式数式の設定
type: docs
weight: 10
url: /ja/cpp/setting-shared-formula/
description: Aspose.Cellsを使用してExcelワークシートに共有数式を設定する方法を学びます。
---

{{% alert color="primary" %}}

計算を行う関数をワークシートに追加したい場合、この記事ではAspose.Cellsを使った方法を説明します。

{{% /alert %}}

## Aspose.Cellsを使用した共有式の設定

次のサンプルワークシートのようなデータで満たされたワークシートがあるとします。

|**入力ファイル（1列のデータ）**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

B2に関数を追加し、最初のデータ行の売上税を計算したいとします。税金は9%です。売上税を計算する式は次のとおりです:"=A2*0.09"。この記事では、Aspose.Cellsでこの式を適用する方法について説明します。

Aspose.Cellsを使用すると、[**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) プロパティを使用して式を指定できます。その他のセル（B3、B4、B5など）に式を追加するためには、2つのオプションがあります。

最初のセルのように操作し、各セルに対して数式を設定し、セル参照を更新します（A3*0.09、A4*0.09、A5*0.09など）。これには各行のセル参照を更新する必要があります。また、Aspose.Cellsは各数式を個別に解析しなければならず、大きなスプレッドシートや複雑な数式の場合は時間がかかることがあります。さらに、ループで多少簡略化できますが、追加のコード行が必要です。

もう1つの方法は、**共有式**を使用することです。共有式を使用すると、式は各行のセル参照に自動的に更新されるため、税金が正しく計算されます。[**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) メソッドは、最初の方法よりも効率的です。

次の例では、その使用方法を示しています。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
