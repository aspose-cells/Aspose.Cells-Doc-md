---
title: Thèmes et couleurs Excel
type: docs
weight: 130
url: /fr/java/excel-2007-themes-and-colors/
---
{{% alert color="primary" %}}

Les thèmes offrent une apparence unifiée avec des styles nommés, des effets graphiques et d'autres objets utilisés dans un classeur. Par exemple, le style Accent1 est différent dans les thèmes Office et Apex. Souvent, vous appliquez un thème de document, puis le modifiez selon vos besoins.

**Application de thèmes dans Microsoft Excel**

![tâche : image_autre_texte](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Obtenir et définir les couleurs du thème**

Les API Aspose.Cells fournissent des fonctionnalités permettant de personnaliser les thèmes et les couleurs. Vous trouverez ci-dessous quelques méthodes et propriétés qui implémentent les couleurs de thème.

- La propriété Style.ForegroundThemeColor peut être utilisée pour définir la couleur de premier plan.
- La propriété Style.BackgroundThemeColor peut être utilisée pour définir la couleur d'arrière-plan.
- La propriété Font.ThemeColor peut être utilisée pour définir la couleur de la police.
- La méthode Workbook.getThemeColor peut être utilisée pour obtenir une couleur de thème.
- La méthode Workbook.setThemeColor peut être utilisée pour définir une couleur de thème.

L'exemple suivant montre comment obtenir et définir des couleurs de thème.

L'exemple suivant utilise un fichier de modèle XLSX, obtient les couleurs pour différents types de couleurs de thème, modifie les couleurs et enregistre le fichier Excel Microsoft.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Personnalisation des thèmes**

L'exemple suivant montre comment appliquer des thèmes personnalisés avec les couleurs souhaitées. L'exemple utilise un exemple de fichier de modèle créé manuellement dans Microsoft Excel 2007.

**Le fichier modèle CustomThemeColor.xlsx**

![tâche : image_autre_texte](excel-2007-themes-and-colors_2.png)

L'exemple suivant charge un fichier de modèle XLSX, définit les couleurs pour différents types de couleurs de thème, applique les couleurs personnalisées et enregistre le fichier Excel.

**Le fichier généré avec des couleurs de thème personnalisées**

![tâche : image_autre_texte](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Utiliser les couleurs du thème**

L'exemple suivant applique les couleurs de premier plan et de police d'une cellule en fonction des types de couleurs de thème par défaut (du classeur). Il enregistre également le fichier Excel sur le disque.

La sortie suivante est générée lors de l'exécution du code.

**Les couleurs du thème appliquées à la cellule D3 de la feuille de calcul** 

![tâche : image_autre_texte](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Sujets avancés**
- [Extraire les données du thème à partir d'un fichier Excel](/cells/fr/java/extract-theme-data-from-excel-file/)
