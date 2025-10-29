---  
title: Обработка цепочек комментариев с помощью Node.js через C++  
linktitle: Нитевые комментарии  
type: docs  
weight: 140  
url: /ru/nodejs-cpp/threaded-comments/  
description: Управляйте цепочечными комментариями в документах Excel с помощью Aspose.Cells for Node.js via C++. Узнайте, как добавлять, читать, редактировать и удалять цепочечные комментарии.  
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

Aspose.Cells предоставляет метод [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) для добавления цепочечных комментариев. Метод [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) принимает три параметра.  

- Имя ячейки: Имя ячейки, в которую будет вставлен комментарий.  
- Текст комментария: Текст комментария.  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor): Автор комментария.  

Следующий пример демонстрирует использование метода [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) для добавления цепочечного комментария в ячейку A1. Пожалуйста, посмотрите сгенерированный файл Excel [выходной файл](89849859.xlsx) для примера.  

#### **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

// Add Author
const authorIndex = workbook.getWorksheets().getThreadedCommentAuthors().add("Aspose Test", "", "");
const author = workbook.getWorksheets().getThreadedCommentAuthors().get(authorIndex);

// Add Threaded Comment
workbook.getWorksheets().get(0).getComments().addThreadedComment("A1", "Test Threaded Comment", author);

workbook.save(outDir + "AddThreadedComments_out.xlsx");
```  

## **Чтение ветвистых комментариев**  

### **Чтение ветвистых комментариев с помощью Excel**  

Для чтения ветвистых комментариев в Excel просто наведите курсор мыши на ячейку с комментариями, чтобы просмотреть комментарии. Просмотр комментариев будет выглядеть так же, как на следующем изображении.  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **Чтение ветвистых комментариев с использованием Aspose.Cells**  

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) для извлечения ветвистых комментариев для указанного столбца. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) принимает имя столбца в качестве параметра и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Вы можете перебирать [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) для просмотра комментариев.  

В следующем примере демонстрируется чтение комментариев из столбца A1 путем загрузки [образца Excel-файла](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.  

#### **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data"); // Adjust as necessary

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook which contains threaded comments
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();
for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
}
```  

#### **Вывод в консоль**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **Прочтите дату создания ветвящихся комментариев**  

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) для получения цепочечных комментариев для указанной колонки. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) принимает название колонки и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Вы можете перебрать [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) и использовать свойство [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--).  

В следующем примере демонстрируется чтение времени создания ветвистых комментариев при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с выводом консоли, сгенерированным кодом для справки.  

#### **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();

for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
console.log("Created Time: " + comment.getCreatedTime());
}
```  

#### **Вывод в консоль**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **Редактировать ветвящиеся комментарии**  

### **Редактировать ветвящийся комментарий с помощью Excel**  

Чтобы отредактировать ветвистый комментарий в Excel, щелкните ссылку **Редактировать** в комментарии, как показано на следующем изображении.  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **Редактирование ветвящегося комментария с использованием Aspose.Cells**  

Aspose.Cells предоставляет метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) для получения цепочечных комментариев для указанной колонки. Метод [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) принимает название колонки и возвращает [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Вы можете обновить нужный комментарий в [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) и сохранить книгу.  

В следующем примере демонстрируется редактирование первого ветвистого комментария в столбце A1 при загрузке [образцового файла Excel](89849861.xlsx). Пожалуйста, ознакомьтесь с [файлом Excel вывода](89849862.xlsx), сгенерированным кодом.  

#### **Образец кода**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comment
const comment = worksheet.getComments().getThreadedComments("A1").get(0);
comment.setNotes("Updated Comment");

workbook.save(outDir + "EditThreadedComments.xlsx");
```  

## **Удалить ветвящиеся комментарии**  

### **Удалить ветвящиеся комментарии с помощью Excel**  

Чтобы удалить ветвистые комментарии в Excel, щелкните правой кнопкой мыши на ячейке с комментариями и выберите опцию **Удалить комментарий**, как показано на следующем изображении.  

![todo:image_alt_text](threaded-comments_8.jpg)   


{{< app/cells/assistant language="nodejs-cpp" >}}
