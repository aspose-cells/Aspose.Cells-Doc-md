---
title: ワークブックのAutoRecoverプロパティを設定する方法
type: docs
weight: 220
url: /ja/python-net/how-to-set-autorecover-property-of-workbook/
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NETを使用して、ワークブックのAutoRecoverプロパティを設定できます。このプロパティのデフォルト値は**true**です。これを**false**に設定すると、Microsoft ExcelはそのExcelファイルの自動回復（オートセーブ）を無効にします。

Aspose.Cells for Python via .NETは、このオプションを有効または無効にするための[**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover)プロパティを提供します。

{{% /alert %}}

次のコードは、ワークブックの[**Workbook.settings.auto_recover**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/auto_recover)プロパティの使い方を示しています。最初にこのプロパティのデフォルト値（**true**）を読み取り、その後**false**に設定してワークブックを保存します。次に、再度ワークブックを読み取り、このプロパティの値（この場合は**false**）を確認します。

## ブックのAutoRecoverプロパティを設定するC#コード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "WorkbookSettings-SetAutoRecovery.py" >}}

## **出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
