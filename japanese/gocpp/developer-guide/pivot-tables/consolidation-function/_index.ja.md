---
title: Golang経由でC++を使った集約関数
linktitle: 統合機能
type: docs
weight: 20
url: /ja/go-cpp/consolidation-function/
description: Golang経由でC++を使用してAspose.Cellsでピボットテーブルのデータフィールドに集約関数を適用する方法を学ぶ。
---

## **統合機能**

Aspose.Cellsを使用して、ピボットテーブルのデータフィールド（または値フィールド）に統合機能を適用できます。Microsoft Excelにおいては、値フィールドを右クリックし、 **「値フィールドの設定...」** を選択し、その後 **「値の集計方法」** タブを選択します。そこから、合計、カウント、平均、最大値、最小値、積、重複排除のような任意の統合機能を選択できます。

Aspose.Cellsは、次の統合機能をサポートするための[**ConsolidationFunction**](https://reference.aspose.com/cells/go-cpp/consolidationfunction/)列挙型を提供します。

- ConsolidationFunction::平均
- ConsolidationFunction::カウント
- ConsolidationFunction::数値のカウント
- ConsolidationFunction::異なる値のカウント
- ConsolidationFunction::最大値
- ConsolidationFunction::最小値
- ConsolidationFunction::積
- ConsolidationFunction::標準偏差
- ConsolidationFunction::母標準偏差
- ConsolidationFunction::合計
- ConsolidationFunction::分散
- ConsolidationFunction::母分散

### **ピボットテーブルのデータフィールドに統合機能を適用する**

次のコードは、最初のデータフィールド（または値フィールド）に **平均** の統合機能を適用し、2番目のデータフィールド（または値フィールド）に **重複排除** の統合機能を適用します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

重複排除の統合機能は、Microsoft Excel 2013でのみサポートされています。

{{% /alert %}}
