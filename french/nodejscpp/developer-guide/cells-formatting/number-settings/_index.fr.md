---  
title: Paramètres de nombre
linktitle: Paramètres de nombre  
description: Aspose.Cells est une bibliothèque Node.js pour travailler avec des fichiers de tableur qui prend en charge de nombreux paramètres différents de numérotation des cellules. Cet article explique comment utiliser la bibliothèque Aspose.Cells pour gérer les paramètres numériques des cellules afin d ajuster les formats de nombres dans les feuilles de calcul.  
keywords: Aspose.Cells, bibliothèque Node.js, tableur électronique, paramètres de numérotation des cellules, mise en forme, gestion, formats de nombres et de dates  
type: docs  
weight: 10  
url: /fr/nodejs-cpp/cells-number-settings/  
---  

## **Comment définir les formats d'affichage des nombres et des dates**  

Une caractéristique très puissante de Microsoft Excel est qu'il permet aux utilisateurs de définir les formats d'affichage des valeurs numériques et des dates. Nous savons que les données numériques peuvent représenter différentes valeurs, notamment décimales, monnaies, pourcentages, fractions ou valeurs comptables, etc. Toutes ces valeurs numériques s'affichent dans des formats différents en fonction du type d'information qu'elles représentent. De même, il existe de nombreux formats dans lesquels une date ou une heure peut être affichée.  
Aspose.Cells prend en charge cette fonctionnalité et permet aux développeurs de définir tout format d'affichage pour un nombre ou une date.  

### **Comment définir les formats d'affichage dans Microsoft Excel**  

Pour définir les formats d'affichage dans Microsoft Excel:  

1. Cliquez avec le bouton droit sur n'importe quelle cellule.  
2. Sélectionnez **Format des cellules**. Une boîte de dialogue s'affichera, permettant de définir les formats d'affichage de tout type de valeur.  

Sur le côté gauche de la boîte de dialogue, il y a de nombreuses catégories de valeurs telles que **Général**, **Nombre**, **Devise**, **Comptabilité**, **Date**, **Heure**, **Pourcentage**, etc. Aspose.Cells prend en charge tous ces formats d'affichage.  

Aspose.Cells fournit un module, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) qui représente un fichier Excel. Le module [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le module [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). Le module [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) offre une collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--). Chaque élément dans la collection [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) représente un objet du module [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell).  

Aspose.Cells fournit des méthodes [**getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getstyle--) et [**setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) pour le module [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Ces méthodes permettent d'obtenir et de définir la mise en forme d'une cellule. Le module [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) propose quelques propriétés utiles pour gérer les formats d’affichage des nombres et des dates.  

### **Comment Utiliser les Formats de Nombre Intégrés**  

Aspose.Cells propose certains formats de nombres intégrés pour configurer les formats d’affichage des nombres et des dates. Ces formats de nombres intégrés peuvent être appliqués en utilisant la méthode [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Tous les formats de nombres intégrés sont attribués de valeurs numériques uniques. Les développeurs peuvent attribuer n'importe quelle valeur numérique désirée à la méthode [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) pour appliquer le format d'affichage. Cette approche est rapide. Les formats de nombres intégrés supportés par Aspose.Cells sont listés ci-dessous.  

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
|46|Time|h:mm:ss|  
|47|Time|mm:ss.0|  
|48|Scientific|##0.0E+00|  
|49|Text|@|  


{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


### **Comment Utiliser les Formats de Nombre Personnalisés**  

Pour définir votre propre chaîne de format personnalisée pour le format d'affichage, utilisez la méthode [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) de l'objet [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style). Cette approche n'est pas aussi rapide que l'utilisation de formats préétablis, mais elle est plus flexible.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-NumberSetting-HowToUseBuiltInNumberFormats.js" >}}


{{% alert color="primary" %}}  

Si vous utilisez la méthode [**setCustom(string)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setCustom-string-) pour définir le format numérique, tout format précédent défini avec la méthode [**setNumber(number)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setNumber-number-) est écrasé, et inversement.  

{{% /alert %}}  

## **Sujets avancés**  
- [Vérifier le format personnalisé du nombre lors de la définition de la propriété de style personnalisé](/cells/fr/nodejs-cpp/check-custom-number-format-when-setting-style-custom-property/)  
- [Liste des Formats de Nombre Supportés](/cells/fr/nodejs-cpp/list-of-supported-number-formats/)  
- [Rendre le modèle de format de date personnalisé g et ge mm dd](/cells/fr/nodejs-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/)  
- [Spécifier les séparateurs de décimales et de groupe personnalisés pour le classeur](/cells/fr/nodejs-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/)  
- [Spécifier la mise en forme du modèle personnalisé DBNum](/cells/fr/nodejs-cpp/specifying-dbnum-custom-pattern-formatting/)  
