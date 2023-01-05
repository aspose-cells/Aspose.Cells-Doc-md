---
title: ブラウザ ウィンドウで GridWeb のサイズを変更する
type: docs
weight: 40
url: /ja/net/resize-gridweb-in-the-browser-window/
---
## **考えられる使用シナリオ**
Aspose.Cells が必要な場合があります。GridWeb は、ブラウザ ウィンドウに合わせてサイズを変更する必要があります。 GridWeb は常にサイズ (高さ、幅) を調整し、ブラウザー ウィンドウのサイズと互換性がある必要があります。 Aspose.Cells.GridWeb はクライアント側を提供します*サイズ変更()*目的のための機能。さらに、ブラウザー ウィンドウで GridWeb コントロールのサイズを変更することもできます。たとえば、右下のハンドルを (マウスで) 使用して、ウィンドウ内の幅/高さをカスタマイズできます。プロジェクトのページソースで機能させるには、jquery Javascript ファイルを含める/指定する必要もあります。
## **GridWeb の resize メソッドを使用する**
次のコードは、サイズ変更アクションが 100 ミリ秒ごとに実行されているかどうかを確認します。サイズ変更アクションがなくなると、サイズ変更操作が終了したと見なされます。 GridWeb にインポートされたサンプル テンプレート ファイルを使用します。クライアント側のコードを使用して GridWeb のサイズを変更します。スクリーンショットは、ブラウザー ウィンドウのサイズを変更するときに、GridWeb がそれに応じてサイズを変更することを示しています。

![todo:画像_代替_文章](resize-gridweb-in-the-browser-window_1.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-ResizeGridWebUsingResizeMethod" >}}


## **サイズ変更可能なjquery ui機能を使用してGridWebをサイズ変更可能にする**
次のコードは、ブラウザー ウィンドウで GridWeb コントロールのサイズを変更できるようにします。たとえば、右下のハンドルを使用して、ウィンドウ内の GridWeb のサイズをカスタマイズできます。最初に GridWeb にインポートされたものと同じテンプレート ファイルを使用します。 jquery スクリプトを使用して、GridWeb をサイズ変更可能にします。スクリーンショットは、ブラウザー ウィンドウの右下のハンドルを使用して GridWeb のサイズが変更されたことを示しています。

![todo:画像_代替_文章](resize-gridweb-in-the-browser-window_2.png)
### **サンプルコード**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-WorkingWithGridWebClientSideScript-MakingGridWebResizableUsingResizablejQueryUiFeature" >}}
