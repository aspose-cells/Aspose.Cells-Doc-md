---
title: Thèmes et couleurs Excel
type: docs
weight: 100
url: /fr/net/excel-themes-and-colors/
description: Code C# pour utiliser le schéma de couleurs Excel avec Aspose.Cells for .NET API
keywords: C# to Create and Apply Color Schemes, c# programmatically Create a Custom Color Scheme, programmatically how to Apply a Custom Color Scheme, c# how to Use Color Scheme in excel
---
##  **Comment appliquer et créer un jeu de couleurs dans Excel**
Les thèmes de document facilitent la coordination des couleurs, des polices et des effets de formatage graphique des documents Excel et les mettent à jour rapidement.
Les thèmes offrent une apparence unifiée avec des styles nommés, des effets graphiques et d'autres objets utilisés dans un classeur. Par exemple, le style Accent1, par exemple, est différent dans les thèmes Office et Apex. Souvent, vous appliquez un thème de document, puis vous le modifiez comme vous le souhaitez.

###  **Comment appliquer un jeu de couleurs dans Excel**
1. Ouvrez Excel et accédez à l'onglet "Mise en page" dans le ruban Excel.
1. Cliquez sur le bouton « Couleurs » dans la section « Thèmes ».
<br>
<img src="color.png" width=70% />
1. Choisissez une palette de couleurs qui correspond à vos besoins ou survolez un schéma pour voir un aperçu en direct.

###  **Comment créer un jeu de couleurs personnalisé dans Excel**
Vous pouvez créer votre propre jeu de couleurs pour donner à votre document un aspect nouveau et unique ou vous conformer aux normes de la marque de votre organisation.

1. Ouvrez Excel et accédez à l'onglet "Mise en page" dans le ruban Excel.
1. Cliquez sur le bouton « Couleurs » dans la section « Thèmes ».
1. Cliquez sur le bouton "Personnaliser les couleurs...".
<br>
<img src="color2.png" width=70% />

1. Dans la boîte de dialogue "Créer de nouvelles couleurs de thème", vous pouvez sélectionner des couleurs pour chaque élément en cliquant sur les listes déroulantes de couleurs à côté d'eux. Vous pouvez choisir des couleurs dans la palette ou définir des couleurs personnalisées à l'aide de l'option « Plus de couleurs ».
<br>
<img src="color3.png" width=70% />
1. Après avoir sélectionné toutes les couleurs souhaitées, indiquez un nom pour votre palette de couleurs personnalisée dans le champ "Nom".

1. Cliquez sur le bouton "Enregistrer" pour enregistrer votre palette de couleurs personnalisée. Votre palette de couleurs personnalisée sera désormais disponible dans le menu déroulant « Couleurs » pour une utilisation future.

##  **Comment créer et appliquer une palette de couleurs dans Aspose.Cells**
Aspose.Cells fournit des fonctionnalités permettant de personnaliser les thèmes et les couleurs.

###  **Comment créer un thème de couleur personnalisé dans Aspose.Cells**
Si des couleurs de thème sont utilisées dans le fichier, nous n'avons pas besoin de modifier chaque cellule individuellement, il suffit de modifier les couleurs du thème.

L'exemple suivant montre comment appliquer des thèmes personnalisés avec les couleurs souhaitées. Nous utilisons un exemple de fichier modèle créé manuellement dans Microsoft Excel 2007.

L'exemple suivant charge un fichier modèle XLSX, définit les couleurs pour différents types de couleurs de thème, applique les couleurs personnalisées et enregistre le fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-CustomizeThemes-1.cs" >}}

###  **Comment appliquer les couleurs du thème dans Aspose.Cells**

L’exemple suivant applique les couleurs de premier plan et de police d’une cellule en fonction des types de couleurs du thème par défaut (du classeur). Il enregistre également le fichier Excel sur le disque.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-UtilizeThemeColors-1.cs" >}}

###  **Comment obtenir et définir les couleurs du thème dans Aspose.Cells**
 Vous trouverez ci-dessous quelques méthodes et propriétés qui implémentent les couleurs du thème.

- [**Style.ForegroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/foregroundthemecolor): Utilisé pour définir la couleur de premier plan.
- [**Style.BackgroundThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/backgroundthemecolor): Utilisé pour définir la couleur d’arrière-plan.
- [**Font.ThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/font/properties/themecolor): Utilisé pour définir la couleur de la police.
- [**Workbook.GetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getthemecolor): Utilisé pour obtenir une couleur de thème.
- [**Classeur.SetThemeColor**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/setthemecolor): Utilisé pour définir une couleur de thème.

L'exemple suivant montre comment obtenir et définir les couleurs du thème.

L'exemple suivant utilise un fichier modèle XLSX, obtient les couleurs pour différents types de couleurs de thème, modifie les couleurs et enregistre le fichier Excel Microsoft.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-Excel2007Themes-GetSetThemeColors-1.cs" >}}

##  **Sujets avancés**
- [Extraire les données du thème à partir d'un fichier Excel](/cells/fr/net/extract-theme-data-from-excel-file/)
