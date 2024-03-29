﻿---
title: Управление комментариями и примечаниями
linktitle: Комментарии и примечания
type: docs
weight: 128
url: /ru/java/comments-and-notes/
description: Вставляйте и управляйте комментариями или примечаниями с помощью Aspose.Cells для java.
keywords: insert comments, insert notes
---
## **Вступление**

Комментарии используются для добавления дополнительной информации к ячейкам. Aspose.Cells предоставляет два метода добавления комментариев к ячейкам. Первый заключается в создании комментариев в файле конструктора вручную. Затем эти комментарии импортируются с использованием Aspose.Cells. Второй способ — добавить комментарии с использованием Aspose.Cells API во время выполнения. В этом разделе обсуждается добавление комментариев к ячейкам с помощью Aspose.Cells API. Также будет объяснено форматирование комментариев.

## **Добавление комментария**

 Добавьте комментарий к ячейке, вызвав метод[**Комментарии**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) коллекция**Добавлять** метод (инкапсулированный в[**Рабочий лист**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) объект). Новый[**Комментарий**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) доступ к объекту возможен из[**Комментарии**](https://reference.aspose.com/cells/java/com.aspose.cells/CommentCollection) коллекции, передав индекс комментария. После доступа к[**Комментарий**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) объект, настройте примечание комментария с помощью[**Комментарий**](https://reference.aspose.com/cells/java/com.aspose.cells/Comment) объекты[**Запись**](https://reference.aspose.com/cells/java/com.aspose.cells/comment#Note)имущество.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddingComment-1.java" >}}

## **Форматирование комментариев**

Также возможно отформатировать внешний вид комментариев, настроив их высоту, ширину и параметры шрифта.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "CommentFormatting-1.java" >}}

## **Добавить изображение в комментарий**

В Microsoft Excel 2007 также можно использовать изображение в качестве фона для комментария к ячейке. В Excel 2007 это достигается выполнением следующих шагов. (Они предполагают, что вы уже добавили комментарий к ячейке.)

1. Щелкните правой кнопкой мыши ячейку, содержащую комментарий.
1.  Выбирать**Показать/скрыть комментарии**и удалите любой текст из комментария.
1. Нажмите на границу комментария, чтобы выделить его.
1.  Выбирать**Формат** , тогда**Комментарий**.
1.  На**Цвета и линии** вкладку, разверните**Цвет** список.
1.  Нажмите**Эффекты заливки**.
1.  На**Рисунок** вкладка, нажмите**Выберите изображение**.
1. Найдите и выберите изображение.
1.  Нажмите**ХОРОШО** пока не закроются все диалоги.

Aspose.Cells также предоставляет эту функцию. Ниже приведен пример кода, который создает файл XLSX с нуля, добавляя комментарий к ячейке «A1» с изображением в качестве фона.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddImageToComment-1.java" >}}

## **Предварительные темы**
- [Изменить направление текста комментария](/cells/ru/java/change-text-direction-of-the-comment/)
- [Как изменить цвет шрифта комментария](/cells/ru/java/how-to-change-the-comment-font-color/)
- [Как установить фон комментария](/cells/ru/java/how-to-set-comment-background/)
- [Резьбовые комментарии](/cells/ru/java/threaded-comments/)

