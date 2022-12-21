---
title: GridCell コメントの削除と取得の作成
type: docs
weight: 100
url: /ja/net/create-remove-and-get-gridcell-comments/
---
## **考えられる使用シナリオ**
次の記事では、GridWeb ワークシート内で GridCell コメントを作成、削除、および取得する方法について説明します。このスクリーンショットに示すように、セルの上にマウスを移動すると、MS-Excel のように GridWeb がコメントをツールチップとして表示することに注意してください。

![todo:画像_代替_文章](create-remove-and-get-gridcell-comments_1.png)
## **Cell 内に Comment オブジェクトを作成する**
GridCell.CreateComment メソッドを使用して、セル内にコメント オブジェクトを作成してください。次のサンプル コードは、GridWeb の最初のワークシートのセル B4 にサンプル コメントを作成します。

{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Cell から Comment オブジェクトを削除します**
GridCell.RemoveComment メソッドを使用して、セルからコメント オブジェクトを削除してください。次のサンプル コードは、GridWeb の最初のワークシート内のセル B4 コメントを削除します。



{{< highlight "java" >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Cell からコメントオブジェクトを取得**
GridCell.GetComment() メソッドを使用して、セルからコメント オブジェクトを取得してください。次のサンプル コードは、セル B4 からコメント オブジェクトを取得し、Author、Note、Visibility などのさまざまなプロパティにアクセスします。

{{< highlight "java" >}}

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
