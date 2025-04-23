---
title: Commentaires en fil de C++
linktitle: Commentaires en fil
type: docs
weight: 140
url: /fr/cpp/threaded-comments/
description: Apprenez comment ajouter, lire, éditer et supprimer des commentaires en fil dans des fichiers Excel en utilisant Aspose.Cells avec C++.
---

## **Commentaires en fil**

MS Excel 365 offre la possibilité d'ajouter des commentaires en fil. Ces commentaires fonctionnent comme des conversations et peuvent être utilisés pour des discussions. Les commentaires sont maintenant dotés d'une boîte de réponse qui permet des conversations en fil. Les anciens commentaires sont appelés Notes dans Excel 365. La capture d'écran ci-dessous montre comment les commentaires en fil sont affichés lorsqu'ils sont ouverts dans Excel.

![todo:image_alt_text](threaded-comments_1.jpg)

Les commentaires en fil sont affichés comme ceci dans les anciennes versions d'Excel. Les images suivantes ont été prises en ouvrant le fichier d'exemple dans Excel 2016.

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells fournit également la fonctionnalité pour gérer les commentaires en fil.

## **Ajouter des commentaires en fil**

### **Ajouter un commentaire en fil avec Excel**

Pour ajouter des commentaires enfilés dans Excel 365, suivez les étapes suivantes.

- Méthode 1
  - Cliquez sur l'onglet **Révision**
  - Cliquez sur le bouton **Nouveau commentaire**
  - Cela ouvrira une boîte de dialogue pour saisir des commentaires dans la cellule active.
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- Méthode 2
  - Cliquez avec le bouton droit sur la cellule où vous souhaitez insérer le commentaire.
  - Cliquez sur l'option **Nouveau commentaire**
  - Cela ouvrira une boîte de dialogue pour saisir des commentaires dans la cellule active.
  - ![todo:image_alt_text](threaded-comments_5)

### **Ajouter un commentaire enfilé à l'aide d'Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) pour ajouter des commentaires filaires. La méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) accepte les trois paramètres suivants.

- Nom de la cellule : Le nom de la cellule où le commentaire sera inséré.
- Texte du commentaire : Le texte du commentaire.
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthor/) : L'auteur du commentaire

L'exemple de code suivant démontre l'utilisation de la méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/addthreadedcomment/) pour ajouter un commentaire enfilé à la cellule A1. Veuillez consulter le fichier Excel de sortie (89849859.xlsx) généré par le code pour référence.

#### **Code d'exemple**

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

## **Lire les Commentaires enfilés**

### **Lire des commentaires enfilés avec Excel**

Pour lire des commentaires enfilés dans Excel, survolez simplement la cellule contenant les commentaires pour les afficher. La vue des commentaires ressemblera à la vue dans l'image suivante.

![todo:image_alt_text](threaded-comments_1.jpg)

### **Lire des commentaires enfilés à l'aide d'Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) pour récupérer les commentaires en fil pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) accepte le nom de colonne en tant que paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Vous pouvez itérer sur le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) pour afficher les commentaires.

L'exemple suivant démontre la lecture des commentaires de la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Code d'exemple**

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

#### **Sortie console**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **Lire l'heure de création des commentaires en fil**

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) pour récupérer les commentaires en fil pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) accepte le nom de colonne en tant que paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Vous pouvez itérer sur le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) et utiliser la propriété [**ThreadedComment.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcomment/getcreatedtime/).

L'exemple suivant démontre la lecture de l'heure de création des commentaires en fil en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.

#### **Code d'exemple**

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

#### **Sortie console**

{{< highlight cpp >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **Modifier les commentaires en fil**

### **Modifier le commentaire en fil avec Excel**

Pour modifier un commentaire en fil dans Excel, cliquez sur le lien **Modifier** sur le commentaire comme indiqué dans l'image suivante.

![todo:image_alt_text](threaded-comments_7.jpg)

### **Modifier le commentaire en fil en utilisant Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) pour récupérer les commentaires en fil pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/getthreadedcomments/) accepte le nom de colonne en tant que paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/). Vous pouvez mettre à jour le commentaire requis dans le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentcollection/) et enregistrer le classeur.

L'exemple suivant démontre l'édition du premier commentaire en fil dans la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter le [fichier Excel de sortie](89849862.xlsx) généré par le code montrant le commentaire mis à jour pour référence.

#### **Code d'exemple**

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

## **Supprimer les commentaires en filigrane**

### **Supprimer les commentaires en filigrane avec Excel**

Pour supprimer les commentaires en filigrane dans Excel, cliquez avec le bouton droit sur la cellule contenant les commentaires et cliquez sur l'option **Supprimer le commentaire** comme indiqué dans l'image suivante.

![todo:image_alt_text](threaded-comments_8.jpg)

### **Supprimer les commentaires en filigrane à l'aide de Aspose.Cells**

Aspose.Cells fournit la méthode [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) pour supprimer les commentaires de la colonne spécifiée. La méthode [**Comments.RemoveAt**](https://reference.aspose.com/cells/cpp/aspose.cells/commentcollection/removeat/) accepte le nom de la colonne en paramètre pour supprimer les commentaires dans cette colonne.

L'exemple suivant montre comment supprimer les commentaires dans la colonne A1 en chargeant le [fichier Excel d'exemple](89849861.xlsx). Veuillez consulter le [fichier Excel de sortie](89849864.xlsx) généré par le code pour référence.

#### **Code d'exemple**

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

Veuillez noter qu'en supprimant le commentaire avec Aspose.Cells, l'auteur n'est pas automatiquement supprimé. Si vous devez également supprimer l'auteur, veuillez utiliser la méthode RemoveAt de la classe [**ThreadedCommentAuthorCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/threadedcommentauthorcollection/) comme indiqué dans l'exemple ci-dessus.

{{% /alert %}}
