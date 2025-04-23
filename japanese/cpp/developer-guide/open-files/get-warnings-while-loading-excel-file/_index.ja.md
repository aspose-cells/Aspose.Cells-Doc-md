---
title: C++を使用してExcelファイルの読み込み中に警告を取得する方法
linktitle: Excelファイルの読み込み時に警告を取得する
type: docs
weight: 110
url: /ja/cpp/get-warnings-while-loading-excel-file/
description: Aspose.Cells for C++を用いてExcelファイルの読み込み時に警告を捕捉し処理する方法を学びます。
---

## **可能な使用シナリオ**

読み込み中に壊れている可能性のあるExcelファイルも例外的にロードできる場合があります。そうした場合、Aspose.Cellsは警告を出します。これらの警告は [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/)インターフェースを実装し、[**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/)プロパティを設定することで捕捉可能です。

## **Excelファイルの読み込み中に警告を受け取る**

Excelファイルをロード中に警告を取得するサンプルコード例。サンプルは[サンプルExcelファイル](sampleDuplicateDefinedName.xlsx)を読み込み、ロード時に警告（[**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/)）を出します。その警告は[**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/)メソッドで捕捉され、コンソールに警告メッセージを出力します。さらに、この例は結果のファイルも保存し、[出力Excelファイル](outputDuplicateDefinedName.xlsx)として保存します。Microsoft Excelで開いた場合も同様の警告が表示されます。以下のコードのコンソール出力も確認してください。

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class WarningCallback : public IWarningCallback {
public:
    void Warning(WarningInfo& warningInfo) override {
        if (warningInfo.GetType() == ExceptionType::DefinedName) {
            std::cout << "Defined Name Warning: " << warningInfo.GetDescription().ToUtf8() << std::endl;
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    LoadOptions options;
    WarningCallback callback;
    options.SetWarningCallback(&callback);

    U16String inputFilePath = srcDir + u"sampleDuplicateDefinedName.xlsx";
    Workbook book(inputFilePath, options);

    U16String outputFilePath = outDir + u"outputDuplicateDefinedName.xlsx";
    book.Save(outputFilePath);

    std::cout << "Workbook saved successfully with warning handling!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **コンソール出力**

提供された[サンプルエクセルファイル](sampleDuplicateDefinedName.xlsx)を使用して上記のコードを実行した際のコンソール出力は次のとおりです。

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
