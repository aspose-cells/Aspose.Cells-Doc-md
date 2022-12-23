---
title: Paramètres du numéro
type: docs
weight: 10
url: /fr/java/cells-number-settings/
---
## **Définition des formats d'affichage de Numbers et des dates**

Une caractéristique très forte de Microsoft Excel est qu'il permet aux utilisateurs de définir les formats d'affichage des valeurs numériques et des dates. Nous savons que les données numériques peuvent être utilisées pour représenter différentes valeurs, notamment des valeurs décimales, monétaires, de pourcentage, de fraction ou comptables, etc. Toutes ces valeurs numériques sont affichées dans différents formats en fonction du type d'informations qu'elles représentent. De même, il existe de nombreux formats dans lesquels une date ou une heure peut être affichée.
Aspose.Cells prend en charge cette fonctionnalité et permet aux développeurs de définir n'importe quel format d'affichage pour un nombre ou une date.

## **Définition des formats d'affichage dans Microsoft Excel**

Pour définir les formats d'affichage dans Microsoft Excel :

1. Cliquez avec le bouton droit sur n'importe quelle cellule.
1.  Sélectionner**Format Cells**. Une boîte de dialogue apparaîtra qui est utilisée pour définir les formats d'affichage de tout type de valeur.

 Dans la partie gauche de la boîte de dialogue, il existe de nombreuses catégories de valeurs telles que**Général**, **Nombre**, **Devise**, **Comptabilité**, **Date**, **Temps**, **Pourcentage,**etc. Aspose.Cells prend en charge tous ces formats d'affichage.

## **Utilisation des formats numériques intégrés**

 Aspose.Cells propose des formats de nombres intégrés pour configurer les formats d'affichage des nombres et des dates. Tous les formats numériques intégrés reçoivent des valeurs numériques uniques. Les développeurs peuvent attribuer n'importe quelle valeur numérique souhaitée au[**Nombre**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number) méthode de la[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/style) objet pour appliquer le format d'affichage. Cette approche est rapide. Les formats numériques intégrés pris en charge par Aspose.Cells sont répertoriés ci-dessous.

|**Évaluer**|**Taper**|**Formater la chaîne**|
|:- |:- |:- |
|0|Général|Général|
|1|Décimal|0|
|2|Décimal|0.00|
|3|Décimal|# ,##0
|
|4|Décimal|# ,##0.00
|
|5|Devise|$#,##0;$-#,##0|
|6|Devise|$#,##0;[Rouge]$-#,##0|
|7|Devise|$#,##0.00;$-#,##0.00|
|8|Devise|$#,##0.00 ;[Rouge]$-#,##0.00|
|9|Pourcentage|0%|
|10|Pourcentage|0.00%|
|11|Scientifique|0.00E+00|
|12|Fraction|# ?/?
|
|13|Fraction|# */*
|
|14|Date|m/j/aa|
|15|Date|j-mmm-aa|
|16|Date|d-mmm|
|17|Date|mmm-aa|
|18|Temps|h:mm AM/PM|
|19|Temps|h:mm:ss AM/PM|
|20|Temps|hmm|
|21|Temps|h:mm:ss|
|22|Temps|j/j/aa h:mm|
|37|Devise|# ,##0;-#,##0
|
|38|Devise|# ,##0;[Rouge]-#,##0
|
|39|Devise|# ,##0.00;-#,##0.00
|
|40|Devise|# ,##0.00;[Rouge]-#,##0.00
|
|41|Comptabilité|_ * #,##0_ ;_ * "_ ;_ @_|
|42|Comptabilité|_ $* #,##0_ ;_ $* "_ ;_ @_|
|43|Comptabilité|_ * #,##0.00_ ;_ * "??_ ;_ @_|
|44|Comptabilité|_ $* #,##0.00_ ;_ $* "??_ ;_ @_|
|45|Temps|mm:ss|
|46|Temps|h :mm:ss|
|47|Temps|mm:ss.0|
|48|Scientifique|## 0.0E+00
|
|49|Texte|@|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingBuiltInNumberFormats-1.java" >}}

## **Utilisation de formats numériques personnalisés**

Pour définir votre propre chaîne de format personnalisée pour définir le format d'affichage, utilisez la[**Personnalisé**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom). Cette approche n'est pas aussi rapide que l'utilisation de formats prédéfinis, mais elle est plus flexible.


{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "UsingCustomNumber-1.java" >}}

{{% alert color="primary" %}}

 Si vous utilisez le[**Personnalisé**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) pour définir le format des nombres, tout format précédent défini à l'aide de[**Nombre**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Number） is overridden and vice versa.

{{% /alert %}}

## **Advance topics**
- [Check Custom Number Format when Setting Style.Custom Property](/cells/java/check-custom-number-format-when-setting-style-custom-property/)
- [Spécifier des séparateurs décimaux et de groupe personnalisés pour le classeur](/cells/fr/java/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Spécification du format de modèle personnalisé DBNum](/cells/fr/java/specifying-dbnum-custom-pattern-formatting/)
