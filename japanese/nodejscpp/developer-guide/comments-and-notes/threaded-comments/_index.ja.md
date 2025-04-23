---  
title: Node.js と C++ を使用したスレッド付きコメントの管理  
linktitle: スレッド型コメント  
type: docs  
weight: 140  
url: /ja/nodejs-cpp/threaded-comments/  
description: Aspose.Cells for Node.js via C++ を使用して Excel ドキュメントのスレッド付きコメントを追加・読み取り・編集・削除する方法を学びましょう。  
---  

## **スレッド化されたコメント**  

MS Excel 365 では、スレッド型コメントを追加する機能が提供されています。これらのコメントは会話として機能し、ディスカッションに使用できます。新しいコメントにはスレッド型の会話が可能なリプライボックスが付属しています。古いコメントは Excel 365 ではノートと呼ばれます。以下のスクリーンショットは、Excel 365 でスレッド型コメントが開かれたときの表示例です。  

![todo:image_alt_text](threaded-comments_1.jpg)  

古いバージョンの Excel では、スレッド型コメントは以下のように表示されます。以下の画像は、サンプルファイルを Excel 2016 で開いたものです。  

![todo:image_alt_text](threaded-comments_2.jpg)  

![todo:image_alt_text](threaded-comments_3.jpg)  

Aspose.Cells では、スレッド型コメントの管理機能も提供されています。  

## **スレッド型コメントの追加**  

### **Excel でスレッド型コメントを追加**  

Excel 365 でスレッド型コメントを追加するには、以下の手順に従ってください。  

- 方法 1  
  - **レビュー** タブをクリック  
  - **新しいコメント** ボタンをクリック  
  - これにより、アクティブなセルにコメントを入力するためのダイアログが開きます。  
  - ![todo:image_alt_text](threaded-comments_4.jpg)  
- 方法 2  
  - コメントを挿入したいセルを右クリック  
  - **新しいコメント** オプションをクリック  
  - これにより、アクティブなセルにコメントを入力するためのダイアログが開きます。  
  - ![todo:image_alt_text](threaded-comments_5)  

### **Aspose.Cells を使用してスレッド型コメントを追加**  

Aspose.Cellsは、[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-)メソッドを使ってスレッド化コメントを追加します。[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-)メソッドは以下の3つのパラメータを受け取ります。  

- セル名: コメントを挿入するセルの名前。  
- コメントのテキスト: コメントのテキスト。  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor): コメントの作者  

以下のコードサンプルは、[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-)メソッドを使用してセルA1にスレッド付きコメントを追加する方法を示しています。参考のために、コードによって生成された[出力Excelファイル](89849859.xlsx)を参照してください。  

#### **サンプルコード**  

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

## **スレッド化されたコメントを読む**  

### **Excelでスレッド化されたコメントを読む**  

Excelでスレッド化されたコメントを読むには、単にコメントを含むセル上にマウスを動かすとコメントが表示されます。コメント表示は、次の画像に示すような表示になります。  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **Aspose.Cellsを使用してスレッド化されたコメントを読む**  

Aspose.Cellsは指定された列のスレッド化されたコメントを取得するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)を繰り返し処理してコメントを表示できます。  

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1からコメントを読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。  

#### **サンプルコード**  

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

#### **コンソール出力**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **スレッド化されたコメントの作成時間を読む**  

Aspose.Cellsは、指定された列のスレッド付きコメントを取得するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)メソッドは列名をパラメータとして受け入れ、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)を繰り返し、[**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--)プロパティを使用できます。  

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んでスレッド化されたコメントの作成時間を読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。  

#### **サンプルコード**  

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

#### **コンソール出力**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **スレッド化されたコメントの編集**  

### **Excelでスレッド化されたコメントを編集する**  

Excelでスレッド化されたコメントを編集するには、次の画像に示すようにコメントの**編集**リンクをクリックします。  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **Aspose.Cellsを使用してスレッド化されたコメントを編集する**  

Aspose.Cellsは、指定された列のスレッド付きコメントを取得するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-)メソッドは列名をパラメータとして受け入れ、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)を返します。必要なコメントを[**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection)で更新し、ワークブックを保存できます。  

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1のコメントを削除することを示しています。参照のためにコードによって生成された更新されたコメントを示す[出力エクセルファイル](89849862.xlsx)をご覧ください。  

#### **サンプルコード**  

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

## **スレッド化されたコメントを削除する**  

### **Excelでスレッド化されたコメントを削除する**  

Excelでスレッド化されたコメントを削除するには、コメントを含むセルを右クリックし、次の画像に示すように**コメントを削除**オプションをクリックします。  

![todo:image_alt_text](threaded-comments_8.jpg)   


