---
title: Filtrer les données
type: docs
weight: 80
url: /fr/net/aspose-cells-gridweb/filter-data/
keywords: GridWeb,filtre,filtrer des données,filtrage de données
description: Cet article présente comment filtrer les données dans GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb fournit des fonctionnalités de filtre automatique et de filtre de données personnalisé. Ces fonctionnalités vous permettent de sélectionner uniquement les éléments d'une feuille de calcul que vous souhaitez afficher dans une liste. De plus, vous pouvez filtrer les éléments d'une liste selon des critères définis. Filtrez du texte, des chiffres ou des dates avec les fonctionnalités de filtrage.

{{% /alert %}} 
## **Travailler avec les filtres**
Utilisez la méthode AddAutoFilter de la feuille de calcul pour activer le filtre automatique pour une feuille de calcul. Cette méthode accepte les index de la ligne, du début et de la fin de la colonne.

Pour activer un filtre personnalisé, utilisez la méthode AddCustomFilter de la feuille de calcul qui accepte l'index de la ligne à laquelle le filtre doit être appliqué et les critères de filtrage personnalisés.

L'exemple ci-dessous met en œuvre à la fois les filtres de données automatiques et personnalisés. Dans l'exemple, la fonction de filtre automatique est activée et les lignes filtrées sont recherchées en fonction de certains critères.

**Entrée : la liste de données dans la première feuille de calcul** 

![todo:image_alt_text](filter-data_1.jpg)

**Sortie : activer la fonction de filtre automatique** 

![todo:image_alt_text](filter-data_2.jpg)
### **Filtre automatique**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Filtre de données personnalisé**
**Données filtrées personnalisées en fonction des critères** 

![todo:image_alt_text](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
