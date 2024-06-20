---
title: Trouver ou rechercher des données
type: docs
weight: 120
url: /fr/java/find-or-search-data/
---

{{% alert color="primary" %}} 

Dans Microsoft Excel, les utilisateurs peuvent rechercher des cellules contenant des données spécifiques. Par exemple, en cliquant sur **Modifier** puis sur **Rechercher**, la boîte de dialogue de recherche s'ouvre. Les utilisateurs saisissent une valeur et cliquent sur **OK** pour la rechercher. Excel surligne les champs correspondants.

**Utilisation de la boîte de dialogue Rechercher pour trouver des cellules contenant une valeur spécifique** 

![todo:image_alt_text](find-or-search-data_1.png)

Dans cet exemple, la valeur de recherche est "Oranges".

Aspose.Cells permet aux développeurs de rechercher dans les cellules d'une feuille de calcul afin de trouver celles qui contiennent une valeur donnée.

{{% /alert %}} 
## **Trouver des cellules contenant des données spécifiques**
Aspose.Cells fournit une classe, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook), qui représente un fichier Excel. La classe [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) contient [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection), une collection qui permet d'accéder à chacune des feuilles de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet).

La classe [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) fournit [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), une collection qui représente toutes les cellules de la feuille de calcul. La collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) fournit plusieurs méthodes pour trouver des cellules dans une feuille de calcul contenant des données spécifiées par l'utilisateur. Quelques-unes de ces méthodes sont discutées ci-dessous en détail.

Toutes les méthodes de recherche renvoient les références des cellules contenant la valeur de recherche spécifiée.
## **Recherche contenant une formule**
Les développeurs peuvent trouver une formule spécifiée dans la feuille de calcul en appelant la méthode [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) de la collection [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells), en définissant [FindOptions.setLookInType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookInType) à [LookInType.FORMULAS](https://reference.aspose.com/cells/java/com.aspose.cells/lookintype#FORMULAS) et en le passant en paramètre à la méthode [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)).

Généralement, la méthode [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)) accepte deux paramètres ou plus :

- Objet à rechercher : représente un objet qui doit être trouvé dans la feuille de calcul.
- La cellule précédente: représente la cellule précédente avec la même formule. Ce paramètre peut être défini sur null lors de la recherche depuis le début.
- Options de recherche: représente les critères de recherche. Dans les exemples ci-dessous, les données de la feuille de calcul suivante sont utilisées pour pratiquer les méthodes de recherche:

**Données d'exemple de la feuille de calcul** 

![todo:image_alt_text](find-or-search-data_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsContainingFormula-FindingCellsContainingFormula.java" >}}
## **Recherche de chaînes**
Rechercher des cellules contenant une valeur de chaîne est facile et flexible. Il existe différentes façons de rechercher, par exemple, recherche de cellules contenant des chaînes qui commencent par un caractère particulier ou un ensemble de caractères.
### **Recherche de chaînes qui commencent par des caractères spécifiques**
Pour rechercher le premier caractère dans une chaîne, appelez la méthode [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection, définissez la méthode [setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) à [LookAtType.START_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#START_WITH) et passez-la comme paramètre à la méthode [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsWithStringOrNumber-FindingCellsWithStringOrNumber.java" >}}
### **Recherche de chaînes se terminant par des caractères spécifiques**
Aspose.Cells peut également trouver des chaînes se terminant par des caractères spécifiques. Pour rechercher les derniers caractères dans une chaîne, appelez la méthode [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) de la collection, définissez la méthode [setLookAtType](https://reference.aspose.com/cells/java/com.aspose.cells/findoptions#LookAtType) à [LookAtType.END_WITH](https://reference.aspose.com/cells/java/com.aspose.cells/lookattype#END_WITH) et passez-la comme paramètre à la méthode [find](https://reference.aspose.com/cells/java/com.aspose.cells/cells#find\(java.lang.Object,%20com.aspose.cells.Cell\)).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingCellsEndWithSpecificCharacters-FindingCellsEndWithSpecificCharacters.java" >}}
## **Recherche avec expressions régulières: la fonctionnalité RegEx**
Une expression régulière fournit un moyen concis et flexible de faire correspondre (spécifier et reconnaître) des chaînes de texte, telles que des caractères, des mots ou des motifs particuliers.

Par exemple, le motif d'expression régulière abc-*~~xyz~~ correspond aux chaînes "abc-123-xyz", "abc-985-xyz" et "abc-pony-xyz". * est un caractère générique, donc le motif correspond à toutes les chaînes qui commencent par "abc" et se terminent par "-xyz", quelle que soit la nature des caractères présents entre les deux.

Aspose.Cells vous permet de rechercher avec des expressions régulières.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-FindingwithRegularExpressions-FindingwithRegularExpressions.java" >}}

## **Sujets avancés**
- [Trouver des cellules avec un style spécifique](/cells/fr/java/find-cells-with-specific-style/)
- [Rechercher des données en utilisant des valeurs originales](/cells/fr/java/search-data-using-original-values/)
