---
title: Cell 値へのアクセスと変更
type: docs
weight: 20
url: /ja/net/access-and-modify-cell-values/
---
{{% alert color="primary" %}} 

[アクセス ワークシート Cells](/cells/ja/net/access-worksheet-cells/)セルへのアクセスについて説明しました。このトピックでは、その説明を拡張して、Aspose.Cells.GridWeb API を使用してセル値にアクセスして変更する方法を示します。

{{% /alert %}} 
## **Cell の値へのアクセスと変更**
### **文字列値**
セルの値にアクセスして変更する前に、セルへのアクセス方法を知っておく必要があります。セルにアクセスするためのさまざまなアプローチの詳細については、次を参照してください。[アクセス ワークシート Cells](/cells/ja/net/access-worksheet-cells/).

各セルには、StringValue という名前のプロパティがあります。セルにアクセスすると、開発者は StringValue プロパティを使用してセルの文字列値にアクセスできます。セル値を変更するために、セルの文字列値を更新するために使用できる特別なメソッド PutValue が提供されています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **すべてのタイプの値**
セルのオブジェクトの PutValue メソッドには、セル内の任意のタイプの値 (Boolean、int、double、DateTime、および string) を変更するために使用できる 8 つのオーバーロードがあります。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



文字列形式の任意の種類の値を取得し、適切なデータ型に自動的に変換できる、PutValue メソッドのオーバーロードされたバージョンもあります。これを実現するには、以下の例に示すように、ブール値 true を PutValue メソッドの別のパラメーターに渡します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
