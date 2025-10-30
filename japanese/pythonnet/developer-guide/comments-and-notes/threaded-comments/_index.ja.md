---
title: スレッド型コメント
type: docs
weight: 140
url: /ja/python-net/threaded-comments/
---

## **スレッド化されたコメント**

MS Excel 365 では、スレッド型コメントを追加する機能が提供されています。これらのコメントは会話として機能し、ディスカッションに使用できます。新しいコメントにはスレッド型の会話が可能なリプライボックスが付属しています。古いコメントは Excel 365 ではノートと呼ばれます。以下のスクリーンショットは、Excel 365 でスレッド型コメントが開かれたときの表示例です。

![todo:image_alt_text](threaded-comments_1.jpg)

古いバージョンの Excel では、スレッド型コメントは以下のように表示されます。以下の画像は、サンプルファイルを Excel 2016 で開いたものです。

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells for Python via .NETは、スレッドコメントの管理機能も提供しています。

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

### **Aspose.Cells for Python via .NETを使用したスレッドコメントの追加**

Aspose.Cells for Python via .NETは、[**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment/)メソッドを提供してスレッドコメントを追加します。[**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment)メソッドは以下の3つのパラメーターを受け取ります。

- セル名: コメントを挿入するセルの名前。
- コメントのテキスト: コメントのテキスト。
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentauthor): コメントの作者

次のコードサンプルは、セルA1にスレッド化されたコメントを追加するための[**Comments.add_threaded_comment**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/add_threaded_comment)メソッドの使用を示しています。参照のためにコードによって生成された[出力エクセルファイル](89849859.xlsx)をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-AddThreadedComments-1.py" >}}

## **スレッド化されたコメントを読む**

### **Excelでスレッド化されたコメントを読む**

Excelでスレッド化されたコメントを読むには、単にコメントを含むセル上にマウスを動かすとコメントが表示されます。コメント表示は、次の画像に示すような表示になります。

![todo:image_alt_text](threaded-comments_1.jpg)

### **Aspose.Cells for Python via .NETを使用したスレッドコメントの読み取り**

Aspose.Cells for Python via .NETは、指定された列のスレッドコメントを取得する[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)メソッドを提供しています。[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)を繰り返してコメントを見ることができます。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1からコメントを読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedComments-1.py" >}}

#### **コンソール出力**

{{< highlight csharp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **スレッド化されたコメントの作成時間を読む**

Aspose.Cells for Python via .NETは、指定された列のスレッドコメントを取得する[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)メソッドを提供しています。[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)を繰り返して[**ThreadedComment.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcomment/created_time)プロパティを使用してコメントを見ることができます。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んでスレッド化されたコメントの作成時間を読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-ReadThreadedCommentCreatedTime-1.py" >}}

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

### **Aspose.Cells for Python via .NETを使用したスレッドコメントの編集**

Aspose.Cells for Python via .NETは、指定された列のスレッドコメントを取得する[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)メソッドを提供しています。[**Comments.get_threaded_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/commentcollection/get_threaded_comments)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)を返します。必要なコメントを[**ThreadedCommentCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/threadedcommentcollection)内で更新し、ワークブックを保存してください。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1のコメントを削除することを示しています。参照のためにコードによって生成された更新されたコメントを示す[出力エクセルファイル](89849862.xlsx)をご覧ください。

#### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Comments-EditThreadedComments-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
