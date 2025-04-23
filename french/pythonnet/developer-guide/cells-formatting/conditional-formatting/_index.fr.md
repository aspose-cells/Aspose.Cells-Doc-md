---
title: Définir des formats conditionnels des fichiers Excel et ODS.
linktitle: Formats conditionnels
type: docs
weight: 60
url: /fr/python-net/conditional-formatting/
description: Comment appliquer des formats conditionnels aux fichiers Excel et ODS en Python.
keywords: appliquer des formats conditionnels 
---

## **Introduction**

La mise en forme conditionnelle est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une cellule ou à une plage de cellules et de faire en sorte que la mise en forme change en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, une cellule peut apparaître en gras uniquement lorsque sa valeur est supérieure à 500. Lorsque la valeur de la cellule satisfait la condition, le format spécifié est appliqué à la cellule. Si la valeur de la cellule ne satisfait pas la condition de format, la mise en forme par défaut de la cellule est utilisée. Dans Microsoft Excel, sélectionnez **Format**, puis **Mise en forme conditionnelle** pour ouvrir la boîte de dialogue Mise en forme conditionnelle.

Aspose.Cells pour Python via .NET supporte l'application de formats conditionnels aux cellules en temps réel. Cet article explique comment. Il explique également comment calculer la couleur utilisée par Excel pour le formatage conditionnel à échelle de couleurs.

## **Application de la mise en forme conditionnelle**

Aspose.Cells pour Python via .NET supporte le formatage conditionnel de plusieurs façons :

- Utilisation de la feuille de calcul du concepteur
- Utilisation de la méthode de copie.
- Création de la mise en forme conditionnelle à l'exécution.

### **Utilisation de la feuille de calcul du concepteur**

Les développeurs peuvent créer une feuille de calcul de conception contenant un formatage conditionnel dans Microsoft Excel, puis ouvrir cette feuille avec Aspose.Cells pour Python via .NET. Aspose.Cells pour Python via .NET charge et enregistre la feuille de concepteur, en conservant tout paramètre de formatage conditionnel.

### **Utilisation de la méthode de copie**

Aspose.Cells pour Python via .NET permet aux développeurs de copier les paramètres de formatage conditionnel d'une cellule à une autre dans la feuille de calcul en appelant la méthode [**Range.copy()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/copy).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCopyMethod-1.py" >}}

## **Application de la mise en forme conditionnelle à l'exécution**

Aspose.Cells pour Python via .NET vous permet à la fois d'ajouter et de supprimer le formatage conditionnel en temps réel. Les exemples de code ci-dessous montrent comment définir le formatage conditionnel :

1. Instancier un classeur.
1. Ajouter une mise en forme conditionnelle vide.
1. Définir la plage à laquelle la mise en forme doit s'appliquer.
1. Définir les conditions de formatage.
1. Enregistrez le fichier.

Après cet exemple, voici un certain nombre d'autres exemples plus petits qui montrent comment appliquer les paramètres de la police, les paramètres des bordures et les motifs.

Microsoft Excel 2007 a ajouté un formatage conditionnel plus avancé que Aspose.Cells pour Python via .NET prend également en charge. Les exemples ici illustrent comment utiliser un formatage simple, les exemples de Microsoft Excel 2007 montrent comment appliquer un formatage conditionnel plus avancé.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ConditionalFormattingatRuntime-1.py" >}}

### **Définir la police**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SettingFontStyle-1.py" >}}

{{% alert color="primary" %}}

Vous ne pouvez changer que le style de police, la couleur du texte, le style de soulignement et le style de barré.

{{% /alert %}}

### **Définir la bordure**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetBorder-1.py" >}}

{{% alert color="primary" %}}

Vous ne pouvez utiliser que des styles de ligne fine pour la bordure de contour. Les lignes diagonales ne sont pas autorisées.

{{% /alert %}}

### **Définir le motif**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-SetPattern-1.py" >}}

## **Sujets avancés**
- [Ajout de mises en forme conditionnelles à 2 couleurs et à 3 couleurs](/cells/fr/python-net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [Appliquer une mise en forme conditionnelle dans les feuilles de calcul](/cells/fr/python-net/apply-conditional-formatting-in-worksheets/)
- [Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle](/cells/fr/python-net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/)
- [Générer des images de barres de données pour la mise en forme conditionnelle](/cells/fr/python-net/generate-conditional-formatting-databars-images/)
- [Obtenir des ensembles d'icônes, des barres de données ou des objets de couleurs utilisés dans la mise en forme conditionnelle](/cells/fr/python-net/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/)

{{< app/cells/assistant language="csharp" >}}
