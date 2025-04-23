---
title: スレッド型コメント
type: docs
weight: 140
url: /ja/net/threaded-comments/
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

Aspose.Cells では、スレッド型コメントを追加するための [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) メソッドが提供されています。[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1) メソッドは、次の3つのパラメーターを受け入れます。

- セル名: コメントを挿入するセルの名前。
- コメントのテキスト: コメントのテキスト。
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthor): コメントの作者

次のコードサンプルは、セルA1にスレッド化されたコメントを追加するための[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/addthreadedcomment/methods/1)メソッドの使用を示しています。参照のためにコードによって生成された[出力エクセルファイル](89849859.xlsx)をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-AddThreadedComments-1.cs" >}}

## **スレッド化されたコメントを読む**

### **Excelでスレッド化されたコメントを読む**

Excelでスレッド化されたコメントを読むには、単にコメントを含むセル上にマウスを動かすとコメントが表示されます。コメント表示は、次の画像に示すような表示になります。

![todo:image_alt_text](threaded-comments_1.jpg)

### **Aspose.Cellsを使用してスレッド化されたコメントを読む**

Aspose.Cellsは指定された列のスレッド化されたコメントを取得するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)を繰り返し処理してコメントを表示できます。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1からコメントを読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedComments-1.cs" >}}

#### **コンソール出力**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **スレッド化されたコメントの作成時間を読む**

Aspose.Cellsは指定された列のスレッド化されたコメントを取得するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentcollection)を繰り返し処理し、[**ThreadedComment.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/threadedcomment/properties/createdtime)プロパティを使用できます。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んでスレッド化されたコメントの作成時間を読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-ReadThreadedCommentCreatedTime-1.cs" >}}

#### **コンソール出力**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **スレッド化されたコメントの編集**

### **Excelでスレッド化されたコメントを編集する**

Excelでスレッド化されたコメントを編集するには、次の画像に示すようにコメントの**編集**リンクをクリックします。

![todo:image_alt_text](threaded-comments_7.jpg)

### **Aspose.Cellsを使用してスレッド化されたコメントを編集する**

Aspose.Cellsは指定された列のコメントを削除するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/net/aspose.cells.commentcollection/getthreadedcomments/methods/1)メソッドは列名をパラメータとして受け取り、その列内のコメントを削除します。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1のコメントを削除することを示しています。参照のためにコードによって生成された更新されたコメントを示す[出力エクセルファイル](89849862.xlsx)をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-EditThreadedComments-1.cs" >}}

## **スレッド化されたコメントを削除する**

### **Excelでスレッド化されたコメントを削除する**

Excelでスレッド化されたコメントを削除するには、コメントを含むセルを右クリックし、次の画像に示すように**コメントを削除**オプションをクリックします。

![todo:image_alt_text](threaded-comments_8.jpg)

### **Aspose.Cellsを使用してスレッド化されたコメントを削除する**

Aspose.Cellsは指定された列のコメントを削除するための[**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)メソッドを提供します。[**Comments.RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/commentcollection/methods/removeat/index)メソッドは列名をパラメータとして受け取り、その列内のコメントを削除します。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1のコメントを削除することを示しています。参照のためにコードによって生成された[出力エクセルファイル](89849864.xlsx)をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-RemoveThreadedComments-1.cs" >}}

{{% alert color="primary" %}}

Aspose.Cellsによるコメントの削除では、作者は自動的に削除されません。作者も削除する必要がある場合は、[**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/net/aspose.cells/threadedcommentauthorcollection)クラスのRemoveAtメソッドを使用してください。前述の例に示すように使用してください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
