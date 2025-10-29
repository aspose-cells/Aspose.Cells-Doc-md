---
title: Thèmes et couleurs Excel
type: docs
weight: 100
url: /fr/python-net/excel-themes-and-colors/
description: Code C# pour utiliser le schéma de couleurs Excel avec Aspose.Cells pour Python via .NET API
keywords: C# pour créer et appliquer des schémas de couleurs, c# créer de manière programmatique un schéma de couleurs personnalisé, de manière programmatique comment appliquer un schéma de couleurs personnalisé, c# comment utiliser un schéma de couleurs dans Excel
---

## **Comment appliquer et créer un schéma de couleurs dans Excel**
Les thèmes de document facilitent la coordination des couleurs, polices et effets de formatage graphique des documents Excel et permettent de les mettre à jour rapidement. 
Les thèmes fournissent un aspect unifié avec des styles nommés, des effets graphiques et d'autres objets utilisés dans un classeur. Par exemple, le style Accent1, par exemple, a un aspect différent dans les thèmes Office et Apex. Souvent, vous appliquez un thème de document, puis vous le modifiez selon vos souhaits.

### **Comment appliquer un schéma de couleurs dans Excel**
1. Ouvrez Excel et allez à l'onglet "Mise en page" dans le ruban Excel.
1. Cliquez sur le bouton "Couleurs" dans la section "Thèmes".
<br>
<img src="color.png" width=70% />
1. Choisissez une palette de couleurs qui correspond à vos besoins ou survolez un schéma pour voir un aperçu en direct.

### **Comment créer un schéma de couleurs personnalisé dans Excel**
Vous pouvez créer votre propre jeu de couleurs pour donner à votre document un aspect frais et unique ou pour respecter les normes de votre organisation.

1. Ouvrez Excel et allez à l'onglet "Mise en page" dans le ruban Excel.
1. Cliquez sur le bouton "Couleurs" dans la section "Thèmes".
1. Cliquez sur le bouton "Personnaliser les couleurs...".
<br>
<img src="color2.png" width=70% />

1. Dans la boîte de dialogue "Créer de nouveaux thèmes de couleurs", vous pouvez sélectionner des couleurs pour chaque élément en cliquant sur les listes déroulantes de couleurs à côté. Vous pouvez choisir des couleurs dans la palette ou définir des couleurs personnalisées à l'aide de l'option "Plus de couleurs".
<br>
<img src="color3.png" width=70% />
1. Après avoir sélectionné toutes les couleurs souhaitées, donnez un nom à votre schéma de couleurs personnalisé dans le champ "Nom".

1. Cliquez sur le bouton "Enregistrer" pour enregistrer votre schéma de couleurs personnalisé. Votre schéma de couleurs personnalisé sera désormais disponible dans le menu déroulant "Couleurs" pour une utilisation future.

## **Comment créer et appliquer un schéma de couleurs dans Aspose.Cells pour Python via .NET**
Aspose.Cells pour Python via .NET propose des fonctionnalités pour personnaliser les thèmes et les couleurs.

### **Comment créer un thème de couleur personnalisé dans Aspose.Cells pour Python via .NET**
Si des couleurs de thème sont utilisées dans le fichier, nous n'avons pas besoin de modifier chaque cellule individuellement, nous devons simplement modifier les couleurs dans le thème.

L'exemple suivant montre comment appliquer des thèmes personnalisés avec vos couleurs souhaitées. Nous utilisons un fichier modèle d'exemple créé manuellement dans Microsoft Excel 2007.

L'exemple suivant charge un fichier XLSX modèle, définit des couleurs pour différents types de couleurs de thème, applique les couleurs personnalisées et enregistre le fichier Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-CustomizeThemes-1.py" >}}

### **Comment appliquer des couleurs de thèmes dans Aspose.Cells pour Python via .NET**

L'exemple suivant applique les couleurs d'avant-plan et de police d'une cellule en fonction des types de couleurs de thème par défaut (du classeur). Il enregistre également le fichier Excel sur le disque.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UtilizeThemeColors-1.py" >}}

### **Comment obtenir et définir les couleurs de thèmes dans Aspose.Cells pour Python via .NET**
 Voici quelques méthodes et propriétés qui implémentent les couleurs de thème.

- [**Style.foreground_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/foreground_theme_color): Utilisé pour définir la couleur avant-plan.
- [**Style.background_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/style/background_theme_color): Utilisé pour définir la couleur arrière-plan.
- [**Font.theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/font/theme_color): Utilisé pour définir la couleur de la police.
- [**Workbook.get_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_theme_color): Utilisé pour obtenir une couleur de thème.
- [**Workbook.set_theme_color**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/set_theme_color): Utilisé pour définir une couleur de thème.

L'exemple suivant montre comment obtenir et définir les couleurs de thème.

L'exemple suivant utilise un fichier XLSX modèle, obtient les couleurs pour différents types de couleurs de thème, modifie les couleurs et enregistre le fichier Microsoft Excel.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetSetThemeColors-1.py" >}}

## **Sujets avancés**
- [Extraire les données de thème à partir du fichier Excel](/cells/fr/python-net/extract-theme-data-from-excel-file/)

{{< app/cells/assistant language="python-net" >}}
