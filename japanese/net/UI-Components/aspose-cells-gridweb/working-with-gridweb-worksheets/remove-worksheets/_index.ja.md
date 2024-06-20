---
title: ワークシートの削除
type: docs
weight: 30
url: /ja/net/aspose-cells-gridweb/remove-worksheets/
keywords: GridWeb,remove,remove GridWorksheet,remove worksheet
description: この記事では、GridWebでワークシート（GridWorksheet）を削除する方法について紹介します。
---

{{% alert color="primary" %}} 

このトピックでは、Aspose.Cells.GridWeb APIを使用してMicrosoft Excelファイルからワークシートを削除する方法についての情報を提供します。シートのインデックスまたは名前を指定してワークシートを削除することが可能です。

{{% /alert %}} 
## **ワークシートの削除**
### **シートインデックスの使用**
GridWorksheetCollectionのRemoveAtメソッドでシートのインデックスを指定してワークシートを削除する方法を以下のコードに示します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingIndex.cs" >}}
### **シート名を使用する**
GridWorksheetCollectionのRemoveAtメソッドでシートの名前を指定してワークシートを削除する方法を以下のコードに示します。



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RemoveWorksheets.aspx-RemoveWorksheetUsingName.cs" >}}

{{% alert color="primary" %}} 

ワークシートの参照またはインスタンスを使用してワークシートを削除することも可能です。その場合、GridWorksheetCollectionのRemoveメソッドを使用します。このアプローチは一般的に使用されます。

{{% /alert %}}
