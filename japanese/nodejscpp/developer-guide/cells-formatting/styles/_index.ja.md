---
title: セルのスタイルを取得および設定する
description: Aspose.Cells for Node.js via C++ でのデータの書式設定とスタイリングの方法、テキスト書式設定、数値書式設定、日付書式設定、その他のスタイルオプションを学びます。私たちのガイドは、魅力的な書式設定を行ったプロフェッショナルなスプレッドシート作成を支援します。
keywords: Aspose.Cells for Node.js via C++、データ書式設定、スタイリング、テキスト書式設定、数値書式設定、日付書式設定、スタイルオプション、スプレッドシート、魅力的な書式設定、プロフェッショナルな見た目。
linktitle: スタイル
type: docs
weight: 50
url: /ja/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++ はセルの書式設定に新たに2つのメソッド（Cell.getStyle と Cell.setStyle）を導入しました。本記事では、Cell.getStyle / setStyle のアプローチを検討し、どちらの技法が最適か判断できるようにします。

{{% /alert %}} 
## **セルの書式設定**
セルの書式設定には2つの方法があります。以下に示します。
### **getStyle() の使用**
このコードでは、書式設定時に各セルのために Style オブジェクトが初期化されます。多くのセルをフォーマットする場合、Style オブジェクトは大きいため多くのメモリを消費します。これらの Style オブジェクトは、Workbook.save メソッドが呼び出されるまで解放されません。

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **setStyle() の使用**
最初の方法は簡単で直感的ですが、なぜ2つ目の方法を追加したのでしょうか？

メモリ使用量を最適化するために、第二のアプローチを追加しました。Cell.getStyle メソッドを使って Style オブジェクトを取得し、それを変更してから Cell.setStyle メソッドを使って再設定します。この Style オブジェクトは保持されず、JavaScript のガベージコレクターによって参照されなくなると収集されます。

Cell.setStyle メソッドを呼び出すと、Style オブジェクトは各セルに保存されません。その代わり、この Style オブジェクトと内部の Style オブジェクトプールを比較し、再利用可能かどうか確認します。既存のものと異なる Style オブジェクトのみが、各 Workbook に保存されます。これにより、各 Excel ファイルには数百の Style オブジェクトのみが存在し、数千ではありません。各セルには、Style オブジェクトプールへのインデックスのみが保持されます。

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **高度なトピック**
- [CellsFactoryクラスを使用してスタイルオブジェクトを作成する](/cells/ja/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [既存のStyleを修正する](/cells/ja/nodejs-cpp/modify-an-existing-style/)
- [Styleオブジェクトの再利用](/cells/ja/nodejs-cpp/reusing-style-objects/)
- [組み込みのスタイルを使用する](/cells/ja/nodejs-cpp/using-built-in-styles/)

{{< app/cells/assistant language="nodejs-cpp" >}}
