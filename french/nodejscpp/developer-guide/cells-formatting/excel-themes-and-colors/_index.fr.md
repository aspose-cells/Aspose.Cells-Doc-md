---  
title: Thèmes et couleurs Excel
linktitle: Thèmes et couleurs Excel  
type: docs  
weight: 100  
url: /fr/nodejs-cpp/excel-themes-and-colors/  
description: Apprenez à utiliser des schémas de couleurs personnalisés avec Aspose.Cells for Node.js via C++.  
keywords: Node.js Créer et appliquer des schémas de couleurs, Créer de manière programmatique un schéma de couleurs personnalisé avec Node.js, comment appliquer un schéma de couleurs personnalisé avec Node.js, comment utiliser le schéma de couleurs dans Excel avec Node.js  
---  

## **Comment appliquer et créer un schéma de couleurs dans Excel**  
Les thèmes de document facilitent la coordination des couleurs, polices et effets de formatage graphique des documents Excel et permettent de les mettre à jour rapidement.  
Les thèmes offrent une apparence unifiée avec des styles nommés, des effets graphiques et d'autres objets utilisés dans un classeur. Par exemple, le style Accent1 apparaît différemment dans les thèmes Office et Apex. Souvent, vous appliquez un thème de document puis le modifiez selon vos préférences.  

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
Si les couleurs du thème sont utilisées dans le fichier, il n'est pas nécessaire de modifier chaque cellule individuellement ; il suffit de modifier les couleurs dans le thème.  

L'exemple suivant montre comment appliquer des thèmes personnalisés avec vos couleurs souhaitées. Nous utilisons un fichier modèle d'exemple créé manuellement dans Microsoft Excel 2007.  

L'exemple suivant charge un fichier XLSX modèle, définit des couleurs pour différents types de couleurs de thème, applique les couleurs personnalisées et enregistre le fichier Excel.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-CreateCustomColorTheme.js" >}}



### **Comment appliquer les couleurs de thème dans Aspose.Cells**  
L'exemple suivant applique la couleur de premier plan et la couleur de police d'une cellule en fonction des types de couleurs par défaut du thème (du classeur). Il enregistre également le fichier Excel sur le disque.  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-ApplyThemeColors.js" >}}


### **Comment obtenir et définir les couleurs de thème dans Aspose.Cells**  
Voici quelques méthodes et propriétés qui implémentent les couleurs de thème.  

- [**Style.setForegroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundThemeColor-themecolor-) : Utilisé pour définir la couleur de premier plan.  
- [**Style.setBackgroundThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundThemeColor-themecolor-) : Utilisé pour définir la couleur d'arrière-plan.  
- [**Font.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/font/#setThemeColor-themecolor-) : Utilisé pour définir la couleur de la police.  
- [**Workbook.getThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getThemeColor-themecolortype-) : Utilisé pour obtenir une couleur de thème.  
- [**Workbook.setThemeColor**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#setThemeColor-themecolortype-color-) : Utilisé pour définir une couleur de thème.  

L'exemple suivant montre comment obtenir et définir les couleurs de thème.  

L'exemple suivant utilise un fichier XLSX modèle, obtient les couleurs pour différents types de couleurs de thème, change les couleurs et enregistre le fichier Microsoft Excel.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ThemesAndColors-GetAndSetThemeColors.js" >}}


## **Sujets avancés**  
- [Extraire les données de thème à partir du fichier Excel](/cells/fr/nodejs-cpp/extract-theme-data-from-excel-file/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
