---
title: フォーマットのコピーを使用する
type: docs
weight: 80
url: /ja/net/aspose-cells-griddesktop/use-format-painter/
keywords: GridDesktop,format painter
description: この記事では、GridDesktopのフォーマットペインターについて紹介します。
---

{{% alert color="primary" %}} 

フォーマットペインターは、MS Excelの機能であり、Aspose.Cells.GridDesktopにも採用されています。非常に便利な機能です。これをまだ使用したことのない人々のために、フォーマットペインターは、ユーザーが任意のフォーカスされたセルの書式設定を別のセルに適用できるようにします。この機能の実装は非常に簡単です。このトピックでは、それもカバーします。

{{% /alert %}} 
## **フォーマットペインターの使用**
**フォーマットペインター**の機能は、ユーザーが他のセルに適用したい書式設定を持つセルを選択し、**GridDesktop**で**StartFormatPainter**メソッドを呼び出すことを要求します。フォーマットペインターには以下の2つのモードがあります：

- **フォーマットペインターを一度のみ使用**
- **常に書式のコピーを使用する**
### **書式のコピーを1回使用する**
開発者がフォーマットペインターの機能を1回だけ使用して、焦点を当てたセルの書式設定を単一のセルに適用する場合は、**StartFormatPainter**メソッドを呼び出して**false**値を渡すことで実現できます。この**false**値は、フォーマットペインターが永久にペイントするのを禁止します。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseOnce.cs" >}}
### ****常にフォーマットペインターを使用する****
フォーマットペインターを常に使用する場合、1つ以上のセルに書式設定を適用する必要があるときに便利な機能です。開発者は、単に**StartFormatPainter**メソッドを呼び出して**true**値を渡すことでこの機能を実現できます。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-UseAlways.cs" >}}


この種のフォーマットペインターは停止するまで常にペイントし続けます。したがって、フォーマットペインターを常にペイントするのを停止する場合は、**GridDesktop**の**EndFormatPainter**メソッドを呼び出すだけで済みます。

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingFormatPainter-EndUse.cs" >}}
