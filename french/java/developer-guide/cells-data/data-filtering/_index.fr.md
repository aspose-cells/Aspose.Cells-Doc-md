---
title: Filtrage des données
type: docs
weight: 60
url: /fr/java/data-filtering/
---

{{% alert color="primary" %}}

Microsoft Excel offre de bonnes fonctionnalités pour filtrer les données des feuilles de calcul. Aspose.Cells prend en charge pleinement les fonctionnalités de filtrage automatique de Microsoft Excel. Cet article explique comment utiliser les fonctionnalités dans Microsoft Excel et comment les programmer à l'aide de Aspose.Cells.

{{% /alert %}}

## **Filtrer automatiquement les données**

Le filtrage automatique est le moyen le plus rapide de sélectionner uniquement les éléments de la feuille de calcul que vous souhaitez afficher dans une liste. La fonction de filtrage automatique permet aux utilisateurs de filtrer les éléments d'une liste selon un critère défini. Filtrez par texte, chiffres ou dates.

### **Filtrer automatiquement dans Microsoft Excel**

Pour activer la fonction de filtrage automatique dans Microsoft Excel :

1. Cliquez sur la ligne d'en-tête dans une feuille de calcul.
1. Dans le menu **Données**, sélectionnez **Filtrer** puis **Filtrage automatique**.

Lorsque vous appliquez un filtrage automatique à une feuille de calcul, des interrupteurs de filtre (flèches noires) apparaissent à droite des en-têtes de colonne.

1. Cliquez sur une flèche de filtre pour voir une liste d'options de filtre.

Certaines des options de filtrage automatique sont :

|**Options**|**Description**|
| :- | :- |
|All|Afficher tous les éléments de la liste une fois.|
|Custom|Personnaliser les critères de filtre comme contient/ne contient pas|
|Filter by Color|Filtres basés sur la couleur remplie|
|Date Filters|Filtrer les lignes en fonction de différents critères de date|
|Number Filters|Différents types de filtres sur les nombres comme comparaison, moyennes et Top 10 etc.|
|Text Filters|Différents filtres comme commence par, se termine par, contient, etc.|
|Blanks/Non Blanks|Ces filtres peuvent être mis en œuvre via Filtre de texte vide|
Les utilisateurs filtrent manuellement les données de leur feuille de calcul dans Microsoft Excel en utilisant ces options.

### **Filtrage automatique avec Aspose.Cells**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) qui représente un fichier Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un autofiltre, utilisez la propriété [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) de la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La propriété [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter) est un objet de la classe [**AutoFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter), qui fournit la propriété [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range) pour spécifier la plage de cellules qui composent une ligne d'en-tête. Un autofiltre est appliqué à la plage de cellules qui constitue la ligne d'en-tête.

Sur chaque feuille de calcul, vous ne pouvez spécifier qu'une seule plage de filtres. Cela est limité par Microsoft Excel. Pour le filtrage de données personnalisé, utilisez la méthode [**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-).

Dans l'exemple ci-dessous, nous avons créé le même filtre automatique en utilisant Aspose.Cells que celui que nous avons créé en utilisant Microsoft Excel dans la section ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Différents types de filtres**

Aspose.Cells propose plusieurs options pour appliquer différents types de filtres comme le filtre par couleur, le filtre par date, le filtre par nombre, le filtre par texte, les filtres vides et non vides.

##### **Couleur de remplissage**

Aspose.Cells fournit une fonction [**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter-int-int-com.aspose.cells.CellsColor-com.aspose.cells.CellsColor-) pour filtrer les données en fonction de la propriété de couleur de remplissage des cellules. Dans l'exemple ci-dessous, un fichier modèle comportant différentes couleurs de remplissage dans la première colonne de la feuille est utilisé pour tester la fonction de filtrage de couleur. Les fichiers suivants peuvent être téléchargés pour vérifier la fonctionnalité.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Date**

Différents types de filtres de date peuvent être mis en œuvre comme filtrer toutes les lignes ayant des dates en janvier 2018. Le code d'exemple suivant démontre ce filtre en utilisant la fonction [**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter-int-int-int-int-int-int-int-int-). Les fichiers suivants peuvent être utilisés pour tester cette fonctionnalité.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Date dynamique**

Parfois, des filtres dynamiques sont requis en fonction d'une date, comme toutes les cellules ayant des dates en janvier, indépendamment de l'année. Dans ce cas, la fonction [**DynamicFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter-int-int-) est utilisée comme indiqué dans le code d'exemple suivant. Les fichiers suivants peuvent être utilisés pour les tests.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Nombre**

Des filtres personnalisés peuvent être appliqués en utilisant Aspose.Cells comme la sélection de cellules ayant un nombre compris entre une plage donnée. L'exemple suivant démontre l'utilisation de la fonction [**custom()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom-int-int-java.lang.Object-) pour filtrer les nombres. Les fichiers d'exemple peuvent être téléchargés à partir des liens suivants.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Text**

Si une colonne contient du texte et que des cellules doivent être sélectionnées contenant un texte particulier, la fonction [**filter()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter-int-java.lang.String-) peut être utilisée. Dans l'exemple suivant, le fichier de modèle contient une liste de pays et la ligne doit être sélectionnée contenant le nom du pays en particulier. Le code suivant démontre le filtrage du texte en utilisant les fichiers d'exemple ci-dessous.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Vides**

Si une colonne contient du texte de telle sorte que quelques cellules sont vides, et qu'un filtre est nécessaire pour sélectionner uniquement les lignes où des cellules vides sont présentes, la fonction [**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks-int-) peut être utilisée comme démontré ci-dessous. Les fichiers d'exemple peuvent être téléchargés à partir des liens suivants.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Non vides**

Lorsque des cellules contenant du texte doivent être filtrées, utilisez la fonction de filtrage [**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks-int-) comme démontré ci-dessous. Les fichiers d'exemple peuvent être téléchargés à partir des liens suivants.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Filtre personnalisé avec Contient**

Excel propose des filtres personnalisés comme filtrer les lignes qui contiennent une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et est démontrée ci-dessous en filtrant les noms dans le fichier d'exemple. Des fichiers d'exemple peuvent être téléchargés à partir des liens suivants.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Filtre personnalisé avec NeContientPas**

Excel propose des filtres personnalisés comme filtrer les lignes qui ne contiennent pas une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et démontrée ci-dessous en filtrant les noms dans le fichier d'exemple donné ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Filtre personnalisé avec Commence par**

Excel propose des filtres personnalisés comme filtrer les lignes qui commencent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et démontrée ci-dessous en filtrant les noms dans le fichier d'exemple donné ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Filtre personnalisé avec Se termine par**

Excel propose des filtres personnalisés comme filtrer les lignes qui se terminent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et est démontrée ci-dessous en filtrant les noms dans le fichier d'exemple donné ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Sujets avancés**
- [Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes](/cells/fr/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtenir tous les indices des lignes masquées après le rafraîchissement de l'Autofiltre](/cells/fr/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

{{< app/cells/assistant language="java" >}}
