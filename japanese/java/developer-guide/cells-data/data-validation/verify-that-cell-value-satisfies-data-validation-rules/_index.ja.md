---
title: セルの値がデータ検証ルールを満たしているかを確認
type: docs
weight: 90
url: /ja/java/verify-that-cell-value-satisfies-data-validation-rules/
---

{{% alert color="primary" %}}

Microsoft Excelを使用すると、ワークシートのセルにデータ検証ルールを追加できます。たとえば、10から20の数値を制限するために10進数の検証を適用できます。指定された範囲外の数値を入力すると、Microsoft Excelはエラーメッセージを表示し、正しい範囲から数値を再入力するようユーザーに促します。ユーザーが数値をコピーして貼り付けると、たとえば3といった数値を入力すると、Excelは検証チェックを実行せず、エラーメッセージを表示しません。

{{% /alert %}}

**データ検証ルールを満たしているか確認**

時々、セルに適用されたデータ検証ルールを動的に確認することが必要です。この目的のために、Aspose.Cells APIは[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--)メソッドを提供します。セルの値がそのセルに適用されたデータ検証ルールを満たさない場合、**False**を返し、それ以外の場合は**True**を返します。

以下のサンプルMicrosoft Excelファイルは、下記のサンプルコードで[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--)メソッドをテストするために使用されます。スナップショットでわかるように、セル** C1 **に** 10から20の間 **の値しか受け付けない**10進数のデータ検証**が適用されています。セルの値が10から20の間にある場合、[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--)メソッドは**True**を返し、それ以外の場合は**False**を返します。

![todo:image_alt_text](verify-that-cell-value-satisfies-data-validation-rules_1.png)

以下のサンプルコードは、[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--)メソッドの動作を示しています。まず、C1に値3を入力します。これはデータ検証ルールを満たさないため、[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--)メソッドは**False**を返します。その後、C1に値15を入力します。この値はデータ検証ルールを満たすため、[**cell.getValidationValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue--)メソッドは**True**を返します。同様に、値30に対しては**False**を返します。

**Javaコード：セルの値がデータ検証ルールを満たしているか確認

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyCellValueSatisfiesDataValidationRules-VerifyCellValueSatisfiesDataValidationRules.java" >}}

## サンプルコードによって生成されたコンソール出力

以下は、上記で示されているサンプルExcelファイルを使用してサンプルコードを実行した際に生成されたコンソール出力です。

{{< highlight java >}}

Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
