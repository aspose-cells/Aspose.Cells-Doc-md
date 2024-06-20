---
title: セルの値がデータ検証ルールを満たしているかを確認
type: docs
weight: 210
url: /ja/python-net/verify-that-cell-value-satisfies-data-validation-rules/
description: Aspose.Cells for Python via .NET API を通じて、セルの値がデータのバリデーション規則を満たしているかどうかを確認する方法を学びます。
keywords: Python Excel ライブラリ、Python でセルのバリデーション値を取得する、Python でセルのバリデーション値を取得する、Python でセルのバリデーションルールを満たすかどうかを検証する
---

{{% alert color="primary" %}} 

Microsoft Excelでは、ユーザーはセルにデータ検証ルールを追加できます。たとえば、10から20までの数値しか入力できないようにする検証を追加します。ユーザーが異なる数値を入力した場合、Excelはエラーメッセージを表示して正しい範囲の数値を入力するよう促します。数値をコピーして貼り付けた場合、Excelは検証チェックを実行せず、エラーメッセージを表示しません。

時には、プログラムでセルに適用されたデータ検証ルールが値を満たしているかどうかを検証する必要があります。たとえば、上記の場合、エントリが失敗する必要があります。

{{% /alert %}} 
## **紹介**
Aspose.Cells for Python via .NET は、セルの値がプログラムでデータバリデーションルールを満たしているかを検証するための [Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) メソッドを提供しています。セルの値がそのセルに適用されたデータバリデーションルールを満たさない場合、**False** を返し、それ以外の場合は**True** を返します。

次のサンプルコードは、[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) メソッドがどのように機能するかを示しています。最初に、値3をC1に入力します。これはデータバリデーションルールを満たさないため、[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) メソッドは**False**を返します。次に、値15をC1に入力します。この値はデータバリデーションルールを満たすため、[Cell.get_validation_value()](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_validation_value/#) メソッドは**True**を返します。同様に、値30については**False** を返します。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-DataValidationRules-1.py" >}}

### **出力**
{{< highlight java >}}

 Is 3 a Valid Value for this Cell: False

Is 15 a Valid Value for this Cell: True

Is 30 a Valid Value for this Cell: False

{{< /highlight >}}
