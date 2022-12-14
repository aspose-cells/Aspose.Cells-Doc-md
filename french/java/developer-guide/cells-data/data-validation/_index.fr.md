---
title: La validation des données
type: docs
weight: 70
url: /fr/java/data-validation/
---
{{% alert color="primary" %}} 

Microsoft Excel fournit de bonnes fonctionnalités pour filtrer automatiquement ou valider les données de la feuille de calcul.

[La validation des données](/cells/fr/java/data-validation/) est la possibilité de définir des règles relatives aux données saisies sur une feuille de calcul. Par exemple, utilisez la validation pour vous assurer qu'une colonne intitulée DATE ne contient que des dates ou qu'une autre colonne ne contient que des nombres. Vous pouvez même vous assurer qu'une colonne intitulée DATE ne contient que des dates comprises dans une certaine plage. Avec la validation des données, vous pouvez contrôler ce qui est entré dans les cellules de la feuille de calcul. Aspose.Cells prend entièrement en charge les fonctions de validation et de filtrage automatique des données d'Excel Microsoft. Cet article explique comment utiliser les fonctionnalités dans Microsoft Excel et comment les coder à l'aide de Aspose.Cells.

{{% /alert %}} 
## **Types de validation des données et exécution**
Microsoft Excel prend en charge un certain nombre de différents types de validation de données. Chaque type est utilisé pour contrôler le type de données saisies dans une cellule ou une plage de cellules. Ci-dessous, des extraits de code illustrent comment valider cela :

- [Les nombres sont entiers](/cells/fr/java/data-validation/)c'est-à-dire qu'ils n'ont pas de partie décimale.
- [Les nombres décimaux suivent la bonne structure](/cells/fr/java/data-validation/). L'exemple de code définit qu'une plage de cellules doit avoir deux espaces décimaux.
- [Les valeurs sont limitées à une liste de valeurs](/cells/fr/java/data-validation/). La validation de liste définit une liste distincte de valeurs qui peuvent être appliquées à une cellule ou à une plage de cellules.
- [Les dates se situent dans une plage spécifique](/cells/fr/java/data-validation/).
- [Le temps est dans une plage spécifique](/cells/fr/java/data-validation/).
- [Un texte est dans une longueur de caractère donnée](/cells/fr/java/data-validation/).
### **Validation des données avec Microsoft Excel**
Pour créer des validations à l'aide de Microsoft Excel :

1. Dans une feuille de calcul, sélectionnez les cellules auxquelles vous souhaitez appliquer la validation.
1. Du**Données**menu, sélectionnez**Validation**.
 La boîte de dialogue de validation s'affiche.
1. Clique le**Réglages**et entrez les paramètres comme indiqué ci-dessous.

   **Paramètres de validation des données** 

![tâche : image_autre_texte](data-validation_1.png)
### **Validation des données avec Aspose.Cells**
La validation des données est une fonctionnalité puissante pour valider les informations saisies dans les feuilles de calcul. Avec la validation des données, les développeurs peuvent fournir aux utilisateurs une liste de choix, limiter les entrées de données à un type ou une taille spécifique, etc.
 Au Aspose.Cells, chaque[Feuille de travail](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)la classe a un[Validations](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Validations)objet qui représente une collection de[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)objets. Pour configurer la validation, définissez certaines des[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)propriétés de la classe :

- [Taper](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Type): représente le type de validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies dans le[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)énumération.
- [Opérateur](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Operator): représente l'opérateur à utiliser dans la validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies dans le[Type d'opérateur](https://reference.aspose.com/cells/java/com.aspose.cells/OperatorType)énumération.
- [Formule 1](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula1): représente la valeur ou l'expression associée à la première partie de la validation des données.
- [Formule2](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#Formula2): représente la valeur ou l'expression associée à la deuxième partie de la validation des données.

Quand le[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation)les propriétés de l'objet ont été configurées, les développeurs peuvent utiliser le[ZoneCellule](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)structure pour stocker des informations sur la plage de cellules qui seront validées à l'aide de la validation créée.
#### **Types de validation des données**
La validation des données vous permet de créer des règles métier dans chaque cellule afin que des entrées incorrectes entraînent des messages d'erreur. Les règles métier sont les politiques et procédures qui régissent le fonctionnement d'une entreprise. Aspose.Cells prend en charge tous les types importants de validation de données.

La[ValidationType](https://reference.aspose.com/cells/java/com.aspose.cells/ValidationType)énumération a les membres suivants :

|**Nom de membre**|**La description**|
|:- |:- |
|[DE N'IMPORTE QUELLE VALEUR](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#ANY_VALUE)|Indique une valeur de n'importe quel type.|
|[NOMBRE ENTIER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)|Indique le type de validation pour les nombres entiers.|
|[DÉCIMAL](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DECIMAL)|Indique le type de validation pour les nombres décimaux.|
|[LISTE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#LIST)|Indique le type de validation pour la liste déroulante.|
|[DATE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#DATE)|Indique le type de validation des dates.|
|[TEMPS](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TIME)|Indique le type de validation pour Time.|
|[TEXT_LENGTH](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#TEXT_LENGTH)|Indique le type de validation pour la longueur du texte.|
|[DOUANE](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#CUSTOM)|Indique le type de validation personnalisé.|
#### **Exemple de programmation : validation des données de nombres entiers**
Avec ce type de validation, les utilisateurs ne peuvent entrer que des nombres entiers dans une plage spécifiée dans les cellules validées. Les exemples de code qui suivent montrent comment implémenter le[NOMBRE ENTIER](https://reference.aspose.com/cells/java/com.aspose.cells/Validationtype#WHOLE_NUMBER)type de validation. L'exemple crée la même validation de données en utilisant Aspose.Cells que nous avons créée en utilisant Microsoft Excel ci-dessus.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-WholeNumberDataValidation-WholeNumberDataValidation.java" >}}



#### **Exemple de programmation : validation des données décimales**
Avec ce type de validation, l'utilisateur peut entrer des nombres décimaux dans les cellules validées. Dans l'exemple, l'utilisateur est limité à la saisie de valeurs décimales uniquement et la zone de validation est A1:A10.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DecimalDataValidation-DecimalDataValidation.java" >}}



#### **Exemple de programmation : Validation des données de liste**
Ce type de validation permet à l'utilisateur de saisir des valeurs à partir d'une liste déroulante. Il fournit une liste : une série de lignes contenant des données. Les utilisateurs ne peuvent sélectionner que des valeurs dans la liste. La zone de validation est la plage de cellules A1:A5 dans la première feuille de calcul.

Il est important ici que vous définissiez[Validation.setInCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) propriété à**vrai**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-ListDataValidation-ListDataValidation.java" >}}



#### **Exemple de programmation : validation des données de date**
Avec ce type de validation, les utilisateurs entrent des valeurs de date dans une plage spécifiée ou répondant à des critères spécifiques dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des dates entre 1970 et 1999. Ici, la zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-DateDataValidation-DateDataValidation.java" >}}



#### **Exemples de programmation : validation des données temporelles**
Avec ce type de validation, les utilisateurs peuvent entrer des heures dans une plage spécifiée ou répondant à certains critères dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des heures entre 09h00 et 11h30. Ici, la zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TimeDataValidation-TimeDataValidation.java" >}}



#### **Exemples de programmation : validation des données de longueur de texte**
Avec ce type de validation, les utilisateurs peuvent entrer des valeurs de texte d'une longueur spécifiée dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des valeurs de chaîne ne dépassant pas 5 caractères. La zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-TextLengthDataValidation-TextLengthDataValidation.java" >}}
## **Règles de validation des données**
Lorsque les validations de données sont mises en œuvre, la validation peut être vérifiée en attribuant différentes valeurs dans les cellules.[Cell.GetValidationValue()](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidationValue\(\)) peut être utilisé pour récupérer le résultat de la validation. L'exemple suivant illustre cette fonctionnalité avec différentes valeurs. Le fichier d'exemple peut être téléchargé à partir du lien suivant pour le test :

[SampleDataValidationRules.xlsx](77987849.xlsx)

**Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-VerifyCellValueSatisfiesDataValidationRules-1.java" >}}
## **Vérifier si la validation dans une cellule est déroulante**
 Comme nous l'avons vu, il existe de nombreux types de validations qui peuvent être mises en œuvre au sein d'une cellule. Si vous voulez vérifier si la validation est déroulante ou non,[Validation.InCellDropDown](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#InCellDropDown) propriété peut être utilisée pour tester cela. L'exemple de code suivant illustre l'utilisation de cette propriété. Le fichier d'exemple pour les tests peut être téléchargé à partir du lien suivant :

[sampleDataValidationRules.xlsx](77987849.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-CheckIfValidationInCellDropDown-1.java" >}}
## **Ajouter CellArea à la validation existante**
Il peut y avoir des cas où vous voudrez peut-être ajouter[ZoneCellule](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)à l'existant[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation). Lorsque vous ajoutez[ZoneCellule](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)utilisant[Validation.AddArea(CellArea cellArea)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea\)), Aspose.Cells vérifie toutes les zones existantes pour voir si la nouvelle zone existe déjà. Si le fichier a un grand nombre de validations, cela affecte les performances. Pour surmonter cela, le API fournit le[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) méthode. La*checkIntersection*Le paramètre indique s'il faut vérifier l'intersection d'une zone donnée avec des zones de validation existantes. Le mettre à**faux**désactivera la vérification des autres zones. La*checkEdge*Le paramètre indique s'il faut vérifier les zones appliquées. Si la nouvelle zone devient la zone supérieure gauche, les paramètres internes sont reconstruits. Si vous êtes sûr que la nouvelle zone n'est pas la zone en haut à gauche, vous pouvez définir ce paramètre comme**faux**.

L'extrait de code suivant illustre l'utilisation de[Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)](https://reference.aspose.com/cells/java/com.aspose.cells/Validation#addArea\(com.aspose.cells.CellArea,%20boolean,%20boolean\)) méthode pour ajouter de nouveaux[ZoneCellule](https://reference.aspose.com/cells/java/com.aspose.cells/CellArea)à l'existant[Validation](https://reference.aspose.com/cells/java/com.aspose.cells/Validation).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-AddValidationArea-1.java" >}}

Les fichiers Excel source et de sortie sont joints pour référence.

[Fichier source](PivotTableHideAndSortSample.xlsx)

[Fichier de sortie](ValidationsSample_out.xlsx)


## **Sujets avancés**
- [Obtenir la validation Cell dans les fichiers ODS](/cells/fr/java/get-cell-validation-in-ods-files/)
- [Obtenez la validation appliquée sur un Cell](/cells/fr/java/get-validation-applied-on-a-cell/)
- [Vérifiez que la valeur Cell satisfait aux règles de validation des données](/cells/fr/java/verify-that-cell-value-satisfies-data-validation-rules/)
