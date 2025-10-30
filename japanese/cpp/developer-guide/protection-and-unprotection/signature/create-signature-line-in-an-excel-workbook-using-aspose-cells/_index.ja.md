---
title: Aspose.Cellsを使ってC++でExcelワークブックに署名行を作成する方法
linktitle: Excelワークブックに署名ラインを作成する
type: docs
weight: 150
url: /ja/cpp/create-signature-line-in-an-excel-workbook-using-aspose-cells/
description: この資料では、C++とAspose.Cells for C++を使用してExcelワークブックに署名行を作成する方法について説明します。
keywords: Excelワークブックに署名行を作成する方法、Excelワークブックに署名行を作成する方法、署名行の追加方法、Excelファイルに署名行を追加する方法
---

## **紹介**

Microsoft ExcelはExcelブック内に**署名行**を追加する機能を提供しています。**挿入**タブをクリックし、**テキスト**グループから**署名行**を選択して、署名行を追加できます。

## **Excelファイルの署名行を作成する方法**

Aspose.Cellsもこの機能を提供し、この目的に[**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/)プロパティを公開しています。この記事では、このプロパティを使用して署名行を追加する方法について説明します。

次のサンプルコードは、[**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/)プロパティを使用して署名行を追加し、ワークブックを保存します。

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

    // Create workbook object
    Workbook workbook;

    // Create signature line object
    SignatureLine s;
    s.SetSigner(u"John Doe");
    s.SetTitle(u"Development Lead");
    s.SetEmail(u"john.doe@aspose.com");

    // Adds a Signature Line to the worksheet.
    workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);

    // Save the workbook
    U16String outputFilePath = outDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully with signature line!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
