---  
title: 改行とテキストの折り返し
linktitle: 改行とテキストの折り返し  
description: Aspose.Cellsライブラリを使用したNode.jsにおけるテキストの折り返しとワードラップの実装方法（C++経由）。Aspose.Cellsライブラリを利用すれば、セルにテキストを簡単に挿入し、手動ワードラップや自動ワードラップ等の折り返し方法を設定できます。このドキュメントでは、これらの機能の実装方法とサンプルコードを詳述します。  
keywords: Aspose.Cells、改行、テキスト折り返し、レイアウト Node.js経由のC++  
type: docs  
weight: 60  
url: /ja/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
セル内のテキストが読み取れるようにするために、明示的な改行とテキストの折り返しを適用することができます。テキストの折り返しは、セル内の一行を複数行に変換し、明示的な改行は望む場所に改行を挿入します。  
{{% /alert %}}  

## **セル内でテキストを折り返す**  
セル内でテキストを折り返すには、[**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-)メソッドを使用します。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **明示的な改行を使用する**  
JavaScriptで‘\n’を使用してセル内に明示的な改行を挿入できます。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



