---
title: C++を使ってExcelでの互換性チェッカーを無効にする
linktitle: 互換性チェッカーを無効にする
type: docs
weight: 170
url: /ja/cpp/disable-compatibility-checker-in-excel/
description: この例は、Aspose.Cells for C++ APIを通じて互換性チェッカーを無効にする方法を示しています。
keywords: C++での互換性チェッカー無効化、Excelの互換性チェッカー無効化、ワークブック内での無効化。 
---

## C++でExcelシート内の互換性チェッカーを無効にする

{{% alert color="primary" %}}

Microsoft Excelの互換性チェッカーは、以前のファイル形式でファイルを保存すると機能の問題や精度の低下が引き起こされる可能性があるとして警告を出します。互換性チェッカーはMicrosoft Office Excel 2007およびMicrosoft Excel 2010の機能です。

以前のバージョンのワークブックをExcel 2007またはExcel 2010からExcel 97からExcel 2003に保存する場合、互換性チェッカーは、以前のバージョンではサポートされていない機能が含まれていないかどうかをワークブックをスキャンします。互換性の問題についての決定を支援するために、互換性チェッカーはオプションを含むダイアログボックスを表示します。また、ワークブックの問題に関するレポートを作成したり、機能を無効にすることもできます。

特定のスプレッドシートで互換性チェッカーを無効にする必要がある場合があります。Aspose.CellsのAPIを使用すると、ユーザーが手動でMicrosoft Excelでファイルを再保存する際に互換性チェッカーダイアログボックスが表示されず、ユーザーが混乱したりイライラしたりしないように、これをプログラムで行うことができます。

{{% /alert %}}

## **Microsoft Excelを使用して互換性チェッカーを無効にする方法**

Microsoft Excel（例: Microsoft Excel 2007/2010）で互換性チェッカーを無効にする場合:

- （Excel 2007）[Office] ボタンをクリックし、「準備」、[互換性の確認] をクリックし、「このブックを保存するときに互換性を確認する」オプションをクリアします.
- (Excel 2010) ファイルタブをクリックし**情報**、**問題の確認**、**互換性を確認**をクリックし、最後に**このブックを保存する場合に互換性をチェック**のチェックを外します。

## **Aspose.Cells APIを使用して互換性チェッカーを無効にする方法**

Microsoft Excelの互換性チェッカーを無効にするには、[**Workbook.GetCheckCompatibility()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcompatibility/)プロパティを**False**に設定します。

### **コード例**

以下のコード例は、Aspose.Cells for C++を用いて互換性チェッカーを無効にする方法を示しています。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open a template file
    U16String templateFilePath = srcDir + u"sample.xlsx";
    Workbook workbook(templateFilePath);

    // Disable the compatibility checker
    workbook.GetSettings().SetCheckCompatibility(false);

    // Path to save the output file
    U16String outputFilePath = srcDir + u"Output_BK_CompCheck.out.xlsx";

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
