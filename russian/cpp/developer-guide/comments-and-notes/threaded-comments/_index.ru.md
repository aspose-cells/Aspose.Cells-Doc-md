---
title: Множественные комментарии с помощью C++
linktitle: Нитевые комментарии
type: docs
weight: 140
url: /ru/cpp/threaded-comments/
description: Узнайте, как добавлять, читать, редактировать и удалять вложенные комментарии в Excel с помощью Aspose.Cells и C++.
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

Aspose.Cells предоставляет метод [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) для добавления цепочечных комментариев. Метод [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) принимает три параметра.

- Имя ячейки: Имя ячейки, в которую будет вставлен комментарий.
- Текст комментария: Текст комментария.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/): Автор комментария.

Приведенный ниже фрагмент кода демонстрирует использование метода [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) для добавления ветвистого комментария в ячейку A1. Пожалуйста, ознакомьтесь с [файлом Excel-результатом](89849859.xlsx), сгенерированным кодом для справки.

#### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add Author
    int authorIndex = workbook.GetWorksheets().GetThreadedCommentAuthors().Add(u"Aspose Test", u"", u"");
    ThreadedCommentAuthor author = workbook.GetWorksheets().GetThreadedCommentAuthors().Get(authorIndex);

    // Add Threaded Comment
    workbook.GetWorksheets().Get(0).GetComments().AddThreadedComment(u"A1", u"Test Threaded Comment", author);

    // Save the workbook
    workbook.Save(outDir + u"AddThreadedComments_out.xlsx");

    std::cout << "Threaded comment added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Чтение ветвистых комментариев**

### **Чтение ветвистых комментариев с помощью Excel**

Для чтения ветвистых комментариев в Excel просто наведите курсор мыши на ячейку с комментариями, чтобы просмотреть комментарии. Просмотр комментариев будет выглядеть так же, как на следующем изображении.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Чтение ветвистых комментариев с использованием Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) для извлечения ветвистых комментариев для указанного столбца. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Вы можете перебирать [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) для просмотра комментариев.

В следующем примере демонстрируется чтение комментариев из столбца A1 путем загрузки [образца Excel-файла](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.

#### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get Threaded Comments
    ThreadedCommentCollection threadedComments = worksheet.GetComments().GetThreadedComments(u"A1");

    // Iterate through threaded comments
    for (int i = 0; i < threadedComments.GetCount(); i++)
    {
        ThreadedComment comment = threadedComments.Get(i);
        cout << "Comment: " << comment.GetNotes().ToUtf8() << endl;
        cout << "Author: " << comment.GetAuthor().GetName().ToUtf8() << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

#### **Вывод в консоль**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Прочтите дату создания ветвящихся комментариев**

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) для извлечения ветвистых комментариев для указанного столбца. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Вы можете перебирать [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) и использовать свойство [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/).

В следующем примере демонстрируется чтение времени создания ветвистых комментариев при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.

#### **Образец кода**

```cpp
#include <iostream>
#include <iomanip>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    ThreadedCommentCollection threadedComments = worksheet.GetComments().GetThreadedComments(u"A1");

    for (int i = 0; i < threadedComments.GetCount(); i++)
    {
        ThreadedComment comment = threadedComments.Get(i);
        cout << "Comment: " << comment.GetNotes().ToUtf8() << endl;
        cout << "Author: " << comment.GetAuthor().GetName().ToUtf8() << endl;
        Date createdTime = comment.GetCreatedTime();
        ostringstream oss;
        oss << setfill('0') 
            << setw(4) << createdTime.year << "-"
            << setw(2) << createdTime.month << "-"
            << setw(2) << createdTime.day << " "
            << setw(2) << createdTime.hour << ":"
            << setw(2) << createdTime.minute << ":"
            << setw(2) << createdTime.second;
        cout << "Created Time: " << oss.str() << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

#### **Вывод в консоль**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Редактировать ветвящиеся комментарии**

### **Редактировать ветвящийся комментарий с помощью Excel**

Чтобы отредактировать ветвистый комментарий в Excel, щелкните ссылку **Редактировать** в комментарии, как показано на следующем изображении.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Редактирование ветвящегося комментария с использованием Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) для извлечения ветвистых комментариев для указанного столбца. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Вы можете обновить необходимый комментарий в [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) и сохранить книгу.

В следующем примере демонстрируется редактирование первого ветвистого комментария в столбце A1 при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с [файлом Excel вывода](89849862.xlsx), сгенерированным кодом.

#### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the threaded comment from cell A1
    ThreadedComment comment = worksheet.GetComments().GetThreadedComments(u"A1").Get(0);

    // Update the comment text
    comment.SetNotes(u"Updated Comment");

    // Save the workbook
    workbook.Save(outDir + u"EditThreadedComments.xlsx");

    std::cout << "Threaded comment updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Удалить ветвящиеся комментарии**

### **Удалить ветвящиеся комментарии с помощью Excel**

Чтобы удалить ветвистые комментарии в Excel, щелкните правой кнопкой мыши на ячейке с комментариями и выберите опцию **Удалить комментарий**, как показано на следующем изображении.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Удаление ветвящихся комментариев с использованием Aspose.Cells**

Aspose.Cells предоставляет метод [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) для удаления комментариев для указанного столбца. Метод [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) принимает имя столбца в качестве параметра и удаляет комментарии в этом столбце.

В следующем примере демонстрируется удаление комментариев в столбце A1 при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с [выводным файлом Excel](89849864.xlsx), сгенерированным кодом для справки.

#### **Образец кода**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"ThreadedCommentsSample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the comments collection
    CommentCollection comments = worksheet.GetComments();

    // Get the author of the first threaded comment in cell A1
    ThreadedCommentAuthor author = worksheet.GetComments().GetThreadedComments(u"A1").Get(0).GetAuthor();

    // Remove the comment at cell A1
    comments.RemoveAt(u"A1");

    // Get the threaded comment authors collection
    ThreadedCommentAuthorCollection authors = workbook.GetWorksheets().GetThreadedCommentAuthors();

    // Save the workbook
    workbook.Save(outDir + u"ThreadedCommentsSample_Out.xlsx");

    std::cout << "Threaded comments processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Обратите внимание, что при удалении комментария с помощью Aspose.Cells автор не удаляется автоматически. Если вам нужно также удалить автора, используйте метод RemoveAt класса [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/), как показано в приведенном выше примере.

{{% /alert %}}
