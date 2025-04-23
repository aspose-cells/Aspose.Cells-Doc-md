---
title: Activation des feuilles et activation d une cellule dans la feuille de calcul
type: docs
weight: 5
url: /fr/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin qu'une feuille de calcul spécifique soit active et affichée lorsque l'utilisateur ouvre un fichier Microsoft Excel dans Excel. De même, vous voudrez peut-être activer une cellule spécifique et définir les barres de défilement pour afficher la cellule active. Aspose.Cells est capable d'accomplir toutes ces tâches comme démontré ci-dessous.

Une **feuille active** est une feuille sur laquelle vous travaillez : le nom de la feuille active sur l'onglet est en gras par défaut.
- Une **cellule active** est une cellule sélectionnée, la cellule dans laquelle les données sont saisies lorsque vous commencez à taper. Une seule cellule est active à la fois. La cellule active est mise en évidence par une bordure épaisse.

{{% /alert %}}

## **Activation des feuilles et activation d'une cellule**

Aspose.Cells fournit des appels d'API spécifiques pour activer une feuille et une cellule. Par exemple, la propriété [**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) est utile pour définir la feuille active dans un classeur. De même, la propriété [**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) peut être utilisée pour définir et obtenir une cellule active dans la feuille de calcul.

Pour vous assurer que les barres de défilement horizontale ou verticale sont à la position de l'indice de ligne et de colonne que vous souhaitez pour afficher des données spécifiques, utilisez les propriétés [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) et [**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn).

L'exemple suivant montre comment activer une feuille de calcul et rendre une cellule active en elle. La sortie suivante est générée lors de l'exécution du code. Les barres de défilement sont défilées pour faire de la 2e ligne et de la 2e colonne leur première ligne et colonne visibles.

**Définition de la cellule B2 comme cellule active**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## Code Java pour définir une feuille de calcul active dans Excel

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

En mode **évaluation**, c'est-à-dire sans définir de licence valide, la feuille de calcul active sera toujours celle contenant le filigrane d'évaluation. Ce comportement ne peut être outrepassé qu'en définissant la licence au démarrage de l'application.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
