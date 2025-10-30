---
title: ファイルをマージする方法をGO言語とC++経由で学びます
linktitle: ファイルの結合
type: docs
weight: 20
url: /ja/go-cpp/merge-files/
description: Aspose.Cells for C++を使用してExcelファイルを効率よく結合する方法を学びます。
---

## **紹介**

Aspose.Cellsはファイルのマージにさまざまな方法を提供しています。データ、書式設定、数式を含むシンプルなファイルには [**Workbook.Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/) 方法が複数のブックを結合するのに適しており、[**Worksheet.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/copy/) 方法はシートを新しいブックにコピーするのに適しています。これらの方法は使いやすく効果的ですが、多数のファイルをマージする場合、システムリソースを大量に使用することがあります。これを避けるために、より効率的な [**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/mergefiles/) 静的メソッドを使用します。

## **Aspose.Cellsを使用してファイルをマージする**

以下のサンプルコードは、[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/) メソッドを使用して大きなファイルをマージする例です。Book1.xlsとBook2.xlsの2つの大きなファイルを対象とし、それらには書式設定済みのデータと数式のみが含まれています。

{{% alert color="primary" %}}

[**CellsHelper.MergeFiles**](https://reference.aspose.com/cells/go-cpp/cellshelper/mergefiles/)メソッドはデータ、スタイル、フォーマット、数式のマージのみをサポートします。チャートや画像、コメントなどのオブジェクトはこの方法ではマージされないことがあります。また、一時データを保存するキャッシュファイルが使用されます。

{{% /alert %}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeFiles.go" >}}
