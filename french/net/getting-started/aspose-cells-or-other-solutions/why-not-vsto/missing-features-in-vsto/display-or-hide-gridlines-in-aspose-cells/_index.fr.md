---
title: Afficher ou masquer le quadrillage dans Aspose.Cells
type: docs
weight: 50
url: /fr/net/display-or-hide-gridlines-in-aspose-cells/
---
{{% alert color="primary" %}}

Toutes les feuilles de calcul Excel ont un quadrillage par défaut. Ils aident à délimiter les cellules, de sorte qu'il est facile d'entrer des données dans des cellules particulières. Le quadrillage nous permet de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

{{% /alert %}}

## **Contrôle de la visibilité du quadrillage**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des lignes de grille, utilisez la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe'[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) la propriété.[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'un**vrai** ou alors**faux** évaluer.

 Un exemple complet est donné ci-dessous qui démontre l'utilisation de la[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) propriété de la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) class pour masquer le quadrillage de la première feuille de calcul du fichier Excel.

Dans la capture d'écran ci-dessous, vous pouvez voir que le fichier Book1.xls contient trois feuilles de calcul : Sheet1, Sheet2 et Sheet3. Toutes les feuilles de calcul ont un quadrillage.

**Book1.xls : vue feuille de calcul avant modification** 

![tâche : image_autre_texte](display-or-hide-gridlines-in-aspose-cells_1.png)

Le fichier Book1.xls est ouvert à l'aide de la classe Workbook et le quadrillage de la première feuille de calcul est masqué. Le fichier modifié est enregistré sous output.xls.

**Output.xls : feuille de calcul après modification** 

![tâche : image_autre_texte](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Télécharger le code d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Télécharger l'exemple de code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
