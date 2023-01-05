---
title: Cell 値がデータ検証ルールを満たしていることを確認する
type: docs
weight: 210
url: /ja/net/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}} 

Microsoft Excel では、ユーザーがデータ検証ルールをセルに追加できます。たとえば、10 進数の検証では、10 ～ 20 の数字のみを入力できるように指定します。ユーザーが別の番号を入力した場合。 Microsoft Excel にエラー メッセージが表示され、正しい範囲の数値を入力するように求められます。たとえば 3 などの数値をコピーしてセルに貼り付けると、Excel は検証チェックを実行せず、エラー メッセージを表示しません。

場合によっては、プログラムによってセルに適用されるデータ検証規則を値が満たしているかどうかを確認する必要があります。たとえば、上記の場合、エントリは失敗するはずです。

{{% /alert %}} 
## **序章**
Aspose.Cells は[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)プログラムでセル値を検証するメソッド。セルの値が、そのセルに適用されたデータ検証規則を満たさない場合は、戻り値が返されます。**間違い**、 それ以外**真実**.

次のサンプル コードは、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドが動作します。まず、値 3 を C1 に入力します。これはデータ検証規則を満たさないため、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドが返す**間違い**.次に、値 15 を C1 に入力します。この値はデータ検証ルールを満たしているため、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドが返す**真実** .同様に、それは戻ります**間違い**値 30 の場合。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **出力**
{{< highlight "java" >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
