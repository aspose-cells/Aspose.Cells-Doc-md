---
title: ワークブックのAutoRecoverプロパティを設定する方法
type: docs
weight: 220
url: /ja/net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してブックのAutoRecoverプロパティを設定できます。このプロパティのデフォルト値は**true**です。ブックに**false**を設定すると、Microsoft ExcelはそのExcelファイルのAutoRecover（自動保存）を無効にします。

Aspose.Cellsは、このオプションを有効または無効にするための[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)プロパティを提供しています。

{{% /alert %}}

以下のコードは、ブックの[**Workbook.Settings.AutoRecover**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/autorecover)プロパティの使用方法を説明しています。コードはまずこのプロパティのデフォルト値である**true**を読み取り、それを**false**と設定してブックを保存します。その後、ブックを再度読み取り、このプロパティの値を読み取ります。この時点での値は**false**です。

## ブックのAutoRecoverプロパティを設定するC#コード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-SetAutoRecovery-SetAutoRecovery.cs" >}}

## **出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
