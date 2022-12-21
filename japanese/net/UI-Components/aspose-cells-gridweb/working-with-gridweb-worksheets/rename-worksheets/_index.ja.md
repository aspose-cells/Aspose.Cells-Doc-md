---
title: ワークシートの名前を変更
type: docs
weight: 40
url: /ja/net/rename-worksheets/
---
{{% alert color="primary" %}} 

ワークシートの名前を変更すると、Aspose.Cells.GridWeb で多くのワークシートを操作し、それらの名前をより意味のあるものに変更する場合に非常に便利です。たとえば、請求書を含むワークシートの名前を Sheet1 ではなく Invoice に変更できます。このトピックでは、この単純ですが便利な機能について説明します。

{{% /alert %}} 
## **ワークシートの名前変更**
すべてのワークシートには、開発者がワークシートの名前にアクセスまたは変更できる Name プロパティが含まれています。ワークシートの名前を変更するには:

1. GridWorksheetCollection からワークシートにアクセスします。
1. 選択したワークシートの名前を変更します。



{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb のワークシートへのアクセス方法の詳細については、こちらを参照してください。[ワークシートへのアクセス](/cells/ja/net/access-worksheets/).

{{% /alert %}} 

コードを実行する前は、ワークシートには Sheet1 などの既定の名前が付けられています。

**入力ファイル: デフォルト名が Sheet1 のワークシート** 

![todo:画像_代替_文章](rename-worksheets_1.png)

コードを実行すると、ワークシートの名前が Students に変更されます。

**出力: ワークシートの名前が Students に変更されます** 

![todo:画像_代替_文章](rename-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}
