---
title: PDFに添付ファイルを埋め込む（C++）
linktitle: PDFに添付を埋め込む
type: docs
weight: 380
url: /ja/cpp/embed-attachment-to-pdf/
description: Aspose.CellsとC++を使用してPDFに添付ファイルを埋め込む方法を学ぶ。
---

Excelではソースデータを持つOle Objectを挿入できます（[embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)）。Ole Objectをダブルクリックすると、埋め込みファイルが開きます。

一般的に、PDF変換時にはOle Objectはアイコンまたはサムネイルとしてレンダリングされ、そのソースデータは表示されません。ただし、[PdfSaveOptions.GetEmbedAttachments()](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getembedattachments/) オプションを使用すると、Ole Objectのソースデータを添付ファイルとしてPDFに埋め込むことができます。アイコンやサムネイルをダブルクリックすると、Ole Objectのソースファイルを開くことができます。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template file
    Workbook workbook(u"embedded-attachments-example.xlsx");

    // Set to embed Ole Object attachment.
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetEmbedAttachments(true);

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF saved successfully with embedded attachments!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

![embedded-attachment.png](embedded-attachment.png)
{{< app/cells/assistant language="cpp" >}}
