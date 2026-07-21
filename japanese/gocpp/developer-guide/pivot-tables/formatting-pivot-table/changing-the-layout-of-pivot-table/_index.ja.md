---
title: Golang経由でC++を使ったピボットテーブルのレイアウト変更
linktitle: ピボットテーブルのレイアウトを変更する
type: docs
weight: 10
url: /ja/go-cpp/changing-the-layout-of-pivot-table/
description: Aspose.Cells for C++を使用して、コンパクト、アウトライン、タブラー形式でピボットテーブルのレイアウトを変更する方法を学びます。
---

{{% alert color="primary" %}}

Microsoft Excelでは、*ピボットテーブルツール > デザイン > レポートレイアウト* メニューコマンドを使用してピボットテーブルのレイアウトを変更できます。これらの三つの形式に変更可能です：

- コンパクト形式で表示
- アウトライン形式で表示
- 表形式で表示

Aspose.Cellsは、[**PivotTable.ShowInCompactForm()**](https://reference.aspose.com/cells/go-cpp/pivottable/showincompactform/)、[**PivotTable.ShowInOutlineForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showinoutlineform/)、および [**PivotTable.ShowInTabularForm()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/showintabularform/) のメソッドを提供して、これら三つの形式でピボットテーブルのレイアウトを変更します。

{{% /alert %}}

次のサンプルコードは、最初にピボットテーブルを【コンパクト形式】で表示し、その後【アウトライン形式】で、最後に【タブラー形式】で表示します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ChangingTheLayoutOfPivotTable.go" >}}
