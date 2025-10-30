---
title: C++でエラー検出オプションを使用
linktitle: エラーチェックオプションを使用する
type: docs
weight: 140
url: /ja/cpp/use-error-checking-options/
description: この記事では、C++ APIまたはライブラリを使用して、Excelワークシートのエラー検出オプション（例：テキストとして保存された数字）をプログラム的に使用するサンプルコードを紹介します。
keywords: C++を使用してExcelに数字をテキストとして保存し、エラー検出オプションを設定する
---

{{% alert color="primary" %}}

Microsoft Excelでは、ユーザーはエラーチェックのオプションやルールを定義することができます。ユーザーが数式を作成する際にエラーチェックが表示されることがよくあり、セルの右上隅に小さな三角形が表示されます。Excelは、一般的な問題を修正するための情報を提供します。

{{% /alert %}}

## **エラーの種類**

数値を0で割るなど、式が結果を返せないエラーは即座の対応が必要であり、セルにエラー値が表示されます。緑色の三角形をクリックすると感嘆符が表示され、これをクリックするとオプションのリストが開きます。

エラーはオプションを使用して解決したり、無視することができます。エラーを無視すると、以降のエラーチェックにそのエラーが表示されなくなります。

Aspose.Cellsはエラーチェックオプション機能を提供しています。[**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/)クラスは、テキストとして保存された数値、式の計算エラー、および検証エラーなど、さまざまなタイプのエラーチェックを管理します。[**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/)列挙型を使用して、希望のエラーチェックを設定します。

## **テキストとして保存された数値**

時折、数値はセル内でテキストとしてフォーマットされ保存されることがあります。これは計算に問題を引き起こしたり、混乱する並び順を生むことがあります。テキストとしてフォーマットされた数値は、セル内で右寄せではなく左寄せになります。セル内で数学的演算を行うはずの式が値を返さない場合は、式が参照しているセルの配置を確認し、これらのいくつかまたはすべてのセルがテキストとして保存された数値である可能性があります。

テキストとして保存された数値を実際の数値に素早く変換するために、エラーチェックオプションを使用できます。Microsoft Excel 2003では:

1. **ツール** メニューで **オプション** をクリックします。
1. エラーチェックタブを選択します。
   **テキストとして保存された数値** オプションがデフォルトでチェックされています。
1. 無効にします。

次のサンプルコードは、Aspose.CellsのAPIを使用してXLSファイルのワークシートにおいてテキストとして保存された数値のエラーチェックオプションを無効にする方法を示しています。

```cpp
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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
