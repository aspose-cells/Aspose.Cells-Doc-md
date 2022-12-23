---
title: La validation des données
type: docs
weight: 90
url: /fr/net/data-validation/
---
{{% alert color="primary" %}}

Microsoft Excel fournit quelques bonnes fonctionnalités pour filtrer ou valider automatiquement les données de la feuille de calcul. Cet article explique comment utiliser les fonctionnalités dans Microsoft Excel et comment les coder à l'aide de Aspose.Cells.

{{% /alert %}}

## **Types de validation des données et exécution**

La validation des données est la possibilité de définir des règles relatives aux données saisies sur une feuille de calcul. Par exemple, utilisez la validation pour vous assurer qu'une colonne intitulée DATE ne contient que des dates ou qu'une autre colonne ne contient que des nombres. Vous pouvez même vous assurer qu'une colonne intitulée DATE ne contient que des dates comprises dans une certaine plage. Avec la validation des données, vous pouvez contrôler ce qui est entré dans les cellules de la feuille de calcul.

Microsoft Excel prend en charge un certain nombre de différents types de validation de données. Chaque type est utilisé pour contrôler le type de données saisies dans une cellule ou une plage de cellules. Ci-dessous, des extraits de code illustrent comment valider cela :

- Numbers sont entiers, c'est-à-dire qu'ils n'ont pas de partie décimale.
- Les nombres décimaux suivent la bonne structure. L'exemple de code définit qu'une plage de cellules doit avoir deux espaces décimaux.
- Les valeurs sont limitées à une liste de valeurs. La validation de liste définit une liste distincte de valeurs qui peuvent être appliquées à une cellule ou à une plage de cellules.
- Les dates se situent dans une plage spécifique.
- Une heure se situe dans une plage spécifique.
- Un texte est dans une longueur de caractère donnée.

### **Validation des données avec Microsoft Excel**

Pour créer des validations à l'aide de Microsoft Excel :

1. Dans une feuille de calcul, sélectionnez les cellules auxquelles vous souhaitez appliquer la validation.
1.  Du**Données** menu, sélectionnez**Validation**. La boîte de dialogue de validation s'affiche.
1.  Clique le**Réglages** onglet et entrez les paramètres.

### **Validation des données avec Aspose.Cells**

La validation des données est une fonctionnalité puissante pour valider les informations saisies dans les feuilles de calcul. Avec la validation des données, les développeurs peuvent fournir aux utilisateurs une liste de choix, limiter les entrées de données à un type ou une taille spécifique, etc.
 Au Aspose.Cells, chaque[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe a un[**Validations**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations)propriété qui représente un ensemble de[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) objets. Pour configurer la validation, définissez certaines des[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation)propriétés de la classe comme suit :

- Type – représente le type de validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies dans le[**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)énumération.
-  Opérateur – représente l'opérateur à utiliser dans la validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies dans le[**Type d'opérateur**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)énumération.
- Formula1 – représente la valeur ou l'expression associée à la première partie de la validation des données.
- Formula2 – représente la valeur ou l'expression associée à la deuxième partie de la validation des données.

 Quand le[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) les propriétés de l'objet ont été configurées, les développeurs peuvent utiliser le[**ZoneCellule**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)structure pour stocker des informations sur la plage de cellules qui seront validées à l'aide de la validation créée.

#### **Types de validation des données**

 Le[**ValidationType**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)énumération a les membres suivants :

|**Nom de membre**|**Description**|
|:- |:- |
|De n'importe quelle valeur|Indique une valeur de n'importe quel type.|
|Nombre entier|Indique le type de validation pour les nombres entiers.|
|Décimal|Indique le type de validation pour les nombres décimaux.|
|Lister|Indique le type de validation pour la liste déroulante.|
|Date|Indique le type de validation des dates.|
|Temps|Indique le type de validation pour le temps.|
|Longueur du texte|Indique le type de validation pour la longueur du texte.|
|Personnalisé|Indique le type de validation personnalisé.|

##### **Validation des données de nombre entier**

Avec ce type de validation, les utilisateurs ne peuvent entrer que des nombres entiers dans une plage spécifiée dans les cellules validées. Les exemples de code qui suivent montrent comment implémenter le type de validation WholeNumber. L'exemple crée la même validation de données en utilisant Aspose.Cells que nous avons créée en utilisant Microsoft Excel ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

##### **Validation des données de liste**

Ce type de validation permet à l'utilisateur de saisir des valeurs à partir d'une liste déroulante. Il fournit une liste : une série de lignes contenant des données. Dans l'exemple, une deuxième feuille de calcul est ajoutée pour contenir la source de la liste. Les utilisateurs ne peuvent sélectionner que des valeurs dans la liste. La zone de validation est la plage de cellules A1:A5 dans la première feuille de calcul.

 Il est important ici que vous définissiez[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) propriété à**vrai**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

##### **Validation des données de date**

Avec ce type de validation, les utilisateurs entrent des valeurs de date dans une plage spécifiée ou répondant à des critères spécifiques dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des dates entre 1970 et 1999. Ici, la zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

##### **Validation des données de temps**

Avec ce type de validation, les utilisateurs peuvent entrer des heures dans une plage spécifiée ou répondant à certains critères dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des heures entre 09h00 et 11h30. Ici, la zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

##### **Validation des données de longueur de texte**

Avec ce type de validation, les utilisateurs peuvent entrer des valeurs de texte d'une longueur spécifiée dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des valeurs de chaîne ne dépassant pas 5 caractères. La zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

### **Règles de validation des données**

Lorsque les validations de données sont mises en œuvre, la validation peut être vérifiée en attribuant différentes valeurs dans les cellules.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) peut être utilisé pour récupérer le résultat de la validation. L'exemple suivant illustre cette fonctionnalité avec différentes valeurs. Le fichier d'exemple peut être téléchargé à partir du lien suivant pour le test :

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

## **Vérifiez si la validation dans la cellule est déroulante**

 Comme nous l'avons vu, il existe de nombreux types de validations qui peuvent être mises en œuvre au sein d'une cellule. Si vous voulez vérifier si la validation est déroulante ou non,[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown) propriété peut être utilisée pour tester cela. L'exemple de code suivant illustre l'utilisation de cette propriété. Un exemple de fichier de test peut être téléchargé à partir du lien suivant :

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

## **Ajouter CellArea à la validation existante**

 Il peut y avoir des cas où vous voudrez peut-être ajouter[**ZoneCellule**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)à l'existant[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation). Lorsque vous ajoutez[**ZoneCellule**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) en utilisant[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells vérifie toutes les zones existantes pour voir si la nouvelle zone existe déjà. Si le fichier a un grand nombre de validations, cela affecte les performances. Pour surmonter cela, le API fournit le[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) méthode. Le*checkIntersection* Le paramètre indique s'il faut vérifier l'intersection d'une zone donnée avec des zones de validation existantes. Le mettre à**faux** désactivera la vérification des autres zones. Le*checkEdge* Le paramètre indique s'il faut vérifier les zones appliquées. Si la nouvelle zone devient la zone supérieure gauche, les paramètres internes sont reconstruits. Si vous êtes sûr que la nouvelle zone n'est pas la zone en haut à gauche, vous pouvez définir ce paramètre comme**faux**.

L'extrait de code suivant illustre l'utilisation de[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) méthode pour ajouter de nouveaux[**ZoneCellule**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)à l'existant[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Les fichiers Excel source et de sortie sont joints pour référence.

[Fichier source](96928093.xlsx)

[Fichier de sortie](96928220.xlsx)


## **Sujets avancés**
- [Obtenir la validation Cell dans les fichiers ODS](/cells/fr/net/get-cell-validation-in-ods-files/)
- [Obtenez la validation appliquée sur un Cell](/cells/fr/net/get-validation-applied-on-a-cell/)
- [Vérifiez que la valeur Cell satisfait aux règles de validation des données](/cells/fr/net/verify-that-cell-value-satisfies-data-validation-rules/)
