---
title: セルに数式を追加する
type: docs
weight: 30
url: /ja/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop,formula
description: 本記事では、GridDesktopのワークシートのセルに数式を取得または設定する方法について紹介します。
---

{{% alert color="primary" %}} 

セルには、数値やテキストのような単純な値だけでなく、その値として数式も含めることができます。 セルの値がいくつかの計算の結果で決定される必要がある場合に数式が使用されます。 このトピックでは、セルに適用された数式にアクセスおよび変更する方法について説明します。

{{% /alert %}} 
## **セルに数式を追加する**
セルに数式を追加することは、前のトピックで説明したセルの値を設定するのと同じように行います：[セルの値にアクセスして変更する](/cells/ja/net/accessing-and-modifying-the-value-of-a-cell/) ただし、その場合は、単純な値をセルに追加しただけでした。 ここでは、数式を追加します。 開発者は、セルの**Value**プロパティを使用して数式にアクセスおよび変更することができます。また、セルの**SetCellValue**メソッドを使用してセルに数式を追加または変更できます。

**重要:** セルの **Value** プロパティを使用するか、**SetCellValue** メソッドを使用するかの基本的な違いは、**Value** プロパティがGridの **RunAllFormulas** メソッドを自動的に呼び出してすべての数式の値を再計算するのに対し、**SetCellValue** メソッドでは開発者がセルに数式を追加した後に **RunAllFormulas** メソッドを明示的に呼び出す必要があります。実際、**SetCellValue** メソッドを使用すると、このメソッドがセルの値を **FormulaType** にのみ設定し、数式を計算しません。さらに、毎回 **RunAllFormulas** メソッドを呼び出す必要はありません。ワークシートのセルに多くの数式を追加したい場合は、最後に一度だけ **RunAllFormulas** メソッドを呼び出すことができます。

数式は文字列値としてセルに追加されます。さらに、数式の構造はMS Excelの数式の構造と互換性がある必要があります。すべての数式は **等号(=)** で始まらなければなりません。

以下の例では、ワークシートの2つのセルの値を掛け合わせた数式を追加し、その結果を別のセルに保存しました。最後に **RunAllFormulas** メソッドも呼び出されています。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



アプリケーションを実行します。数式が追加されたセルをダブルクリックすると、バックエンドで値を計算している実際の数式に値が置き換えられることに気付くでしょう。

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop はMS Excelの一般に使用される関数のほとんどをサポートしています。サポートされている関数のリストの詳細については、[こちらをクリックしてください。](/cells/ja/net/list-of-supported-functions/)

{{% /alert %}}
