---
title: Paramètres de protection avancée depuis Excel XP dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---

{{% alert color="primary" %}}

- Supprimer des lignes ou des colonnes.
- Modifier le contenu, les objets ou les scénarios.
- Formater les cellules, les lignes ou les colonnes.
- Insérer des lignes, des colonnes ou des hyperliens.
- Sélectionner des cellules verrouillées ou déverrouillées.
- Utiliser des tableaux croisés dynamiques et bien plus encore.

Aspose.Cells prend en charge tous les paramètres de protection avancés offerts par Excel XP ou les versions ultérieures.

{{% /alert %}}

## **Paramètres de protection avancés utilisant Excel XP et les versions ultérieures**

Pour afficher les paramètres de protection disponibles dans Excel XP :

1. Dans le menu **Outils**, sélectionnez **Protection** suivi de **Protéger la feuille**.
   Une boîte de dialogue s'affiche.

   **Boîte de dialogue pour afficher les options de protection dans Excel XP**

![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Autoriser ou restreindre les fonctionnalités des feuilles de calcul ou appliquer un mot de passe.

### **Paramètres de protection avancés utilisant Aspose.Cells**

Aspose.Cells supporte tous les paramètres de protection avancés.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit la propriété [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) utilisée pour appliquer ces paramètres de protection avancés. La propriété [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) est en fait un objet de la classe [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) qui encapsule plusieurs propriétés booléennes pour désactiver ou activer les restrictions.

Voici un petit exemple d'application. Il ouvre un fichier Excel et utilise la plupart des paramètres de protection avancés pris en charge par Excel XP et les versions ultérieures.

**C#**

{{< highlight csharp >}}

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

## **Télécharger le code en cours d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
