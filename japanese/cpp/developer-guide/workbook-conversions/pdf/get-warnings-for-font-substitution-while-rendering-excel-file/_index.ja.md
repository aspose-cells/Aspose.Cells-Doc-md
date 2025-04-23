---
title: Excelファイルのレンダリング時にフォント代替の警告を取得
linktitle: フォント置換に関する警告を取得
type: docs
weight: 230
url: /ja/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: Aspose.Cellsを使用して、C++でExcelファイルをPDFにレンダリングする際にフォント置換の警告を取得する方法について学びます。
---

{{% alert color="primary" %}}

Microsoft ExcelファイルをPDFにレンダリングする際、Aspose.Cellsはフォントを置換する場合があります。Aspose.Cellsには、特定のフォントが置換されたことを開発者に知らせる機能が備わっており、警告を表示することができます。これは、Aspose.Cellsがレンダリング結果が元のMicrosoft Excelファイルと異なって見える理由を特定し、適切な対策を取るための有用な機能です。たとえば、不足しているフォントをインストールして、レンダリング結果が同じに見えるようにできます。

{{% /alert %}}

ExcelファイルをPDFにレンダリングする際のフォント置換警告を取得するには、`IWarningCallback`インターフェースを実装し、`PdfSaveOptions.WarningCallback`プロパティにあなたの実装したインターフェースを設定します。

以下のスクリーンショットは、次のコードで使用する元のExcelファイルを示しています。セルA6およびA7には、Microsoft Excelによって正しくレンダリングされないフォントでテキストが含まれています。

|**すべてのフォントが正しくレンダリングされているわけではありません**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cellsは、セルA6とA7のフォントを適切なフォントで置き換えます。

|**置き換えフォント**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **ソースファイルと出力PDFのダウンロード**
以下のリンクからソースExcelファイルと出力されるPDFをダウンロードできます：

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **コード**
以下のコードは、`IWarningCallback`を実装し、`PdfSaveOptions.WarningCallback`にインターフェースを設定する方法を示しています。これにより、セル内のフォントが置換されるたびにAspose.Cellsが`WarningCallback.Warning()`メソッド内で警告を発信します。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GetWarningsForFontSubstitution : public IWarningCallback
{
public:
    void Warning(WarningInfo& info) override
    {
        if (info.GetType() == ExceptionType::FontSubstitution)
        {
            std::cout << "WARNING INFO: " << info.GetDescription().ToUtf8() << std::endl;
        }
    }

    static void Run()
    {
        U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
        U16String outDir(u"..\\Data\\02_OutputDirectory\\");
        Workbook workbook(srcDir + u"source.xlsx");
        PdfSaveOptions options;
        auto callback = std::make_shared<GetWarningsForFontSubstitution>();
        options.SetWarningCallback(callback.get());
        workbook.Save(outDir + u"output_out.pdf", options);
        std::cout << "PDF saved successfully with font substitution warnings!" << std::endl;
    }
};

int main()
{
    Aspose::Cells::Startup();
    GetWarningsForFontSubstitution::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **出力**
ExcelファイルをPDFに変換した後、警告は次のようにデバッグコンソールに出力されます。

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、`Workbook.CalculateFormula`メソッドを呼び出して、スプレッドシートをPDFに変換する直前に数式依存値を再計算し、正しい値をレンダリングさせることが最良です。

{{% /alert %}}
