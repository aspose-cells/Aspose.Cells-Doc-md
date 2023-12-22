---
title: Cell 値がデータ検証ルールを満たしていることを確認する
type: docs
weight: 210
url: /ja/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for .NET API を通じて Cell の値がデータ検証ルールを満たしていることを確認する方法を学習します。
keywords: Get Cell Validation Value, Obtain Cell Validation Value, Verify whether a value satisfies the data validation rules applied to the cell
---
{{% alert color="primary" %}} 

Microsoft Excel では、ユーザーがデータ検証ルールをセルに追加できます。たとえば、10 進数の検証では、10 から 20 までの数値のみを入力できるように指定されます。ユーザーが別の番号を入力した場合。 Microsoft Excel にエラー メッセージが表示され、正しい範囲の数値を入力するよう求められます。数値 (たとえば 3) をコピーしてセルに貼り付けても、Excel では入力チェックは実行されず、エラー メッセージも表示されません。

場合によっては、値がプログラム的にセルに適用されるデータ検証ルールを満たしているかどうかを確認する必要があります。たとえば上記の場合、エントリは失敗するはずです。

{{% /alert %}} 
##  **導入**
 Aspose.Cells は、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)セル値をプログラム的に検証するメソッド。セル内の値がそのセルに適用されるデータ検証ルールを満たさない場合は *False** を返し、それ以外の場合は *True** を返します。

次のサンプル コードは、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドは機能します。まず、C1 に値 3 を入力します。これはデータ検証ルールを満たさないため、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドの戻り値**間違い**。次に、値 15 を C1 に入力します。この値はデータ検証ルールを満たしているため、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) メソッドは **True** を返します。同様に、**False を返します。**値 30 の場合。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
###  **出力**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
