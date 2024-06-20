---
title: GridCellコメントの作成、削除、取得
type: docs
weight: 10
url: /ja/java/create-remove-and-get-gridcell-comments/
---

## **可能な使用シナリオ**
次の記事では、GridWebワークシート内のGridCellコメントの作成、削除、取得方法について説明しています。 GridWebは、マウスをセルの上に置くとMS-Excelのようにコメントをツールチップとして表示します。

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **セル内にコメントオブジェクトを作成**
セル内にコメントオブジェクトを作成するには、GridCell.CreateCommentメソッドを使用してください。次のサンプルコードは、GridWebの最初のワークシートのセルB4にサンプルコメントを作成します。

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **セルからコメントオブジェクトを削除**
GridWebの最初のワークシート内のセルB4コメントを削除するには、GridCell.RemoveCommentメソッドを使用してください。次のサンプルコードは、セルB4のコメントを削除します。



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **セルからコメントオブジェクトを取得**
GridCell.GetComment()メソッドを使用して、セルからコメントオブジェクトを取得してください。次のサンプルコードは、セルB4からコメントオブジェクトを取得し、Author、Note、Visibilityなどのさまざまなプロパティにアクセスします。

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Get comment of this cell

GridComment gridComm = cell.getComment();

// Access its various properties

String strAuth = gridComm.getAuthor();

String strNote = gridComm.getNote();

boolean isVis = gridComm.isVisible();


{{< /highlight >}}




