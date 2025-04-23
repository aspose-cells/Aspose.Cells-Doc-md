---
title: スレッド型コメント
type: docs
weight: 140
url: /ja/java/threaded-comments/
---

# **スレッド化されたコメント**
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
  - **Review**タブをクリックします
  - **新しいコメント**ボタンをクリックします
  - これにより、アクティブなセルにコメントを入力するためのダイアログが開きます。
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- 方法 2
  - コメントを挿入したいセルを右クリック
  - **新しいコメント**オプションをクリックします
  - これにより、アクティブなセルにコメントを入力するためのダイアログが開きます。
  - ![todo:image_alt_text](threaded-comments_5)
### **Aspose.Cells を使用してスレッド型コメントを追加**
Aspose.Cellsは、スレッド付きコメントを追加するための[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-)メソッドを提供します。[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-)メソッドは、次の3つのパラメータを受け取ります。

- セル名: コメントを挿入するセルの名前。
- コメントのテキスト: コメントのテキスト。
- [ThreadedCommentAuthor](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor)：コメントの著者

以下のコードサンプルは、[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment-java.lang.String-java.lang.String-com.aspose.cells.ThreadedCommentAuthor-)メソッドを使用してセルA1にスレッド付きコメントを追加する例です。参考のために、コードが生成する[出力Excelファイル](AddThreadedComments_out.xlsx)を参照してください。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **スレッド化されたコメントを読む**
### **Excelでスレッド化されたコメントを読む**
Excelでスレッド化されたコメントを読むには、単にコメントを含むセル上にマウスを動かすとコメントが表示されます。コメント表示は、次の画像に示すような表示になります。

![todo:image_alt_text](threaded-comments_1.jpg)
### **Aspose.Cellsを使用してスレッド化されたコメントを読む**
Aspose.Cellsは、[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-)メソッドを提供し、指定された列のスレッド付きコメントを取得します。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-)メソッドは、列の名前をパラメータとして受け取り、[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)を返します。 [ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)を反復処理してコメントを閲覧できます。

次の例は、コードによって生成された出力を参照するために、列A1からコメントを読み込む方法を示しています。サンプルExcelファイルを読み込むことで、コンソール出力を参照してください。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **コンソール出力**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **スレッド化されたコメントの作成時間を読む**
Aspose.Cellsは、[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-)メソッドを提供し、指定された列のスレッド付きコメントを取得します。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-)メソッドは、列の名前をパラメータとして受け取り、[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)を返します。これらの[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)を反復処理し、[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)プロパティを使用します。

次の例は、サンプルExcelファイルを読み込むことで、スレッド付きコメントの作成時刻を読む方法を示しています。コンソール出力を参照してください。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **コンソール出力**

{{< highlight java >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 2019-05-15T12:46:23

{{< /highlight >}}

## **スレッド化されたコメントの編集**
### **Excelでスレッド化されたコメントを編集する**
Excelでスレッド化されたコメントを編集するには、以下の画像に示すように、コメント内の**編集**リンクをクリックします。

![todo:image_alt_text](threaded-comments_7.jpg)
### **Aspose.Cellsを使用してスレッド化されたコメントを編集する**
Aspose.Cellsは、[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-)メソッドを提供し、指定された列のスレッド付きコメントを取得します。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments-java.lang.String-)メソッドは、列の名前をパラメータとして受け取り、[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)を返します。必要なコメントを[ThreadedCommentCollection](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)内で更新し、ワークブックを保存できます。

以下の例は、最初のスレッド化されたコメントをA1列で編集する方法を示しています。このコードにより生成された[出力Excelファイル](EditThreadedComments.xlsx)を参照して、更新されたコメントをご覧ください。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **スレッド化されたコメントを削除する**
### **Excelでスレッド化されたコメントを削除する**
Aspose.Cellsを使用してスレッド化されたコメントを削除する

![todo:image_alt_text](threaded-comments_8.jpg)
### **Aspose.Cellsを使用してスレッド化されたコメントを削除する**
Aspose.Cellsは、[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-)メソッドを提供し、指定された列のコメントを削除します。 [Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt-int-)メソッドは、列名をパラメータとして受け取り、その列のコメントを削除します。 

以下の例は、列A1のコメントを削除する方法を示しています。このコードにより生成された[出力Excelファイル](ThreadedCommentsSample_Out.xlsx)を参照し、参照用のコメントをご覧ください。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

Aspose.Cellsを使用してコメントを削除した場合、著者は自動的に削除されません。著者も削除する必要がある場合は、上記の例に示すように[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt-int-)メソッドを使用してください。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
