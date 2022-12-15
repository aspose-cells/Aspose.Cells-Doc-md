---
title: Afficher et masquer les feuilles de calcul et les onglets
type: docs
weight: 10
url: /fr/net/show-and-hide-worksheets-and-tabs/
---
{{% alert color="primary" %}}

Aspose.Cells permet à l'utilisateur d'afficher et de masquer des éléments d'un classeur, y compris des feuilles de calcul et des onglets.

{{% /alert %}}

## **Afficher et masquer une feuille de calcul**

 Un fichier Excel peut contenir une ou plusieurs feuilles de calcul. Chaque fois que nous créons un fichier Excel, nous ajoutons des feuilles de calcul au fichier Excel dans lequel nous travaillons. Chaque feuille de calcul dans un fichier Excel est indépendante de l'autre feuille de calcul en ayant ses propres paramètres de données et de formatage, etc. Parfois, les développeurs peuvent avoir besoin de masquer quelques feuilles de calcul et d'autres visibles dans le fichier Excel pour leur propre intérêt. Alors,**Aspose.Cells** permet aux développeurs de contrôler la visibilité des feuilles de calcul dans leurs fichiers Excel.

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

 Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour contrôler la visibilité d'une feuille de calcul, utilisez la[**Est visible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) propriété de la[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer.[**Est visible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'un**vrai** ou**faux** évaluer.

### **Rendre une feuille de calcul visible**

 Rendre une feuille de calcul visible en définissant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer'[**Est visible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) propriété à**vrai**

### **Masquer une feuille de calcul**

 Masquer une feuille de calcul en définissant le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classer'[**Est visible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) propriété à**faux**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Afficher et masquer les onglets**

Si vous regardez attentivement le bas d'un fichier Excel Microsoft, vous verrez un certain nombre de contrôles. Ceux-ci inclus:

- Onglets de feuille.
- Boutons de défilement des onglets.

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur n'importe quel onglet pour passer à cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel contient un bon nombre de feuilles de calcul, vous avez besoin de boutons pour les parcourir. Ainsi, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de la feuille.

À l'aide de Aspose.Cells, les développeurs peuvent contrôler la visibilité des onglets de feuille et des boutons de défilement des onglets dans les fichiers Excel.

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel. La[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) fournit un large éventail de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des onglets dans un fichier Excel, les développeurs peuvent utiliser le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classer'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) propriété.[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'un**vrai** ou**faux** évaluer.

### **Rendre les onglets visibles**

 Rendre les onglets visibles avec le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classer'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) propriété à**vrai**.

### **Masquer les onglets**

 Masquer les onglets dans un fichier Excel en définissant le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classer'[**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs)propriété à false.

Vous trouverez ci-dessous un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous output.xls. Après l'exécution du code, vous verrez que les onglets du classeur sont masqués.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Contrôle de la largeur de la barre d'onglets**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
