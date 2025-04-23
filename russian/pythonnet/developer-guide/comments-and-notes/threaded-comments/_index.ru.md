---
title: Нитевые комментарии
type: docs
weight: 140
url: /ru/python-net/threaded-comments/
---

## **Комментарии с цепочкой**

MS Excel 365 предоставляет возможность добавлять нитевые комментарии. Эти комментарии работают как разговоры и могут использоваться для обсуждений. Теперь комментарии идут с полем Ответа, которое позволяет вести разговоры в нитевом порядке. Старые комментарии в Excel 365 называются Примечаниями. Ниже показано, как выглядят нитевые комментарии, когда они открываются в Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Нитевые комментарии показываются таким образом в старых версиях Excel. Следующие изображения были получены при открытии образцового файла в Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells для Python via .NET также предоставляет возможность управления вложенными комментариями.

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

### **Добавить вложенный комментарий с помощью Aspose.Cells для Python via .NET.**

Aspose.Cells для Python via .NET предоставляет метод [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/) для добавления вложенных комментариев. Метод [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) принимает следующие три параметра.

- Имя ячейки: Имя ячейки, в которую будет вставлен комментарий.
- Текст комментария: Текст комментария.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor): Автор комментария.

Приведенный ниже фрагмент кода демонстрирует использование метода [**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment) для добавления ветвистого комментария в ячейку A1. Пожалуйста, ознакомьтесь с [файлом Excel-результатом](89849859.xlsx), сгенерированным кодом для справки.

#### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **Чтение ветвистых комментариев**

### **Чтение ветвистых комментариев с помощью Excel**

Для чтения ветвистых комментариев в Excel просто наведите курсор мыши на ячейку с комментариями, чтобы просмотреть комментарии. Просмотр комментариев будет выглядеть так же, как на следующем изображении.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Прочитать потоковые комментарии с использованием Aspose.Cells для Python via .NET**

Aspose.Cells для Python via .NET предоставляет метод [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) для получения потоковых комментариев для указанного столбца. Метод [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Вы можете пройтись по [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection), чтобы просмотреть комментарии.

В следующем примере демонстрируется чтение комментариев из столбца A1 путем загрузки [образца Excel-файла](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.

#### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **Вывод в консоль**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Прочтите дату создания ветвящихся комментариев**

Aspose.Cells для Python via .NET предоставляет метод [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) для получения потоковых комментариев для указанного столбца. Метод [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Вы можете пройтись по [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) и использовать свойство [**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time).

В следующем примере демонстрируется чтение времени создания ветвистых комментариев при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.

#### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **Редактировать потоковый комментарий с использованием Aspose.Cells для Python via .NET**

Aspose.Cells для Python via .NET предоставляет метод [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) для получения потоковых комментариев для указанного столбца. Метод [**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection). Вы можете обновить необходимый комментарий в [**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection) и сохранить рабочую книгу.

В следующем примере демонстрируется редактирование первого ветвистого комментария в столбце A1 при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с [файлом Excel вывода](89849862.xlsx), сгенерированным кодом.

#### **Образец кода**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

