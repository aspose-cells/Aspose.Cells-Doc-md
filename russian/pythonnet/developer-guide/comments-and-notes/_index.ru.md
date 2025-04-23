---
title: Управление комментариями и заметками
linktitle: Комментарии и заметки
type: docs
weight: 128
url: /ru/python-net/comments-and-notes/
description: Вставка и управление комментариями или заметками с помощью Aspose.Cells для .Net
keywords: вставка комментариев, вставка заметок
---

## **Введение**

Комментарии используются для добавления дополнительной информации к ячейкам. Aspose.Cells предоставляет два способа добавления комментариев к ячейкам. Первый - создавать комментарии в файле дизайнера вручную. Затем эти комментарии импортируются с использованием Aspose.Cells. Второй - добавлять комментарии с использованием API Aspose.Cells во время выполнения. В этой теме будет рассмотрено добавление комментариев к ячейкам с использованием API Aspose.Cells. Также будет объяснено форматирование комментариев.

## **Добавление комментария**

Добавление комментария в ячейку, вызвав метод [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add) коллекции [**Comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection) (инкапсулированный в объекте [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Новый объект [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment) может быть получен из коллекции [**Comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection), передав индекс комментария. После доступа к объекту [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment), настроить заметку комментария можно, используя свойство [**note**](https://reference.aspose.com/cells/python-net/aspose.cells/comment/note) объекта [**Comment**](https://reference.aspose.com/cells/python-net/aspose.cells/comment).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddingComment-1.cs" >}}

## **Форматирование комментариев**

Также возможно форматировать внешний вид комментариев, настроив их высоту, ширину и параметры шрифта.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-CommentFormatting-1.cs" >}}

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Comments-AddImageToComment-1.cs" >}}

## **Продвинутые темы**
- [Изменение направления текста комментария](/cells/ru/python-net/change-text-direction-of-the-comment/)
- [Как изменить цвет шрифта комментария](/cells/ru/python-net/how-to-change-the-comment-font-color/)
- [Как установить фон комментария](/cells/ru/python-net/how-to-set-comment-background/)
- [Комментарии с цепочкой](/cells/ru/python-net/threaded-comments/)

