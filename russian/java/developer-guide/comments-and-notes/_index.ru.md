---
title: Управление комментариями и заметками
linktitle: Комментарии и заметки
type: docs
weight: 128
url: /ru/java/comments-and-notes/
description: Вставка и управление комментариями или заметками с использованием Aspose.Cells для Java
keywords: вставка комментариев, вставка заметок
---

## **Введение**

Комментарии используются для добавления дополнительной информации к ячейкам. Aspose.Cells предоставляет два способа добавления комментариев к ячейкам. Первый - создавать комментарии в файле дизайнера вручную. Затем эти комментарии импортируются с использованием Aspose.Cells. Второй - добавлять комментарии с использованием API Aspose.Cells во время выполнения. В этой теме будет рассмотрено добавление комментариев к ячейкам с использованием API Aspose.Cells. Также будет объяснено форматирование комментариев.

## **Добавление комментария**

Добавьте комментарий в ячейку, вызвав метод **Add** коллекции [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) (инкапсулированный в объекте [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)). Новый объект [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) можно получить из коллекции [**Comments**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection), передав индекс комментария. После получения объекта [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) настройте комментарий, используя свойство [**Note**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note) объекта [**Comment**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Форматирование комментариев**

Также возможно форматировать внешний вид комментариев, настроив их высоту, ширину и параметры шрифта.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Добавить изображение в комментарий**

С помощью Microsoft Excel 2007 также возможно иметь изображение в качестве фона комментария к ячейке. В Excel 2007 это можно сделать, выполнив следующие шаги. (Предполагается, что вы уже добавили комментарий к ячейке.)

1. Щелкните правой кнопкой мыши ячейку, содержащую комментарий.
1. Выберите **Показать/скрыть комментарии** и очистите любой текст из комментария.
1. Щелкните по границе комментария, чтобы выбрать его.
1. Выберите **Формат**, затем **Комментарий**.
1. На вкладке **Цвета и линии** разверните список **Цвет**.
1. Нажмите **Изменение заливки**.
1. На вкладке **Изображение** нажмите **Выбрать изображение**.
1. Найдите и выберите изображение.
1. Нажмите **ОК**, пока все диалоговые окна не закроются.

Aspose.Cells также предоставляет эту функцию. Ниже приведен пример кода, который создает файл XLSX с нуля, добавляя комментарий в ячейку "A1" с установленным изображением в качестве его фона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Продвинутые темы**
- [Изменение направления текста комментария](/cells/ru/java/change-text-direction-of-the-comment/)
- [Как изменить цвет шрифта комментария](/cells/ru/java/how-to-change-the-comment-font-color/)
- [Как установить фон комментария](/cells/ru/java/how-to-set-comment-background/)
- [Комментарии с цепочкой](/cells/ru/java/threaded-comments/)

{{< app/cells/assistant language="java" >}}
