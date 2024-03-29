﻿---
title: Filtrage des données
type: docs
weight: 60
url: /fr/java/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel fournit quelques bonnes fonctionnalités pour filtrer automatiquement les données de feuille de calcul. Aspose.Cells prend entièrement en charge les fonctionnalités de filtrage automatique d'Excel Microsoft. Cet article explique comment utiliser les fonctionnalités dans Microsoft Excel et comment les coder à l'aide de Aspose.Cells.

{{% /alert %}}

## **Données de filtrage automatique**

Le filtrage automatique est le moyen le plus rapide de sélectionner uniquement les éléments de la feuille de calcul que vous souhaitez afficher dans une liste. La fonction de filtrage automatique permet aux utilisateurs de filtrer les éléments d'une liste en fonction de critères définis. Filtre basé sur du texte, des nombres ou des dates.

### **Filtre automatique dans Microsoft Excel**

Pour activer la fonction de filtre automatique dans Microsoft Excel :

1. Cliquez sur la ligne d'en-tête dans une feuille de calcul.
1. Du**Données**menu, sélectionnez**Filtre**et puis**Filtre automatique**.

Lorsque vous appliquez un filtre automatique à une feuille de calcul, des commutateurs de filtre (flèches noires) apparaissent à droite des en-têtes de colonne.

1. Cliquez sur une flèche de filtre pour afficher une liste d'options de filtre.

Certaines des options de filtre automatique sont :

|**Choix**|**Description**|
|:- |:- |
|Tout|Afficher tous les éléments de la liste une fois.|
|Personnalisé|Personnalisez les critères de filtre comme contient/ne contient pas|
|Filtrer par couleur|Filtres basés sur la couleur remplie|
|Filtres de dates|Filtre les lignes en fonction de différents critères à la date|
|Filtres numériques|Différents types de filtres sur les nombres comme la comparaison, les moyennes et le Top 10, etc.|
|Filtres de texte|Différents filtres comme commence par, se termine par, contient etc,|
|Blancs/non blancs|Ces filtres peuvent être implémentés via Text Filter Blank|
Les utilisateurs filtrent manuellement leurs données de feuille de calcul dans Microsoft Excel à l'aide de ces options.

### **Filtre automatique avec Aspose.Cells**

Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)qui représente un fichier Excel. Le[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)classe contient un[**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection)qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)La classe fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un filtre automatique, utilisez le[**Filtre automatique**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)propriété de la[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)classe. Le[**Filtre automatique**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)la propriété est un objet de la[**Filtre automatique**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#AutoFilter)classe, qui fournit la[**Intervalle**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#Range)propriété pour spécifier la plage de cellules qui composent une ligne d'en-tête. Un filtre automatique est appliqué à la plage de cellules qui correspond à la ligne d'en-tête.

Dans chaque feuille de calcul, vous ne pouvez spécifier qu'une seule plage de filtres. Ceci est limité par Microsoft Excel. Pour un filtrage de données personnalisé, utilisez le[**AutoFilter.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) méthode.

Dans l'exemple ci-dessous, nous avons créé le même filtre automatique en utilisant Aspose.Cells que nous avons créé en utilisant Microsoft Excel dans la section ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterData.java" >}}

#### **Différents types de filtre**

Aspose.Cells offre plusieurs options pour appliquer différents types de filtres comme le filtre de couleur, le filtre de date, le filtre de nombre, le filtre de texte, les filtres vides et les filtres aucun vide.

##### **La couleur de remplissage**

Aspose.Cells fournit une fonction[**addFillColorFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addFillColorFilter(int,%20int,%20com.aspose.cells.CellsColor,%20com.aspose.cells.CellsColor)pour filtrer les données en fonction de la propriété de couleur de remplissage des cellules. Dans l'exemple ci-dessous, un fichier modèle ayant différentes couleurs de remplissage dans la première colonne de la feuille est utilisé pour tester la fonction de filtrage des couleurs. Les fichiers suivants peuvent être téléchargés pour vérifier la fonctionnalité.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterColor.java" >}}

##### **Date**

Différents types de filtres de date peuvent être implémentés comme le filtrage de toutes les lignes ayant des dates en janvier 2018. L'exemple de code suivant illustre ce filtre en utilisant[**addDateFilter**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#addDateFilter(int,%20int,%20int,%20int,%20int,%20int,%20int,%20int)) une fonction. Les fichiers suivants peuvent être utilisés pour tester cette fonctionnalité.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDate.java" >}}

##### **Date dynamique**

Parfois, des filtres dynamiques sont nécessaires en fonction d'une date, comme toutes les cellules ayant des dates en janvier, quelle que soit l'année. Dans ce cas,[**FiltreDynamique**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#dynamicFilter(int,%20int)) est utilisée comme indiqué dans l'exemple de code suivant. Les fichiers suivants peuvent être utilisés pour les tests.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterDynamicFilter.java" >}}

##### **Nombre**

Des filtres personnalisés peuvent être appliqués à l'aide de Aspose.Cells, comme la sélection de cellules dont le nombre se situe dans une plage donnée. L'exemple suivant montre l'utilisation de[**Douane()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#custom(int,%20int,%20java.lang.Object)) fonction pour filtrer les nombres. Des exemples de fichiers peuvent être téléchargés à partir des liens suivants.

1. [Numéro.xlsx](72417320.xlsx)
1. [NuméroFiltré.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNumber.java" >}}

##### **Texte**

Si une colonne contient du texte et que des cellules doivent être sélectionnées contenant un texte particulier,[**filtre()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#filter(int,%20java.lang.String)) peut être utilisée. Dans l'exemple suivant, le fichier modèle contient une liste de pays et la ligne doit être sélectionnée contenant un nom de pays particulier. Le code suivant illustre le filtrage de texte à l'aide des exemples de fichiers ci-dessous.

1. [Texte.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterText.java" >}}

##### **Blancs**

Si une colonne contient du texte tel que peu de cellules sont vides et qu'un filtre est nécessaire pour sélectionner uniquement les lignes contenant des cellules vides,[**matchBlanks()**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchBlanks(int)) peut être utilisée comme illustré ci-dessous. Des exemples de fichiers peuvent être téléchargés à partir des liens suivants.

1. [Vide.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterBlank.java" >}}

##### **Non vierges**

Lorsque des cellules contenant du texte doivent être filtrées, utilisez[**MatchNonBlanks**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#matchNonBlanks(int)) fonction de filtre comme illustré ci-dessous. Des exemples de fichiers peuvent être téléchargés à partir des liens suivants.

1. [Vide.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterNonBlank.java" >}}

##### **Filtre personnalisé avec Contient**

Excel fournit des filtres personnalisés tels que des lignes de filtre contenant une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et illustrée ci-dessous en filtrant les noms dans le fichier d'exemple. Des exemples de fichiers peuvent être téléchargés à partir des liens suivants.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-Contains.java" >}}

##### **Filtre personnalisé avec NotContains**

Excel fournit des filtres personnalisés tels que des lignes de filtre qui ne contiennent pas de chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et illustrée ci-dessous en filtrant les noms dans l'exemple de fichier ci-dessous.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-NotContains.java" >}}

##### **Filtre personnalisé avec BeginsWith**

Excel fournit des filtres personnalisés comme des lignes de filtre qui commencent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et illustrée ci-dessous en filtrant les noms dans l'exemple de fichier ci-dessous.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-BeginsWith.java" >}}

##### **Filtre personnalisé avec EndsWith**

Excel fournit des filtres personnalisés comme des lignes de filtre qui se terminent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et illustrée ci-dessous en filtrant les noms dans l'exemple de fichier ci-dessous.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-AutofilterData-AutofilterCustom-EndsWith.java" >}}

## **Sujets avancés**
- [Appliquer le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes](/cells/fr/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtenir tous les indices de lignes masquées après l'actualisation du filtre automatique](/cells/fr/java/get-all-hidden-rows-indices-after-refreshing-autofilter/)

