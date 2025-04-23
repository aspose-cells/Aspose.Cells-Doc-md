---
title: Affichage ou masquage des quadrillages dans Aspose.Cells
type: docs
weight: 50
url: /fr/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

Toutes les feuilles de calcul Excel ont des quadrillages par défaut. Ils permettent de délimiter les cellules, ce qui facilite l'entrée de données dans des cellules particulières. Les quadrillages nous permettent de visualiser une feuille de calcul comme une collection de cellules, où chaque cellule est facilement identifiable.

{{% /alert %}}

## **Contrôler la visibilité des quadrillages**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit une large gamme de propriétés et de méthodes pour gérer une feuille de calcul. Pour contrôler la visibilité des quadrillages, utilisez la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

Un exemple complet est donné ci-dessous qui démontre l'utilisation de la propriété [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) pour masquer les quadrillages de la première feuille de calcul du fichier Excel.

Sur la capture d'écran ci-dessous, vous pouvez voir que le fichier Book1.xls contient trois feuilles de calcul : Sheet1, Sheet2 et Sheet3. Toutes les feuilles de calcul ont des quadrillages.

** Book1.xls : vue de la feuille de calcul avant modification ** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

Le fichier Book1.xls est ouvert en utilisant la classe Workbook et les lignes de la grille sur la première feuille de calcul sont cachées. Le fichier modifié est enregistré sous le nom de output.xls.

**Output.xls : feuille de calcul après modification** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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

## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **Télécharger le code source d'exemple**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
