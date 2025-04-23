---
title: Définir la couleur d onglet de feuille de calcul dans Aspose.Cells
type: docs
weight: 90
url: /fr/java/set-worksheet-tab-color-in-aspose-cells/
---

## **Aspose.Cells - Définir la couleur d'onglet de feuille de calcul**
Aspose.Cells vous permet de changer la couleur des onglets de feuille de calcul individuels pour les rendre plus visibles par rapport au reste. Par exemple, vous pouvez mettre Dépenses en rouge, Ventes en vert, Actifs en bleu, etc.
#### **Définition de la couleur de l'onglet de feuille de calcul avec Microsoft Excel**
1. Cliquez avec le bouton droit sur un onglet dans la feuille d'onglets en bas de la feuille de calcul actuelle.
1. Sélectionnez **Couleur de l'onglet**.
1. Sélectionnez une couleur dans la palette.
1. Cliquez sur **OK**.

**Java**

{{< highlight java >}}

 //Instantiate a new Workbook

Workbook workbook = new Workbook(dataPath + "workbook.xls");

//Get the first worksheet in the book

Worksheet worksheet = workbook.getWorksheets().get(0);

//Set the tab color

worksheet.setTabColor(Color.getRed());

//Save the Excel file

workbook.save(dataPath + "AsposeColoredTab_Out.xls");

{{< /highlight >}}
## **Télécharger le code en cours d'exécution**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Télécharger le code source d'exemple**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SetWorksheetTabColor.java)

{{% alert color="primary" %}} 

Pour plus de détails, visitez [Définir la couleur de l'onglet de feuille de calcul](/java/set-worksheet-tab-color).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
