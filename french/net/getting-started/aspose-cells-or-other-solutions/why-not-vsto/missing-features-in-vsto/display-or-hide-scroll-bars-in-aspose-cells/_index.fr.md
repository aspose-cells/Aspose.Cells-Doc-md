---
title: Afficher ou masquer les barres de défilement dans Aspose.Cells
type: docs
weight: 70
url: /fr/net/display-or-hide-scroll-bars-in-aspose-cells/
---
{{% alert color="primary" %}}

Les barres de défilement sont très utilisées pour naviguer dans le contenu de n'importe quel fichier. Normalement, il existe deux types de barres de défilement :

- Barres de défilement verticales
- Barres de défilement horizontales

Microsoft Excel fournit également des barres de défilement horizontales et verticales permettant aux utilisateurs de faire défiler le contenu des feuilles de calcul. En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des deux types de barres de défilement dans les fichiers Excel.

{{% /alert %}}

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fournit un large éventail de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des barres de défilement, utilisez le[**Paramètres du classeur**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings) classer'[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) et[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) Propriétés.[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible) et[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible) sont des propriétés booléennes, ce qui signifie que ces propriétés ne peuvent stocker**vrai** ou**faux** valeurs.

Vous trouverez ci-dessous un code complet qui ouvre un fichier Excel, book1.xls, masque les deux barres de défilement, puis enregistre le fichier modifié sous output.xls .

La capture d'écran ci-dessous montre le fichier Book1.xls contenant les deux barres de défilement. Le fichier modifié est enregistré en tant que fichier output.xls, également affiché ci-dessous.

**Book1.xls : fichier Excel avant toute modification**

![tâche : image_autre_texte](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls : fichier Excel après modification**

![tâche : image_autre_texte](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Télécharger le code d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **Télécharger l'exemple de code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
