--- 
title: 正規表現を使用してワークブック内のテキストを置換するC++コード
linktitle: 正規表現を使用してブック内のテキストを置換する
type: docs 
weight: 90 
url: /ja/cpp/replace-text-in-a-workbook-using-regular-expression/ 
description: Aspose.Cellsを使用してC++で正規表現を使ったテキストの置換を行います。 
--- 

Aspose.Cellsは、正規表現を使ってワークブック内のテキストを置換する機能を提供しています。これには、APIの[**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/)プロパティと[**ReplaceOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/)クラスを使用します。[**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/)を**true**に設定すると、検索キーが正規表現であることを示します。

次のコードスニペットは、[サンプルExcelファイル](101089318.xlsx)を使用して [**GetRegexKey()**](https://reference.aspose.com/cells/cpp/aspose.cells/replaceoptions/getregexkey/) プロパティの使用例を示しています。このコードによって生成された [出力ファイル](101089319.xlsx) を参考として添付しています。

## **サンプルコード** 

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook from the input file
    Workbook workbook(sourceDir + u"SampleRegexReplace.xlsx");

    // Create replace options
    ReplaceOptions replace;
    replace.SetCaseSensitive(false);
    replace.SetMatchEntireCellContents(false);
    // Set to true to indicate that the searched key is regex
    replace.SetRegexKey(true);

    // Perform the regex replace operation
    workbook.Replace(u"\\bKIM\\b", u"^^^TIM^^^", replace);

    // Save the modified workbook
    workbook.Save(outputDir + u"RegexReplace_out.xlsx");

    std::cout << "Regex replace operation completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
