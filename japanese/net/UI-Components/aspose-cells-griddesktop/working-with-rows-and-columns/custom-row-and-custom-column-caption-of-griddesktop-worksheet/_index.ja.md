---
title: GridDesktop ワークシートのカスタム行とカスタム列のキャプション
type: docs
weight: 120
url: /ja/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/
---
## **考えられる使用シナリオ**
GridDesktop ワークシートの行と列のキャプションをカスタマイズできます。通常、行は 1 から始まり、列は A から始まります。この動作を変更して、GridDesktop ワークシートの行と列に独自のキャプションを使用できます。行と列のキャプションを変更するには、ICustomRowCaption および ICustomColumnCaption インターフェイスを実装してください。
## **GridDesktop ワークシートのカスタム行とカスタム列のキャプション**
次のサンプル コードは、ICustomRowCaption および ICustomColumnCaption インターフェイスを実装し、行と列のキャプションを変更します。スクリーンショットは、参考のためにこのサンプル コードの実行結果を示しています。



![todo:画像_代替_文章](custom-row-and-custom-column-caption-of-griddesktop-worksheet_1.png)

## **サンプルコード**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples-GridDesktop-CSharp-WorkingWithRowsandColumns-Form_CustomRowAndCustomColumnCaptionOfGridDesktopWorksheet.cs" >}}
