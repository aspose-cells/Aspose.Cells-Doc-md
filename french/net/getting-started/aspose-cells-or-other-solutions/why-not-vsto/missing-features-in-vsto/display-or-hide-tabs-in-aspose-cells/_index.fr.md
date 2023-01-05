---
title: Afficher ou masquer les onglets dans Aspose.Cells
type: docs
weight: 80
url: /fr/net/display-or-hide-tabs-in-aspose-cells/
---
{{% alert color="primary" %}} 

Si vous regardez attentivement le bas d'un fichier Excel Microsoft, vous verrez un certain nombre de contrôles. Ceux-ci inclus:

- Onglets de feuille.
- Boutons de défilement des onglets.

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur n'importe quel onglet pour passer à cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel contient un bon nombre de feuilles de calcul, vous avez besoin de boutons pour les parcourir. Ainsi, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de la feuille.

**Onglets de feuille et boutons de défilement d'onglet** 

![tâche : image_autre_texte](display-or-hide-tabs-in-aspose-cells_1.png)

À l'aide de Aspose.Cells, les développeurs peuvent contrôler la visibilité des onglets de feuille et des boutons de défilement des onglets dans les fichiers Excel.

{{% /alert %}} 

Vous trouverez ci-dessous un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous output.xls.

Vous pouvez voir que le fichier Book1.xls contient des onglets dans la figure ci-dessous. Une fois l'exemple de code exécuté, les onglets sont masqués, comme vous pouvez le voir sur la capture d'écran du fichier output.xls ci-dessous.

**book1.xls : fichier Excel avant toute modification** 

![tâche : image_autre_texte](display-or-hide-tabs-in-aspose-cells_2.png)

**output.xls : fichier Excel après modification** 

![tâche : image_autre_texte](display-or-hide-tabs-in-aspose-cells_3.png)

**C#**

{{< highlight "csharp" >}}

 //Instantiating a Workbook object

//Opening the Excel file

Workbook workbook = new Workbook("book1.xls");

//Hiding the tabs of the Excel file

workbook.Settings.ShowTabs = false;

//Saving the modified Excel file

workbook.Save("output.xls");



{{< /highlight >}}
## **Contrôle de la largeur de la barre d'onglets**
**C#**

{{< highlight "csharp" >}}

 //Adjusting the sheet tab bar width

workbook.Worksheets.SheetTabBarWidth = 800;



{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Tabs)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
