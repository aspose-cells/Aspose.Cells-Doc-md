---
title: Golangを使ったC++経由でWorkbookの自動回復プロパティを設定する方法
linktitle: ワークブックのAutoRecoverプロパティを設定する方法
type: docs
weight: 220
url: /ja/go-cpp/how-to-set-autorecover-property-of-workbook/
description: ブックの自動回復プロパティを有効または無効にする方法（Aspose.Cells for C++を使用）を学びます。
---

{{% alert color="primary" %}}

Aspose.Cells を使用して、ブックの自動回復プロパティを設定できます。このプロパティのデフォルト値は **true** です。ブックでこれを **false** に設定すると、Microsoft Excel はそのExcelファイルの自動回復（自動保存）を無効にします。

Aspose.Cells は、このオプションを有効または無効にするための [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) プロパティを提供します。

{{% /alert %}}

以下のコードは、ブックの [**Workbook.GetAutoRecover()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getautorecover/) プロパティの使用方法を示しています。最初にこのプロパティのデフォルト値（**true**）を読み取り、その後に **false** に設定し、ブックを保存します。その後、再度ブックを読み取り、このプロパティの値（この時点では **false**）を確認します。

## C++ コード：Workbook の自動回復プロパティを設定

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToSetAutorecoverPropertyOfWorkbook.go" >}}
## **出力**

上記のサンプルコードのコンソール出力は次の通りです。

{{< highlight java >}}

AutoRecover: True

AutoRecover: False

{{< /highlight >}}
