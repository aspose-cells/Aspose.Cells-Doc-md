---
title: GridCell コメントの作成と削除および取得
type: docs
weight: 10
url: /ja/java/create-remove-and-get-gridcell-comments/
---
##  **考えられる使用シナリオ**
次の記事では、GridWeb ワークシート内で GridCell コメントを作成、削除、取得する方法について説明します。このスクリーンショットに示すように、セルの上にマウスを置くと、GridWeb は MS-Excel のようにツールチップとしてコメントを表示することに注意してください。

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
##  **Cell 内に Comment オブジェクトを作成します**
GridCell.CreateComment メソッドを使用して、セル内にコメント オブジェクトを作成してください。次のサンプル コードは、GridWeb の最初のワークシートのセル B4 にサンプル コメントを作成します。

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
##  **Cell からコメントオブジェクトを削除**
セルからコメント オブジェクトを削除するには、GridCell.RemoveComment メソッドを使用してください。次のサンプル コードは、GridWeb の最初のワークシート内のセル B4 のコメントを削除します。



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
##  **Cell からコメントオブジェクトを取得**
セルからコメント オブジェクトを取得するには、GridCell.GetComment() メソッドを使用してください。次のサンプル コードは、セル B4 からコメント オブジェクトを取得し、作成者、メモ、表示設定などのさまざまなプロパティにアクセスします。

{{< highlight "java" >}}

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




