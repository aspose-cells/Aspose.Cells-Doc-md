---
title: Paramètres du numéro
type: docs
weight: 10
url: /fr/net/cells-number-settings/
---
## **Définition des formats d'affichage de Numbers et des dates**

Une caractéristique très forte de Microsoft Excel est qu'il permet aux utilisateurs de définir les formats d'affichage des valeurs numériques et des dates. Nous savons que les données numériques peuvent être utilisées pour représenter différentes valeurs, notamment des valeurs décimales, monétaires, de pourcentage, de fraction ou comptables, etc. Toutes ces valeurs numériques sont affichées dans différents formats en fonction du type d'informations qu'elles représentent. De même, il existe de nombreux formats dans lesquels une date ou une heure peut être affichée.
Aspose.Cells prend en charge cette fonctionnalité et permet aux développeurs de définir n'importe quel format d'affichage pour un nombre ou une date.

### **Définition des formats d'affichage dans Microsoft Excel**

Pour définir les formats d'affichage dans Microsoft Excel :

1. Cliquez avec le bouton droit sur n'importe quelle cellule.
1.  Sélectionner**Format Cells**. Une boîte de dialogue apparaîtra qui est utilisée pour définir les formats d'affichage de tout type de valeur.

 Dans la partie gauche de la boîte de dialogue, il existe de nombreuses catégories de valeurs telles que**Général**, **Nombre**, **Devise**, **Comptabilité**, **Date**, **Temps**, **Pourcentage,**etc. Aspose.Cells prend en charge tous ces formats d'affichage.

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell)classe.

 Aspose.Cells fournit[**ObtenirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getstyle) et[**DéfinirStyle**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setstyle) méthodes pour la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe. Ces méthodes sont utilisées pour obtenir et définir la mise en forme d'une cellule. Le[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)fournit des propriétés utiles pour gérer les formats d'affichage des nombres et des dates.

### **Utilisation des formats numériques intégrés**

 Aspose.Cells propose des formats de nombres intégrés pour configurer les formats d'affichage des nombres et des dates. Ces formats numériques intégrés peuvent être appliqués à l'aide de la[**Nombre**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) propriété de la[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objet. Tous les formats numériques intégrés reçoivent des valeurs numériques uniques. Les développeurs peuvent attribuer n'importe quelle valeur numérique souhaitée au[**Nombre**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number) propriété de la[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)objet pour appliquer le format d'affichage. Cette approche est rapide. Les formats numériques intégrés pris en charge par Aspose.Cells sont répertoriés ci-dessous.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingBuiltInNumberFormats-1.cs" >}}

### **Utilisation de formats numériques personnalisés**

Pour définir votre propre chaîne de format personnalisée pour définir le format d'affichage, utilisez la[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) objets[**Personnalisé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom)la propriété. Cette approche n'est pas aussi rapide que l'utilisation de formats prédéfinis, mais elle est plus flexible.


{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-SettingDisplayFormats-UsingCustomNumber-1.cs" >}}

{{% alert color="primary" %}}

 Si vous utilisez le[**Personnalisé**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/custom) propriété pour définir le format numérique, tout format précédent défini à l'aide de la[**Nombre**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/number)propriété est remplacée et vice versa.

{{% /alert %}}

## **Sujets avancés**
- [Vérifier le format numérique personnalisé lors de la définition de la propriété Style.Custom](/cells/fr/net/check-custom-number-format-when-setting-style-custom-property/)
- [Liste des formats de nombre pris en charge](/cells/fr/net/list-of-supported-number-formats/)
- [Modèle de format de date personnalisé de rendu g et ge mm jj](/cells/fr/net/render-custom-date-format-pattern-g-and-ge-mm-dd/)
- [Spécifier des séparateurs décimaux et de groupe personnalisés pour le classeur](/cells/fr/net/specify-custom-number-decimal-and-group-separators-for-workbook/)
- [Spécification du format de modèle personnalisé DBNum](/cells/fr/net/specifying-dbnum-custom-pattern-formatting/)
