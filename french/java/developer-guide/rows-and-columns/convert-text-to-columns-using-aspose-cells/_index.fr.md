---
title: Convertir du texte en colonnes à l'aide de Aspose.Cells
type: docs
weight: 70
url: /fr/java/convert-text-to-columns-using-aspose-cells/
---
## **Scénarios d'utilisation possibles**
Vous pouvez convertir votre texte en colonnes en utilisant Microsoft Excel. Cette fonctionnalité est disponible à partir de*Outils de données* sous le*Données* languette. Afin de diviser le contenu d'une colonne en plusieurs colonnes, les données doivent contenir un délimiteur spécifique tel qu'une virgule (ou tout autre caractère) sur la base duquel Microsoft Excel divise le contenu d'une cellule en plusieurs cellules. Aspose.Cells fournit également cette fonctionnalité via[TexteVersColonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) méthode.
## **Convertir du texte en colonnes à l'aide de Aspose.Cells**
L'exemple de code suivant explique l'utilisation de[TexteVersColonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) méthode. Le code ajoute d'abord des noms de personnes dans la colonne A de la première feuille de calcul. Le prénom et le nom sont séparés par un espace. Ensuite, il applique le[TexteVersColonnes](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\) ) sur la colonne A et l'enregistre en tant que fichier Excel de sortie. Si vous ouvrez le[fichier excel de sortie](25395230.xlsx), vous verrez, les prénoms sont dans la colonne A tandis que les noms de famille sont dans la colonne B, comme indiqué dans cette capture d'écran.

![tâche : image_autre_texte](convert-text-to-columns-using-aspose-cells_1.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
