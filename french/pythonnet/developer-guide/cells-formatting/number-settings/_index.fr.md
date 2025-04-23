---
title: Paramètres de nombre
description: Aspose.Cells est une bibliothèque Python pour travailler avec des fichiers de feuilles de calcul qui supporte de nombreux paramètres de numérotation des cellules. Cet article explique comment utiliser la bibliothèque Aspose.Cells pour gérer les paramètres de numérotation des cellules afin que les utilisateurs puissent ajuster le format des nombres dans la feuille de calcul selon leurs besoins.
keywords: Aspose.Cells, bibliothèque Python, feuille de calcul électronique, paramètres de numérotation des cellules, mise en forme, gestion, formats de nombres et de dates
type: docs
weight: 10
url: /fr/python-net/cells-number-settings/
---

## **Comment définir les formats d'affichage des nombres et des dates**

Une fonctionnalité très forte d'Excel de Microsoft est qu'elle permet aux utilisateurs de définir les formats d'affichage des valeurs numériques et des dates. Nous savons que des données numériques peuvent être utilisées pour représenter différentes valeurs, y compris des valeurs décimales, monétaires, en pourcentage, en fraction ou en comptabilité, etc. Toutes ces valeurs numériques sont affichées sous différents formats en fonction du type d'informations qu'elles représentent. De même, il existe de nombreux formats dans lesquels une date ou une heure peuvent être affichées.
Aspose.Cells pour Python via .NET supporte cette fonctionnalité et permet aux développeurs de définir n’importe quel format d’affichage pour un nombre ou une date.

### **Comment définir les formats d'affichage dans Microsoft Excel**

Pour définir les formats d'affichage dans Microsoft Excel:

1. Cliquez avec le bouton droit sur n'importe quelle cellule.
1. Sélectionnez **Format des cellules**. Une boîte de dialogue s'affichera qui est utilisée pour définir les formats d'affichage de n'importe quel type de valeur.

Dans la partie gauche de la boîte de dialogue, il y a de nombreuses catégories de valeurs comme **Général**, **Nombre**, **Devise**, **Comptabilité**, **Date**, **Heure**, **Pourcentage**, etc. Aspose.Cells pour Python via .NET supporte tous ces formats d’affichage.

Aspose.Cells pour Python via .NET fournit une classe, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contient une collection [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets) qui permet d’accéder à chaque feuille dans le fichier Excel. Une feuille est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) fournit une collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells). Chaque élément de la collection [**cells**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell).

Aspose.Cells pour Python via .NET fournit des méthodes [**get_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_style) et [**set_style**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_style) pour la classe [**Cell**](https://reference.aspose.com/cells/python-net/aspose.cells/cell). Ces méthodes sont utilisées pour obtenir et définir la mise en forme d'une cellule. La classe [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) offre quelques propriétés utiles pour traiter les formats d’affichage des nombres et des dates.

### **Comment Utiliser les Formats de Nombre Intégrés**

Aspose.Cells pour Python via .NET propose certains formats de nombres intégrés pour configurer les formats d’affichage des nombres et des dates. Ces formats intégrés peuvent être appliqués en utilisant la propriété [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) de l’objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style). Tous les formats de nombres intégrés ont des valeurs numériques uniques. Les développeurs peuvent assigner n’importe quelle valeur numérique souhaitée à la propriété [**Number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) de l’objet [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) pour appliquer le format d’affichage. Cette approche est rapide. Les formats de nombres intégrés pris en charge par Aspose.Cells sont listés ci-dessous.

|**Valeur**|**Type**|**Chaîne de format**|
| :- | :- | :- |
|0|General|General|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|#,##0|
|4|Decimal|#,##0.00|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Red]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Red]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|# ?/?|
|13|Fraction|# */*|
|14|Date|m/d/yyyy|
|15|Date|d-mmm-yy|
|16|Date|d-mmm|
|17|Date|mmm-yy|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|h:mm|
|21|Time|h:mm:ss|
|22|Time|m/d/yy h:mm|
|37|Currency|#,##0;-#,##0|
|38|Currency|#,##0;[Red]-#,##0|
|39|Currency|#,##0.00;-#,##0.00|
|40|Currency|#,##0.00;[Red]-#,##0.00|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|##0.0E+00|
|49|Text|@|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingBuiltInNumberFormats-1.py" >}}

### **Comment Utiliser les Formats de Nombre Personnalisés**

Pour définir votre propre chaîne de format personnalisée pour définir le format d'affichage, utilisez la propriété [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) de l'objet [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom). Cette approche n'est pas aussi rapide que l'utilisation de formats prédéfinis, mais elle est plus flexible.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-UsingCustomNumber-1.py" >}}

{{% alert color="primary" %}}

Si vous utilisez la propriété [**custom**](https://reference.aspose.com/cells/python-net/aspose.cells/style/custom) pour définir le format de nombre, tout format précédemment défini en utilisant la propriété [**number**](https://reference.aspose.com/cells/python-net/aspose.cells/style/number) est remplacé et vice versa.

{{% /alert %}}

## **Sujets avancés**
- [Vérifier le format personnalisé du nombre lors de la définition de la propriété de style personnalisé](/cells/fr/python-net/check-custom-number-format-when-setting-style-custom-property/)
- [Liste des Formats de Nombre Supportés](/cells/fr/python-net/list-of-supported-number-formats/)
- [Rendre le modèle de format de date personnalisé g et ge mm dd](/cells/fr/python-net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Spécifier les séparateurs de décimales et de groupe personnalisés pour le classeur](/cells/fr/python-net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Spécifier la mise en forme du modèle personnalisé DBNum](/cells/fr/python-net/specifying-dbnum-custom-pattern-formatting/)

