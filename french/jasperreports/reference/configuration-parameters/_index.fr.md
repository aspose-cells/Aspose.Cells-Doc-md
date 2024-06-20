---
title: Paramètres de configuration
type: docs
weight: 10
url: /fr/jasperreports/configuration-parameters/
---

{{% alert color="primary" %}} 

Le tableau suivant répertorie les paramètres de configuration. 

{{% /alert %}} 

| **Nom du paramètre** | **Description** |
| :- | :- |
|FORMAT_TYPE |Peut être défini sur "EXCEL97TO2003" ou "EXCEL2007" pour générer des fichiers au format Microsoft Excel 79 0 2003 ou Excel 2007. |
|IS_ONE_PAGE_PER_SHEET |Une valeur booléenne spécifiant si chaque page de rapport doit être écrite dans une feuille de calcul XLS différente. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_ROWS |Une valeur booléenne spécifiant si les espaces vides qui peuvent apparaître entre les lignes doivent être supprimés ou non. |
|IS_REMOVE_EMPTY_SPACE_BETWEEN_COLUMNS |Une valeur booléenne spécifiant si les espaces vides qui peuvent apparaître entre les colonnes doivent être supprimés ou non. |
|IS_WHITE_PAGE_BACKGROUND |Une valeur booléenne spécifiant si l'arrière-plan de la page doit être blanc ou la couleur de l'arrière-plan XLS par défaut. La couleur de fond XLS peut varier en fonction des propriétés de visualisation XLS ou du schéma de couleurs du système d'exploitation. |
|IS_DETECT_CELL_TYPE |Drapeau indiquant si l'exportateur doit tenir compte du type des expressions de champ de texte d'origine et définir les types de cellules et les valeurs en conséquence. |
|SHEET_NAMES |Un tableau de chaînes représentant des noms de feuilles personnalisées. C'est utile lorsqu'il est utilisé avec le paramètre IS_ONE_PAGE_PER_SHEET. |
|IS_FONT_SIZE_FIX_ENABLED |Drapeau pour réduire la taille de la police afin que le texte s'adapte à la hauteur de cellule spécifiée. |
|MAXIMUM_ROWS_PER_SHEET |Une valeur entière spécifiant le nombre maximum de lignes autorisées à être affichées dans une feuille. Lorsqu'il est défini, une nouvelle feuille est créée pour afficher les lignes restantes. Des valeurs négatives ou nulles signifient qu'aucune limite n'a été définie. |
|IS_IGNORE_GRAPHICS |Drapeau pour ignorer les éléments graphiques et exporter uniquement les éléments textuels. |
|IS_COLLAPSE_ROW_SPAN |Drapeau pour réduire l'étendue de lignes et éviter la fusion des cellules entre les lignes. |
|IS_IGNORE_CELL_BORDER |Drapeau pour ignorer la bordure des cellules. |
|IS_USE_EXCEL_CHART |Drapeau pour utiliser un graphique modifiable au format Microsoft Excel plutôt que des images statiques. La valeur par défaut est true. |

