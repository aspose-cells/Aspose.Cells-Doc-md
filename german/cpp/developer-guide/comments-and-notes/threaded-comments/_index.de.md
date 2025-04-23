---
title: Threaded Kommentare mit C++
linktitle: Threaded Comments
type: docs
weight: 140
url: /de/cpp/threaded-comments/
description: Lernen Sie, wie Sie verschachtelte Kommentare in Excel Dateien mit Aspose.Cells und C++ hinzufügen, lesen, bearbeiten und entfernen.
---

## **Antwortkommentare**

MS Excel 365 bietet eine Funktion zum Hinzufügen von Threaded-Kommentaren. Diese Kommentare fungieren als Unterhaltungen und können für Diskussionen verwendet werden. Die Kommentare enthalten nun eine Antwortbox, die Threaded-Konversationen ermöglicht. Die alten Kommentare werden in Excel 365 als Notizen bezeichnet. Der Screenshot unten zeigt, wie threaded Kommentare angezeigt werden, wenn sie in Excel geöffnet werden.

![todo:image_alt_text](threaded-comments_1.jpg)

Threaded comments werden in älteren Versionen von Excel so angezeigt. Die folgenden Bilder wurden erstellt, indem die Beispieldatei in Excel 2016 geöffnet wurde.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells bietet auch die Funktion zur Verwaltung von Threaded-Kommentaren.

## **Threaded-Kommentare hinzufügen**

### **Threaded-Kommentar mit Excel hinzufügen**

Um Threaded-Kommentare in Excel 365 hinzuzufügen, befolgen Sie die folgenden Schritte.

- Methode 1
  - Klicken Sie auf die Registerkarte **Überprüfen**
  - Klicken Sie auf die Schaltfläche **Neuer Kommentar**
  - Dadurch wird ein Dialogfeld geöffnet, um Kommentare in der aktiven Zelle einzugeben.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Methode 2
  - Klicken Sie mit der rechten Maustaste auf die Zelle, in die Sie den Kommentar einfügen möchten.
  - Klicken Sie auf die Option **Neuer Kommentar**.
  - Dadurch wird ein Dialogfeld geöffnet, um Kommentare in der aktiven Zelle einzugeben.
  - ![todo:image_alt_text](threaded-comments_5)

### **Fügen Sie einen Kommentarfaden mit Aspose.Cells hinzu**

Aspose.Cells bietet die Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/), um threaded comments hinzuzufügen. Die Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) akzeptiert die folgenden drei Parameter.

- Zellenname: Der Name der Zelle, in die der Kommentar eingefügt wird.
- Kommentartext: Der Text des Kommentars.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/): Der Verfasser des Kommentars

Das folgende Codebeispiel zeigt die Verwendung der Methode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) zum Hinzufügen eines kommentierten Fadens zur Zelle A1. Bitte sehen Sie die durch den Code generierte [Ausgabe-Excel-Datei](89849859.xlsx) zur Referenz an.

#### **Beispielcode**

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

## **Lese kommentierte Fäden**

### **Lese kommentierte Fäden mit Excel**

Um kommentierte Fäden in Excel zu lesen, fahren Sie einfach mit der Maus über die Zelle, die Kommentare enthält, um die Kommentare anzuzeigen. Die Ansicht der Kommentare wird der Darstellung im folgenden Bild ähneln.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Lese kommentierte Fäden mit Aspose.Cells**

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) zum Abrufen von kommentierten Fäden für die angegebene Spalte. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) zurück. Sie können über die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) iterieren, um die Kommentare anzuzeigen.

Das folgende Beispiel zeigt das Lesen von Kommentaren aus Spalte A1 durch Laden der [Beispiel-Excel-Datei](89849861.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe zur Referenz an.

#### **Beispielcode**

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

#### **Konsolenausgabe**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Lese Erstellungszeitpunkt von kommentierten Fäden**

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) zum Abrufen von kommentierten Fäden für die angegebene Spalte. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) akzeptiert den Spaltennamen als Parameter und gibt die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) zurück. Sie können über die [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) iterieren und die [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/)-Eigenschaft verwenden.

Das folgende Beispiel zeigt das Lesen des Erstellungszeitpunkts von kommentierten Fäden durch Laden der [Beispiel-Excel-Datei](89849861.xlsx). Bitte sehen Sie die durch den Code generierte Konsolenausgabe zur Referenz an.

#### **Beispielcode**

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

#### **Konsolenausgabe**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Kommentare bearbeiten**

### **Bearbeiten Sie kommentierte Kommentare mit Excel**

Um einen kommentierten Kommentar in Excel zu bearbeiten, klicken Sie auf den **Bearbeiten**-Link im Kommentar wie im folgenden Bild gezeigt.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Threaded-Kommentar bearbeiten mit Aspose.Cells**

Aspose.Cells bietet die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) zum Abrufen von Threaded-Kommentaren für die angegebene Spalte. Die Methode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) akzeptiert den Spaltennamen als Parameter und gibt das [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) zurück. Sie können den erforderlichen Kommentar in den [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) aktualisieren und die Arbeitsmappe speichern.

Das folgende Beispiel demonstriert die Bearbeitung des ersten Threaded-Kommentars in Spalte A1 durch Laden der [Beispiel Excel Datei](89849861.xlsx). Bitte beachten Sie die [Ausgabe Excel-Datei](89849862.xlsx), die vom Code generiert wird und die aktualisierten Kommentare zur Referenz zeigt.

#### **Beispielcode**

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

## **Threaded-Kommentare entfernen**

### **Threaded-Kommentare mit Excel entfernen**

Um Threaded-Kommentare in Excel zu entfernen, klicken Sie mit der rechten Maustaste auf die Zelle mit den Kommentaren und wählen Sie die Option **Kommentar löschen**, wie im folgenden Bild gezeigt.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Threaded-Kommentare mit Aspose.Cells entfernen**

Aspose.Cells bietet die Methode [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) zum Entfernen von Kommentaren für die angegebene Spalte. Die Methode [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) akzeptiert den Spaltennamen als Parameter und entfernt die Kommentare in dieser Spalte.

Das folgende Beispiel demonstriert das Entfernen von Kommentaren in Spalte A1 durch Laden der [Beispiel Excel Datei](89849861.xlsx). Bitte sehen Sie die [Ausgabe Excel-Datei](89849864.xlsx), die vom Code generiert wurde, zur Referenz.

#### **Beispielcode**

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

Bitte beachten Sie, dass durch Entfernen von Kommentaren mit Aspose.Cells der Autor nicht automatisch entfernt wird. Wenn Sie den Autor ebenfalls entfernen müssen, verwenden Sie bitte die RemoveAt-Methode der [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/)-Klasse, wie im obigen Beispiel gezeigt.

{{% /alert %}}
