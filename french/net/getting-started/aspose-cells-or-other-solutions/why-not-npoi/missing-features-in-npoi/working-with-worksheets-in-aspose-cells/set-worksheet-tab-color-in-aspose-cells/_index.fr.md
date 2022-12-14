---
title: Définir la couleur de l'onglet de la feuille de calcul dans Aspose.Cells
type: docs
weight: 20
url: /fr/net/set-worksheet-tab-color-in-aspose-cells/
---
## **Aspose.Cells - Définir la couleur de l'onglet de la feuille de calcul**
Aspose.Cells vous permet de changer la couleur des onglets de feuille de calcul individuels pour les faire ressortir du reste. Par exemple, vous pouvez rendre les dépenses rouges, les ventes vertes, les actifs bleus, etc.
### **Définition de la couleur de l'onglet de la feuille de calcul avec Microsoft Excel**
1. Cliquez avec le bouton droit sur un onglet dans la feuille à onglets au bas de la feuille de calcul actuelle.
1. Sélectionner**Couleur de l'onglet**.
1. Sélectionnez une couleur dans la palette.
1. Cliquez sur**D'ACCORD**.

**C#**

{{< highlight "cs" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the first worksheet in the book

Worksheet worksheet = workbook.Worksheets[0];

//Set the tab color

worksheet.TabColor = Color.Red;

//Save the Excel file

workbook.Save("AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Télécharger le code d'exécution**
 Télécharger**Définir la couleur de l'onglet de la feuille de calcul** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Worksheet.Tab.Color.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Définir la couleur de l'onglet de la feuille de calcul](/cells/fr/net/set-worksheet-tab-color/).

{{% /alert %}}
