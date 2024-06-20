---
title: Insérer et supprimer des commentaires de cellules dans une feuille de calcul
type: docs
weight: 30
url: /fr/net/inserting-and-removing-cell-comments-in-a-worksheet/
---

{{% alert color="primary" %}}

Généralement, les commentaires sont utilisés pour ajouter des informations supplémentaires aux cellules d'une feuille de calcul. Nous les utilisons de temps en temps et les supprimons lorsque nous n'en avons plus besoin. Les commentaires sont utiles si vous devez documenter une valeur particulière ou vous aider à vous rappeler ce que fait une formule. Lorsque vous déplacez le pointeur de la souris sur une cellule qui a un commentaire, le commentaire apparaît dans une petite boîte.

Dans cet article, nous comparons comment ajouter et supprimer des commentaires des cellules en utilisant VSTO et Aspose.Cells for .NET. Aspose.Cells for .NET fonctionne avec des fichiers Microsoft Excel indépendamment de l'automatisation Office et vous offre des outils puissants pour créer et manipuler des feuilles de calcul.

{{% /alert %}}

## **Ajouter et supprimer des commentaires sur les cellules**

Pour ajouter des commentaires aux cellules :

1. Ouvrez un fichier Excel existant.
1. Ajoutez un commentaire à une cellule.
1. Enregistrez le fichier.

Pour supprimer les commentaires, le processus est similaire, à l'exception que le commentaire est supprimé.

Les extraits de code ci-dessous illustrent d'abord comment [ajouter un commentaire](/cells/fr/net/inserting-and-removing-cell-comments-in-a-worksheet/) et ensuite comment [supprimer un commentaire](/cells/fr/net/inserting-and-removing-cell-comments-in-a-worksheet/) avec VSTO ou Aspose.Cells for .NET.

## **Insertion de Commentaires**

Ces extraits de code montrent comment ajouter un commentaire à une cellule d'abord avec [VSTO](/cells/fr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) et ensuite avec [Aspose.Cells for .NET](/cells/fr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB).

### **Insertion d'un commentaire avec VSTO**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the A1 cell.

Excel.Range rng1=excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

rng1.AddComment("This is my comment");

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **Insertion d'un commentaire avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

int commentIndex=workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

Comment comment=workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

comment.Note="This is my comment";

//Save As the excel file.

workbook.Save(@"d:\test\Book1.xls");



{{< /highlight >}}

## **Supprimer les Commentaires**

Pour supprimer un commentaire d'une cellule, utilisez les lignes de code suivantes pour [VSTO](/cells/fr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) et [Aspose.Cells](/cells/fr/net/inserting-and-removing-cell-comments-in-a-worksheet/) pour .NET (C#, VB).

### **Suppression d'un commentaire avec VSTO**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Suppression d'un commentaire avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
