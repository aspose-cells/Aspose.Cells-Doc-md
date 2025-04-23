---
title: ファイル読み込み時に自動的に行高さを調整
linktitle: Excel ファイルを読み込む際に自動的に行の高さを調整する
type: docs
weight: 120
url: /ja/cpp/autofit-row-height/
description: Aspose.Cells for C++を使用してカスタムされていない行の高さをフィットさせる方法を学びます。
keywords: ファイルを読み込むと行の高さが自動的にコンテンツのフォントに一致しますが、キャッシュされた行の高さがファイルのコンテンツの高さと一致しない場合、MS Excel はファイルを読み込む際に行の高さを自動的に調整しますが、Aspose.Cells はパフォーマンスを向上させるために自動的には調整しません。 Aspose.Cells プログラムを使用してファイルを読み込む際に行の高さを自動的に一致させる必要がある場合は、[LoadOptions.AutoFitterOptions.OnlyAuto](https //reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) パラメータを使用して目標を達成できます。
---

## **可能な使用シナリオ**
行の高さは自動的に内容のフォントに合わせて調整されますが、キャッシュされた行の高さがファイル内の内容の高さと一致しない場合、MS Excelはファイルを読み込むときに自動的に行の高さを調整しますが、Aspose.Cellsはパフォーマンス向上のために自動調整しません。ファイルの読み込み時にAspose.Cellsプログラムで行の高さを自動的に一致させたい場合は、パラメータ[LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/)を使用して実現できます。

次の画像データを参照してください。 行11のキャッシュ行の高さは15であることがわかりますが、Excel はファイルを読み込む際に行の高さを自動的に調整しました。
<br>
<img src="1.png" width=70% />

## **Aspose.Cells を使用して行の高さを調整する**
ファイルを直接読み込んで PDF に保存すると、キャッシュ行の高さが15であるため、PDF にデータが完全に表示されません。
<br>
<img src="2.png" width=70% />
<br>
ファイルを読み込む際に[LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/)をtrueに設定すると、Aspose.Cellsは行の高さを自動調整します。調整されたラインの高さは、テキストの表示要件を効果的に満たすことができます。
<br>
<img src="3.png" width=70% />

## **C++サンプルコード**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
