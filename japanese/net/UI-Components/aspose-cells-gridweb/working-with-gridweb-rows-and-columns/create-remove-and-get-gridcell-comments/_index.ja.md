---
title: GridCellコメントの作成、削除、取得
type: docs
weight: 100
url: /ja/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: この記事では、GridWeb内のコメントの処理方法について紹介しています。
---

## **可能な使用シナリオ**
次の記事では、GridWebワークシート内のセル（GridCell）からコメントを作成、削除、取得する方法について説明します。GridWebは、セル上でマウスをホバーすると、MS-Excelのようにコメントをツールチップとして表示します。

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **セル内にコメントオブジェクトを作成**
セル内にコメントオブジェクトを作成するには、GridCell.CreateCommentメソッドを使用してください。次のサンプルコードは、GridWebの最初のワークシートのセルB4にサンプルコメントを作成します。

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **セルからコメントオブジェクトを削除**
セルからコメントオブジェクトを削除するには、GridCell.RemoveCommentメソッドを使用してください。次のサンプルコードは、GridWebの最初のワークシートのセルB4のコメントを削除します。



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **セルからコメントオブジェクトを取得**
セルからコメントオブジェクトを取得するには、GridCell.GetComment()メソッドを使用してください。次のサンプルコードは、セルB4からコメントオブジェクトを取得し、その作者、ノート、表示などのさまざまなプロパティにアクセスします。

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Get comment of this cell

GridComment gridComm = cell.GetComment();

//Access its various properties

string strAuth = gridComm.Author;

string strNote = gridComm.Note;

bool isVis = gridComm.IsVisible;

{{< /highlight >}}
