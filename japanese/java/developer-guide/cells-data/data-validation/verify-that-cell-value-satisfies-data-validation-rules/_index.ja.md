---
title: Cell 値がデータ検証ルールを満たしていることを確認する
type: docs
weight: 90
url: /ja/java/verify-that-cell-value-satisfies-data-validation-rules/
---
{{% alert color="primary" %}}

Microsoft Excel では、ユーザーがワークシートのセルにデータ検証ルールを追加できます。たとえば、10 から 20 の間の数値を制限するために、10 進数の検証を適用できます。この指定された範囲外の数値が入力された場合、Microsoft Excel はエラー メッセージを表示し、ユーザーに正しい範囲の数値を再入力するように求めます。ユーザーが 3 などの数字をコピーしてセルに貼り付けると、Excel は検証チェックを実行しないか、エラー メッセージを表示しません。

{{% /alert %}}

## Cell 値がデータ検証ルールを満たしていることを確認する

場合によっては、特定の値がセルに適用されるデータ検証ルールを満たしているかどうかを動的に検証する必要があります。この目的のために、Aspose.Cells API は[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ） 方法。セルの値が、そのセルに適用されたデータ検証規則を満たさない場合は、戻り値が返されます。**間違い**、 それ以外**真実**.

次のサンプル Microsoft Excel ファイルは、以下のサンプル コードで使用され、[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ） 方法。スナップショットでわかるように、セルは**C1**もっている**小数データの検証**適用され、値のみを受け入れます**10から20の間**.セルの値が 10 から 20 の間にあるときはいつでも、[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) メソッドが返されます**真実**、それ以外の場合は戻ります**間違い**.

![todo:画像_代替_文章](verify-that-cell-value-satisfies-data-validation-rules_1.png)

次のサンプル コードは、[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ）メソッドが機能します。まず、値 3 を C1 に入力します。これはデータ検証規則を満たさないため、[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) メソッドが返す**間違い**.次に、値 15 を C1 に入力します。この値はデータ検証ルールを満たしているため、[**cell.getValidationValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue() ) メソッドが返す**真実** .同様に、それは戻ります**間違い**値 30 の場合。

## Cell 値がデータ検証ルールを満たしているかどうかを検証するための Java コード

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## サンプル コードによって生成されたコンソール出力

上記のサンプル Excel ファイルでサンプル コードを実行したときに生成されるコンソール出力を次に示します。

{{< highlight "java" >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
