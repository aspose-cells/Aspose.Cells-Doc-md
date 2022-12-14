---
title: Spécifiez comment croiser la chaîne dans le HTML de sortie à l'aide de HtmlCrossType
type: docs
weight: 140
url: /fr/net/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
---
## **Scénarios d'utilisation possibles**

Lorsque la cellule contient du texte ou une chaîne mais qu'elle est plus grande que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel en HTML, vous pouvez contrôler ce débordement en précisant le type croisé à l'aide de la[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) énumération. Il a les valeurs suivantes

- **HtmlCrossType.Default**: Affichage comme MS Excel, dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne se croisera ou sera tronquée.

- **HtmlCrossType.MSExport**: Affichez la chaîne comme MS Excel exportant HTML.

- **HtmlCrossType.Cross**: Afficher la chaîne croisée HTML, les performances de création de fichiers HTML volumineux seront plus de dix fois plus rapides qu'en définissant la valeur sur Par défaut ou FitToCell.

- **HtmlCrossType.FitToCell**: affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser la chaîne dans le HTML de sortie à l'aide de HtmlCrossType**

 L'exemple de code suivant charge le[exemple de fichier Excel](51740732.xlsx) et l'enregistre au format HTML en spécifiant différents[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) . Veuillez télécharger le[HTML de sortie](51740734.zip) généré avec ce code. L'exemple de fichier Excel contient l'image bordée de rouge comme indiqué dans cette capture d'écran qui montre l'effet de la[**HtmlCrossType**](https://reference.aspose.com/cells/net/aspose.cells/htmlcrosstype) valeurs sur le HTML de sortie.

![tâche : image_autre_texte](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-SpecifyHtmlCrossTypeInOutputHTML.cs" >}}
