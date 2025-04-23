---
title: Excel および ODS ファイルの条件付き書式を設定する。
linktitle: 条件付き書式
type: docs
weight: 60
url: /ja/net/conditional-formatting/
description: CSharp で Excel および ODS ファイルに条件付き書式を適用する方法。
keywords: 条件付き書式の適用 
---

## **紹介**

条件付き書式は、Microsoft Excel の高度な機能で、セルやセル範囲に書式を適用し、その値や数式に応じて書式を変更することができます。たとえば、セルの値が 500 より大きいときにのみ太字にすることができます。セルの値が条件を満たした場合、指定された書式が適用されます。セルの値が書式条件を満たさない場合は、セルのデフォルトの書式が使用されます。Microsoft Excel では、**書式**、**条件付き書式** を選択して、条件付き書式ダイアログを開きます。

Aspose.Cells はセルに条件付き書式を実行時に適用することをサポートしています。この記事ではその方法を説明します。また、Excel が色スケールの条件付き書式に使用する色の計算方法も説明します。

## **条件付き書式の適用**

Aspose.Cells はいくつかの方法で条件付き書式をサポートしています。

- デザイナー スプレッドシートを使用
- コピー メソッドを使用
- 実行時に条件付き書式を作成

### **デザイナー スプレッドシートを使用**

開発者は、Microsoft Excel で条件付き書式を含むデザイナー スプレッドシートを作成し、そのスプレッドシートを Aspose.Cells で開くことができます。 Aspose.Cells は、デザイナー スプレッドシートを読み込み、保持し、条件付き書式の設定を保持します。

### **コピー メソッドを使用**

Aspose.Cells は、ワークシート内のセルから別のセルへ条件付き書式設定をコピーすることができます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **ランタイムで条件付き書式を適用**

Aspose.Cells では、条件付き書式をランタイムで追加および削除することができます。以下のコードサンプルでは、条件付き書式の設定方法を示しています。

1. ワークブックをインスタンス化してください。
1. 空の条件付き書式を追加してください。
1. 書式を適用する範囲を設定してください。
1. 書式の条件を定義してください。
1. ファイルを保存します。

この後に、フォント設定や罫線設定、パターン設定などの他の小さな例が続きます。

Microsoft Excel 2007 では、より高度な条件付き書式が追加され、それを Aspose.Cells もサポートしています。ここにある例では単純な書式設定を示していますが、Microsoft Excel 2007 の例ではより高度な条件付き書式の適用方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **フォントの設定**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

フォントスタイル、テキストの色、下線スタイル、取り消し線スタイルのみを変更できます。

{{% /alert %}}

### **境界線の設定**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

アウトライン境界線には細い線スタイルのみを使用できます。対角線は許可されていません。

{{% /alert %}}

### **パターンの設定**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **高度なトピック**
- [2色系規則と3色系規則の条件付き書式設定を追加する](/cells/ja/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [高度な条件付き書式の適用](/cells/ja/net/apply-advanced-conditional-formatting/)
- [ワークシートで条件付き書式設定を適用する](/cells/ja/net/apply-conditional-formatting-in-worksheets/)
- [条件付き書式設定を使用して、交互に行と列に影を付ける](/cells/ja/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [条件付き書式データバーイメージの生成](/cells/ja/net/generate-conditional-formatting-databars-images/)
- [条件付き書式で使用されるアイコンセット、データバー、またはカラースケールオブジェクトの取得](/cells/ja/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
