---
title: パブリック API Aspose.Cells 8.7.1 の変更点
type: docs
weight: 250
url: /ja/java/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.7.0 から 8.7.1 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **LookInType.ORIGINAL_VALUES プロパティを追加**
Aspose.Cells API はすでに[データの検索または検索](/cells/ja/java/find-or-search-data/)セル値と数式で特定のコンテンツを見つけるためのスプレッドシートの機能。ただし、この機能には、セルに適用される書式設定の側面が欠けていたため、内容の値だけでなく外観も変更される可能性があり、その結果、元の値を使用してテキストを検索できなくなります。 Aspose.Cells API のこのリリースでは、LookInType.ORIGINAL_VALUES という名前の別の定数がパブリック API に公開され、上記の状況を克服することができます。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[元の値を使用してデータを検索する](https://docs.aspose.com/cells/java/search-data-using-original-values/)

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
