---
title: Golangを使用してC++経由でセルの値がデータ検証ルールを満たしているかどうかを確認します
linktitle: セルの値がデータ検証ルールを満たしているかを確認
type: docs
weight: 210
url: /ja/go-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for C++ APIを通じてセル値がデータ検証ルールを満たしているか確認する方法を学びます。
keywords: セル検証値を取得し、セル検証値を取得し、セルに適用されたデータ検証ルールを値が満たしているかを検証します
---

{{% alert color="primary" %}} 

Microsoft Excelは、セルにデータ検証ルールを追加できるようにしています。例えば、少数点の検証は10から20の間の数値のみを入力可能にします。異なる数字を入力した場合、Excelはエラーメッセージを表示し、正しい範囲の数字を入力するよう促します。数字をコピー＆ペーストした場合、検証は行われずエラーメッセージも表示されません。

時には、プログラムでセルに適用されたデータ検証ルールが値を満たしているかどうかを検証する必要があります。たとえば、上記の場合、エントリが失敗する必要があります。

{{% /alert %}} 

## **紹介**
Aspose.Cellsは、プログラムでセルの値を検証するための[Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/)メソッドを提供します。セル内の値がそのセルに適用されたデータ検証ルールを満たさない場合、Falseを返し、満たす場合はTrueを返します。

次のサンプルコードは、[Cell.GetValidationValue()](https://reference.aspose.com/cells/go-cpp/cell/getvalidationvalue/)メソッドの動作例を示しています。まず、C1に値3を入力します。この値は検証ルールを満たしていないため、Cell.GetValidationValue()メソッドはFalseを返します。次に、値15をC1に入力します。この値は検証ルールを満たしているため、Cell.GetValidationValue()はTrueを返します。同様に、30の場合はFalseを返します。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-VerifyThatCellValueSatisfiesDataValidationRules.go" >}}
### **出力**
{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
