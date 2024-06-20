---
title: Paramètres de nombre
type: docs
weight: 10
url: /fr/java/cells-number-settings/
---

## **Paramétrage des formats d'affichage des nombres et des dates**

Une fonctionnalité très forte d'Excel de Microsoft est qu'elle permet aux utilisateurs de définir les formats d'affichage des valeurs numériques et des dates. Nous savons que des données numériques peuvent être utilisées pour représenter différentes valeurs, y compris des valeurs décimales, monétaires, en pourcentage, en fraction ou en comptabilité, etc. Toutes ces valeurs numériques sont affichées sous différents formats en fonction du type d'informations qu'elles représentent. De même, il existe de nombreux formats dans lesquels une date ou une heure peuvent être affichées.
Aspose.Cells prend en charge cette fonctionnalité et permet aux développeurs de définir tout format d'affichage pour un nombre ou une date.

## **Définition des formats d'affichage dans Microsoft Excel**

Pour définir les formats d'affichage dans Microsoft Excel:

1. Cliquez avec le bouton droit sur n'importe quelle cellule.
1. Sélectionnez **Format des cellules**. Une boîte de dialogue s'affichera qui est utilisée pour définir les formats d'affichage de n'importe quel type de valeur.

À gauche de la boîte de dialogue, il y a de nombreuses catégories de valeurs comme **Général**, **Nombre**, **Monétaire**, **Comptabilité**, **Date**, **Heure**, **Pourcentage**, etc. Aspose.Cells prend en charge tous ces formats d'affichage.

## **Utilisation des formats de nombre intégrés**

Aspose.Cells propose certains formats de nombre intégrés pour configurer les formats d'affichage des nombres et des dates. Tous les formats de nombre intégrés reçoivent des valeurs numériques uniques. Les développeurs peuvent attribuer n'importe quelle valeur numérique souhaitée à la méthode [**Number**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) de l'objet [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) pour appliquer le format d'affichage. Cette approche est rapide. Les formats de nombre intégrés pris en charge par Aspose.Cells sont énumérés ci-dessous.

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

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Utilisation de formats de nombre personnalisés**

Pour définir votre propre chaîne de format personnalisée pour définir le format d'affichage, utilisez [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Cette approche n'est pas aussi rapide que l'utilisation de formats prédéfinis, mais elle est plus flexible.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

Si vous utilisez [**Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) pour définir le format de nombre, tout format précédent défini à l'aide du [**Nombre**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) est remplacé et vice versa.

{{% /alert %}}

## **Sujets avancés**
- [Vérifier le format personnalisé du nombre lors de la définition de la propriété de style personnalisé](/cells/fr/java/check-custom-number-format-when-setting-style-custom-property/)
- [Spécifier les séparateurs de décimales et de groupe personnalisés pour le classeur](/cells/fr/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Spécifier la mise en forme du modèle personnalisé DBNum](/cells/fr/java/specifying-dbnum-custom-pattern-formatting/)
