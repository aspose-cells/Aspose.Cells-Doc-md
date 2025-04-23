---
title: Thèmes et couleurs Excel
type: docs
weight: 130
url: /fr/java/excel-2007-themes-and-colors/
---

{{% alert color="primary" %}}

Les thèmes offrent un aspect unifié avec des styles nommés, des effets graphiques et d'autres objets utilisés dans un classeur. Par exemple, le style Accent1 a un aspect différent dans les thèmes Office et Apex. Souvent, vous appliquez un thème de document, puis l'amendez selon vos besoins.

**Application de thèmes dans Microsoft Excel**

![todo:image_alt_text](excel-2007-themes-and-colors_1.png)

{{% /alert %}}

## **Obtenir et définir les couleurs de thème**

Les API Aspose.Cells offrent des fonctionnalités pour personnaliser les thèmes et les couleurs. Voici quelques méthodes et propriétés qui implémentent les couleurs de thème.

- La propriété Style.ForegroundThemeColor peut être utilisée pour définir la couleur d'avant-plan.
- La propriété Style.BackgroundThemeColor peut être utilisée pour définir la couleur d'arrière-plan.
- La propriété Font.ThemeColor peut être utilisée pour définir la couleur de la police.
- La méthode Workbook.getThemeColor peut être utilisée pour obtenir une couleur de thème.
- La méthode Workbook.setThemeColor peut être utilisée pour définir une couleur de thème.

L'exemple suivant montre comment obtenir et définir les couleurs de thème.

L'exemple suivant utilise un fichier XLSX modèle, obtient les couleurs pour différents types de couleurs de thème, modifie les couleurs et enregistre le fichier Microsoft Excel.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSetThemeColors-GetSetThemeColors.java" >}}

### **Personnalisation des thèmes**

L'exemple suivant montre comment appliquer des thèmes personnalisés avec les couleurs de votre choix. L'exemple utilise un fichier de modèle d'exemple créé manuellement dans Microsoft Excel 2007.

**Le fichier modèle CustomThemeColor.xlsx**

![todo:image_alt_text](excel-2007-themes-and-colors_2.png)

L'exemple suivant charge un fichier XLSX modèle, définit des couleurs pour différents types de couleurs de thème, applique les couleurs personnalisées et enregistre le fichier Excel.

**Le fichier généré avec des couleurs de thème personnalisées**

![todo:image_alt_text](excel-2007-themes-and-colors_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CustomizingThemes-CustomizingThemes.java" >}}

### **Utilisation des couleurs de thème**

L'exemple suivant applique les couleurs d'avant-plan et de police d'une cellule en fonction des types de couleurs de thème par défaut (du classeur). Il enregistre également le fichier Excel sur le disque.

La sortie ci-dessous est générée lors de l'exécution du code.

**Les couleurs de thème appliquées à la cellule D3 de la feuille de calcul** 

![todo:image_alt_text](excel-2007-themes-and-colors_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UseThemeColors-UseThemeColors.java" >}}

## **Sujets avancés**
- [Extraire les données de thème à partir du fichier Excel](/cells/fr/java/extract-theme-data-from-excel-file/)
{{< app/cells/assistant language="java" >}}
