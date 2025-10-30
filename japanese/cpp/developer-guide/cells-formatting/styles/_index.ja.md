---
title: C++を使ったセルのスタイル取得と設定
linktitle: スタイル
type: docs
weight: 50
url: /ja/cpp/styling-and-data-formatting/
description: Aspose.Cells for C++でデータの書式設定やスタイリングを行う方法を紹介します。これにはテキスト設定、数値設定、日付設定、その他のスタイリングオプションが含まれます。私たちのガイドは、魅力的な書式設定でプロフェッショナルなスプレッドシートを作成するのに役立ちます。
keywords: Aspose.Cells for C++、データ書式設定、スタイリング、テキスト書式設定、数値書式設定、日付書式設定、スタイルオプション、スプレッドシート、魅力的な書式設定、プロフェッショナルな外観。
---

{{% alert color="primary" %}}

Aspose.Cells for C++は、セルの書式設定に新たな2つの方法：`Cell.GetStyle`と`Cell.SetStyle`を導入しました。この方法の概要と、それがあなたに適しているかどうかを判断するための記事です。

{{% /alert %}}

## **セルの書式設定**
セルの書式設定には2つの方法があります。以下に示します。

### **GetStyle()を使用する**
このコードでは、書式設定時に各セルに`Style`オブジェクトを作成します。多くのセルを書式設定する場合、`Style`オブジェクトは大きなオブジェクトであるため大量のメモリを消費します。これらの`Style`オブジェクトは`Workbook.Save`メソッドが呼び出されるまで解放されません。

**C++**

```cpp
cell.GetStyle()->GetFont()->SetIsBold(true);
```

### **SetStyle()を使用する**
最初のアプローチは簡単でわかりやすいため、第2のアプローチを追加しました。

2番目のアプローチを追加したのは、メモリ使用量を最適化するためです。`Cell.GetStyle`メソッドを使って`Style`オブジェクトを取得し、それを修正して`Cell.SetStyle`メソッドでセルに設定します。この`Style`オブジェクトは保持されず、参照されなくなったときにC++のランタイムによって収集されます。

`Cell.SetStyle`メソッドを呼び出すとき、`Style`オブジェクトは各セルに保存されません。その代わりに、内部の`Style`オブジェクトプールと比較して再利用できるかどうかを判断します。既存のものと異なる`Style`オブジェクトのみが各`Workbook`に保存されます。つまり、Excelファイルごとに数百の`Style`オブジェクトしかなく、数千ではありません。各セルは`Style`オブジェクトプールのインデックスのみが保持されます。

**C++**

```cpp
auto style = cell.GetStyle();
style->GetFont()->SetIsBold(true);
cell.SetStyle(style);
```

## **上級トピック**
- [CellsFactoryクラスを使用してスタイルオブジェクトを作成する](/cells/ja/cpp/create-style-object-using-cellsfactory-class/)
- [既存のStyleを修正する](/cells/ja/cpp/modify-an-existing-style/)
- [Styleオブジェクトの再利用](/cells/ja/cpp/reusing-style-objects/)
- [組み込みのスタイルを使用する](/cells/ja/cpp/using-built-in-styles/)
{{< app/cells/assistant language="cpp" >}}
