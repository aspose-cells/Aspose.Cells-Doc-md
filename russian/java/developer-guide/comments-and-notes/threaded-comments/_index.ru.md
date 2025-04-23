---
title: Нитевые комментарии
type: docs
weight: 140
url: /ru/java/threaded-comments/
---

# **Комментарии с цепочкой**
MS Excel 365 предоставляет возможность добавлять нитевые комментарии. Эти комментарии работают как разговоры и могут использоваться для обсуждений. Теперь комментарии идут с полем Ответа, которое позволяет вести разговоры в нитевом порядке. Старые комментарии в Excel 365 называются Примечаниями. Ниже показано, как выглядят нитевые комментарии, когда они открываются в Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Нитевые комментарии показываются таким образом в старых версиях Excel. Следующие изображения были получены при открытии образцового файла в Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)



![todo:image_alt_text](threaded-comments_3.jpg)



Aspose.Cells также предоставляет возможность управлять нитевыми комментариями. 
## **Добавить нитевые комментарии**
### **Добавить нитевой комментарий с Excel**
Чтобы добавить нитевые комментарии в Excel 365, выполните следующие шаги.

- Метод 1
  - Нажмите вкладку **Обзор**
  - Нажмите кнопку **Новый комментарий**
  - Это откроет диалог для ввода комментариев в активной ячейке.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Метод 2
  - Щелкните правой кнопкой мыши на ячейке, куда нужно вставить комментарий.
  - Нажмите на опцию **Новый комментарий**.
  - Это откроет диалог для ввода комментариев в активной ячейке.
  - ![todo:image_alt_text](threaded-comments_5)
### **Добавить ветвистый комментарий с помощью Aspose.Cells**
Aspose.Cells предоставляет метод [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) для добавления потоковых комментариев. Метод [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-) принимает три параметра.

- Имя ячейки: Имя ячейки, в которую будет вставлен комментарий.
- Текст комментария: Текст комментария.
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor): Автор комментария

Следующий пример кода демонстрирует использование метода [Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) для добавления потокового комментария в ячейку A1. Пожалуйста, посмотрите [выходной файл Excel](AddThreadedComments_out.xlsx), созданный этим кодом, для справки.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **Чтение ветвистых комментариев**
### **Чтение ветвистых комментариев с помощью Excel**
Для чтения ветвистых комментариев в Excel просто наведите курсор мыши на ячейку с комментариями, чтобы просмотреть комментарии. Просмотр комментариев будет выглядеть так же, как на следующем изображении.

![todo:image_alt_text](threaded-comments_1.jpg)
### **Чтение ветвистых комментариев с использованием Aspose.Cells**
Aspose.Cells предоставляет метод [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) для получения потоковых комментариев для указанного столбца. Метод [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) принимает название столбца в качестве параметра и возвращает [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Вы можете пройтись по [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection), чтобы просмотреть комментарии.

Следующий пример демонстрирует чтение комментариев из столбца A1, загружая [образец файла Excel](ThreadedCommentsSample.xlsx). Пожалуйста, ознакомьтесь с выводом в консоль, сгенерированным кодом для справки.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **Вывод в консоль**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Прочтите дату создания ветвящихся комментариев**
Aspose.Cells предоставляет метод [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) для получения потоковых комментариев для указанного столбца. Метод [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) принимает название столбца и возвращает [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Вы можете пройтись по [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) и использовать свойство [ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime).

В следующем примере показано чтение времени создания ветвящихся комментариев путем загрузки [образцового файла Excel] (ThreadedCommentsSample.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **Вывод в консоль**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **Редактировать ветвящиеся комментарии**
### **Редактировать ветвящийся комментарий с помощью Excel**
Чтобы отредактировать ветвящийся комментарий в Excel, щелкните по ссылке **Редактировать** в комментарии, как показано на следующем изображении.

![todo:image_alt_text](threaded-comments_7.jpg)
### **Редактирование ветвящегося комментария с использованием Aspose.Cells**
Aspose.Cells предоставляет метод [Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-) для получения потоковых комментариев для указанного столбца. Метод принимает название столбца и возвращает [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection). Вы можете обновить необходимый комментарий в [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection) и сохранить рабочую книгу.

В следующем примере демонстрируется редактирование первого ветвящегося комментария в ячейке A1 путем загрузки [образцового файла Excel] (ThreadedCommentsSample.xlsx). Пожалуйста, ознакомьтесь с [выходным файлом Excel] (EditThreadedComments.xlsx), сгенерированным кодом, показывающим обновленный комментарий для справки.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **Удалить ветвящиеся комментарии**
### **Удалить ветвящиеся комментарии с помощью Excel**
Чтобы удалить ветвящиеся комментарии в Excel, щелкните правой кнопкой мыши на ячейке с комментариями и нажмите на опцию **Удалить комментарий**, как показано на следующем изображении.

![todo:image_alt_text](threaded-comments_8.jpg)
### **Удаление ветвящихся комментариев с использованием Aspose.Cells**
Aspose.Cells предоставляет метод [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-) для удаления комментариев в указанном столбце. Метод принимает название столбца и удаляет комментарии в этом столбце. 

Следующий пример демонстрирует удаление комментариев в столбце A1 путем загрузки [образца файла Excel] (ThreadedCommentsSample.xlsx). Пожалуйста, ознакомьтесь с [выходным файлом Excel] (ThreadedCommentsSample_Out.xlsx), сгенерированным кодом для справки.
#### **Образец кода**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

Обратите внимание, что при удалении комментария с помощью Aspose.Cells автоматически не удаляется автор. Если нужно также удалить автора, используйте метод [ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt-int-) как показано в примере выше.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
