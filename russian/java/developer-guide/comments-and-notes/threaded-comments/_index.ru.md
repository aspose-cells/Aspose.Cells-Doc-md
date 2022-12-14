---
title: Резьбовые комментарии
type: docs
weight: 140
url: /ru/java/threaded-comments/
---
# **Резьбовые комментарии**
MS Excel 365 предоставляет функцию добавления цепочек комментариев. Эти комментарии работают как разговоры и могут использоваться для обсуждений. Комментарии теперь сопровождаются полем для ответа, которое позволяет вести цепочку бесед. Старые комментарии называются примечаниями в Excel 365. На приведенном ниже снимке экрана показано, как отображаются связанные комментарии при открытии в Excel.

![дело:изображение_альтернативный_текст](threaded-comments_1.jpg)

Ветвистые комментарии отображаются в более старых версиях Excel таким образом. Следующие изображения были получены путем открытия файла примера в Excel 2016.

![дело:изображение_альтернативный_текст](threaded-comments_2.jpg)



![дело:изображение_альтернативный_текст](threaded-comments_3.jpg)



Aspose.Cells также предоставляет возможность управления цепочками комментариев.
## **Добавить цепочку комментариев**
### **Добавить цепочку комментариев с помощью Excel**
Чтобы добавить цепочку комментариев в Excel 365, выполните следующие действия.

- Способ 1
 - Нажмите на**Обзор**Вкладка
 - Нажмите на**Новый комментарий**кнопка
 - Откроется диалоговое окно для ввода комментариев в активную ячейку.
  - ![дело:изображение_альтернативный_текст](threaded-comments_4.jpg)
- Способ 2
 - Щелкните правой кнопкой мыши ячейку, в которую вы хотите вставить комментарий.
 - Нажмите на**Новый комментарий**вариант.
 - Откроется диалоговое окно для ввода комментариев в активную ячейку.
  - ![дело:изображение_альтернативный_текст](threaded-comments_5)
### **Добавить цепочку комментариев, используя Aspose.Cells**
Aspose.Cells предоставляет[Комментарии.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) для добавления цепочек комментариев.[Комментарии.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) принимает следующие три параметра.

- Cell Имя: имя ячейки, в которую будет вставлен комментарий.
- Текст комментария: текст комментария.
- [РезьбовойКомментарийАвтор](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): Автор комментария

В следующем примере кода показано использование[Комментарии.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) для добавления связанного комментария к ячейке A1. Пожалуйста, смотрите[выходной файл Excel](AddThreadedComments_out.xlsx)сгенерированный кодом для справки.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Читать ветки комментариев**
### **Чтение цепочек комментариев в Excel**
Чтобы прочитать цепочку комментариев в Excel, просто наведите указатель мыши на ячейку, содержащую комментарии, чтобы просмотреть комментарии. Представление комментариев будет выглядеть так, как показано на следующем изображении.

![дело:изображение_альтернативный_текст](threaded-comments_1.jpg)
### **Читать ветки комментариев, используя Aspose.Cells**
Aspose.Cells предоставляет[Комментарии.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) для получения связанных комментариев для указанного столбца.[Комментарии.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) принимает имя столбца в качестве параметра и возвращает[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Вы можете перебирать[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)для просмотра комментариев.

В следующем примере показано чтение комментариев из столбца A1 путем загрузки[образец файла Excel](ThreadedCommentsSample.xlsx). Для справки см. вывод консоли, сгенерированный кодом.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Консольный вывод**
Комментарий: тестовый тематический комментарий

Автор: Aspose Тест
### **Чтение времени создания цепочек комментариев**
Aspose.Cells предоставляет[Комментарии.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) для получения связанных комментариев для указанного столбца.[Комментарии.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) принимает имя столбца в качестве параметра и возвращает[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Вы можете перебирать[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)и использовать[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)имущество.

В следующем примере показано чтение времени создания цепочек комментариев путем загрузки[образец файла Excel](ThreadedCommentsSample.xlsx). Для справки см. вывод консоли, сгенерированный кодом.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Консольный вывод**
Комментарий: тестовый тематический комментарий

Автор: Aspose Тест

Время создания: 2019-05-15T12:46:23
## **Редактировать цепочку комментариев**
### **Редактировать цепочку комментариев с помощью Excel**
Чтобы отредактировать связанный комментарий в Excel, щелкните значок**Редактировать**ссылку на комментарий, как показано на следующем изображении.

![дело:изображение_альтернативный_текст](threaded-comments_7.jpg)
### **Отредактируйте цепочку комментариев, используя Aspose.Cells.**
Aspose.Cells предоставляет[Комментарии.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) для получения связанных комментариев для указанного столбца.[Комментарии.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) принимает имя столбца в качестве параметра и возвращает[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Вы можете обновить нужный комментарий в[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)и сохраните книгу.

В следующем примере показано редактирование первого связанного комментария в столбце A1 путем загрузки[образец файла Excel](ThreadedCommentsSample.xlsx). Пожалуйста, смотрите[выходной файл Excel](EditThreadedComments.xlsx)сгенерированный кодом, показывающим обновленный комментарий для справки.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Удалить цепочку комментариев**
### **Удалить цепочку комментариев с помощью Excel**
Чтобы удалить связанные комментарии в Excel, щелкните правой кнопкой мыши ячейку, содержащую комментарии, и щелкните значок**Удалить комментарий**вариант, как показано на следующем изображении.

![дело:изображение_альтернативный_текст](threaded-comments_8.jpg)
### **Удалите ветки комментариев, используя Aspose.Cells**
Aspose.Cells предоставляет[Комментарии.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) для удаления комментариев для указанного столбца.[Комментарии.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) принимает имя столбца в качестве параметра и удаляет комментарии в этом столбце.

В следующем примере показано удаление комментариев в столбце A1 путем загрузки[образец файла Excel](ThreadedCommentsSample.xlsx). Пожалуйста, смотрите[выходной файл Excel](ThreadedCommentsSample_Out.xlsx)сгенерированный кодом для справки.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

 Обратите внимание, что при удалении комментария с номером Aspose.Cells автор не удаляется автоматически. Если вам нужно удалить автора, пожалуйста, используйте[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)), как показано в примере выше.

{{% /alert %}}
