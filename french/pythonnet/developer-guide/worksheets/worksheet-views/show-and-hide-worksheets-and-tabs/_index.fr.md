---
title: Afficher et masquer des feuilles de calcul et des onglets
type: docs
weight: 10
url: /fr/python-net/show-and-hide-worksheets-and-tabs/
description: Cet article fournit un code d exemple pour utiliser l API Aspose.Cells pour Python via .NET afin d afficher et de masquer de manière programmatique un classeur Excel. De plus, comment montrer et masquer les onglets de classeur Excel.
keywords: Bibliothèque Excel Python, Python montrer et masquer une feuille de calcul, Python montrer et masquer les onglets, Python contrôler la largeur de la barre d onglets.
---

{{% alert color="primary" %}}

Aspose.Cells pour Python via .NET permet à l'utilisateur de montrer et de masquer les éléments d'un classeur, y compris les feuilles de calcul et les onglets.

{{% /alert %}}

## **Afficher et masquer une feuille de calcul**

Un fichier Excel peut contenir une ou plusieurs feuilles de calcul. Chaque fois que nous créons un fichier Excel, nous ajoutons des feuilles de calcul dans lesquelles nous travaillons. Chaque feuille de calcul dans un fichier Excel est indépendante des autres en ayant ses propres données, paramètres de mise en forme, etc. Parfois, les développeurs peuvent souhaiter rendre certaines feuilles cachées et d'autres visibles dans le fichier Excel pour leur propre intérêt. Ainsi, **Aspose.Cells for Python via .NET** permet aux développeurs de contrôler la visibilité des feuilles dans leurs fichiers Excel.

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d’accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour contrôler la visibilité d'une feuille de calcul, utilisez la propriété [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) est une propriété booléenne, ce qui signifie qu'elle ne peut stocker qu'une valeur **vrai** ou **faux**.

### **Rendre une feuille de calcul visible**

Rendez une feuille de calcul visible en définissant la propriété [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **vrai**

### **Masquer une feuille de calcul**

Masquer une feuille de calcul en définissant la propriété [**is_visible**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/is_visible) de la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) sur **faux**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideUnhideWorksheet-1.py" >}}

## **Afficher et masquer les onglets**

Si vous regardez de près le bas d'un fichier Microsoft Excel, vous verrez un certain nombre de contrôles. Ceux-ci incluent:

- Onglets de feuille.
- Boutons de défilement d'onglets.

Les onglets de feuille représentent les feuilles de calcul dans le fichier Excel. Cliquez sur un onglet pour basculer vers cette feuille de calcul. Plus il y a de feuilles de calcul dans le classeur, plus il y a d'onglets de feuille. Si le fichier Excel comporte un bon nombre de feuilles de calcul, vous avez besoin de boutons pour naviguer à travers elles. Donc, Microsoft Excel fournit des boutons de défilement d'onglets pour faire défiler les onglets de feuille.

En utilisant Aspose.Cells pour Python via .NET, les développeurs peuvent contrôler la visibilité des onglets de feuilles et des boutons de défilement des onglets dans les fichiers Excel.

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) offre une large gamme de propriétés et de méthodes pour gérer un fichier Excel. Pour contrôler la visibilité des onglets dans un fichier Excel, les développeurs peuvent utiliser la propriété [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) est une propriété booléenne, ce qui signifie qu’elle ne peut stocker qu’une valeur **true** ou **false**.

### **Rendre les onglets visibles**

Rendez les onglets visibles avec la propriété [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) à **true**.

### **Masquage des onglets**

Masquez les onglets dans un fichier Excel en définissant la propriété [**WorkbookSettings.show_tabs**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/show_tabs) de la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) à false.

Voici un exemple complet qui ouvre un fichier Excel (book1.xls), masque ses onglets et enregistre le fichier modifié sous le nom de output.xls. Après l'exécution du code, vous verrez que les onglets du classeur sont masqués.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-HideTabs-1.py" >}}

### **Contrôler la largeur de la barre d'onglets**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Display-ControlTabBarWidth-1.py" >}}
