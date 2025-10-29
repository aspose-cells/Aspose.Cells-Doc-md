---  
title: Commentaires filaires avec Node.js via C++  
linktitle: Commentaires en fil  
type: docs  
weight: 140  
url: /fr/nodejs-cpp/threaded-comments/  
description: Gérez les commentaires filaires dans les documents Excel en utilisant Aspose.Cells for Node.js via C++. Apprenez à ajouter, lire, modifier et supprimer des commentaires filaires.  
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

Aspose.Cells fournit la méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) pour ajouter des commentaires filaires. La méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) accepte les trois paramètres suivants.  

- Nom de la cellule : Le nom de la cellule où le commentaire sera inséré.  
- Texte du commentaire : Le texte du commentaire.  
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentauthor) : L'auteur du commentaire  

L'exemple de code ci-dessous illustre l'utilisation de la méthode [**Comments.AddThreadedComment**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-) pour ajouter un commentaire filaire à la cellule A1. Veuillez consulter le [fichier Excel de sortie](89849859.xlsx) généré par le code pour référence.  

#### **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const outDir = path.join(__dirname, "output");

const workbook = new AsposeCells.Workbook();

// Add Author
const authorIndex = workbook.getWorksheets().getThreadedCommentAuthors().add("Aspose Test", "", "");
const author = workbook.getWorksheets().getThreadedCommentAuthors().get(authorIndex);

// Add Threaded Comment
workbook.getWorksheets().get(0).getComments().addThreadedComment("A1", "Test Threaded Comment", author);

workbook.save(outDir + "AddThreadedComments_out.xlsx");
```  

## **Lire les Commentaires enfilés**  

### **Lire des commentaires enfilés avec Excel**  

Pour lire des commentaires enfilés dans Excel, survolez simplement la cellule contenant les commentaires pour les afficher. La vue des commentaires ressemblera à la vue dans l'image suivante.  

![todo:image_alt_text](threaded-comments_1.jpg)  

### **Lire des commentaires enfilés à l'aide d'Aspose.Cells**  

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) pour récupérer les commentaires en fil pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) accepte le nom de colonne en tant que paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Vous pouvez itérer sur le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) pour afficher les commentaires.  

L'exemple suivant démontre la lecture des commentaires de la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.  

#### **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data"); // Adjust as necessary

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook which contains threaded comments
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();
for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
}
```  

#### **Sortie console**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

{{< /highlight >}}  

### **Lire l'heure de création des commentaires en fil**  

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) pour récupérer les commentaires filaires pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) accepte le nom de colonne en paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Vous pouvez parcourir le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) et utiliser la propriété [**ThreadedComment.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/threadedcomment/#getCreatedTime--).  

L'exemple suivant démontre la lecture de l'heure de création des commentaires en fil en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter la sortie de la console générée par le code pour référence.  

#### **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comments
const threadedComments = worksheet.getComments().getThreadedComments("A1");

const count = threadedComments.getCount();

for (let i = 0; i < count; i++) {
const comment = threadedComments.get(i);
console.log("Comment: " + comment.getNotes());
console.log("Author: " + comment.getAuthor().getName());
console.log("Created Time: " + comment.getCreatedTime());
}
```  

#### **Sortie console**  

{{< highlight javascript >}}  

Comment: Test Threaded Comment  

Author: Aspose Test  

Created Time: 5/15/2019 12:46:23 PM  

{{< /highlight >}}  

## **Modifier les commentaires en fil**  

### **Modifier le commentaire en fil avec Excel**  

Pour modifier un commentaire en fil dans Excel, cliquez sur le lien **Modifier** sur le commentaire comme indiqué dans l'image suivante.  

![todo:image_alt_text](threaded-comments_7.jpg)  

### **Modifier le commentaire en fil en utilisant Aspose.Cells**  

Aspose.Cells fournit la méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) pour récupérer les commentaires filaires pour la colonne spécifiée. La méthode [**Comments.GetThreadedComments**](https://reference.aspose.com/cells/nodejs-cpp/commentcollection/#getthreadedcomments-string-) accepte le nom de colonne en paramètre et retourne le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection). Vous pouvez mettre à jour le commentaire requis dans le [**ThreadedCommentCollection**](https://reference.aspose.com/cells/nodejs-cpp/threadedcommentcollection) et sauvegarder le classeur.  

L'exemple suivant démontre l'édition du premier commentaire en fil dans la colonne A1 en chargeant le [Fichier Excel d'exemple](89849861.xlsx). Veuillez consulter le [fichier Excel de sortie](89849862.xlsx) généré par le code montrant le commentaire mis à jour pour référence.  

#### **Code d'exemple**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source and output directories
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "ThreadedCommentsSample.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get Threaded Comment
const comment = worksheet.getComments().getThreadedComments("A1").get(0);
comment.setNotes("Updated Comment");

workbook.save(outDir + "EditThreadedComments.xlsx");
```  

## **Supprimer les commentaires en filigrane**  

### **Supprimer les commentaires en filigrane avec Excel**  

Pour supprimer les commentaires en filigrane dans Excel, cliquez avec le bouton droit sur la cellule contenant les commentaires et cliquez sur l'option **Supprimer le commentaire** comme indiqué dans l'image suivante.  

![todo:image_alt_text](threaded-comments_8.jpg)   


{{< app/cells/assistant language="nodejs-cpp" >}}
