---
title: ワークシートを追加
type: docs
weight: 20
url: /ja/net/add-worksheets/
---
{{% alert color="primary" %}} 

ワークシートは、Aspose.Cells.GridWeb の不可欠な部分です。すべてのデータは、ワークシートの形式で管理および保存されます。 Aspose.Cells.GridWeb を使用すると、開発者は 1 つ以上のワークシートを Aspose.Cells.GridWeb コントロールに追加できます。このトピックでは、ワークシートを Aspose.Cells.GridWeb に追加する簡単な方法を示します。

{{% /alert %}} 
## **ワークシートの追加**
### **シート名を指定せずに**
ワークシートを Aspose.Cells.GridWeb に追加する最も簡単な方法は、GridWeb コントロールで GridWorksheetCollection コレクションの Add メソッドを呼び出すことです。これにより、既定の名前 (Sheet1、Sheet2、Sheet3 など) を使用するワークシートが作成され、GridWeb コントロールに追加されます。

**出力: デフォルト名のワークシートが GridWeb に追加されました** 

![todo:画像_代替_文章](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 Add メソッドは、このワークシートのインスタンスへのアクセスに使用できる新しいワークシートのインデックスを返します。ワークシートへのアクセス方法の詳細については、次を参照してください。[ワークシートへのアクセス](/cells/ja/net/access-worksheets/).

{{% /alert %}} 
### **シート名指定あり**
既定の名前付けスキームを使用する代わりに、特定の名前を持つワークシートを GridWeb コントロールに追加するには、指定された SheetName を受け取る Add メソッドのオーバーロード バージョンを呼び出します。たとえば、次の例では Invoice という名前のワークシートを追加します。

**出力: 指定した名前のワークシートが GridWeb に追加されました** 

![todo:画像_代替_文章](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

ワークシート名を文字列として受け取る Add メソッドは、GridWorksheet のインスタンスを返します。

{{% /alert %}}
