---
title: コントロール内およびコントロールと Excel の間で GridDesktop の行をコピーして貼り付ける
type: docs
weight: 70
url: /ja/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

コントロール内またはコントロールと Excel の間で GridDesktop の行のコピー アンド ペーストを有効にする場合は、GridDesktop.ClipboardCopyPaste プロパティを true に設定してください。このプロパティは、設計時またはコードで設定できます。このプロパティのデフォルト値は false です。現在、セル値のコピーと貼り付けのみが可能で、書式や枠線スタイルなどのセルのその他の設定はコピーされません。

{{% /alert %}} 
## **デザイン モードおよびランタイムでの GridDesktop.ClipboardCopyPaste プロパティの設定**
次のサンプル コードでは、GridDesktop.ClipboardCopyPaste プロパティを設定します。**実行時間**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
