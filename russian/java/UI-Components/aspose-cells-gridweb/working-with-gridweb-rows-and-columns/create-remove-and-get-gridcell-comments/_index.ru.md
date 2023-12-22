---
title: Создать удаление и получить комментарии GridCell
type: docs
weight: 10
url: /ru/java/create-remove-and-get-gridcell-comments/
---
##  **Возможные сценарии использования**
В следующей статье объясняется, как создавать, удалять и получать комментарии GridCell внутри листа GridWeb. Стоит отметить, что GridWeb отображает комментарий в виде всплывающей подсказки, как MS-Excel, когда вы наводите указатель мыши на ячейку, как показано на этом снимке экрана.

![задача: image_alt_text](create-remove-and-get-gridcell-comments_1.png)
##  **Создайте объект комментария внутри Cell.**
Используйте метод GridCell.CreateComment, чтобы создать объект комментария внутри ячейки. Следующий пример кода создает образец комментария в ячейке B4 первого листа GridWeb.

{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Create comment with these parameters

// i.e. note, author, isvisible

cell.createComment("This is a B4 note.", "Peter", true);

{{< /highlight >}}
##  **Удалить объект комментария из Cell**
Используйте метод GridCell.RemoveComment, чтобы удалить объект комментария из ячейки. Следующий пример кода удаляет комментарий к ячейке B4 на первом листе GridWeb.



{{< highlight "java" >}}

 // Access first worksheet of GridWeb

GridWorksheet sheet = GridWeb1.getWorkSheets().get(0);

// Access cell B4

GridCell cell = sheet.getCells().get("B4");

// Remove the comment object from this cell.

cell.removeComment();

{{< /highlight >}}
##  **Получить объект комментария от Cell**
Используйте метод GridCell.GetComment(), чтобы получить объект комментария из ячейки. Следующий пример кода получает объект комментария из ячейки B4, а затем получает доступ к его различным свойствам, таким как «Автор», «Заметка», «Видимость» и т. д.

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




