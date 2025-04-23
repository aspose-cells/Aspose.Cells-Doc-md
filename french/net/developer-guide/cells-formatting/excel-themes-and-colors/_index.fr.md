---
title: Thèmes et couleurs Excel
type: docs
weight: 100
url: /fr/net/excel-themes-and-colors/
description: Code C# pour utiliser le schéma de couleurs Excel avec l API Aspose.Cells for .NET
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

## **Comment créer et appliquer un schéma de couleurs dans Aspose.Cells**
Aspose.Cells offre des fonctionnalités pour personnaliser les thèmes et les couleurs.

### **Comment créer un thème de couleurs personnalisé dans Aspose.Cells**
Si des couleurs de thème sont utilisées dans le fichier, nous n'avons pas besoin de modifier chaque cellule individuellement, nous devons simplement modifier les couleurs dans le thème.

L'exemple suivant montre comment appliquer des thèmes personnalisés avec vos couleurs souhaitées. Nous utilisons un fichier modèle d'exemple créé manuellement dans Microsoft Excel 2007.

L'exemple suivant charge un fichier XLSX modèle, définit des couleurs pour différents types de couleurs de thème, applique les couleurs personnalisées et enregistre le fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

### **Comment appliquer les couleurs de thème dans Aspose.Cells**

L'exemple suivant applique les couleurs d'avant-plan et de police d'une cellule en fonction des types de couleurs de thème par défaut (du classeur). Il enregistre également le fichier Excel sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

### **Comment obtenir et définir les couleurs de thème dans Aspose.Cells**
 Voici quelques méthodes et propriétés qui implémentent les couleurs de thème.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Utilisé pour définir la couleur avant-plan.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Utilisé pour définir la couleur arrière-plan.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Utilisé pour définir la couleur de la police.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Utilisé pour obtenir une couleur de thème.
- [**Workbook.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Utilisé pour définir une couleur de thème.

L'exemple suivant montre comment obtenir et définir les couleurs de thème.

L'exemple suivant utilise un fichier XLSX modèle, obtient les couleurs pour différents types de couleurs de thème, modifie les couleurs et enregistre le fichier Microsoft Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

## **Sujets avancés**
- [Extraire les données de thème à partir du fichier Excel](/cells/fr/net/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="csharp" >}}
