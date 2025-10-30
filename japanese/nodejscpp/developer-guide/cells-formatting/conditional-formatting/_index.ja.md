---  
title: ExcelとODSファイルの条件付き書式を設定する
linktitle: 条件付き書式  
type: docs  
weight: 60  
url: /ja/nodejs-cpp/conditional-formatting/  
description: Node.js経由のC++でExcelとODSファイルに条件付き書式を適用する方法。  
keywords: Node.jsで条件付き書式をC++経由で適用  
---  

## **紹介**

条件付き書式は、高度な機能で、セルまたはセル範囲に書式を適用し、その書式がセルの値や式の値に応じて変化します。例えば、セルの値が500より大きい場合にのみ太字を表示することができます。 条件を満たすと指定された書式がセルに適用され、条件を満たさない場合は標準の書式が使用されます。Microsoft Excelでは、**書式**を選択し、次に**条件付き書式**をクリックして条件付き書式のダイアログを開きます。

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

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **ランタイムで条件付き書式を適用**

Aspose.Cells では、条件付き書式をランタイムで追加および削除することができます。以下のコードサンプルでは、条件付き書式の設定方法を示しています。

1. ワークブックをインスタンス化してください。
1. 空の条件付き書式を追加してください。
1. 書式を適用する範囲を設定してください。
1. 書式の条件を定義してください。
1. ファイルを保存します。

この後に、フォント設定や罫線設定、パターン設定などの他の小さな例が続きます。

Microsoft Excel 2007はより高度な条件付き書式を追加し、Aspose.Cellsもサポートしています。ここでは簡単な書式設定の例を示し、Microsoft Excel 2007の例ではより高度な条件付き書式の適用方法を示します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **フォントの設定**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

フォントスタイル、テキストの色、下線スタイル、取り消し線スタイルのみを変更できます。

{{% /alert %}}

### **境界線の設定**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

アウトラインの境界線には細い線種のみ使用できます。斜線は許可されていません。

{{% /alert %}}

### **パターンの設定**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **高度なトピック**  
- [2色系規則と3色系規則の条件付き書式設定を追加する](/cells/ja/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [ワークシートで条件付き書式設定を適用する](/cells/ja/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [条件付き書式設定を使用して、交互に行と列に影を付ける](/cells/ja/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [条件付き書式データバーイメージの生成](/cells/ja/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [条件付き書式で使用されるアイコンセット、データバー、またはカラースケールオブジェクトの取得](/cells/ja/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
