---
title: Définissez les formats conditionnels des fichiers Excel et ODS.
linktitle: Formats conditionnels
type: docs
weight: 60
url: /fr/net/conditional-formatting/
description: Comment appliquer des formats conditionnels aux fichiers Excel et ODS dans CSharp.
keywords: apply conditional formats 
---
## **Introduction**

 La mise en forme conditionnelle est une fonctionnalité Excel avancée Microsoft qui vous permet d'appliquer des formats à une cellule ou à une plage de cellules et de modifier cette mise en forme en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, vous pouvez faire apparaître une cellule en gras uniquement lorsque la valeur de la cellule est supérieure à 500. Lorsque la valeur de la cellule répond à la condition, le format spécifié est appliqué à la cellule. Si la valeur de la cellule ne répond pas à la condition de format, la mise en forme par défaut de la cellule est utilisée. Dans Microsoft Excel, sélectionnez**Format** , alors**Mise en forme conditionnelle** pour ouvrir la boîte de dialogue Formatage conditionnel.

Aspose.Cells prend en charge l'application de la mise en forme conditionnelle aux cellules lors de l'exécution. Cet article explique comment. Il explique également comment calculer la couleur utilisée par Excel pour la mise en forme conditionnelle de l'échelle de couleurs.

## **Appliquer une mise en forme conditionnelle**

Aspose.Cells prend en charge la mise en forme conditionnelle de plusieurs manières :

- Utilisation d'une feuille de calcul de concepteur
- Utilisation de la méthode de copie.
- Création d'une mise en forme conditionnelle à l'exécution.

### **Utilisation de la feuille de calcul Designer**

Les développeurs peuvent créer une feuille de calcul de concepteur contenant une mise en forme conditionnelle dans Microsoft Excel, puis ouvrir cette feuille de calcul avec Aspose.Cells. Aspose.Cells charge et enregistre la feuille de calcul de concepteur, en conservant tout paramètre de mise en forme conditionnelle.

### **Utilisation de la méthode de copie**

 Aspose.Cells permet aux développeurs de copier les paramètres de format conditionnel d'une cellule à une autre dans la feuille de calcul en appelant le[**Range.Copy()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/copy/index) méthode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-UsingCopyMethod-1.cs" >}}

## **Application de la mise en forme conditionnelle à l'exécution**

Aspose.Cells vous permet à la fois d'ajouter et de supprimer une mise en forme conditionnelle lors de l'exécution. Les exemples de code ci-dessous montrent comment définir la mise en forme conditionnelle :

1. Instancier un classeur.
1. Ajoutez un format conditionnel vide.
1. Définissez la plage à laquelle la mise en forme doit s'appliquer.
1. Définissez les conditions de formatage.
1. Enregistrez le fichier.

Après cet exemple, un certain nombre d'autres exemples plus petits montrent comment appliquer les paramètres de police, les paramètres de bordure et les motifs.

Microsoft Excel 2007 a ajouté une mise en forme conditionnelle plus avancée que Aspose.Cells prend également en charge. Les exemples ici illustrent comment utiliser une mise en forme simple, les exemples Microsoft Excel 2007 montrent comment appliquer une mise en forme conditionnelle plus avancée.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ConditionalFormattingatRuntime-1.cs" >}}

### **Définir la police**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-DealingWithFontSettings-SettingFontStyle-1.cs" >}}

{{% alert color="primary" %}}

Vous ne pouvez modifier que le style de police, la couleur du texte, le style de soulignement et le style barré.

{{% /alert %}}

### **Définir la bordure**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetBorder-1.cs" >}}

{{% alert color="primary" %}}

Vous ne pouvez utiliser que des styles de lignes fines pour la bordure du contour. Les lignes diagonales ne sont pas autorisées.

{{% /alert %}}

### **Définir le motif**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SetPattern-1.cs" >}}

## **Sujets avancés**
- [Ajout de mises en forme conditionnelles d'échelle de 2 couleurs et d'échelle de 3 couleurs](/cells/fr/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Appliquer une mise en forme conditionnelle avancée](/cells/fr/net/apply-advanced-conditional-formatting/)
- [Appliquer la mise en forme conditionnelle dans les feuilles de calcul](/cells/fr/net/apply-conditional-formatting-in-worksheets/)
- [Appliquer un ombrage à d'autres lignes et colonnes avec une mise en forme conditionnelle](/cells/fr/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Générer des images de barres de données de mise en forme conditionnelle](/cells/fr/net/generate-conditional-formatting-databars-images/)
- [Obtenir des jeux d'icônes, des barres de données ou des échelles de couleurs Objets utilisés dans le formatage conditionnel](/cells/fr/net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

