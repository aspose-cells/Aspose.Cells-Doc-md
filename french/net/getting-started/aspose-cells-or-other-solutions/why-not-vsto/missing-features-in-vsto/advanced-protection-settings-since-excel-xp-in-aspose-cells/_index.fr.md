---
title: Paramètres de protection avancés depuis Excel XP dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- Supprimer des lignes ou des colonnes.
- Modifiez des contenus, des objets ou des scénarios.
- Mettre en forme les cellules, les lignes ou les colonnes.
- Insérez des lignes, des colonnes ou des hyperliens.
- Sélectionnez les cellules verrouillées ou déverrouillées.
- Utilisez des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells prend en charge tous les paramètres de protection avancés offerts par Excel XP ou les versions ultérieures.

{{% /alert %}}

## **Paramètres de protection avancés à l'aide d'Excel XP et des versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1.  Du**Outils** menu, sélectionnez**protection** suivie par**Feuille de protection**.
 Une boîte de dialogue s'affiche.

   **Boîte de dialogue pour afficher les options de protection dans Excel XP**

![tâche : image_autre_texte](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Autorisez ou restreignez les fonctionnalités des feuilles de calcul ou appliquez un mot de passe.

### **Paramètres de protection avancés à l'aide de Aspose.Cells**

Aspose.Cells prend en charge tous les paramètres de protection avancés.

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer.

 La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe fournit la[**protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)propriété utilisée pour appliquer ces paramètres de protection avancés. La[**protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) la propriété est en fait un objet de la[**protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) classe qui encapsule plusieurs propriétés booléennes pour désactiver ou activer des restrictions.

Ci-dessous un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
