---
title: 行内の最大列インデックスと列内の最大行インデックスの取得
type: docs
weight: 600
url: /ja/nodejs-cpp/get-max-index-in-row-and-column/
description: Aspose.Cells for Node.js via C++ APIを使用して行の最大列インデックスと列の最大行インデックスを取得する方法を学ぶ。
keywords: Node.jsを用いたC++での行の最大列インデックス取得、列の最大行インデックス取得、行の最大データ列インデックス取得、列の最大データ行インデックス取得。
---

## **可能な使用シナリオ**
行や列の一部のデータを操作するだけの場合、行列範囲のデータ範囲を知る必要があります。Aspose.Cells for Node.js via C++はこの機能を提供します。行の最大列インデックスを取得するには、[**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)と[**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)メソッドを使用し、その後[**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)メソッドを使って最大列インデックスと最大データ列インデックスを取得します。列の最大行インデックスと最大行データインデックスを取得するには、列に範囲を作成し、その範囲をトラバースして最後のセルを見つけ、最終的にセルの[**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)メソッドを呼び出します。

Aspose.Cells for Node.js via C++は、次のプロパティとメソッドを提供して、あなたの目標を達成するのに役立ちます。
- [**Row.getLastCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastCell--)
- [**Row.getLastDataCell()**](https://reference.aspose.com/cells/nodejs-cpp/row/#getLastDataCell--)
- [**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)
- [**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)

## **行の最大列インデックスと列の最大行インデックスを取得**
この例では、次のことができます:

1. [サンプルファイル](sample.xlsx)をロードする。
1. 最大列インデックスと最大データ列インデックスを取得する行を取得します。
1. セルの[**Cell.getColumn()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getColumn--)メソッドを呼び出します。
1. 列に基づいて範囲を作成します。
1. イテレータを取得して範囲をトラバースします。
1. セルの[**Cell.getRow()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getRow--)メソッドを呼び出します。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-max-index-in-row-and-column.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
