---
title: Changements dans l API publique dans Aspose.Cells 8.0.0
type: docs
weight: 10
url: /fr/net/public-api-changes-in-aspose-cells-8-0-0/
---

{{% alert color="primary" %}} 

Cette page répertorie les changements dans l'API publique qui ont été introduits dans Aspose.Cells 8.0.0. Il inclut non seulement les nouvelles méthodes publiques et obsolètes, mais aussi une description de tout changement dans le comportement en arrière-plan dans Aspose.Cells qui peut affecter le code existant.

{{% /alert %}} 
## **Ajout de MemorySetting aux options de chargement et aux paramètres du classeur**
À partir de la version 8.0.0 de Aspose.Cells for .NET, nous avons fourni des options d'utilisation de la mémoire pour des considérations de performances. La propriété MemorySetting est désormais disponible dans les classes LoadOptions & WorkbookSettings.
##### **Exemple**
Démontre comment lire un fichier Excel (de grande taille) en mode optimisé.

**C#**

{{< highlight csharp >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Démontre comment écrire un grand ensemble de données dans une feuille de calcul en mode optimisé.

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.Settings.MemorySetting = MemorySetting.MEMORY_PREFERENCE;

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

Veuillez consulter l'article détaillé sur [Optimiser la mémoire lors du travail avec de grands fichiers](/cells/fr/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/).

{{% /alert %}}
## **Les implémentations de Row & Cell ont changé**
Dans les versions précédentes, les objets Row et Cell étaient conservés en mémoire pour représenter la ligne et la cellule correspondantes dans une feuille de calcul. La même instance était renvoyée chaque fois que **RowCollection[int index]** ou **Cells[int row, int column]** étaient récupérés. Pour des considérations de performances en matière de mémoire, seules les propriétés et les données de Row et Cell seront désormais conservées en mémoire. Par conséquent, les objets Row & Cell sont devenus les enveloppes desdites propriétés.
### **Exemple**
Démontre comment comparer les objets Cell et Row à partir de maintenant.

**C#**

{{< highlight csharp >}}

 //..

row1.Equals(row2);


cell1.Equals(cell2);

//..

{{< /highlight >}}

Étant donné que les objets Row et Cell sont instanciés en fonction de l'appel, ils ne seront pas conservés et gérés en mémoire par le composant Cells. Par conséquent, après certaines opérations d'insertion et de suppression, les index des lignes et des colonnes peuvent ne pas être mis à jour ou même ces objets deviennent invalides.
### **Exemple**
Par exemple, le code suivant renverra des résultats incorrects en utilisant 8.0.0 et supérieur,

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}



Avec la nouvelle version, l'objet Cell deviendra invalide ou se référera à A2 avec une valeur indésirable. Pour éviter une telle situation, récupérez à nouveau les objets Row ou Cell de la collection cells pour obtenir le résultat correct.

**C#**

{{< highlight csharp >}}

 Cell cell = cells["A2"];

Console.WriteLine(cell.Name + ":" + cell.Value);

cells.InsertRange(CellArea.CreateCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells["A3"];

Console.WriteLine(cell.Name + ":" + cell.Value);

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection n'hérite plus de CollectionBase car il n'y a pas d'objet Row dans sa liste interne.

{{% /alert %}}
## **Le comportement de Cell.StringValue a changé**
Dans les versions précédentes, le motif spécial _ était ignoré lors de la mise en forme des valeurs de cellule, tandis que le caractère spécial * produisait toujours un caractère dans le résultat mis en forme. À partir de cette version, nous avons modifié la logique pour gérer les caractères spéciaux _ et * afin de rendre le résultat mis en forme identique à celui de l'application Excel. Par exemple, le format de cellule personnalisé "_(\$* #,##0.00_)" utilisé pour représenter la valeur 123 produisait le résultat "$ 123.00". Avec les nouvelles versions, Cell.StringValue contiendra le résultat comme "$123.00" qui est le même comportement que l'application Excel pour copier la cellule en texte ou exporter au format CSV.
## **Ajout de CreatedTime à PdfSaveOptions**
Maintenant, les utilisateurs peuvent obtenir ou définir l'heure de création du PDF lors de l'enregistrement de la feuille de calcul au format PDF en utilisant la classe PdfSaveOptions.
## **Ajout de ShowFormulas à Worksheet**
Désormais, les utilisateurs peuvent utiliser la propriété booléenne ShowFormulas offerte par Worksheet pour passer de la formule à la valeur d'une feuille de calcul donnée.
## **Ajout de Ooxml à FileFormatType**
Une nouvelle constante Ooxml a été ajoutée à la classe FileFormatType pour représenter le fichier XML Office encrypté tel que XLSX, DOCX, PPTX et plus encore.
## **Obsolète FilterColumnCollection d'AutoFilter**
Avec Aspose.Cells for Java, la propriété FilterColumnCollection a été marquée comme obsolète. Il est suggéré d'utiliser la propriété AuotFilter.FilterColumns à la place.
## **Remplacé SeriesCollection.SecondCatergoryData par SeriesCollection.SecondCategoryData**
Nous avons corrigé l'erreur de typographie dans le nom de propriété pour SeriesCollection.SecondCatergoryData. Vous pouvez désormais utiliser la propriété SeriesCollection.SecondCategoryData à partir de maintenant, tandis que la propriété d'origine SeriesCollection.SecondCatergoryData a été marquée comme obsolète.
{{< app/cells/assistant language="csharp" >}}
