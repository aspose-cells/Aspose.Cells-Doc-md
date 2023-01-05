---
title: Définir la couleur de l'onglet de la feuille de calcul dans xlsx4j
type: docs
weight: 60
url: /fr/java/set-worksheet-tab-color-in-xlsx4j/
---
## **Aspose.Cells - Définir la couleur de l'onglet de la feuille de calcul**
Aspose.Cells vous permet de changer la couleur des onglets de feuille de calcul individuels pour les faire ressortir du reste. Par exemple, vous pouvez rendre les dépenses rouges, les ventes vertes, les actifs bleus, etc.
### **Définition de la couleur de l'onglet de la feuille de calcul avec Microsoft Excel**
1. Cliquez avec le bouton droit sur un onglet dans la feuille à onglets au bas de la feuille de calcul actuelle.
1. Sélectionner**Couleur de l'onglet**.
1. Sélectionnez une couleur dans la palette.
1. Cliquez sur**D'ACCORD**.

**Java**

{{< highlight "java" >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataDir + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataDir + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Télécharger le code d'exécution**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Télécharger l'exemple de code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/settabcolor/AsposeSetWorksheetTabColor.java)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Définir la couleur de l'onglet de la feuille de calcul](/java/set-worksheet-tab-color).

{{% /alert %}}
