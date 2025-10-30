---
title: Trådade kommentarer med C++
linktitle: Trådade kommentarer
type: docs
weight: 140
url: /sv/cpp/threaded-comments/
description: Lär dig hur man lägger till, läser, redigerar och tar bort trådade kommentarer i Excel filer med Aspose.Cells och C++.
---

## **Trådade Kommentarer**

MS Excel 365 ger en funktion för att lägga till trådade kommentarer. Dessa kommentarer fungerar som konversationer och kan användas för diskussioner. Kommentarerna levereras nu med en svarsruta som möjliggör trådade konversationer. De gamla kommentarerna kallas anteckningar i Excel 365. Skärmavbildningen nedan visar hur trådade kommentarer visas när de öppnas i Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Trådade kommentarer visas så här i äldre versioner av Excel. Följande bilder har tagits genom att öppna provfilen i Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells tillhandahåller också funktionen att hantera trådade kommentarer.

## **Lägg till trådade kommentarer**

### **Lägg till trådad kommentar med Excel**

För att lägga till trådade kommentarer i Excel 365 följer du följande steg.

- Metod 1
  - Klicka på fliken **Granska**
  - Klicka på knappen **Ny kommentar**
  - Detta kommer att öppna en dialogruta för att ange kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Metod 2
  - Högerklicka på den cell där du vill infoga kommentaren.
  - Klicka på alternativet **Ny kommentar**
  - Detta kommer att öppna en dialogruta för att ange kommentarer i den aktiva cellen.
  - ![todo:image_alt_text](threaded-comments_5)

### **Lägg till trådad kommentar med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller metoden [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) för att lägga till trådade kommentarer. Metoden [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) accepterar följande tre parametrar.

- Cell namn: Namnet på cellen där kommentaren ska infogas.
- Kommentartext: Kommentarens innehåll.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/): Kommentarens författare

Följande kodexempel visar användningen av [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/)-metoden för att lägga till trådad kommentar till cell A1. Se den [utdata Excel-filen](89849859.xlsx) som genererats av koden för referens.

#### **Exempelkod**

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

## **Läs trådade kommentarer**

### **Läs trådade kommentarer med Excel**

För att läsa trådade kommentarer i Excel, svep helt enkelt musen över cellen som innehåller kommentarerna för att visa kommentarerna. Kommentarerna kommer att se ut som i följande bild.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Läs trådade kommentarer med Aspose.Cells**

Aspose.Cells tillhandahåller metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) för att hämta trådade kommentarer för den angivna kolumnen. Metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) tar kolumnnamnet som en parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) för att visa kommentarerna.

Följande exempel visar hur man läser kommentarer från kolumn A1 genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.

#### **Exempelkod**

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

#### **Konsoloutput**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Läs skapad tid för trådade kommentarer**

Aspose.Cells tillhandahåller metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) för att hämta trådad kommentar för den angivna kolumnen. Metoden [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) tar kolumnnamnet som en parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Du kan iterera över [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) och använda egenskapen [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/).

Följande exempel visar hur man läser skapad tid för trådade kommentarer genom att läsa in [provexemplet Excel-filen](89849861.xlsx). Se konsolens utdata som genererats av koden för referens.

#### **Exempelkod**

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

#### **Konsoloutput**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Redigera trådade kommentarer**

### **Redigera trådad kommentar med Excel**

För att redigera en trådad kommentar i Excel, klicka på länken **Redigera** i kommentaren enligt bilden nedan.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Redigera trådad kommentar med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) metod för att hämta trådade kommentarer för den angivna kolumnen. [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) metoden accepterar kolumnnamnet som en parameter och returnerar [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Du kan uppdatera den kommentar du behöver i [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) och spara arbetsboken.

Följande exempel visar redigering av den första trådade kommentaren i kolumn A1 genom att ladda den [Exempel på Excel-fil](89849861.xlsx). Se också den [utdata av Excel-filen](89849862.xlsx) som genererats av koden och visar den uppdaterade kommentaren för referens.

#### **Exempelkod**

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

## **Ta bort trådade kommentarer**

### **Ta bort trådade kommentarer med Excel**

För att ta bort trådade kommentarer i Excel, högerklicka på cellen som innehåller kommentarerna och välj alternativet **Radera kommentar** enligt bilden nedan.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Ta bort trådade kommentarer med hjälp av Aspose.Cells**

Aspose.Cells tillhandahåller [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) metod för att ta bort kommentarer för den angivna kolumnen. [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) metoden accepterar kolumnnamnet som en parameter och tar bort kommentarerna i den kolumnen.

Följande exempel visar borttagning av kommentarer i kolumn A1 genom att ladda den [Exempel på Excel-fil](89849861.xlsx). Se också den [utdata av Excel-filen](89849864.xlsx) som genererats av koden för referens.

#### **Exempelkod**

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

Observera att genom att ta bort kommentaren med Aspose.Cells tas inte författaren bort automatiskt. Om du behöver ta bort författaren också, använd RemoveAt-metoden i [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/) -klassen enligt exemplet ovan.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
