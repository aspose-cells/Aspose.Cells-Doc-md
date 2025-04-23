---
title: ワークシートに署名行を追加（C++）
linktitle: 署名行を追加
type: docs
weight: 200
url: /ja/cpp/add-signature-line/
description: この資料では、C++コードとAspose.Cells for C++を使ってワークシートに署名行を追加する方法について説明します。
keywords: ワークシートに署名行を追加する方法、ワークシートに署名行を追加する方法、Excelファイルに署名行を追加する方法
---

## **紹介**

Aspose.Cellsは、ワークシートの署名行を追加するための[**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/)プロパティを提供します。

## **ワークシートに署名行を追加する方法**

以下のサンプルコードは、[**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/)プロパティを使用してワークシートの署名行を追加する方法を示します。実行後のサンプルExcelファイルの効果をスクリーンショットで示します。

![todo:image_alt_text](add-signature-line.png)

## **サンプルコード**

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook wb;

    SignatureLine signatureLine;
    signatureLine.SetSigner(u"Aspose.Cells");
    signatureLine.SetTitle(u"signed by Aspose.Cells");

    wb.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, signatureLine);

    U16String certificatePath = srcDir + u"rsa2048.pfx";
    U16String password = u"123456";

    std::time_t now = std::time(nullptr);
    struct tm now_tm;
    localtime_s(&now_tm, &now);

    Date currentDate{
        now_tm.tm_year + 1900,
        now_tm.tm_mon + 1,
        now_tm.tm_mday,
        now_tm.tm_hour,
        now_tm.tm_min,
        now_tm.tm_sec,
        0
    };

    DigitalSignature signature(certificatePath, password, u"test Microsoft Office signature line", currentDate);

    DigitalSignatureCollection dsCollection;
    dsCollection.Add(signature);

    wb.SetDigitalSignature(dsCollection);

    U16String outputPath = srcDir + u"signatureLine.xlsx";
    wb.Save(outputPath);

    std::cout << "Workbook with signature line saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
