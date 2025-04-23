---
title: 用 C++ 实现线程评论
linktitle: 分线评论
type: docs
weight: 140
url: /zh/cpp/threaded-comments/
description: 学习如何使用 Aspose.Cells 与 C++ 在 Excel 文件中添加、读取、编辑和删除线程评论。
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

Aspose.Cells 提供 [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) 方法以添加线程评论。[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) 方法接受以下三个参数。

- 单元格名称：要插入评论的单元格的名称。
- 评论文本：评论的文本。
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/)：评论的作者

以下代码示例演示了使用[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/)方法向单元格A1添加分线评论。请参考代码生成的[输出Excel文件](89849859.xlsx)。

#### **示例代码**

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

## **读取分线评论**

### **使用Excel读取分线评论**

要在Excel中读取分线评论，只需将鼠标悬停在包含评论的单元格上以查看评论。评论视图将类似于以下图像中的视图。

![todo:image_alt_text](threaded-comments_1.jpg)

### **使用Aspose.Cells读取分线评论**

Aspose.Cells提供[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/)方法来检索指定列的分线评论。[**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/)方法接受列名称作为参数，并返回[**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)。您可以遍历[**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)以查看评论。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 从A1列读取评论。请查看生成的代码控制台输出以供参考。

#### **示例代码**

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

#### **控制台输出**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **读取线程评论的创建时间**

Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) 方法来检索指定列的线程评论。 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) 方法接受列名称作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)。您可以遍历 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) 并使用 [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/) 属性。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 读取线程评论的创建时间。请查看生成的代码控制台输出以供参考。

#### **示例代码**

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

#### **控制台输出**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **编辑线程评论**

### **使用Excel编辑线程评论**

要在Excel中编辑线程评论，请单击评论上显示的**编辑**链接，如下图所示。

![todo:image_alt_text](threaded-comments_7.jpg)

### **使用Aspose.Cells编辑线程评论**

Aspose.Cells 提供 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) 方法来检索指定列的线程评论。 [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) 方法接受列名称作为参数并返回 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/)。您可以更新 [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) 中所需的评论并保存工作簿。

以下示例演示了通过加载 [示例Excel文件](89849861.xlsx) 编辑A1列中的第一个线程评论。请查看生成的代码以供参考。

#### **示例代码**

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

## **删除线程评论**

### **使用Excel删除线程评论**

要在Excel中删除线程评论，请右键单击包含评论的单元格，然后单击下图所示的**删除评论**选项。

![todo:image_alt_text](threaded-comments_8.jpg)

### **使用Aspose.Cells删除线程评论**

Aspose.Cells 提供 [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) 方法来删除指定列的评论。 [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) 方法接受列名称作为参数并删除该列中的评论。

以下示例演示了通过加载[sample Excel File](89849861.xlsx)文件来删除A1列中的注释。请参考代码生成的[output Excel file](89849864.xlsx)。

#### **示例代码**

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

请注意，使用Aspose.Cells删除注释时，作者不会自动删除。如果您需要同时删除作者，请像上面的示例中所示使用[**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/)类的RemoveAt方法。

{{% /alert %}}
