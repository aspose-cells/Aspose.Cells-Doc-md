---  
title: C++でワークブック内の未使用スタイルを削除する  
linktitle: ワークブック内の未使用のスタイルを削除する  
type: docs  
weight: 340  
url: /ja/cpp/remove-unused-styles-inside-the-workbook/  
description: Aspose.Cellsを使ってExcelワークブックの未使用スタイルを削除します。  
---  

{{% alert color="primary" %}}  

Excelファイルの未使用スタイルは容量を増やすだけでなく、PDFやHTMLなど他のフォーマットに変換する際にパフォーマンス問題も引き起こします。Aspose.Cellsは、[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/)を提供し、ワークブック内の未使用スタイルをすべて削除します。  

{{% /alert %}}  

次のコードは [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) の使用法を説明しています。このコードは提供されたリンクからダウンロード可能な [テンプレートExcelファイル](5115520.xlsx) を読み込みます。これは未使用のスタイル **AsposeStyle** を含んでいます; このスタイル及びすべての未使用スタイルは、コードの実行後に削除されます。  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

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

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
