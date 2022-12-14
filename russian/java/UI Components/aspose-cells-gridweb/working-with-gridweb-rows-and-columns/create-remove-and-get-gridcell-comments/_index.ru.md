---
title: Создать Удалить и получить комментарии GridCell
type: docs
weight: 10
url: /ru/java/create-remove-and-get-gridcell-comments/
---
## **Возможные сценарии использования**
В следующей статье объясняется, как создавать, удалять и получать комментарии GridCell на листе GridWeb. Стоит отметить, что GridWeb отображает комментарий в виде всплывающей подсказки, как MS-Excel, когда вы наводите указатель мыши на ячейку, как показано на этом снимке экрана.

![дело:изображение_альтернативный_текст](create-remove-and-get-gridcell-comments_1.png)
## **Создать объект комментария внутри Cell**
Используйте метод GridCell.CreateComment для создания объекта комментария внутри ячейки. Следующий пример кода создает образец комментария в ячейке B4 первого рабочего листа GridWeb.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
## **Удалить объект комментария из Cell**
Используйте метод GridCell.RemoveComment, чтобы удалить объект комментария из ячейки. Следующий пример кода удаляет комментарий к ячейке B4 на первом листе GridWeb.



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
## **Получить объект комментария от Cell**
Используйте метод GridCell.GetComment(), чтобы получить объект комментария из ячейки. Следующий пример кода получает объект комментария из ячейки B4, а затем получает доступ к его различным свойствам, таким как автор, примечание, видимость и т. д.

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




