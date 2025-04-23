---
title: セルの値がデータ検証ルールを満たしているかを確認
type: docs
weight: 210
url: /ja/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for Node.js via C++ APIを通じて、セルの値がデータ検証ルールを満たしているか確認する方法を学びましょう。
keywords: Node.jsからC++を介してセルの検証値を取得する、Node.jsからC++を介してセルの検証値を得る、セルに適用されたデータ検証ルールを満たしているか確認する（Node.js via C++）
---

{{% alert color="primary" %}} 

Microsoft Excelは、セルにデータ検証ルールを追加できるようにしています。例えば、少数点の検証は10から20の間の数値のみを入力可能にします。異なる数字を入力した場合、Excelはエラーメッセージを表示し、正しい範囲の数字を入力するよう促します。数字をコピー＆ペーストした場合、検証は行われずエラーメッセージも表示されません。

時には、プログラムでセルに適用されたデータ検証ルールが値を満たしているかどうかを検証する必要があります。たとえば、上記の場合、エントリが失敗する必要があります。

{{% /alert %}} 
## **紹介**
Aspose.Cells for Node.js via C++は、[Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--)メソッドを提供し、プログラムmaticallyセルの値を検証します。セルの値が適用されたデータ検証ルールを満たさない場合は**false**を返し、満たす場合は**true**を返します。

以下のサンプルコードは、[Cell.getValidationValue()](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--)メソッドの動作例を示しています。まず、C1に値3を入力します。この値はデータ検証ルールを満たさないため、メソッドは**false**を返します。その後、値15をC1に入力すると、この値はルールを満たすため、メソッドは**true**を返します。同様に、値30では**false**となります。

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-VerifyValidationCellValues.js" >}}


### **出力**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
