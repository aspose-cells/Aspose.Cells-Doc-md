---
title: 組み込みドキュメントプロパティのScaleCropとLinksUpToDateプロパティをC++で設定する
linktitle: ScaleCropとLinksUpToDateプロパティの設定方法
type: docs
weight: 320
url: /ja/cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Aspose.Cells for C++を使用して、組み込みドキュメントプロパティのScaleCropとLinksUpToDateの設定方法を学びます。
---

## **可能な使用シナリオ**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/)と[GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/)は、OpenXmlフォーマット内に定義された2つの拡張組み込みドキュメントプロパティです。これらの目的は以下の通りです：

## **1) ScaleCrop**
この要素は、ドキュメントサムネイルの表示モードを示します。この要素を**TRUE**に設定すると、ドキュメントサムネイルを表示に合わせてスケーリングします。この要素を**FALSE**に設定すると、ドキュメントサムネイルを表示に合わせてクロップします。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。

## **2) LinksUpToDate**
この要素は、ドキュメント内のハイパーリンクが最新であるかどうかを示します。この要素を**TRUE**に設定すると、ハイパーリンクが更新されていることを示します。この要素を**FALSE**に設定すると、ハイパーリンクが更新されていないことを示します。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。

## **これらのプロパティを示すスクリーンショット**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **組み込みドキュメントプロパティのScaleCropとLinksUpToDateの設定**
次のサンプルコードは、ワークブックの拡張組み込みドキュメントプロパティである[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) と [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) を設定します。このコードで生成された出力Excelファイル（5115500.xlsx）を確認し、その拡張子を.zipに変更して内容を抽出し、app.xmlを閲覧してください。スクリーンショットのように見えます。

```c++
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

    // Instantiating a Workbook object.
    Workbook workbook;

    // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
    workbook.GetBuiltInDocumentProperties().SetScaleCrop(true);
    workbook.GetBuiltInDocumentProperties().SetLinksUpToDate(true);

    // Saving the Excel file.
    workbook.Save(outDir + u"output.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
