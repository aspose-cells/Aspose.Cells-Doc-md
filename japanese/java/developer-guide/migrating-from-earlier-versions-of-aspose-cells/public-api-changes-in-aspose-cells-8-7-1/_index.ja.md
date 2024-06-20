---
title: Aspose.Cells 8.7.1 での公開 API 変更
type: docs
weight: 250
url: /ja/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.7.0 から 8.7.1 への変更について、モジュール/アプリケーション開発者に興味を持つ可能性がある内容が記載されています。新しいおよび更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の背後での挙動に変更があった場合についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **Added LookInType.ORIGINAL_VALUES Property**
Aspose.Cells API はすでにスプレッドシートの [検索またはデータ検索](/cells/ja/java/find-or-search-data/) 機能をサポートしており、セルの値および数式の特定の内容を見つけるための機能を提供しています。ただし、この機能では、セルに適用された書式の側面が欠けており、外観および値を変更する可能性のある内容を元の値で検索できなくなる場合があります。このリリースの Aspose.Cells API では、LookInType.ORIGINAL_VALUES という名前の定数が公開 API に公開され、上述の状況を克服することができます。 

{{% alert color="primary" %}} 

この機能の詳細については、[元の値を使用してデータを検索](https://docs.aspose.com/cells/java/search-data-using-original-values/)する詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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
