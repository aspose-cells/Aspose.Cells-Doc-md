---
title: ビルトインドキュメントプロパティを使用したExcelファイルの言語指定方法（C++）
linktitle: Excelファイルの言語を指定する
type: docs
weight: 30
url: /ja/cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
description: Aspose.Cells for C++を用いてExcelファイルの言語をプログラムで変更する方法を学びます。
---

## **可能な使用シナリオ**

Excelファイルの言語を変更するには、ファイルを右クリックして[プロパティ] > [詳細設定]を選択し、言語フィールドを編集します。プログラムで変更するには、[**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/)プロパティをAspose.Cells APIを使用して使用してください。

## **ビルドインドキュメントプロパティを使用してExcelファイルの言語を指定する**

以下のサンプルコードは、ワークブックを作成し、組み込みのドキュメントプロパティである言語を変更します。コードによって生成された[出力Excelファイル](64716891.xlsx)と、[**BuiltInDocumentPropertyCollection.GetLanguage()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlanguage/)プロパティによる修正された言語フィールドのスクリーンショットをご覧ください。

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **サンプルコード**

```c++
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

    // Set the language of the Excel file
    bdpc.SetLanguage(u"German, French");

    // Save the workbook in xlsx format
    wb.Save(u"..\\Data\\02_OutputDirectory\\outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx", SaveFormat::Xlsx);

    std::cout << "Language set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
