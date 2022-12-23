---
title: Rechercher ou rechercher des données
type: docs
weight: 120
url: /fr/java/find-or-search-data/
---
{{% alert color="primary" %}} 

 Dans Microsoft Excel, les utilisateurs peuvent rechercher des cellules contenant des données spécifiques. Par exemple, en cliquant**Éditer** et puis**Trouver** ouvre la boîte de dialogue Rechercher. Les utilisateurs entrent une valeur et cliquent**D'ACCORD** pour le chercher. Excel met en évidence les champs correspondants.

**Utilisation de la boîte de dialogue Rechercher pour rechercher des cellules contenant une valeur spécifique** 

![tâche : image_autre_texte](find-or-search-data_1.png)

Dans cet exemple, la valeur de recherche est "Oranges".

Aspose.Cells permet aux développeurs de rechercher dans les cellules d'une feuille de calcul pour trouver celles qui contiennent une valeur donnée.

{{% /alert %}} 
## **Recherche de Cells contenant des données spécifiques**
 Aspose.Cells fournit une classe,[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) , qui représente un fichier Excel. Le[Cahier](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) la classe contient[WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) , une collection qui permet d'accéder à chacune des feuilles de calcul du fichier Excel. Une feuille de calcul est représentée par le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)classe.

 Le[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) la classe fournit[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) , une collection qui représente toutes les cellules de la feuille de calcul.[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)collection fournit plusieurs méthodes pour rechercher des cellules dans une feuille de calcul contenant des données spécifiées par l'utilisateur. Quelques-unes de ces méthodes sont décrites ci-dessous plus en détail.

Toutes les méthodes de recherche renvoient les références de cellule pour toutes les cellules contenant la valeur de recherche spécifiée.
## **Recherche contenant une formule**
 Les développeurs peuvent trouver une formule spécifiée dans la feuille de calcul en appelant le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[trouver](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\) ), en définissant la[FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) à[LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS)et en le passant comme paramètre au[trouver](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) méthode.

 Typiquement, le[trouver](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) accepte deux paramètres ou plus :

- Objet à rechercher : représente un objet à rechercher dans la feuille de calcul.
- Le précédent Cell : représente la cellule précédente avec la même formule. Ce paramètre peut être défini sur null lors de la recherche depuis le début.
- Options de recherche : représente les critères de recherche. Dans les exemples ci-dessous, les données de feuille de calcul suivantes sont utilisées pour pratiquer les méthodes de recherche :

**Exemple de données de feuille de calcul** 

![tâche : image_autre_texte](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Recherche de chaînes**
La recherche de cellules contenant une valeur de chaîne est simple et flexible. Il existe différentes manières de rechercher, par exemple, rechercher des cellules contenant des chaînes commençant par un caractère particulier ou un ensemble de caractères.
### **Recherche de chaînes commençant par des caractères spécifiques**
 Pour rechercher le premier caractère d'une chaîne, appelez le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[trouver](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)), définissez la méthode[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) à[LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH)et le passer en paramètre au[trouver](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Recherche de chaînes se terminant par des caractères spécifiques**
 Aspose.Cells peut également trouver des chaînes qui se terminent par des caractères spécifiques. Pour rechercher les derniers caractères d'une chaîne, appelez le[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection[trouver](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)), définissez la méthode[FindOptions.setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) à[LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH)et le passer en paramètre au[trouver](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) méthode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Recherche avec des expressions régulières : la fonctionnalité RegEx**
Une expression régulière fournit un moyen concis et flexible de faire correspondre (spécifier et reconnaître) des chaînes de texte, telles que des caractères, des mots ou des modèles particuliers.

Par exemple, le modèle d'expression régulière abc-* ~~xyz~~ correspond aux chaînes "abc-123-xyz", "abc-985-xyz" et "abc-pony-xyz".* est un caractère générique afin que le modèle corresponde à toutes les chaînes commençant par "abc" et se terminant par "-xyz", quels que soient les caractères au milieu.

Aspose.Cells vous permet de rechercher avec des expressions régulières.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Sujets avancés**
- [Trouver des cellules avec un style spécifique](/cells/fr/java/find-cells-with-specific-style/)
- [Rechercher des données à l'aide des valeurs d'origine](/cells/fr/java/search-data-using-original-values/)
