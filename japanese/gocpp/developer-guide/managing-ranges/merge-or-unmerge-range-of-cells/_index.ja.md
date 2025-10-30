---
title: GolangoとC++経由でセルの範囲をマージまたは解除する
linktitle: セル範囲の結合または解除
type: docs
weight: 190
url: /ja/go-cpp/merge-or-unmerge-range-of-cells/
description: Excelのセル範囲をGolangoとC++経由でマージ・解除
keywords: C++を使った範囲内のセルのマージと解除、C++でのセルのマージと解除、C++を使用して範囲内のセルをマージおよび解除、C++とExcelでセルをマージおよび解除する、Excelでセルをマージおよび解除（C++使用）
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してセルの範囲を結合または分割できます。 Aspose.Cellsはこの目的のための[**Range.Merge()**](https://reference.aspose.com/cells/go-cpp/range/merge/)および[**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)メソッドを提供します。この記事では、セルの範囲を単一のセルに結合する方法について説明します。

{{% /alert %}}

## **例**

以下のサンプルコードは、最初に範囲（A1:D4）を作成し、その範囲内のセルを[**Range.Merge()**](https://reference.aspose.com/cells/go-cpp/range/merge/)メソッドを使って1つのセルにマージします。同様に、範囲を作成し、[**Range.UnMerge()**](https://reference.aspose.com/cells/cpp/aspose.cells/range/unmerge/)メソッドを呼び出すことでセルを分割できます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeOrUnmergeRangeOfCells.go" >}}
