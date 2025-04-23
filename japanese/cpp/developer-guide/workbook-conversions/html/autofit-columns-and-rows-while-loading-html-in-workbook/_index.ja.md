---
title: C++でワークブックにHTMLを読み込む際の列と行の自動調整
linktitle: ワークブックにHTMLをロードする際の列と行を自動調整する
type: docs
weight: 120
url: /ja/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/
description: HTMLを読み込みながら列と行を自動調整する方法について、Aspose.Cells for C++を使用して学びます。
---

## **可能な使用シナリオ**

HTMLファイルをWorkbookオブジェクト内で読み込む際に列と行を自動調整できます。このためには、[**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/)プロパティを**true**に設定してください。

## **ワークブックにHTMLをロードする際の列と行を自動調整する**

次のサンプルコードは、最初にロードオプションなしでサンプルHTMLをWorkbookに読み込み、XLSX形式で保存します。その後、[**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/)プロパティを**true**に設定してサンプルHTMLをWorkbookに再度読み込み、XLSX形式で保存します。出力エクセルファイル、つまり[Auftput Excel File Without AutoFitColsAndRows](outputWithout_AutoFitColsAndRows.xlsx)と[AutoFitColsAndRowsを使用した出力Excelファイル](outputWith_AutoFitColsAndRows.xlsx)をダウンロードしてください。次のスクリーンショットは、[**HtmlLoadOptions.GetAutoFitColsAndRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getautofitcolsandrows/)プロパティの効果を示したものです。

![todo:image_alt_text](autofit-columns-and-rows-while-loading-html-in-workbook_1.png)

## **サンプルコード**

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

    // Sample HTML string
    U16String sampleHtml(u"<html><body><table><tr><td>This is sample text.</td><td>Some text.</td></tr><tr><td>This is another sample text.</td><td>Some text.</td></tr></table></body></html>");

    // Convert HTML string to memory stream
    std::string utf8Data = sampleHtml.ToUtf8();
    Vector<uint8_t> ms(utf8Data.size());
    std::memcpy(ms.GetData(), utf8Data.data(), utf8Data.size());

    // Load memory stream into workbook
    Workbook wb(ms);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"outputWithout_AutoFitColsAndRows.xlsx");

    // Specify the HTMLLoadOptions and set AutoFitColsAndRows = true
    HtmlLoadOptions opts;
    opts.SetAutoFitColsAndRows(true);

    // Load memory stream into workbook with the above HTMLLoadOptions
    Workbook wbWithOptions(ms, opts);

    // Save the workbook in xlsx format
    wbWithOptions.Save(outDir + u"outputWith_AutoFitColsAndRows.xlsx");

    std::cout << "HTML to Excel conversion completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
