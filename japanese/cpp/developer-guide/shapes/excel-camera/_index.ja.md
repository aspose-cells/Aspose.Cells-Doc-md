---
title: Aspose.Cells for C++ の Excel カメラ
description: セル範囲にリンクされ、ソースデータが更新されると再描画され、すべての書式を保持する動的ピクチャを作成するために Aspose.Cells for C++ で Excel カメラを使用する方法を説明します。
linktitle: Excel カメラ
keywords: Aspose.Cells, C++, Excel カメラ, 動的ピクチャ, リンクピクチャ, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /ja/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel カメラは、セル範囲のライブ画像をレンダリングするワークシートオブジェクトであり、通常のピクチャのように描画レイヤーに浮かんで表示されます。Aspose.Cells は 2 つの作成モードをサポートしています。ソースデータが変更されるたびに自動更新される動的ピクチャと、範囲のワンタイムスナップショットをキャプチャする静的ピクチャです。この記事では両方の方法を説明しますので、レイアウトに合った方法を選択できます。

## Excel カメラとは?
Excel カメラは、本質的にワークシートの描画レイヤーの特定の行と列に固定されたピクチャオブジェクトです。通常の挿入ピクチャとは異なり、カメラは `A1:F10` などの A1 形式の数式を通じてソース範囲にリンクされています。その範囲内のセルが変更されるたびに、カメラの画像は新しい内容を反映して自動的に更新されます。カメラはソース領域の完全な書式（罫線、背景色、フォント、数値書式）を保持するため、セル内で表示されているすべてのものがカメラの画像内にも表示されます。このため、カメラはダッシュボード、サマリー、サイドパネル、レポートレイアウトなど、スクロールやデータの繰り返しなしにリモート領域のビジュアルプレビューを表示したい場合に特に便利です。2 つの注意点があります。ワークブックを保存する前に `UpdateSelectedValue()` を呼び出す必要があります。また、ファイルは HTML または PDF にエクスポートされます。これらの形式はライブ再計算ではなく埋め込まれた画像データに依存しているためです。

## 方法 1 — 動的カメラピクチャの追加
動的カメラは最も一般的なアプローチであり、Excel の組み込みカメラツールに最も近いものです。これは、初期画像コンテンツを持たないピクチャを追加し、ソース範囲を参照する `Formula` を割り当てることによって機能します。数式が割り当てられた後、`UpdateSelectedValue()` を呼び出すと、埋め込まれた画像データが更新され、反映先のセルと同期します。カメラは専用クラスでは実装されておらず、完全に標準の `Picture` 型に基づいて構築されています。
主要な API は次のとおりです。
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — 指定された行と列に固定されたピクチャを追加します。空の `Vector<uint8_t>()` を渡すと、動的カメラのプレースホルダーとして機能する空のピクチャが作成されます。このメソッドは新しいピクチャのインデックスを返します。
- `worksheet.GetPictures().Get(int index)` — インデックスによってコレクションから特定の `Picture` を取得します。
- `Picture.SetFormula(U16String value)` — カメラがミラーリングするソース範囲への A1 形式参照（`U16String("A1:F10")` など）を設定します。
- `Picture.UpdateSelectedValue()` — `Formula` で参照されているセルから埋め込まれた画像データを更新します。

{{% alert color="primary" %}}
出力が HTML または PDF の場合、`UpdateSelectedValue()` は保存前に必ず呼び出す必要があります。呼び出さないと、エクスポートされたファイルにピクチャデータが含まれず、レンダリングされた出力ではカメラが空白で表示されます。
{{% /alert %}}

次のコードは、ワークブックを作成し、10 行 6 列に固定された空のピクチャを追加し、`Formula` プロパティを通じて `A1:F10` のソース範囲にリンクし、埋め込まれた画像データを更新して、ワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // 動的カメラ: 空の画像を追加し、Formulaを使ってA1:F10にリンクし、更新します
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 方法 2 — 静的カメラピクチャの追加
静的カメラは本質的に、セル範囲のワンタイムレンダリングプレビューです。ライブリンクを維持する代わりに、範囲を `Vector<uint8_t>` バイトバッファに一度レンダリングし、そのバッファを `Pictures.Add(row, col, data)` に直接渡します。画像コンテンツは作成時に固定され、ソースセルが変更されても自動更新されません。
主要な API は次のとおりです。
- `Cells.CreateRange(U16String address)` — `U16String("A1:F10")` などの A1 形式のアドレスから `Range` オブジェクトを構築します。
- `Range.ToImage(ImageOrPrintOptions options)` — 範囲を `Vector<uint8_t>` バイトバッファにレンダリングします。`nullptr` を渡すとデフォルトのレンダリングオプションが使用されます。出力のより細かい制御用のオーバーロードも存在します。
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — 指定された行と列にピクチャを追加します。今回は `Range.ToImage` によって生成されたバイトバッファを渡します。
次のコードは、ワークブックを作成し、`A1:F10` の `Range` を構築し、`Range.ToImage(nullptr)` を通じて画像バイトにレンダリングし、10 行 6 列に固定されたピクチャを追加して、ワークブックを保存します。

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // 静的カメラ: Rangeを構築し、バイトにレンダリングし、画像として追加
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## 動的と静的の選択
- **動的カメラ:** 再計算のたびに更新され、`UpdateSelectedValue()` 後の HTML および PDF エクスポートをサポートし、ファイルの存続期間にわたってライブリンク動作を保持します。
- **静的カメラ:** 更新されないワンタイムレンダリングで、ライブミラーリングではなくビルド時に埋め込まれた固定のビジュアルスナップショットが必要な場合に役立ちます。
Aspose.Cells は、`Picture.Formula` と `UpdateSelectedValue()` に基づいて構築された自動更新される動的カメラと、`Range.ToImage` と `Vector<uint8_t>` に基づいて構築されたワンショット静的カメラの両方をサポートします。出力をソースセルと同期させる必要がある場合は動的アプローチを、ビルド時に固定のビジュアルスナップショットのみが必要な場合は静的アプローチを選択してください。cpp

{{< app/cells/assistant language="cpp" >}}