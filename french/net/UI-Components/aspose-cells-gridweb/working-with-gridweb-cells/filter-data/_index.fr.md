---
title: Filtrer les données
type: docs
weight: 80
url: /fr/net/filter-data/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb fournit des fonctionnalités de filtre automatique et de filtre de données personnalisé. Ces fonctionnalités vous permettent de sélectionner uniquement les éléments d'une feuille de calcul que vous souhaitez afficher dans une liste. De plus, vous pouvez filtrer les éléments d'une liste en fonction de critères définis. Filtrez du texte, des nombres ou des dates avec les fonctions de filtrage.

{{% /alert %}} 
## **Travailler avec des filtres**
Utilisez la méthode de feuille de calcul AddAutoFilter pour activer le filtre automatique pour une feuille de calcul. Cette méthode accepte les index de ligne, de début et de fin de colonne.

Pour activer le filtre personnalisé, utilisez la méthode AddCustomFilter de la feuille de calcul qui accepte l'index de ligne auquel le filtre doit être appliqué et les critères de filtrage personnalisés.

L'exemple ci-dessous implémente à la fois des filtres de données automatiques et personnalisés. Dans l'exemple, la fonctionnalité de filtrage automatique est activée et les lignes filtrées sont recherchées en fonction de certains critères.

**Entrée : la liste de données dans la première feuille de calcul** 

![tâche : image_autre_texte](filter-data_1.jpg)

**Sortie : activer la fonction de filtrage automatique** 

![tâche : image_autre_texte](filter-data_2.jpg)
### **Filtre automatique**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetAutoFilter.aspx-SetAutoFilter.cs" >}}
### **Filtre de données personnalisé**
**Données filtrées personnalisées en fonction des critères** 

![tâche : image_autre_texte](filter-data_3.jpg)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-SetCustomFilter.aspx-SetCustomFilter.cs" >}}
