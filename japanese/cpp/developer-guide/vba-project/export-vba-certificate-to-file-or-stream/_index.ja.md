---
title: C++でVBA証明書をファイルまたはストリームにエクスポートする方法
linktitle: ファイルまたはストリームにVBAデジタル証明書をエクスポート
type: docs
weight: 90
url: /ja/cpp/export-vba-certificate-to-file-or-stream/
description: Aspose.Cells for C++を使用してVBAデジタル証明書をファイルまたはメモリストリームにエクスポートする方法について学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、VBAデジタル証明書をファイルやメモリストリームなどのストリームにエクスポートできます。[**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/)プロパティを使用して、VBAデジタル証明書の生データにアクセスできます。

{{% /alert %}}

## **C++でVBA証明書をファイルまたはストリームにエクスポート**

以下のサンプルコードを参照してください。このコードで使用される[サンプルExcelファイル](5115031.xlsm)を提供リンクからダウンロードできます。

```cpp
#include <iostream>
#include <fstream>
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
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Retrieve bytes data of Digital Certificate of VBA Project
    Vector<uint8_t> certBytes = workbook.GetVbaProject().GetCertRawData();

    // Save Certificate Data into FileStream
    U16String outputFilePath = outDir + u"Cert_out_";
    std::ofstream outFile(outputFilePath.ToUtf8(), std::ios::binary);
    if (outFile.is_open())
    {
        outFile.write(reinterpret_cast<const char*>(certBytes.GetData()), certBytes.GetLength());
        outFile.close();
    }

    Aspose::Cells::Cleanup();
}
```
