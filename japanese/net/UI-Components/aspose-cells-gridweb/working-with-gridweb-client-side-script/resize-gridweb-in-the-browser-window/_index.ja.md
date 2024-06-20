---
title: ブラウザウィンドウでGridWebをリサイズする
type: docs
weight: 40
url: /ja/net/aspose-cells-gridweb/resize-gridweb-in-the-browser-window/
keywords: GridWeb,resize
description: この記事では、GridWebのリサイズ方法について紹介します。
---

## **可能な使用シナリオ**
Aspose.Cells.GridWebを常にブラウザウィンドウのサイズに合わせてリサイズする必要がある場合があります。Aspose.Cells.GridWebはそのためにクライアントサイドの*resize()*関数を提供しています。また、ブラウザウィンドウ内でGridWebコントロールをリサイズ可能にすることもできます。例えば、ウィンドウ内で幅や高さをカスタマイズするために、右下のハンドル（マウスを使用）を使用できます。プロジェクトのページソースでそれを機能させるためにjqueryのJavascriptファイルを含める/指定する必要もあります。
## **GridWebのresizeメソッドの使用**
次のコードは、100ミリ秒ごとにリサイズアクションが行われているかどうかをチェックします。リサイズアクションがなくなったら、リサイズ操作が終了したと判断します。GridWebにインポートされたサンプルテンプレートファイルを使用します。GridWebをリサイズするためにクライアントサイドコードを使用します。スクリーンショットには、ブラウザウィンドウのサイズを変更するとGridWebがそれに応じて自動的にリサイズする様子が示されています。

![todo:image_alt_text](resize-gridweb-in-the-browser-window_1.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **jQuery UIのresizable機能を使用してGridWebをリサイズ可能にする**
次のコードを使用すると、GridWebコントロールをブラウザウィンドウ内でリサイズできます。たとえば、GridWebのサイズをブラウザウィンドウ内でカスタマイズするために、右下のハンドルを使用できます。最初にGridWebにインポートされる同じテンプレートファイルを使用します。GridWebをリサイズ可能にするために、jqueryスクリプトを使用します。スクリーンショットは、ブラウザウィンドウ内でGridWebが右下のハンドルを使用してリサイズされたことを示しています。

![todo:image_alt_text](resize-gridweb-in-the-browser-window_2.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
