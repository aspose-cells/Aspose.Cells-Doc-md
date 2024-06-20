---
title: Validation de données
type: docs
weight: 70
url: /fr/java/data-validation/
---

{{% alert color="primary" %}} 

Microsoft Excel propose de bonnes fonctionnalités pour filtrer automatiquement ou valider les données de la feuille de calcul.

[Validation des données](/cells/fr/java/data-validation/) est la capacité de définir des règles concernant les données saisies sur une feuille de calcul. Par exemple, utilisez la validation pour garantir qu'une colonne libellée DATE ne contient que des dates, ou qu'une autre colonne ne contient que des nombres. Vous pourriez même vous assurer qu'une colonne libellée DATE ne contient que des dates dans une certaine plage. Avec la validation des données, vous pouvez contrôler ce qui est saisi dans les cellules de la feuille de calcul. Aspose.Cells prend en charge pleinement la validation des données de Microsoft Excel et les fonctionnalités de filtre automatique. Cet article explique comment utiliser les fonctionnalités dans Microsoft Excel et comment les coder en utilisant Aspose.Cells.

{{% /alert %}} 
## **Types de validation des données et exécution**
Microsoft Excel prend en charge plusieurs types de validation des données. Chaque type est utilisé pour contrôler le type de données entrées dans une cellule ou une plage de cellules. Ci-dessous, des extraits de code illustrent comment valider que:

- [Les numéros sont entiers](/cells/fr/java/data-validation/), c'est-à-dire qu'ils n'ont pas de partie décimale.
- [Les nombres décimaux suivent la bonne structure](/cells/fr/java/data-validation/). L'exemple de code définit qu'une plage de cellules doit avoir deux décimales.
- [Les valeurs sont restreintes à une liste de valeurs](/cells/fr/java/data-validation/). La validation de liste définit une liste distincte de valeurs qui peuvent être appliquées à une cellule ou une plage de cellules.
- [Les dates tombent dans une plage spécifique](/cells/fr/java/data-validation/).
- [Le temps se situe dans une plage spécifique](/cells/fr/java/data-validation/).
- [Un texte est dans une longueur de caractère donnée](/cells/fr/java/data-validation/).
### **Validation des données avec Microsoft Excel**
Pour créer des validations avec Microsoft Excel:

1. Dans une feuille de calcul, sélectionnez les cellules auxquelles vous voulez appliquer la validation.
1. Dans le menu **Données**, sélectionnez **Validation**.
   La boîte de dialogue de validation s'affiche.
1. Cliquez sur l'onglet **Paramètres** et saisissez les paramètres comme indiqué ci-dessous. 

   **Paramètres de validation des données** 

![todo:image_alt_text](data-validation_1.png)
### **Validation des données avec Aspose.Cells**
La validation des données est une fonctionnalité puissante pour valider les informations saisies dans les feuilles de calcul. Avec la validation des données, les développeurs peuvent fournir aux utilisateurs une liste de choix, restreindre les saisies de données à un type ou une taille spécifique, etc.
Dans Aspose.Cells, chaque [classe de feuille de calcul](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) a un objet [Validations](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations) qui représente une collection d'objets [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). Pour configurer la validation, définissez certaines des propriétés de la classe [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) :

- [Type](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type) : représente le type de validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies de l'énumération [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType).
- [Operator](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator) : représente l'opérateur à utiliser dans la validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies de l'énumération [OperatorType](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType).
- [Formula1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1) : représente la valeur ou l'expression associée à la première partie de la validation des données.
- [Formula2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2) : représente la valeur ou l'expression associée à la deuxième partie de la validation des données.

Lorsque les propriétés de l'objet [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) ont été configurées, les développeurs peuvent utiliser la structure [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) pour stocker des informations sur la plage de cellules qui sera validée en utilisant la validation créée.
#### **Types de validation des données**
La validation des données vous permet de créer des règles métier dans chaque cellule de sorte que les entrées incorrectes entraînent des messages d'erreur. Les règles métier sont les politiques et procédures qui régissent le fonctionnement d'une entreprise. Aspose.Cells prend en charge tous les types importants de validation des données.

L'énumération [ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType) comprend les membres suivants:

|**Nom du membre**|**Description**|
| :- | :- |
|[ANY_VALUE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Désigne une valeur de n'importe quel type.|
|[WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Désigne le type de validation pour les nombres entiers.|
|[DECIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Désigne le type de validation pour les nombres décimaux.|
|[LIST](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Désigne le type de validation pour une liste déroulante.|
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Désigne le type de validation pour les dates.|
|[TIME](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Désigne le type de validation pour l'heure.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Désigne le type de validation pour la longueur du texte.|
|[CUSTOM](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Désigne le type de validation personnalisée.|
#### **Exemple de programmation: Validation des données de nombres entiers**
Avec ce type de validation, les utilisateurs ne peuvent saisir que des nombres entiers dans une plage spécifiée dans les cellules validées. Les exemples de code suivants montrent comment implémenter le type de validation [WHOLE_NUMBER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER). L'exemple crée la même validation des données en utilisant Aspose.Cells que celle créée à l'aide de Microsoft Excel ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Exemple de programmation: Validation des données décimales**
Avec ce type de validation, l'utilisateur peut saisir des nombres décimaux dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir uniquement des valeurs décimales et la zone de validation est A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Exemple de programmation: Validation des données de liste**
Ce type de validation permet à l'utilisateur de saisir des valeurs à partir d'une liste déroulante. Il fournit une liste: une série de lignes contenant des données. Les utilisateurs peuvent uniquement sélectionner des valeurs dans la liste. La zone de validation est la plage de cellules A1:A5 dans la première feuille de calcul.

Il est important ici de définir la propriété [Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) sur **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Exemple de programmation : Validation des données de date**
Avec ce type de validation, les utilisateurs saisissent des valeurs de date dans une plage spécifiée, ou répondant à des critères spécifiques, dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des dates entre 1970 et 1999. Ici, la zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Exemples de programmation : Validation des données de l'heure**
Avec ce type de validation, les utilisateurs peuvent saisir des heures dans une plage spécifiée, ou répondant à certains critères, dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des heures entre 09h00 et 11h30. Ici, la zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Exemples de programmation : Validation de la longueur du texte**
Avec ce type de validation, les utilisateurs peuvent saisir des valeurs textuelles d'une longueur spécifiée dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des valeurs de chaîne ne dépassant pas 5 caractères. La zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Règles de validation des données**
Lorsque les validations des données sont implémentées, la validation peut être vérifiée en attribuant différentes valeurs aux cellules. [Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) peut être utilisé pour obtenir le résultat de validation. L'exemple suivant illustre cette fonctionnalité avec différentes valeurs. Le fichier d'exemple peut être téléchargé via le lien suivant pour les tests :

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Vérifier si la validation dans une cellule est un menu déroulant**
Comme nous l'avons vu, il existe de nombreux types de validations qui peuvent être implémentés dans une cellule. Si vous voulez vérifier si la validation est un menu déroulant ou non, la propriété [Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) peut être utilisée pour le tester. Le code d'exemple suivant illustre l'utilisation de cette propriété. Le fichier d'exemple pour les tests peut être téléchargé via le lien suivant :

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Ajouter une CellArea à une validation existante**
Il peut arriver que vous souhaitiez ajouter une [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) à une [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) existante. Lorsque vous ajoutez une [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) en utilisant [Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells vérifie toutes les zones existantes pour voir si la nouvelle zone existe déjà. Si le fichier contient un grand nombre de validations, cela affecte les performances. Pour surmonter cela, l'API fournit la méthode [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)). Le paramètre *checkIntersection* indique s'il faut vérifier l'intersection d'une zone donnée avec les zones de validation existantes. Le définir sur **false** désactive la vérification des autres zones. Le paramètre *checkEdge* indique s'il faut vérifier les zones appliquées. Si la nouvelle zone devient la zone en haut à gauche, les paramètres internes sont reconstruits. Si vous êtes sûr que la nouvelle zone n'est pas la zone en haut à gauche, vous pouvez définir ce paramètre sur **false**.

Le code suivant illustre l'utilisation de la méthode [Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) pour ajouter une nouvelle [CellArea](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea) à une [Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation) existante.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Les fichiers Excel source et de sortie sont joints pour référence.

[Fichier Source](PivotTableCacheEtTrierExemple.xlsx)

[Fichier de Sortie](ValidationsExemple_out.xlsx)


## **Sujets avancés**
- [Obtenir la validation de la cellule dans les fichiers ODS](/cells/fr/java/get-cell-validation-in-ods-files/)
- [Obtenir la validation appliquée sur une cellule](/cells/fr/java/get-validation-applied-on-a-cell/)
- [Vérifier que la valeur de la cellule satisfait aux règles de validation des données](/cells/fr/java/verify-that-cell-value-satisfies-data-validation-rules/)
