---
title: BuiltInドキュメントプロパティを使用してExcelファイルのバージョンを指定するC++による方法
linktitle: ドキュメントバージョンの指定
type: docs
weight: 20
url: /ja/cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: ビルトインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する方法を学びます。Aspose.Cells for C++を使用して解説します。
---

## **可能な使用シナリオ**

Excelファイルの**バージョン番号**を変更するには、ファイルを右クリックし、[プロパティ]→[詳細]を選択し、**バージョン番号**の欄を編集してください。Aspose.Cells APIを使ってプログラムで変更するには[**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/)プロパティを使用してください。

## **ビルドインドキュメントプロパティを使用してExcelファイルのドキュメントバージョンを指定する**

次のサンプルコードは、ワークブックを作成し、そのビルトインドキュメントプロパティ（タイトル、作者、バージョン番号）を変更します。コードで生成された[出力Excelファイル](64716811.xlsx)と、その中のバージョン番号が[**BuiltInDocumentPropertyCollection.GetDocumentVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getdocumentversion/)プロパティによって変更されたスクリーンショットを確認してください。

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)

## **サンプルコード**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Properties;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb;

    // Access built-in document property collection
    BuiltInDocumentPropertyCollection bdpc = wb.GetBuiltInDocumentProperties();

    // Set the title
    bdpc.SetTitle(u"Aspose File Format APIs");

    // Set the author
    bdpc.SetAuthor(u"Aspose APIs Developers");

    // Set the document version
    bdpc.SetDocumentVersion(u"Aspose.Cells Version - 18.3");

    // Save the workbook in xlsx format
    wb.Save(u"outputSpecifyDocumentVersionOfExcelFile.xlsx", SaveFormat::Xlsx);

    std::cout << "Document properties set and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
