---
title: Нитевые комментарии
type: docs
weight: 140
url: /ru/net/threaded-comments/
---

## **Комментарии с цепочкой**

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
  - Нажмите кнопку **Новый комментарий**
  - Это откроет диалог для ввода комментариев в активной ячейке.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Метод 2
  - Щелкните правой кнопкой мыши на ячейке, куда нужно вставить комментарий.
  - Нажмите на **Новый комментарий**.
  - Это откроет диалог для ввода комментариев в активной ячейке.
  - ![todo:image_alt_text](threaded-comments_5)

### **Добавить ветвистый комментарий с помощью Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) для добавления ветвистых комментариев. Метод [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) принимает следующие три параметра.

- Имя ячейки: Имя ячейки, в которую будет вставлен комментарий.
- Текст комментария: Текст комментария.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): Автор комментария.

Приведенный ниже фрагмент кода демонстрирует использование метода [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) для добавления ветвистого комментария в ячейку A1. Пожалуйста, ознакомьтесь с [файлом Excel-результатом](89849859.xlsx), сгенерированным кодом для справки.

#### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **Чтение ветвистых комментариев**

### **Чтение ветвистых комментариев с помощью Excel**

Для чтения ветвистых комментариев в Excel просто наведите курсор мыши на ячейку с комментариями, чтобы просмотреть комментарии. Просмотр комментариев будет выглядеть так же, как на следующем изображении.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Чтение ветвистых комментариев с использованием Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) для извлечения ветвистых комментариев для указанного столбца. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Вы можете перебирать [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) для просмотра комментариев.

В следующем примере демонстрируется чтение комментариев из столбца A1 путем загрузки [образца Excel-файла](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.

#### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **Вывод в консоль**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Прочтите дату создания ветвящихся комментариев**

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) для извлечения ветвистых комментариев для указанного столбца. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Вы можете перебирать [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) и использовать свойство [**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime).

В следующем примере демонстрируется чтение времени создания ветвистых комментариев при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.

#### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **Вывод в консоль**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Редактировать ветвящиеся комментарии**

### **Редактировать ветвящийся комментарий с помощью Excel**

Чтобы отредактировать ветвистый комментарий в Excel, щелкните ссылку **Редактировать** в комментарии, как показано на следующем изображении.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Редактирование ветвящегося комментария с использованием Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) для извлечения ветвистых комментариев для указанного столбца. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection). Вы можете обновить необходимый комментарий в [**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection) и сохранить книгу.

В следующем примере демонстрируется редактирование первого ветвистого комментария в столбце A1 при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с [файлом Excel вывода](89849862.xlsx), сгенерированным кодом.

#### **Образец кода**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **Удалить ветвящиеся комментарии**

### **Удалить ветвящиеся комментарии с помощью Excel**

Чтобы удалить ветвистые комментарии в Excel, щелкните правой кнопкой мыши на ячейке с комментариями и выберите опцию **Удалить комментарий**, как показано на следующем изображении.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Удаление ветвящихся комментариев с использованием Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) для удаления комментариев для указанного столбца. Метод [**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index) принимает имя столбца в качестве параметра и удаляет комментарии в этом столбце.

В следующем примере демонстрируется удаление комментариев в столбце A1 при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с [выводным файлом Excel](89849864.xlsx), сгенерированным кодом для справки.

#### **Образец кода**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

Обратите внимание, что при удалении комментария с помощью Aspose.Cells автор не удаляется автоматически. Если вам нужно также удалить автора, используйте метод RemoveAt класса [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection), как показано в приведенном выше примере.

{{% /alert %}}
