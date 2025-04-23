---
title: Définir des formats conditionnels des fichiers Excel et ODS.
linktitle: Formats conditionnels
type: docs
weight: 60
url: /fr/net/conditional-formatting/
description: Comment appliquer des formats conditionnels aux fichiers Excel et ODS en CSharp.
keywords: appliquer des formats conditionnels 
---

## **Introduction**

La mise en forme conditionnelle est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une cellule ou à une plage de cellules et de faire en sorte que la mise en forme change en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, une cellule peut apparaître en gras uniquement lorsque sa valeur est supérieure à 500. Lorsque la valeur de la cellule satisfait la condition, le format spécifié est appliqué à la cellule. Si la valeur de la cellule ne satisfait pas la condition de format, la mise en forme par défaut de la cellule est utilisée. Dans Microsoft Excel, sélectionnez **Format**, puis **Mise en forme conditionnelle** pour ouvrir la boîte de dialogue Mise en forme conditionnelle.

Aspose.Cells prend en charge l'application de la mise en forme conditionnelle aux cellules à l'exécution. Cet article explique comment procéder. Il explique également comment calculer la couleur utilisée par Excel pour la mise en forme conditionnelle de l'échelle de couleurs.

## **Application de la mise en forme conditionnelle**

Aspose.Cells prend en charge la mise en forme conditionnelle de plusieurs manières :

- Utilisation de la feuille de calcul du concepteur
- Utilisation de la méthode de copie.
- Création de la mise en forme conditionnelle à l'exécution.

### **Utilisation de la feuille de calcul du concepteur**

Les développeurs peuvent créer une feuille de calcul du concepteur contenant une mise en forme conditionnelle dans Microsoft Excel, puis ouvrir cette feuille de calcul avec Aspose.Cells. Aspose.Cells charge et enregistre la feuille de calcul du concepteur en conservant tous les paramètres de mise en forme conditionnelle.

### **Utilisation de la méthode de copie**

Aspose.Cells permet aux développeurs de copier les paramètres de mise en forme conditionnelle d'une cellule à une autre dans la feuille de calcul en appelant la méthode [**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Application de la mise en forme conditionnelle à l'exécution**

Aspose.Cells vous permet d'ajouter et de supprimer la mise en forme conditionnelle à l'exécution. Les exemples de code ci-dessous montrent comment définir la mise en forme conditionnelle :

1. Instancier un classeur.
1. Ajouter une mise en forme conditionnelle vide.
1. Définir la plage à laquelle la mise en forme doit s'appliquer.
1. Définir les conditions de formatage.
1. Enregistrez le fichier.

Après cet exemple, voici un certain nombre d'autres exemples plus petits qui montrent comment appliquer les paramètres de la police, les paramètres des bordures et les motifs.

Microsoft Excel 2007 a ajouté une mise en forme conditionnelle plus avancée que Aspose.Cells prend également en charge. Les exemples ici illustrent comment utiliser la mise en forme simple, les exemples de Microsoft Excel 2007 montrent comment appliquer une mise en forme conditionnelle plus avancée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Définir la police**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Vous ne pouvez changer que le style de police, la couleur du texte, le style de soulignement et le style de barré.

{{% /alert %}}

### **Définir la bordure**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Vous ne pouvez utiliser que des styles de ligne fine pour la bordure de contour. Les lignes diagonales ne sont pas autorisées.

{{% /alert %}}

### **Définir le motif**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Sujets avancés**
- [Ajout de mises en forme conditionnelles à 2 couleurs et à 3 couleurs](/cells/fr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Appliquer une mise en forme conditionnelle avancée](/cells/fr/net/apply-advanced-conditional-formatting/)
- [Appliquer une mise en forme conditionnelle dans les feuilles de calcul](/cells/fr/net/apply-conditional-formatting-in-worksheets/)
- [Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle](/cells/fr/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Générer des images de barres de données pour la mise en forme conditionnelle](/cells/fr/net/generate-conditional-formatting-databars-images/)
- [Obtenir des ensembles d'icônes, des barres de données ou des objets de couleurs utilisés dans la mise en forme conditionnelle](/cells/fr/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
