---
title: Создание, удаление и получение комментариев GridCell
type: docs
weight: 10
url: /ru/java/create-remove-and-get-gridcell-comments/
---

## **Возможные сценарии использования**
В следующей статье объясняется, как создавать, удалять и получать комментарии ячейки GridWeb. Стоит отметить, что GridWeb отображает комментарии в виде подсказок, как MS-Excel, когда вы наводите мышью на ячейку, как показано на этом скриншоте.

![todo:image_alt_text](create-remove-and-get-gridcell-comments_1.png)
## **Создать объект Comment внутри ячейки**
Используйте метод GridCell.CreateComment для создания объекта комментария внутри ячейки. В следующем примере кода создается образец комментария в ячейке B4 первого рабочего листа GridWeb.

{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Удалить объект комментария из ячейки**
Пожалуйста, используйте метод GridCell.RemoveComment для удаления объекта комментария из ячейки. Следующий образец кода удаляет комментарий ячейки B4 на первом листе GridWeb.



{{< highlight java >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Получить объект комментария из ячейки**
Пожалуйста, используйте метод GridCell.GetComment() для получения объекта комментария из ячейки. Следующий образец кода получает объект комментария из ячейки B4, а затем обращается к его различным свойствам, таким как Автор, Заметка, Видимость и т.д.

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




