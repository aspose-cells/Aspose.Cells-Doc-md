---
title: Commenti Threaded con C++
linktitle: Commenti filettati
type: docs
weight: 140
url: /it/cpp/threaded-comments/
description: Impara come aggiungere, leggere, modificare e rimuovere commenti threaded in file Excel usando Aspose.Cells con C++.
---

## **Commenti in discussione**

MS Excel 365 fornisce una funzionalità per aggiungere commenti filettati. Questi commenti funzionano come conversazioni e possono essere utilizzati per le discussioni. I commenti ora sono dotati di una casella Rispondi che consente conversazioni filettate. I vecchi commenti sono chiamati Note in Excel 365. La schermata qui sotto mostra come vengono visualizzati i commenti filettati quando aperti in Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

I commenti filettati vengono mostrati in questo modo nelle versioni più vecchie di Excel. Le seguenti immagini sono state scattate aprendo il file di esempio in Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells fornisce anche la funzionalità di gestire commenti in thread.

## **Aggiungi Commenti in Thread**

### **Aggiungi commento in thread con Excel**

Per aggiungere commenti in thread in Excel 365, seguire i seguenti passaggi.

- Metodo 1
  - Fare clic sulla scheda **Revisione**
  - Fare clic sul pulsante **Nuovo commento**
  - Si aprirà un dialogo per inserire commenti nella cella attiva.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Metodo 2
  - Fare clic con il pulsante destro del mouse sulla cella in cui si desidera inserire il commento.
  - Fare clic sull'opzione **Nuovo commento**
  - Si aprirà un dialogo per inserire commenti nella cella attiva.
  - ![todo:image_alt_text](threaded-comments_5)

### **Aggiungi Commento in Thread utilizzando Aspose.Cells**

Aspose.Cells fornisce il metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) per aggiungere commenti annidati. Il metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) accetta i seguenti tre parametri.

- Nome della cella: Il nome della cella in cui verrà inserito il commento.
- Testo del commento: Il testo del commento.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/): L'autore del commento

Il seguente esempio di codice dimostra l'uso del metodo [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) per aggiungere un Commento in Thread alla cella A1. Si prega di vedere il [file Excel di output](89849859.xlsx) generato dal codice per riferimento.

#### **Codice di Esempio**

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

## **Leggi Commenti in Thread**

### **Leggi commenti in thread con Excel**

Per leggere i commenti in Excel, passa semplicemente il mouse sopra la cella contenente i commenti per visualizzarli. La visualizzazione dei commenti assomiglierà alla vista dell'immagine seguente.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Leggi i commenti con thread utilizzando Aspose.Cells**

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) per recuperare i commenti con thread per la colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Puoi iterare sul [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) per visualizzare i commenti.

L'esempio seguente dimostra la lettura dei commenti dalla colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

#### **Codice di Esempio**

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

#### **Output della console**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Leggi l'ora della creazione dei commenti con thread**

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) per recuperare i commenti con thread per la colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Puoi iterare su [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) e utilizzare la proprietà [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/).

L'esempio seguente dimostra la lettura dell'orario di creazione dei commenti con thread caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare l'output della console generato dal codice per riferimento.

#### **Codice di Esempio**

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

#### **Output della console**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Modifica i commenti con thread**

### **Modifica il commento con thread con Excel**

Per modificare un commento con thread in Excel, fare clic sul collegamento **Modifica** nel commento come mostrato nell'immagine seguente.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Modifica il commento con thread utilizzando Aspose.Cells**

Aspose.Cells fornisce il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) per recuperare i commenti con thread per la colonna specificata. Il metodo [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) accetta il nome della colonna come parametro e restituisce il [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Puoi aggiornare il commento richiesto su [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) e salvare il workbook.

L'esempio seguente dimostra la modifica del primo commento con thread nella colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare il [file Excel di output](89849862.xlsx) generato dal codice che mostra il commento aggiornato per riferimento.

#### **Codice di Esempio**

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

## **Rimuovi i commenti con thread**

### **Rimuovi i commenti con thread con Excel**

Per rimuovere i commenti con thread in Excel, fai clic con il pulsante destro del mouse sulla cella contenente i commenti e seleziona l'opzione **Elimina commento** come mostrato nell'immagine seguente.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Rimuovi i commenti con thread utilizzando Aspose.Cells**

Aspose.Cells fornisce il metodo [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) per rimuovere i commenti per la colonna specificata. Il metodo [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) accetta il nome della colonna come parametro e rimuove i commenti in quella colonna.

L'esempio seguente dimostra la rimozione dei commenti nella colonna A1 caricando il [file Excel di esempio](89849861.xlsx). Si prega di consultare il [file Excel di output](89849864.xlsx) generato dal codice per riferimento.

#### **Codice di Esempio**

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

Si noti che rimuovendo un commento con Aspose.Cells, l'autore non viene automaticamente rimosso. Se è necessario rimuovere anche l'autore, utilizzare il metodo RemoveAt della classe [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/) come mostrato nell'esempio sopra.

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
