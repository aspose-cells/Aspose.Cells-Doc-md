---
title: Paramètres numériques
type: docs
weight: 10
url: /fr/java/cells-number-settings/
---
##  **Définition des formats d'affichage de Numbers et des dates**

Une fonctionnalité très intéressante de Microsoft Excel est qu'il permet aux utilisateurs de définir les formats d'affichage des valeurs numériques et des dates. Nous savons que les données numériques peuvent être utilisées pour représenter différentes valeurs, notamment des valeurs décimales, monétaires, en pourcentage, fractionnaires ou comptables, etc. Toutes ces valeurs numériques sont affichées dans différents formats selon le type d'information qu'elles représentent. De même, il existe de nombreux formats dans lesquels une date ou une heure peut être affichée.
Aspose.Cells prend en charge cette fonctionnalité et permet aux développeurs de définir n'importe quel format d'affichage pour un nombre ou une date.

##  **Définition des formats d'affichage dans Microsoft Excel**

Pour définir les formats d'affichage dans Excel Microsoft :

1. Cliquez avec le bouton droit sur n’importe quelle cellule.
1. Sélectionnez *Format Cells**. Une boîte de dialogue apparaîtra, utilisée pour définir les formats d'affichage de tout type de valeur.

 Dans la partie gauche de la boîte de dialogue, il existe de nombreuses catégories de valeurs telles que**Général**, **Nombre**, **Devise**, **Comptabilité**, **Date**, **Heure**, **Pourcentage,**etc. Aspose.Cells prend en charge tous ces formats d'affichage.

##  **Utilisation des formats de nombres intégrés**

 Aspose.Cells propose des formats de nombres intégrés pour configurer les formats d'affichage des nombres et des dates. Tous les formats de nombres intégrés reçoivent des valeurs numériques uniques. Les développeurs peuvent attribuer n'importe quelle valeur numérique souhaitée au[**Nombre**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) méthode du[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) objet pour appliquer le format d’affichage. Cette approche est rapide. Les formats de nombres intégrés pris en charge par Aspose.Cells sont répertoriés ci-dessous.

|**Valeur**|**Taper**|**Formater la chaîne**|
| :- | :- | :- |
|0|General|Général|
|1|Decimal|0|
|2|Decimal|0.00|
|3|Decimal|# ,##0
|
|4|Decimal|# ,##0.00
|
|5|Currency|$#,##0;$-#,##0|
|6|Currency|$#,##0;[Rouge]$-#,##0|
|7|Currency|$#,##0.00;$-#,##0.00|
|8|Currency|$#,##0.00;[Rouge]$-#,##0.00|
|9|Percentage|0%|
|10|Percentage|0.00%|
|11|Scientific|0.00E+00|
|12|Fraction|#  ?/?
|
|13|Fraction|#  */*
|
|14|Date|m/j/aaaa|
|15|Date|j-mmm-aa|
|16|Date|d-mmm|
|17|Date|mmm-aa|
|18|Time|h:mm AM/PM|
|19|Time|h:mm:ss AM/PM|
|20|Time|Hmm|
|21|Time|h:mm:ss|
|22|Time|m/j/aa h:mm|
|37|Currency|# ,##0;-#,##0
|
|38|Currency|# ,##0;[Rouge]-#,##0
|
|39|Currency|# ,##0.00;-#,##0.00
|
|40|Currency|# ,##0.00;[Rouge]-#,##0.00
|
|41|Accounting|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Accounting|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Accounting|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Accounting|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Time|mm:ss|
|46|Time|h :mm:ss|
|47|Time|mm:ss.0|
|48|Scientific|## 0.0E+00
|
|49|Text|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

##  **Utilisation de formats de nombres personnalisés**

 Pour définir votre propre chaîne de format personnalisée pour définir le format d'affichage, utilisez l'option[**Coutume**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Cette approche n'est pas aussi rapide que l'utilisation de formats prédéfinis, mais elle est plus flexible.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Si vous utilisez le[**Coutume**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) pour définir le format numérique, tout format précédent défini à l'aide de la touche[**Nombre**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Spécifier des séparateurs décimaux et de groupe de nombres personnalisés pour le classeur](/cells/fr/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Spécification du formatage du modèle personnalisé DBNum](/cells/fr/java/specifying-dbnum-custom-pattern-formatting/)
