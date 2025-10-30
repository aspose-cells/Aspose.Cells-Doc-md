---
title: C++を使ったスレッド化されたコメント
linktitle: スレッド型コメント
type: docs
weight: 140
url: /ja/cpp/threaded-comments/
description: Aspose.Cellsを使ってExcelファイルにスレッド化コメントを追加、読み取り、編集、削除する方法を学びましょう。
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

Aspose.Cellsは、[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/)メソッドを使ってスレッド化コメントを追加します。[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/)メソッドは以下の3つのパラメータを受け取ります。

- セル名: コメントを挿入するセルの名前。
- コメントのテキスト: コメントのテキスト。
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/): コメントの作者

次のコードサンプルは、セルA1にスレッド化されたコメントを追加するための[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/)メソッドの使用を示しています。参照のためにコードによって生成された[出力エクセルファイル](89849859.xlsx)をご覧ください。

#### **サンプルコード**

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

## **スレッド化されたコメントを読む**

### **Excelでスレッド化されたコメントを読む**

Excelでスレッド化されたコメントを読むには、単にコメントを含むセル上にマウスを動かすとコメントが表示されます。コメント表示は、次の画像に示すような表示になります。

![todo:image_alt_text](threaded-comments_1.jpg)

### **Aspose.Cellsを使用してスレッド化されたコメントを読む**

Aspose.Cellsは指定された列のスレッド化されたコメントを取得するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)を繰り返し処理してコメントを表示できます。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1からコメントを読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

#### **サンプルコード**

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

#### **コンソール出力**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **スレッド化されたコメントの作成時間を読む**

Aspose.Cellsは指定された列のスレッド化されたコメントを取得するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)を繰り返し処理し、[**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/)プロパティを使用できます。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んでスレッド化されたコメントの作成時間を読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

#### **サンプルコード**

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

#### **コンソール出力**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **スレッド化されたコメントの編集**

### **Excelでスレッド化されたコメントを編集する**

Excelでスレッド化されたコメントを編集するには、次の画像に示すようにコメントの**編集**リンクをクリックします。

![todo:image_alt_text](threaded-comments_7.jpg)

### **Aspose.Cellsを使用してスレッド化されたコメントを編集する**

Aspose.Cellsは指定された列のコメントを削除するための[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/)メソッドを提供します。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/)メソッドは列名をパラメータとして受け取り、その列内のコメントを削除します。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1のコメントを削除することを示しています。参照のためにコードによって生成された更新されたコメントを示す[出力エクセルファイル](89849862.xlsx)をご覧ください。

#### **サンプルコード**

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

## **スレッド化されたコメントを削除する**

### **Excelでスレッド化されたコメントを削除する**

Excelでスレッド化されたコメントを削除するには、コメントを含むセルを右クリックし、次の画像に示すように**コメントを削除**オプションをクリックします。

![todo:image_alt_text](threaded-comments_8.jpg)

### **Aspose.Cellsを使用してスレッド化されたコメントを削除する**

Aspose.Cellsは指定された列のコメントを削除するための[**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/)メソッドを提供します。[**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/)メソッドは列名をパラメータとして受け取り、その列内のコメントを削除します。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1のコメントを削除することを示しています。参照のためにコードによって生成された[出力エクセルファイル](89849864.xlsx)をご覧ください。

#### **サンプルコード**

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

Aspose.Cellsによるコメントの削除では、作者は自動的に削除されません。作者も削除する必要がある場合は、[**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/)クラスのRemoveAtメソッドを使用してください。前述の例に示すように使用してください。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
