---
title: Afficher et masquer des feuilles de calcul et des onglets
type: docs
weight: 10
url: /fr/net/show-and-hide-worksheets-and-tabs/
description: Cet article fournit un code d exemple pour utiliser l API C# ou la bibliothèque .NET pour afficher et masquer de manière programmatique une feuille de calcul Excel. De plus, comment afficher et masquer les onglets du classeur Excel.
---

{{% alert color="primary" %}}

Aspose.Cells permet à l'utilisateur d'afficher et de masquer des éléments d'un classeur, y compris des feuilles de calcul et des onglets.

{{% /alert %}}

## **Afficher et masquer une feuille de calcul**

Un fichier Excel peut avoir une ou plusieurs feuilles de calcul. Lorsque nous créons un fichier Excel, nous ajoutons des feuilles de calcul au fichier Excel dans lequel nous travaillons. Chaque feuille de calcul dans un fichier Excel est indépendante de l'autre feuille de calcul en ayant ses propres données et paramètres de formatage, etc. Parfois, les développeurs peuvent avoir besoin de masquer quelques feuilles de calcul et d'autres visibles dans le fichier Excel pour leur propre intérêt. Donc, **Aspose.Cells** permet aux développeurs de contrôler la visibilité des feuilles de calcul dans leurs fichiers Excel.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour contrôler la visibilité d'une feuille de calcul, utilisez la propriété [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **vrai** ou **faux**.

### **Rendre une feuille de calcul visible**

Rendez une feuille de calcul visible en définissant la propriété [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sur **vrai**

### **Masquer une feuille de calcul**

Masquer une feuille de calcul en définissant la propriété [**IsVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isvisible) de la classe [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) sur **faux**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideUnhideWorksheet-1.cs" >}}

## **Afficher et masquer les onglets**

Si vous regardez de près le bas d'un fichier Microsoft Excel, vous verrez un certain nombre de contrôles. Ceux-ci incluent:

- Onglets de feuille.
- Boutons de défilement d'onglets.

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur un onglet pour basculer vers cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel comporte un bon nombre de feuilles de calcul, vous avez besoin de boutons pour naviguer à travers elles. Donc, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de feuille.

En utilisant Aspose.Cells, les développeurs peuvent contrôler la visibilité des onglets de feuille et des boutons de défilement dans les fichiers Excel.

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) offre un large éventail de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des onglets dans un fichier Excel, les développeurs peuvent utiliser la propriété [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook). [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **true** ou **false**.

### **Rendre les onglets visibles**

Rendez les onglets visibles avec la propriété [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) à **true**.

### **Masquage des onglets**

Masquez les onglets dans un fichier Excel en définissant la propriété [**WorkbookSettings.ShowTabs**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/showtabs) de la classe [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) à false.

Voici un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous le nom de output.xls. Après l'exécution du code, vous verrez que les onglets du classeur sont masqués.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-HideTabs-1.cs" >}}

### **Contrôler la largeur de la barre d'onglets**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Display-ControlTabBarWidth-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
