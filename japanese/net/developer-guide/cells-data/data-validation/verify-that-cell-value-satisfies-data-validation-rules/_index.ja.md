---
title: セルの値がデータ検証ルールを満たしているかを確認
type: docs
weight: 210
url: /ja/net/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for .NET APIを介してセルの値がデータ検証ルールを満たしているかを学びます。
keywords: セル検証値を取得し、セル検証値を取得し、セルに適用されたデータ検証ルールを値が満たしているかを検証します
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ユーザーはセルにデータ検証ルールを追加できます。たとえば、10から20までの数値しか入力できないようにする検証を追加します。ユーザーが異なる数値を入力した場合、Excelはエラーメッセージを表示して正しい範囲の数値を入力するよう促します。数値をコピーして貼り付けた場合、Excelは検証チェックを実行せず、エラーメッセージを表示しません。

時には、プログラムでセルに適用されたデータ検証ルールが値を満たしているかどうかを検証する必要があります。たとえば、上記の場合、エントリが失敗する必要があります。

{{% /alert %}} 
## **紹介**
Aspose.Cellsは、セルの値をプログラムで検証するための[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドを提供しています。セルの値がそのセルに適用されたデータ検証ルールを満たさない場合、**False**を返し、満たす場合は**True**を返します。

次のサンプルコードは、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドの動作を説明しています。まず、C1に値3を入力します。これはデータ検証ルールを満たさないため、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドは**False**を返します。その後、C1に値15を入力します。この値はデータ検証ルールを満たすため、[Cell.GetValidationValue()](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue)メソッドは**True**を返します。同様に、値30に対しては**False**を返します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}
### **出力**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
