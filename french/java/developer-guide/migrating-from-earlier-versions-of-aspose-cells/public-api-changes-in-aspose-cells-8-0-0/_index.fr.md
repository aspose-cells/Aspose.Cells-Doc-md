---
title: Public API Changements dans Aspose.Cells 8.0.0
type: docs
weight: 20
url: /fr/java/public-api-changes-in-aspose-cells-8-0-0/
---
{{% alert color="primary" %}} 

Cette page répertorie les modifications API publiques introduites dans Aspose.Cells 8.0.0. Il comprend non seulement des méthodes publiques nouvelles et obsolètes, mais également une description de tout changement dans le comportement en arrière-plan de Aspose.Cells susceptible d'affecter le code existant.

{{% /alert %}} 
## **Ajout de MemorySetting à LoadOptions & WorkbookSettings**
À partir de la v8.0.0 de Aspose.Cells for Java, nous avons fourni les options d'utilisation de la mémoire pour des considérations de performances. La propriété MemorySetting est maintenant disponible dans les classes LoadOptions et WorkbookSettings.
### **Exemple**
Montre comment lire un fichier Excel (de grande taille) en mode optimisé.

**Java**

{{< highlight "csharp" >}}

 //Initialize LoadOptions

LoadOptions options = new LoadOptions();

//Set memory preferences

options.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Instantiate the Workbook with an object of LoadOptions

Workbook book = new Workbook(myDir + "large.xlsx", options);

{{< /highlight >}}

Montre comment écrire un grand ensemble de données dans une feuille de calcul en mode optimisé.

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences for WorkbookSettings

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large data into the cells

//.........

{{< /highlight >}}

{{% alert color="primary" %}} 

 Veuillez consulter l'article détaillé sur[Optimisation de la mémoire lors de l'utilisation de fichiers volumineux](/cells/fr/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)s.

{{% /alert %}}
## **Les implémentations de Row & Cell ont changé**
 Dans les versions précédentes, les objets Row et Cell étaient conservés en mémoire pour représenter la ligne et la cellule correspondantes dans une feuille de calcul. La même instance était renvoyée à chaque fois**RowCollection[int index]** ou alors**Cells[int ligne, int colonne]** ont été récupérés. Pour des raisons de performances de la mémoire, seules les propriétés et les données de Row et Cell seront conservées dans la mémoire à partir de maintenant. Par conséquent, l'objet Row & Cell est devenu l'enveloppe des propriétés susmentionnées.
### **Exemple**
Montre comment comparer les objets Cell et Row à partir de maintenant.

**Java**

{{< highlight "csharp" >}}

 //..

row1.equals(row2);


cell1.equals(cell2);

//..

{{< /highlight >}}

Comme les objets Row et Cell sont instanciés en fonction de l'invocation, ils ne seront pas conservés et gérés en mémoire par le composant Cells. Par conséquent, après certaines opérations d'insertion et de suppression, les index de lignes et de colonnes peuvent ne pas être mis à jour ou, pire encore, ces objets deviennent invalides.
### **Exemple**
Par exemple, l'extrait de code suivant renverra des résultats non valides en utilisant 8.0.0 et supérieur,

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

Avec la nouvelle version, l'objet Cell deviendra invalide ou fera référence à A2 avec une valeur indésirable. Afin d'éviter une telle situation, récupérez les objets Row ou Cell à partir de la collection de cellules pour récupérer le résultat correct.

**Java**

{{< highlight "csharp" >}}

 Cell cell = cells.get("A2");

System.out.println(cell.getName() + ":" + cell.getValue());

cells.insertRange(CellArea.createCellArea("A1", "A1"), ShiftType.DOWN);

//Fetch the cell reference again

Cell cell = cells.get("A3");

System.out.println(cell.getName() + ":" + cell.getValue());

{{< /highlight >}}

{{% alert color="primary" %}} 

RowCollection n'hérite plus de CollectionBase car il n'y a pas d'objet Row dans sa liste interne.

{{% /alert %}}
## **Cell. Comportement de StringValue modifié**
 Dans les versions précédentes, motif spécial_ été ignoré lors du formatage des valeurs de cellule, où le caractère spécial * produisait toujours un caractère dans le résultat formaté. A partir de cette version, nous avons changé la logique pour gérer les caractères spéciaux_ et* afin de rendre le résultat formaté identique à celui de l'application Excel. Par exemple, le format de cellule personnalisé "_(\$* #,##0.00_)" utilisé pour représenter la valeur 123 produit le résultat sous la forme "123,00 $". Avec les nouvelles versions, Cell.StringValue contiendra le résultat sous la forme "123,00 $", ce qui correspond au même comportement que l'application Excel lors de la copie de la cellule pour envoyer un SMS ou exporter vers CSV.
## **Ajout de CreatedTime à PdfSaveOptions**
Désormais, les utilisateurs peuvent obtenir ou définir l'heure de création PDF tout en enregistrant la feuille de calcul sur PDF tout en utilisant la classe PdfSaveOptions.
## **Ajout de ShowFormulas à la feuille de calcul**
À partir de maintenant, les utilisateurs peuvent utiliser la propriété booléenne ShowFormulas offerte par Worksheet pour basculer la vue entre la formule et la valeur d'une feuille de calcul donnée.
## **Ooxml ajouté à FileFormatType**
Une nouvelle constante Ooxml a été ajoutée à la classe FileFormatType pour représenter le fichier XML ouvert Office chiffré tel que XLSX, DOCX, PPTX et plus.
## **Obsolète FilterColumnCollection of AutoFilter**
Avec Aspose.Cells for Java, la méthode getFilterColumnCollection a été marquée comme obsolète. Il est suggéré d'utiliser la méthode AuotFilter.getFilterColumns à la place.
## **Remplacement de SeriesCollection.SecondCatergoryData par SeriesCollection.SecondCategoryData**
Nous avons essentiellement corrigé l'erreur de frappe dans le nom de la méthode pour SeriesCollection.getSecondCatergoryData. Vous pouvez utiliser la méthode SeriesCollection.getSecondCategoryData maintenant, alors que la méthode originale SeriesCollection.getSecondCatergoryData a été marquée comme obsolète.
