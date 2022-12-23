---
title: Paramètres de configuration
type: docs
weight: 10
url: /fr/jasperreports/configuration-parameters/
---
{{% alert color="primary" %}} 

 Le tableau suivant répertorie les paramètres de configuration.

{{% /alert %}} 

|**Le nom du paramètre** |**Description** |
|:- |:- |
| FORMAT_TYPE| Peut être défini sur "EXCEL97TO2003" ou "EXCEL2007" pour générer des fichiers au format Microsoft Excel 79 0 2003 ou Excel 2007.|
|EST_UN_PAGE_PAR_ FEUILLE| Une valeur booléenne spécifiant si chaque page de rapport doit être écrite dans une feuille de calcul XLS différente.|
|EST_SUPPRIMER_VIDER_ESPACER_ BETWEEN_ROWS| Une valeur booléenne spécifiant si les espaces vides qui peuvent apparaître entre les lignes doivent être supprimés ou non.|
|EST_SUPPRIMER_VIDER_ESPACER_ BETWEEN_COLUMNS|Une valeur booléenne spécifiant si les espaces vides qui peuvent apparaître entre les colonnes doivent être supprimés ou non.|
|EST_BLANCHE_ PAGE_BACKGROUND| Une valeur booléenne spécifiant si l'arrière-plan de la page doit être blanc ou la couleur d'arrière-plan par défaut XLS. La couleur d'arrière-plan XLS peut varier en fonction des propriétés de la visionneuse XLS ou du jeu de couleurs du système d'exploitation.|
|EST_DÉTECTER_ CELL_TYPE| Indicateur utilisé pour indiquer si l'exportateur doit prendre en considération le type des expressions de champ de texte d'origine et définir les types de cellule et les valeurs en conséquence.|
| SHEET_NAMES|Un tableau de chaînes représentant des noms de feuilles personnalisées. Ceci est utile lorsqu'il est utilisé avec l'IS_UN_PAGE_PAR_ Paramètre FEUILLE.|
|EST_POLICE DE CARACTÈRE_TAILLE_RÉPARER_ AUTORISÉ| Indicateur pour réduire la taille de la police afin que le texte tienne dans la hauteur de cellule spécifiée.|
|MAXIMUM_LIGNES_ PAR FEUILLE|Valeur entière spécifiant le nombre maximal de lignes pouvant être affichées dans une feuille. Lorsqu'il est défini, une nouvelle feuille est créée pour les lignes restantes à afficher. Des valeurs négatives ou zéro signifient qu'aucune limite n'a été définie.|
|EST_IGNORER_ GRAPHIQUE| Drapeau pour ignorer les éléments graphiques et exporter uniquement les éléments de texte.|
|EST_S'EFFONDRER_ ROW_SPAN| Indicateur pour réduire l'étendue de la ligne et éviter de fusionner les cellules entre les lignes.|
|EST_IGNORER_ CELL_BORDER| Drapeau pour ignorer la bordure de cellule.|
|EST_UTILISATION_ EXCEL_CHART| Indicateur d'utilisation d'un graphique modifiable au format Excel Microsoft plutôt que d'images statiques. La valeur par défaut est true.|

