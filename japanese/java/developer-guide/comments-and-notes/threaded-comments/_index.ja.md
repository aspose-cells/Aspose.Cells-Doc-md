---
title: スレッド化されたコメント
type: docs
weight: 140
url: /ja/java/threaded-comments/
---
# **スレッド化されたコメント**
MS Excel 365 には、スレッド化されたコメントを追加する機能があります。これらのコメントは会話として機能し、ディスカッションに使用できます。コメントには、スレッド化された会話を可能にする返信ボックスが付属しています。古いコメントは、Excel 365 ではメモと呼ばれます。下のスクリーンショットは、Excel で開いたときにスレッド化されたコメントがどのように表示されるかを示しています。

![todo:画像_代替_文章](threaded-comments_1.jpg)

古いバージョンの Excel では、スレッド化されたコメントはこのように表示されます。以下の画像はサンプルファイルをExcel 2016で開いて撮影したものです。

![todo:画像_代替_文章](threaded-comments_2.jpg)



![todo:画像_代替_文章](threaded-comments_3.jpg)



Aspose.Cells は、スレッド化されたコメントを管理する機能も提供します。
## **スレッド化されたコメントを追加**
### **Excel でスレッド化されたコメントを追加する**
Excel 365 でスレッド化されたコメントを追加するには、次の手順に従います。

- 方法 1
 - クリック**レビュー**タブ
 - クリック**新しいコメント**ボタン
 これにより、アクティブ セルにコメントを入力するためのダイアログが開きます。
  - ![todo:画像_代替_文章](threaded-comments_4.jpg)
- 方法 2
 - コメントを挿入するセルを右クリックします。
 - クリック**新しいコメント**オプション。
 これにより、アクティブ セルにコメントを入力するためのダイアログが開きます。
  - ![todo:画像_代替_文章](threaded-comments_5)
### **Aspose.Cells を使用してスレッド コメントを追加**
Aspose.Cells提供[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) スレッド化されたコメントを追加するメソッド。[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) メソッドは、次の 3 つのパラメーターを受け入れます。

- Cell 名前: コメントが挿入されるセルの名前。
- コメント テキスト: コメントのテキスト。
- [スレッドコメント作成者](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentAuthor)コメントの作成者

次のコード サンプルは、[Comments.AddThreadedComment](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#addThreadedComment\(java.lang.String,%20java.lang.String,%20com.aspose.cells.ThreadedCommentAuthor\)) メソッドを使用して、スレッド化されたコメントをセル A1 に追加します。をご覧ください[出力エクセルファイル](AddThreadedComments_out.xlsx)参照用のコードによって生成されます。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "AddThreadedComments-1.java" >}}
## **スレッド化されたコメントを読む**
### **Excel でスレッド化されたコメントを読む**
Excel でスレッド化されたコメントを読むには、コメントを含むセルの上にマウスを置くだけで、コメントが表示されます。コメント ビューは、次の図のビューのようになります。

![todo:画像_代替_文章](threaded-comments_1.jpg)
### **Aspose.Cells を使用してスレッド化されたコメントを読む**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) メソッドを使用して、指定された列のスレッド化されたコメントを取得します。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) メソッドは、列名をパラメーターとして受け入れ、[スレッドコメントコレクション](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection).を繰り返すことができます[スレッドコメントコレクション](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)コメントを表示します。

次の例は、列 A1 からコメントを読み取る方法を示しています。[サンプル Excel ファイル](ThreadedCommentsSample.xlsx).コードによって生成されたコンソール出力を参照してください。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedComments-1.java" >}}
#### **コンソール出力**
コメント: スレッド化されたコメントのテスト

作者: Aspose テスト
### **スレッド化されたコメントの作成時間を読み取る**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) メソッドを使用して、指定された列のスレッド化されたコメントを取得します。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) メソッドは、列名をパラメーターとして受け入れ、[スレッドコメントコレクション](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection).を繰り返すことができます[スレッドコメントコレクション](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)を使用します。[ThreadedComment.CreatedTime](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcomment#CreatedTime)財産。

次の例は、[サンプル Excel ファイル](ThreadedCommentsSample.xlsx).コードによって生成されたコンソール出力を参照してください。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ReadThreadedCommentCreatedTime-1.java" >}}
#### **コンソール出力**
コメント: スレッド化されたコメントのテスト

作者: Aspose テスト

作成時間: 2019-05-15T12:46:23
## **スレッド化されたコメントの編集**
### **スレッド化されたコメントを Excel で編集する**
Excel でスレッド化されたコメントを編集するには、**編集**次の画像に示すように、コメントにリンクします。

![todo:画像_代替_文章](threaded-comments_7.jpg)
### **Aspose.Cells を使用してスレッド コメントを編集**
Aspose.Cells提供[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) メソッドを使用して、指定された列のスレッド化されたコメントを取得します。[Comments.GetThreadedComments](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#getThreadedComments\(java.lang.String\)) メソッドは、列名をパラメーターとして受け入れ、[スレッドコメントコレクション](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection).で必要なコメントを更新できます。[スレッドコメントコレクション](https://reference.aspose.com/cells/java/com.aspose.cells/ThreadedCommentCollection)ブックを保存します。

次の例は、列 A1 の最初のスレッド化されたコメントを編集する方法を示しています。[サンプル Excel ファイル](ThreadedCommentsSample.xlsx).をご覧ください[出力エクセルファイル](EditThreadedComments.xlsx)参照用に更新されたコメントを示すコードによって生成されます。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "EditThreadedComments-1.java" >}}
## **スレッド化されたコメントを削除**
### **Excel でスレッド化されたコメントを削除する**
Excel でスレッド化されたコメントを削除するには、コメントを含むセルを右クリックし、**コメントを削除**次の図に示すようにオプションを選択します。

![todo:画像_代替_文章](threaded-comments_8.jpg)
### **Aspose.Cells を使用してスレッド化されたコメントを削除します**
Aspose.Cells提供[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) メソッドを使用して、指定された列のコメントを削除します。[Comments.RemoveAt](https://reference.aspose.com/cells/java/com.aspose.cells/commentcollection#removeAt\(int\)) メソッドは、列名をパラメーターとして受け入れ、その列のコメントを削除します。

次の例は、列 A1 をロードしてコメントを削除する方法を示しています。[サンプル Excel ファイル](ThreadedCommentsSample.xlsx).をご覧ください[出力エクセルファイル](ThreadedCommentsSample_Out.xlsx)参照用のコードによって生成されます。
#### **サンプルコード**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "RemoveThreadedComments-1.java" >}}

{{% alert color="primary" %}} 

 Aspose.Cells のコメントを削除しても、著者は自動的に削除されませんのでご注意ください。作成者も削除する必要がある場合は、[ThreadedCommentAuthorCollection.removeAt](https://reference.aspose.com/cells/java/com.aspose.cells/threadedcommentauthorcollection#removeAt\(int\)) メソッドを上記の例に示します。

{{% /alert %}}
