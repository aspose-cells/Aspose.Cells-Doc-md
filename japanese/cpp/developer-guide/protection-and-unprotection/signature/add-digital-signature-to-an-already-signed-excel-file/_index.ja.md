---
title: 既に署名されているExcelファイルにデジタル署名を追加する（C++）
linktitle: すでに署名されたExcelファイルにデジタル署名を追加する
type: docs
weight: 20
url: /ja/cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Aspose.Cells for C++を使用して、署名済みExcelファイルにデジタル署名を追加する方法を学びます。複数の署名を維持して、ドキュメントの完全性を保ちます。
keywords: 既に署名されているExcelファイルにデジタル署名を追加する方法、C++によるデジタル署名、Excelドキュメントのセキュリティ
---

## **可能な使用シナリオ**

Aspose.Cellsは、既に署名されたExcelファイルにデジタル署名を追加するための[**Workbook::AddDigitalSignature(DigitalSignatureCollectionPtr digitalSignatureCollection)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/)メソッドを提供します。

{{% alert color="primary" %}}

既に署名されたExcelドキュメントにデジタル署名を追加する際の注意点：元のドキュメントがAspose.Cellsで生成された場合は正常に動作します。ただし、他のエンジン（例：Microsoft Excel）で作成された場合、Aspose.Cells for C++はロードと再保存後に正確なファイル構造を維持できず、既存の署名が無効になる可能性があります。

{{% /alert %}}

## **すでに署名されたExcelファイルにデジタル署名を追加する方法**

以下のコード例は、[**Workbook::AddDigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/adddigitalsignature/)を使用して署名済みExcelファイルにデジタル署名を追加する例です。サンプルExcelファイル（50528280.xlsx）は事前に署名済みです。出力ファイル（50528281.xlsx）は結果を示します。デモ証明書[ AsposeDemo.pfx ]（50528279.pfx）とパスワード**aspose**を使用しています。

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Certificate and workbook paths
    U16String certFilePath = srcDir + u"AsposeDemo.pfx";
    U16String inputFilePath = srcDir + u"sampleDigitallySignedByCells.xlsx";
    U16String outputFilePath = outDir + u"outputDigitallySignedByCells.xlsx";

    // Load digitally signed workbook
    Workbook workbook(inputFilePath);

    // Create digital signature collection
    DigitalSignatureCollection dsCollection;

    // Create digital signature using PFX certificate
    U16String password = u"aspose";
    U16String comments = u"Aspose.Cells added new digital signature in existing digitally signed workbook.";
    DigitalSignature signature(certFilePath, password, comments, Date());

    // Add signature to collection
    dsCollection.Add(signature);

    // Apply digital signatures to workbook
    workbook.AddDigitalSignature(dsCollection);

    // Save modified workbook
    workbook.Save(outputFilePath);

    std::cout << "Digital signature added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
