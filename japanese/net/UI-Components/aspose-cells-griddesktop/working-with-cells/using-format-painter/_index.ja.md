---
title: フォーマット ペインターの使用
type: docs
weight: 80
url: /ja/net/using-format-painter/
---
{{% alert color="primary" %}} 

書式ペインタは、Aspose.Cells.GridDesktop で採用された MS Excel の機能です。とてもいい機能です。この機能をまだ使用していない人のために、フォーマット ペインターを使用すると、ユーザーはフォーカスされたセルの書式設定を別のセルに適用できます。この機能の実装は非常に簡単です。このトピックでは、それについても説明します。

{{% /alert %}} 
## **フォーマット ペインターの使用**
の特徴**フォーマットペインター**書式設定を他のセルに適用するセルを選択してから呼び出す必要があります。**StartFormatPainter**方法**グリッドデスクトップ**.フォーマット ペインターには、次の 2 つのモードがあります。

- **Format Painter を 1 回使用する**
- **Format Painter を常に使用する**
### **Format Painter を 1 回使用する**
開発者がフォーマット ペインターの機能を 1 回だけ使用して、フォーカスされたセルの書式設定を 1 つのセルに適用したい場合は、呼び出して実行できます。**StartFormatPainter**メソッドと渡す**間違い**それに値します。この**間違い**値は、フォーマット ペインターによる描画を永久に禁止します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### **Format Painter を常に使用する**
複数のセルに書式設定を適用する必要がある場合、常に書式ペインタを使用することは便利な機能です。開発者は、単に呼び出すだけでこの機能を実現できます。**StartFormatPainter**メソッドと渡す**真実**それに値します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


この種のフォーマット ペインターは、私たちが止めない限り永遠に絵を描き続けます。したがって、フォーマットペインターが常にペイントするのを止めるには、単に呼び出すことができます**EndFormatPainter**方法**グリッドデスクトップ**.

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
