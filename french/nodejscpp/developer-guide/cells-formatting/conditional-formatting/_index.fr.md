---  
title: Définir les formats conditionnels des fichiers Excel et ODS
linktitle: Formats conditionnels  
type: docs  
weight: 60  
url: /fr/nodejs-cpp/conditional-formatting/  
description: Comment appliquer des formats conditionnels aux fichiers Excel et ODS dans Node.js via C++.  
keywords: appliquer des formats conditionnels Node.js via C++  
---  

## **Introduction**

Le formatage conditionnel est une fonctionnalité avancée qui permet d'appliquer des formats à une cellule ou une plage de cellules, et que ce format change en fonction de la valeur de la cellule ou d'une formule. Par exemple, une cellule n'apparaîtra en gras que lorsque sa valeur est supérieure à 500. Lorsque la condition est remplie, le format spécifié est appliqué à la cellule. Si la valeur ne correspond pas à la condition, le format par défaut de la cellule est utilisé. Dans Microsoft Excel, sélectionnez **Format**, puis **Mise en forme conditionnelle** pour ouvrir la boîte de dialogue Mise en forme conditionnelle.

Aspose.Cells prend en charge l'application de la mise en forme conditionnelle aux cellules à l'exécution. Cet article explique comment procéder. Il explique également comment calculer la couleur utilisée par Excel pour la mise en forme conditionnelle de l'échelle de couleurs.

## **Application de la mise en forme conditionnelle**

Aspose.Cells prend en charge la mise en forme conditionnelle de plusieurs manières :

- Utilisation de la feuille de calcul du concepteur
- Utilisation de la méthode de copie.
- Création de la mise en forme conditionnelle à l'exécution.

### **Utilisation de la feuille de calcul du concepteur**

Les développeurs peuvent créer une feuille de calcul du concepteur contenant une mise en forme conditionnelle dans Microsoft Excel, puis ouvrir cette feuille de calcul avec Aspose.Cells. Aspose.Cells charge et enregistre la feuille de calcul du concepteur en conservant tous les paramètres de mise en forme conditionnelle.

### **Utilisation de la méthode de copie**

Aspose.Cells permet aux développeurs de copier les paramètres de mise en forme conditionnelle d'une cellule à une autre dans la feuille de calcul en appelant la méthode [**Range.copy()**](https://reference.aspose.com/cells/nodejs-cpp/range/#copy-range-).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-CopyConditionalFormattsByCopyRange.js" >}}


## **Application de la mise en forme conditionnelle à l'exécution**

Aspose.Cells vous permet d'ajouter et de supprimer la mise en forme conditionnelle à l'exécution. Les exemples de code ci-dessous montrent comment définir la mise en forme conditionnelle :

1. Instancier un classeur.
1. Ajouter une mise en forme conditionnelle vide.
1. Définir la plage à laquelle la mise en forme doit s'appliquer.
1. Définir les conditions de formatage.
1. Enregistrez le fichier.

Après cet exemple, voici un certain nombre d'autres exemples plus petits qui montrent comment appliquer les paramètres de la police, les paramètres des bordures et les motifs.

Microsoft Excel 2007 a ajouté une mise en forme conditionnelle plus avancée que Aspose.Cells supporte également. Les exemples ici illustrent comment utiliser une mise en forme simple, tandis que les exemples Excel 2007 montrent comment appliquer une mise en forme conditionnelle plus avancée.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyingConditionalFormattingAtRuntime.js" >}}


### **Définir la police**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetFont.js" >}}



{{% alert color="primary" %}}

Vous ne pouvez changer que le style de police, la couleur du texte, le style de soulignement et le style de barré.

{{% /alert %}}

### **Définir la bordure**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetBorder.js" >}}


{{% alert color="primary" %}}

Vous ne pouvez utiliser que des styles de ligne fins pour la bordure extérieure. Les lignes diagonales ne sont pas autorisées.

{{% /alert %}}

### **Définir le motif**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-SetPattern.js" >}}



## **Sujets avancés**  
- [Ajout de mises en forme conditionnelles à 2 couleurs et à 3 couleurs](/cells/fr/nodejs-cpp/adding-2-color-scale-and-3-color-scale-conditional-formattings/)  
- [Appliquer une mise en forme conditionnelle dans les feuilles de calcul](/cells/fr/nodejs-cpp/apply-conditional-formatting-in-worksheets/)  
- [Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle](/cells/fr/nodejs-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)  
- [Générer des images de barres de données pour la mise en forme conditionnelle](/cells/fr/nodejs-cpp/generate-conditional-formatting-databars-images/)  
- [Obtenir des ensembles d'icônes, des barres de données ou des objets de couleurs utilisés dans la mise en forme conditionnelle](/cells/fr/nodejs-cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)  


