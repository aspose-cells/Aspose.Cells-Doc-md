---
title: Filtrage des données
type: docs
weight: 85
url: /fr/python-net/data-filtering/
description: Apprenez à ajouter un filtre de données en utilisant l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Python Excel, Python Ajouter un filtre par couleur, Python Ajouter des filtres de date, Python Ajouter des filtres numériques, Python Ajouter un filtre dynamique, Python Ajouter des filtres de texte, Python Ajouter un filtre personnalisé avec Contient, Python Ajouter un filtre personnalisé avec NeContientPas, Python Ajouter un filtre personnalisé avec CommencePar, Python Ajouter un filtre personnalisé avec SeTerminePar
---

{{% alert color="primary" %}}

Microsoft Excel offre de bonnes fonctionnalités pour filtrer automatiquement les données de la feuille de calcul. Aspose.Cells pour Python via .NET prend en charge pleinement les fonctionnalités de filtrage automatique de Microsoft Excel. Cet article explique comment utiliser les fonctionnalités de Microsoft Excel et comment les coder en utilisant Aspose.Cells pour Python via .NET.

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
|Number Filters|Différents types de filtres sur les nombres tels que la comparaison, les moyennes et les Top 10, etc.|
|Text Filters|Différents filtres comme commence par, se termine par, contient, etc.|
|Blanks/Non Blanks|Ces filtres peuvent être mis en œuvre via Filtre de texte vide|

Les utilisateurs filtrent manuellement les données de leur feuille de calcul dans Microsoft Excel en utilisant ces options.

### **Filtre automatique avec la bibliothèque Aspose.Cells pour Python Excel**

Aspose.Cells pour Python via .NET fournit une classe, Workbook, qui représente un fichier Excel. La classe Workbook contient une collection de feuilles de calcul qui permet d'accéder à chaque feuille de calcul dans le fichier Excel.

Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit une large gamme de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un filtre automatique, utilisez la propriété AutoFilter de la classe Worksheet. La propriété AutoFilter est un objet de la classe AutoFilter, qui fournit la propriété Plage pour spécifier la plage de cellules qui compose une ligne d'en-tête. Un filtre automatique est appliqué à la plage de cellules qui constitue la ligne d'en-tête.

Dans chaque feuille de calcul, vous ne pouvez spécifier qu'une seule plage de filtre. Cela est limité par Microsoft Excel. Pour un filtrage personnalisé des données, utilisez la méthode AutoFilter.Custom.

Dans l'exemple ci-dessous, nous avons créé le même filtre automatique en utilisant Aspose.Cells pour Python via .NET que celui créé avec Microsoft Excel dans la section précédente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterData-1.py" >}}

#### **Différents types de filtres**

Aspose.Cells pour Python via .NET offre plusieurs options pour appliquer différents types de filtres tels que Filtre de couleur, Filtre de date, Filtre de nombre, Filtre de texte, Filtres vides et Filtres non vides.

##### **Couleur de remplissage**

Aspose.Cells pour Python via .NET fournit une fonction AddFillColorFilter pour filtrer les données en fonction de la propriété de couleur de remplissage des cellules. Dans l'exemple ci-dessous, un fichier modèle contenant différentes couleurs de remplissage dans la première colonne de la feuille est utilisé pour tester la fonction de filtrage par couleur. Les fichiers d'exemple peuvent être téléchargés à partir des liens suivants.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterColor-1.py" >}}

##### **Date**

Différents types de filtres de date peuvent être implémentés comme filtrer toutes les lignes ayant des dates en janvier 2018. Le code d'exemple suivant démontre ce filtre en utilisant la fonction AddDateFilter. Les fichiers d'exemple sont donnés ci-dessous.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDate-1.py" >}}

##### **Date dynamique**

Parfois, des filtres dynamiques sont nécessaires en fonction de la date comme toutes les cellules ayant des dates en janvier, indépendamment de l'année. Dans ce cas, la fonction DynamicFilter est utilisée comme donné dans le code d'exemple suivant. Les fichiers d'exemple sont donnés ci-dessous.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterDynamicFilter-1.py" >}}

##### **Nombre**

Les filtres personnalisés peuvent être appliqués à l'aide d'Aspose.Cells pour Python via .NET comme la sélection de cellules ayant un nombre compris entre une plage donnée. L'exemple suivant montre l'utilisation de la fonction Custom() pour filtrer les nombres. Des fichiers d'exemple sont donnés ci-dessous.

1. [Number.xlsx](72417320.xlsx)
1. [FilteredNumber.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNumber-1.py" >}}

##### **Text**

Si une colonne contient du texte et que des cellules doivent être sélectionnées contenant un texte particulier, la fonction Filter() peut être utilisée. Dans l'exemple suivant, le fichier modèle contient une liste de pays et une ligne doit être sélectionnée contenant le nom d'un pays particulier. Le code suivant montre le filtrage du texte. Des fichiers d'exemple sont donnés ci-dessous.

1. [Text.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterText-1.py" >}}

##### **Vides**

Si une colonne contient du texte et que certaines cellules sont vides, et qu'un filtre est nécessaire pour sélectionner uniquement les lignes où des cellules vides sont présentes, la fonction MatchBlanks() peut être utilisée comme démontré ci-dessous. Des fichiers d'exemple sont donnés ci-dessous.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterBlank-1.py" >}}

##### **Non vides**

Lorsque des cellules contenant du texte doivent être filtrées, utilisez la fonction de filtre MatchNonBlanks comme démontré ci-dessous. Des fichiers d'exemple sont donnés ci-dessous.

1. [Blank.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterNonBlank-1.py" >}}

##### **Filtre personnalisé avec Contient**

Excel propose des filtres personnalisés comme filtrer les lignes qui contiennent une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells pour Python via .NET et est démontrée ci-dessous en filtrant les noms dans le fichier d'exemple. Des fichiers d'exemple sont donnés ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-Contains-1.py" >}}

##### **Filtre personnalisé avec NeContientPas**

Excel propose des filtres personnalisés tels que filtrer les lignes qui ne contiennent pas une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells pour Python via .NET et est démontrée ci-dessous en filtrant les noms dans le fichier d'exemple donné ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-Filtering-AutofilterCustom-NotContains-1.py" >}}

##### **Filtre personnalisé avec Commence par**

Excel propose des filtres personnalisés tels que filtrer les lignes qui commencent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells pour Python via .NET et est démontrée ci-dessous en filtrant les noms dans le fichier d'exemple donné ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterBeginsWith-1.py" >}}

##### **Filtre personnalisé avec Se termine par**

Excel propose des filtres personnalisés tels que filtrer les lignes qui se terminent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells pour Python via .NET et est démontrée ci-dessous en filtrant les noms dans le fichier d'exemple donné ci-dessous.

1. [sourseSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-FilteringAndValidation-AutofilterEndsWith-1.py" >}}

## **Sujets avancés**
- [Appliquer un filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes](/cells/fr/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtenir tous les indices des lignes masquées après le rafraîchissement de l'Autofiltre](/cells/fr/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
{{< app/cells/assistant language="python-net" >}}
