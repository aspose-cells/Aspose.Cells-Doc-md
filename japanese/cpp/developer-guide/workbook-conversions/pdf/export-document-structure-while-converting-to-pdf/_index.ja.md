---  
title: PDF変換時にドキュメント構造をエクスポートする（C++）  
linktitle: PDF への変換時にドキュメント構造をエクスポート  
type: docs  
weight: 360  
url: /ja/cpp/export-document-structure-while-converting-to-pdf/  
description: Aspose.Cellsを使用してPDFに変換中にドキュメント構造をエクスポートする方法について学ぶ（C++）  
---  

PDFの論理構造機能は、ドキュメントの内容構造に関する情報をPDFファイルに組み込む仕組みを提供します。Aspose.Cellsは、Microsoft Excelドキュメントからセル、行、表、ワークシート、画像、シェイプ、ヘッダー/フッターなどの構造情報を保持します。  

[PdfSaveOptions.GetExportDocumentStructure()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getexportdocumentstructure/)オプションを使用すれば、ドキュメント構造をエクスポートしたタグ付きPDFとして保存可能です。  

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the Excel file with image, shape, chart, etc.
    Workbook workbook(u"document-structure-example.xlsx");

    // Set to export document structure.
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetExportDocumentStructure(true);

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully with document structure!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  


