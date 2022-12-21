---
title: Excel および ODS ファイルの条件付き書式を設定します。
linktitle: 条件付き書式
type: docs
weight: 60
url: /ja/net/conditional-formatting/
description: CSharp で条件付き書式を Excel および ODS ファイルに適用する方法。
keywords: apply conditional formats 
---
## **序章**

条件付き書式は、セルまたはセル範囲に書式を適用し、セルの値または数式の値に応じて書式を変更できる高度な Microsoft Excel 機能です。たとえば、セルの値が 500 より大きい場合にのみ、セルを太字で表示することができます。セルの値が条件を満たすと、指定された書式がセルに適用されます。セルの値がフォーマット条件を満たさない場合、セルのデフォルトのフォーマットが使用されます。 Microsoft Excel で、**フォーマット**、 それから**条件付き書式**をクリックして、条件付き書式設定ダイアログを開きます。

Aspose.Cells は、実行時に条件付き書式をセルに適用することをサポートします。この記事では、その方法について説明します。また、Excel でカラー スケールの条件付き書式に使用される色を計算する方法についても説明します。

## **条件付き書式の適用**

Aspose.Cells は、いくつかの方法で条件付き書式をサポートしています。

- デザイナー スプレッドシートの使用
- コピー方式を採用。
- 実行時に条件付き書式を作成します。

### **Designer スプレッドシートの使用**

開発者は、Microsoft Excel で条件付き書式を含むデザイナー スプレッドシートを作成し、そのスプレッドシートを Aspose.Cells で開くことができます。

### **コピー方法の使用**

Aspose.Cells を使用すると、開発者は、条件付き書式設定をワークシート内のあるセルから別のセルにコピーできます。[**範囲.コピー()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index)方法。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **実行時に条件付き書式を適用する**

Aspose.Cells を使用すると、実行時に条件付き書式を追加および削除できます。以下のコード サンプルは、条件付き書式を設定する方法を示しています。

1. ワークブックをインスタンス化します。
1. 空の条件付き書式を追加します。
1. フォーマットを適用する範囲を設定します。
1. フォーマット条件を定義します。
1. ファイルを保存します。

この例の後には、フォント設定、境界線設定、およびパターンを適用する方法を示す他のいくつかの小さな例が続きます。

Microsoft Excel 2007 では、Aspose.Cells もサポートする、より高度な条件付き書式が追加されました。ここの例は、単純な書式設定の使用方法を示しています。Microsoft Excel 2007 の例は、より高度な条件付き書式を適用する方法を示しています。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **フォントの設定**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

フォント スタイル、テキストの色、下線のスタイル、取り消し線のスタイルのみを変更できます。

{{% /alert %}}

### **境界線を設定**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

輪郭線には細い線のスタイルのみを使用できます。対角線は使用できません。

{{% /alert %}}

### **パターンの設定**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **先行トピック**
- [色スケールおよび 3 色スケールの条件付き書式の追加](/cells/ja/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [高度な条件付き書式を適用する](/cells/ja/net/apply-advanced-conditional-formatting/)
- [ワークシートに条件付き書式を適用する](/cells/ja/net/apply-conditional-formatting-in-worksheets/)
- [条件付き書式を使用して交互の行と列に陰影を適用する](/cells/ja/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [条件付き書式の DataBars 画像を生成する](/cells/ja/net/generate-conditional-formatting-databars-images/)
- [条件付き書式で使用されるアイコン セット、データ バー、またはカラー スケール オブジェクトを取得する](/cells/ja/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

