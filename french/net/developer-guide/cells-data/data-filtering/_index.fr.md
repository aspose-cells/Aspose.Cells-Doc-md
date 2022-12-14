---
title: Filtrage des données
type: docs
weight: 85
url: /fr/net/data-filtering/
---
{{% alert color="primary" %}}

Microsoft Excel fournit quelques bonnes fonctionnalités pour filtrer automatiquement les données de feuille de calcul. Aspose.Cells prend entièrement en charge les fonctionnalités de filtrage automatique d'Excel Microsoft. Cet article explique comment utiliser les fonctionnalités dans Microsoft Excel et comment les coder à l'aide de Aspose.Cells.

{{% /alert %}}

## **Données de filtrage automatique**

Le filtrage automatique est le moyen le plus rapide de sélectionner uniquement les éléments de la feuille de calcul que vous souhaitez afficher dans une liste. La fonction de filtrage automatique permet aux utilisateurs de filtrer les éléments d'une liste en fonction de critères définis. Filtre basé sur du texte, des nombres ou des dates.

### **Filtre automatique dans Microsoft Excel**

Pour activer la fonction de filtre automatique dans Microsoft Excel :

1. Cliquez sur la ligne d'en-tête dans une feuille de calcul.
1.  Du**Données** menu, sélectionnez**Filtre** et alors**Filtre automatique**.

Lorsque vous appliquez un filtre automatique à une feuille de calcul, des commutateurs de filtre (flèches noires) apparaissent à droite des en-têtes de colonne.

1. Cliquez sur une flèche de filtre pour afficher une liste d'options de filtre.

Certaines des options de filtre automatique sont :

|**Choix**|**La description**|
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

Aspose.Cells fournit une classe Workbook qui représente un fichier Excel. La classe Workbook contient une collection Worksheets qui permet d'accéder à chaque feuille de calcul du fichier Excel.

Une feuille de calcul est représentée par la classe Worksheet. La classe Worksheet fournit un large éventail de propriétés et de méthodes pour gérer les feuilles de calcul. Pour créer un filtre automatique, utilisez la propriété AutoFilter de la classe Worksheet. La propriété AutoFilter est un objet de la classe AutoFilter, qui fournit la propriété Range pour spécifier la plage de cellules qui composent une ligne d'en-tête. Un filtre automatique est appliqué à la plage de cellules qui correspond à la ligne d'en-tête.

Dans chaque feuille de calcul, vous ne pouvez spécifier qu'une seule plage de filtres. Ceci est limité par Microsoft Excel. Pour le filtrage de données personnalisé, utilisez la méthode AutoFilter.Custom.

Dans l'exemple ci-dessous, nous avons créé le même filtre automatique en utilisant Aspose.Cells que nous avons créé en utilisant Microsoft Excel dans la section ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterData-1.cs" >}}

#### **Différents types de filtre**

Aspose.Cells offre plusieurs options pour appliquer différents types de filtres comme le filtre de couleur, le filtre de date, le filtre de nombre, le filtre de texte, les filtres vides et les filtres aucun vide.

##### **La couleur de remplissage**

Aspose.Cells fournit une fonction AddFillColorFilter pour filtrer les données en fonction de la propriété de couleur de remplissage des cellules. Dans l'exemple ci-dessous, un fichier modèle ayant différentes couleurs de remplissage dans la première colonne de la feuille est utilisé pour tester la fonction de filtrage des couleurs. Des exemples de fichiers peuvent être téléchargés à partir des liens suivants.

1. [ColouredCells.xlsx](72417315.xlsx)
1. [FilteredColouredCells.xlsx](72417316.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterColor-1.cs" >}}

##### **Date**

Différents types de filtres de date peuvent être implémentés, comme le filtrage de toutes les lignes ayant des dates en janvier 2018. L'exemple de code suivant illustre ce filtre à l'aide de la fonction AddDateFilter. Des exemples de fichiers sont donnés ci-dessous.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDate.xlsx](72417318.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDate-1.cs" >}}

##### **Date dynamique**

Parfois, des filtres dynamiques sont nécessaires en fonction de la date, comme toutes les cellules ayant des dates en janvier, quelle que soit l'année. Dans ce cas, la fonction DynamicFilter est utilisée comme indiqué dans l'exemple de code suivant. Des exemples de fichiers sont donnés ci-dessous.

1. [Date.xlsx](72417317.xlsx)
1. [FilteredDynamicDate.xlsx](72417319.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterDynamicFilter-1.cs" >}}

##### **Numéro**

Des filtres personnalisés peuvent être appliqués à l'aide de Aspose.Cells, comme la sélection de cellules dont le nombre se situe dans une plage donnée. L'exemple suivant montre l'utilisation de la fonction Custom() pour filtrer les nombres. Des exemples de fichiers sont donnés ci-dessous.

1. [Numéro.xlsx](72417320.xlsx)
1. [NuméroFiltré.xlsx](72417321.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNumber-1.cs" >}}

##### **Texte**

Si une colonne contient du texte et que des cellules doivent être sélectionnées contenant un texte particulier, la fonction Filter() peut être utilisée. Dans l'exemple suivant, le fichier de modèle contient une liste de pays et la ligne doit être sélectionnée contenant le nom de pays particulier. Le code suivant illustre le filtrage du texte. Des exemples de fichiers sont donnés ci-dessous.

1. [Texte.xlsx](72417322.xlsx)
1. [FilteredText.xlsx](72417323.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterText-1.cs" >}}

##### **Blancs**

Si une colonne contient du texte tel que peu de cellules sont vides et qu'un filtre est nécessaire pour sélectionner uniquement les lignes contenant des cellules vides, la fonction MatchBlanks() peut être utilisée comme illustré ci-dessous. Des exemples de fichiers sont donnés ci-dessous.

1. [Vide.xlsx](72417324.xlsx)
1. [FilteredBlank.xlsx](72417325.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterBlank-1.cs" >}}

##### **Non vierges**

Lorsque des cellules contenant du texte doivent être filtrées, utilisez la fonction de filtre MatchNonBlanks comme illustré ci-dessous. Des exemples de fichiers sont donnés ci-dessous.

1. [Vide.xlsx](72417324.xlsx)
1. [FilteredNonBlank.xlsx](72417326.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterNonBlank-1.cs" >}}

##### **Filtre personnalisé avec Contient**

Excel fournit des filtres personnalisés tels que des lignes de filtre contenant une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et illustrée ci-dessous en filtrant les noms dans le fichier d'exemple. Des exemples de fichiers sont donnés ci-dessous.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx)
1. [outSourseSampleCountryNames.xlsx](outSourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-Contains-1.cs" >}}

##### **Filtre personnalisé avec NotContains**

Excel fournit des filtres personnalisés tels que des lignes de filtre qui ne contiennent pas de chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et illustrée ci-dessous en filtrant les noms dans l'exemple de fichier ci-dessous.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-Filtering-AutofilterCustom-NotContains-1.cs" >}}

##### **Filtre personnalisé avec BeginsWith**

Excel fournit des filtres personnalisés comme des lignes de filtre qui commencent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et illustrée ci-dessous en filtrant les noms dans l'exemple de fichier ci-dessous.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterBeginsWith-1.cs" >}}

##### **Filtre personnalisé avec EndsWith**

Excel fournit des filtres personnalisés comme des lignes de filtre qui se terminent par une chaîne spécifique. Cette fonctionnalité est disponible dans Aspose.Cells et illustrée ci-dessous en filtrant les noms dans l'exemple de fichier ci-dessous.

1. [sourceSampleCountryNames.xlsx](sourseSampleCountryNames.xlsx).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-AutofilterEndsWith-1.cs" >}}

## **Sujets avancés**
- [Appliquer le filtre avancé de Microsoft Excel pour afficher les enregistrements répondant à des critères complexes](/cells/fr/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Obtenir tous les indices de lignes masquées après l'actualisation du filtre automatique](/cells/fr/net/get-all-hidden-rows-indices-after-refreshing-autofilter/)
