---
title: Создание, удаление и получение комментариев GridCell
type: docs
weight: 100
url: /ru/net/aspose-cells-gridweb/manage-comment/
keywords: GridWeb,comment
description: Эта статья рассказывает, как работать с комментариями в GridWeb.
---

## **Возможные сценарии использования**
В следующей статье объясняется, как создавать, удалять и получать комментарий из ячейки (GridCell) в рабочем листе GridWeb. Следует отметить, что GridWeb отображает комментарий в виде всплывающей подсказки, как в MS-Excel, когда вы наводите курсор на ячейку, как показано на этом скриншоте.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Создать объект Comment внутри ячейки**
Используйте метод GridCell.CreateComment для создания объекта комментария внутри ячейки. В следующем примере кода создается образец комментария в ячейке B4 первого рабочего листа GridWeb.

{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Create comment with these parameters

//i.e. note, author, isvisible

cell.CreateComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Удалить объект комментария из ячейки**
Используйте метод GridCell.RemoveComment для удаления объекта комментария из ячейки. В следующем примере кода удаляется комментарий ячейки B4 внутри первого рабочего листа GridWeb.



{{< highlight java >}}

 //Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.WorkSheets[0];

//Access cell B4

GridCell cell = sheet.Cells["B4"];

//Remove the comment object from this cell.

cell.RemoveComment();

{{< /highlight >}}
## **Получить объект комментария из ячейки**
Используйте метод GridCell.GetComment(), чтобы получить объект комментария из ячейки. В следующем примере кода получается объект комментария из ячейки B4, после чего обращается к его различным свойствам, таким как Author, Note, Visibility и т. д.

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
