---
title: Afficher ou masquer les en-têtes de colonne de ligne dans Aspose.Cells
type: docs
weight: 60
url: /fr/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

Toutes les feuilles de calcul d'un fichier Excel sont composées de cellules disposées en lignes et en colonnes. Toutes les lignes et colonnes ont des valeurs uniques qui sont utilisées pour les identifier et pour identifier des cellules individuelles. Par exemple, les lignes sont numérotées – 1, 2, 3, 4, etc. – et les colonnes sont classées par ordre alphabétique – A, B, C, D, etc. Les valeurs des lignes et des colonnes sont affichées dans les en-têtes. À l'aide de Aspose.Cells, les développeurs peuvent contrôler la visibilité de ces en-têtes de ligne et de colonne.

{{% /alert %}}

## **Contrôle de la visibilité des feuilles de calcul**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans un fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour contrôler la visibilité des en-têtes de ligne et de colonne, utilisez la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer'[**EstRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propriété.[**EstRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'un**vrai** ou**faux** évaluer.

 Un exemple complet est donné ci-dessous qui montre comment utiliser le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer'[**EstRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) propriété pour masquer les en-têtes de ligne et de colonne sur la première feuille de calcul d'un fichier.

La capture d'écran montre Book1.xls, le fichier d'entrée. Il contient trois feuilles de calcul : Feuil1, Feuil2 et Feuil3. Chaque feuille de calcul affiche des en-têtes de ligne et de colonne.

**Book1.xls : feuille de calcul avant modification**

![tâche : image_autre_texte](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls est ouvert en appelant la méthode Open de la classe Workbook et les en-têtes de ligne et de colonne de la première feuille de calcul sont masqués. Le fichier modifié est enregistré sous output.xls.

**Output.xls : feuille de calcul après modification** 

![tâche : image_autre_texte](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
