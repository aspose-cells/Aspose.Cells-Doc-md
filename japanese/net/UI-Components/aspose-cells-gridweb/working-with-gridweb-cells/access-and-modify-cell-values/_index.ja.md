---
title: セルの値へのアクセスと変更
type: docs
weight: 20
url: /ja/net/aspose-cells-gridweb/access-and-modify-cell-value/
keywords: GridWeb、セルの値、変更、値
description: この記事では、GridWebを使用してセルの値を取得および変更する方法について紹介します。
---

{{% alert color="primary" %}} 

[ワークシートセルへのアクセス](/cells/ja/net/aspose-cells-gridweb/access-worksheet-cells/)では、セルへのアクセスについて説明しています。このトピックでは、Aspose.Cells.GridWeb APIを使用してセルの値にアクセスおよび変更する方法を示します。

{{% /alert %}} 
## **セルの値のアクセスおよび変更**
### **文字列の値**
セルの値にアクセスし変更する前に、セルへのアクセス方法について知る必要があります。セルへのアクセス方法の詳細については、[ワークシートセルへのアクセス](/cells/ja/net/aspose-cells-gridweb/access-worksheet-cells/) を参照してください。

各セルには、StringValueというプロパティがあります。セルにアクセスした後、開発者はStringValueプロパティを使用してセルの文字列値にアクセスできます。セルの値を変更するには、セルの文字列値を更新するための特別なPutValueメソッドが提供されており、これを使用してセルの文字列値を更新できます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellStringValue.cs" >}}
### **すべての種類の値**
セルのオブジェクトのPutValueメソッドには8つのオーバーロードがあり、セル内の任意のタイプの値（Boolean、int、double、DateTime、およびstring）を変更するために使用できます。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellIntValue.cs" >}}



PutValueメソッドのオーバーロードバージョンもあり、任意のkind of valueを文字列形式で受け取り、自動的に適切なデータ型に変換できます。これを実現するには、PutValueメソッドの別のパラメーターにtrueというBoolean値を渡します。以下の例に示すように。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-ModifyCells.aspx-AddCellDoubleValue.cs" >}}
