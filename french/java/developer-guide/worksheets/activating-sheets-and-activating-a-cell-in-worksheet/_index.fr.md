---
title: Activation des feuilles et activation d'un Cell dans la feuille de calcul
type: docs
weight: 5
url: /fr/java/activating-sheets-and-activating-a-cell-in-worksheet/
---
{{% alert color="primary" %}}

Parfois, vous avez besoin qu'une feuille de calcul spécifique soit active et affichée lorsqu'un utilisateur ouvre un fichier Excel Microsoft dans Excel. De même, vous souhaiterez peut-être activer une cellule spécifique et définir les barres de défilement pour afficher la cellule active. Aspose.Cells est capable de faire toutes ces tâches comme démontré ci-dessous.

-  Un**feuille active** est une feuille sur laquelle vous travaillez : le nom de la feuille active sur l'onglet est en gras par défaut.
-  Un**cellule active** est une cellule sélectionnée, la cellule dans laquelle les données sont saisies lorsque vous commencez à taper. Une seule cellule est active à la fois. La cellule active est mise en évidence par une bordure épaisse.

{{% /alert %}}

## **Activation des feuilles et activation d'un Cell**

Aspose.Cells fournit des appels spécifiques API pour activer une feuille et une cellule. Par exemple, le[**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex)La propriété est utile pour définir la feuille active dans un classeur. De même, le[**Feuille de travail.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell)La propriété peut être utilisée pour définir et obtenir une cellule active dans la feuille de calcul.

Pour vous assurer que les barres de défilement horizontales ou verticales se trouvent à la position d'index de ligne et de colonne où vous souhaitez afficher des données spécifiques, utilisez la[**Feuille de calcul.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow)et[**Feuille de calcul.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn)Propriétés.

L'exemple suivant montre comment activer une feuille de calcul et y rendre une cellule active. La sortie suivante est générée lors de l'exécution du code. Les barres de défilement défilent pour faire de la 2e ligne et de la 2e colonne leur première ligne et colonne visibles.

**Définir la cellule B2 comme cellule active**

![tâche : image_autre_texte](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Java code pour définir une feuille de calcul active dans Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

 Dans**évaluation** mode, c'est-à-dire; sans définir de licence valide, la feuille de calcul active sera toujours celle contenant le filigrane d'évaluation. Ce comportement ne peut être annulé qu'en définissant la licence au démarrage de l'application.

{{% /alert %}}
