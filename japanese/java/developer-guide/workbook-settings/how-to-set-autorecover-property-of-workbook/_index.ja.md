---
title: Workbook の AutoRecover プロパティを設定する方法
type: docs
weight: 160
url: /ja/java/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

Aspose.Cells を使用して、ブックの AutoRecover プロパティを設定できます。このプロパティのデフォルト値は**真実**.設定すると**間違い**ワークブックでは、Microsoft Excel はその Excel ファイルの自動回復 (自動保存) を無効にします。

Aspose.Cells提供[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)このオプションを有効または無効にするプロパティ。

{{% /alert %}}

## Java Workbook の AutoRecover プロパティを設定するコード

次のコードは、使用方法を説明しています[**Workbook.getSettings().setAutoRecover()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#AutoRecover)ブックのプロパティ。コードは最初にこのプロパティのデフォルト値を読み取ります。**真実** 、次にそれを次のように設定します**間違い**ブックを保存します。次に、ワークブックを再度読み取り、この時点で false であるこのプロパティの値を読み取ります。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SetAutoRecoverProperty-SetAutoRecoverProperty.java" >}}

## サンプル コードによって生成される出力

上記のサンプル コードのコンソール出力を次に示します。

{{< highlight "java" >}}

AutoRecover: true

AutoRecover: false

{{< /highlight >}}
