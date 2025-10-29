---  
title: 使用 Node.js 通过 C++ 处理嵌套评论  
linktitle: 分线评论  
type: docs  
weight: 140  
url: /zh/nodejs-cpp/threaded-comments/  
description: 使用 Aspose.Cells for Node.js via C++ 管理 Excel 文档中的嵌套评论。学习添加、读取、编辑和删除嵌套评论。  
---  

## **线程化的批注**  

MS Excel 365提供了一个添加分线评论的功能。这些评论可以用作对话，并可用于讨论。现在的评论带有一个回复框，允许进行分线对话。Excel 365中的旧注释称为注释。下面的截图显示了在Excel中打开分线评论时的显示方式。  

![todo:image_alt_text](threaded-comments_1.jpg)  

在较旧版本的Excel中，分线评论显示如下。以下图片是打开在Excel 2016中的样本文件时拍摄的。  

![todo:image_alt_text](threaded-comments_2.jpg)  

![todo:image_alt_text](threaded-comments_3.jpg)  

Aspose.Cells还提供了管理分线评论的功能。  

## **添加分线评论**  

### **使用Excel添加分线评论**  

在Excel 365中添加分线评论，请按照以下步骤进行。  

- 方法1  
  - 单击**审阅**选项卡  
  - 单击**新建评论**按钮  
  - 这将打开一个对话框，以输入活动单元格中的评论。  
  - ![todo:image_alt_text](threaded-comments_4.jpg)  
- 方法2  
  - 右键单击要插入评论的单元格。  
  - 单击**新建评论**选项。  
  - 这将打开一个对话框，以输入活动单元格中的评论。  
  - ![todo:image_alt_text](threaded-comments_5)  

### **使用Aspose.Cells添加分线评论**  

Aspose.Cells 提供 [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) 方法以添加线程评论。[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) 方法接受以下三个参数。  

- 单元格名称：要插入评论的单元格的名称。  
- 评论文本：评论的文本。  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor)：评论的作者  

 以下代码示例演示了如何使用 [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) 方法向单元格 A1 添加嵌套评论。请参考由代码生成的 [输出 Excel 文件](89849859.xlsx)。  

#### **示例代码**  

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

## **读取分线评论**  

### **使用Excel读取分线评论**  

要在Excel中读取分线评论，只需将鼠标悬停在包含评论的单元格上以查看评论。评论视图将类似于以下图像中的视图。  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **使用Aspose.Cells读取分线评论**  

Aspose.Cells提供[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)方法来检索指定列的分线评论。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)方法接受列名称作为参数，并返回[**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)。您可以遍历[**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)以查看评论。  

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 从A1列读取评论。请查看生成的代码控制台输出以供参考。  

#### **示例代码**  

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

#### **控制台输出**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **读取线程评论的创建时间**  

 Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) 方法以检索指定列的嵌套评论。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) 方法接受列名作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)。你可以遍历 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) ，并使用 [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--) 属性。  

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 读取线程评论的创建时间。请查看生成的代码控制台输出以供参考。  

#### **示例代码**  

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

#### **控制台输出**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **编辑线程评论**  

### **使用Excel编辑线程评论**  

要在Excel中编辑线程评论，请单击评论上显示的**编辑**链接，如下图所示。  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **使用Aspose.Cells编辑线程评论**  

 Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) 方法以检索指定列的嵌套评论。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) 方法接受列名作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)。你可以在 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) 中更新所需的评论并保存工作簿。  

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 编辑A1列中的第一个线程评论。请查看生成的代码以供参考。  

#### **示例代码**  

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

## **删除线程评论**  

### **使用Excel删除线程评论**  

要在Excel中删除线程评论，请右键单击包含评论的单元格，然后单击下图所示的**删除评论**选项。  

![todo:image_alt_text](threaded-comments_8.jpg)   


{{< app/cells/assistant language="nodejs-cpp" >}}
