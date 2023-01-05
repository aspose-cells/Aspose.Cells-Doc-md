---
title: Workbook の AutoRecover プロパティを設定する方法
type: docs
weight: 220
url: /ja/net/how-to-set-autorecover-property-of-workbook/
---
{{% alert color="primary" %}}

Aspose.Cells を使用して、ブックの AutoRecover プロパティを設定できます。このプロパティのデフォルト値は**真実**.設定すると**間違い**ワークブックでは、Microsoft Excel はその Excel ファイルの自動回復 (自動保存) を無効にします。

Aspose.Cells提供[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)このオプションを有効または無効にするプロパティ。

{{% /alert %}}

次のコードは、使用方法を説明しています[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)ブックのプロパティ。コードは最初にこのプロパティのデフォルト値を読み取ります。**真実** 、次にそれを次のように設定します**間違い**ブックを保存します。次に、ワークブックを再度読み取り、このプロパティの値を読み取ります。**間違い**現時点では。

## C# Workbook の AutoRecover プロパティを設定するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **出力**

上記のサンプル コードのコンソール出力を次に示します。

{{< highlight "java" >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
