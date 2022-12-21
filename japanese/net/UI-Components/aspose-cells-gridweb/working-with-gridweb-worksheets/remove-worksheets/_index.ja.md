---
title: ワークシートを削除
type: docs
weight: 30
url: /ja/net/remove-worksheets/
---
{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridWeb API を使用して Microsoft Excel ファイルからワークシートを削除する方法について説明します。シート インデックスまたは名前を指定して、ワークシートを削除することができます。

{{% /alert %}} 
## **ワークシートの削除**
### **シート インデックスの使用**
次のコードは、GridWorksheetCollection の RemoveAt メソッドでシート インデックスを指定して、ワークシートを削除する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **シート名の使用**
次のコードは、GridWorksheetCollection の RemoveAt メソッドでシート名を指定してワークシートを削除する方法を示しています。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

参照またはインスタンスを使用してワークシートを削除することもできます。これを行うには、GridWorksheetCollection の Remove メソッドを使用します。このアプローチは一般的に使用されます。

{{% /alert %}}
