---
title: Convertir du texte en colonnes à l'aide de Aspose.Cells
type: docs
weight: 30
url: /fr/net/convert-text-to-columns-using-aspose-cells/
---
## **Scénarios d'utilisation possibles**

Vous pouvez convertir votre texte en colonnes en utilisant Microsoft Excel. Cette fonctionnalité est disponible à partir de*Outils de données* sous le*Données* languette. Afin de diviser le contenu d'une colonne en plusieurs colonnes, les données doivent contenir un délimiteur spécifique tel qu'une virgule (ou tout autre caractère) sur la base duquel Microsoft Excel divise le contenu d'une cellule en plusieurs cellules. Aspose.Cells fournit également cette fonctionnalité via[**Feuille de calcul.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns)méthode.

## **Convertir du texte en colonnes à l'aide de Aspose.Cells**

 L'exemple de code suivant explique l'utilisation de[**Feuille de calcul.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) méthode. Le code ajoute d'abord le nom de certaines personnes dans la colonne A de la première feuille de calcul. Le prénom et le nom sont séparés par un espace. Ensuite, il s'applique[**Feuille de calcul.Cells.TextToColumns()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/texttocolumns) méthode sur la colonne A et enregistrez-la en tant que fichier Excel de sortie. Si vous ouvrez le[fichier excel de sortie](25395213.xlsx), vous verrez, les prénoms sont dans la colonne A tandis que les noms de famille sont dans la colonne B, comme indiqué dans cette capture d'écran.

![tâche : image_autre_texte](convert-text-to-columns-using-aspose-cells_1.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-ConvertTextToColumns.cs" >}}
