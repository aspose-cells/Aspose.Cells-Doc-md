---
title: La validation des données
type: docs
weight: 90
url: /fr/net/data-validation/
description: Découvrez comment ajouter la validation des données via le Aspose.Cells for .NET API.
keywords: Add Data Validation, Get Validation Value, Add Whole Number Data Validation, Add List Data Validation, Add Date Data Validation, Add Time Data Validation, Add Text Length Data Validation, Add CellArea to existing Validation, Check if validation in cell is dropdown, Add Custom Valication  
---
{{% alert color="primary" %}}

Microsoft Excel fournit de bonnes fonctionnalités pour filtrer ou valider automatiquement les données d'une feuille de calcul. Aspose.Cells prend entièrement en charge les fonctionnalités de validation des données et de filtrage automatique d'Excel Microsoft. Cet article explique comment utiliser les fonctionnalités de Microsoft Excel et comment les coder à l'aide de Aspose.Cells.

{{% /alert %}}

##  **Types de validation des données et exécution**

La validation des données est la possibilité de définir des règles relatives aux données saisies sur une feuille de calcul. Par exemple, utilisez la validation pour vous assurer qu'une colonne intitulée DATE contient uniquement des dates ou qu'une autre colonne ne contient que des nombres. Vous pouvez même vous assurer qu'une colonne intitulée DATE contient uniquement des dates comprises dans une certaine plage. Avec la validation des données, vous pouvez contrôler ce qui est saisi dans les cellules de la feuille de calcul.

Microsoft Excel prend en charge différents types de validation de données. Chaque type est utilisé pour contrôler le type de données saisies dans une cellule ou une plage de cellules. Ci-dessous, des extraits de code illustrent comment valider cela :

- Numbers sont entiers, c'est-à-dire qu'ils n'ont pas de partie décimale.
- Les nombres décimaux suivent la bonne structure. L'exemple de code définit qu'une plage de cellules doit comporter deux espaces décimaux.
- Les valeurs sont limitées à une liste de valeurs. La validation de liste définit une liste distincte de valeurs pouvant être appliquées à une cellule ou à une plage de cellules.
- Les dates se situent dans une plage spécifique.
- Une heure se situe dans une plage spécifique.
- Un texte ne dépasse pas une longueur de caractères donnée.

###  **Validation des données avec Microsoft Excel**

Pour créer des validations à l'aide d'Excel Microsoft :

1. Dans une feuille de calcul, sélectionnez les cellules auxquelles vous souhaitez appliquer la validation.
1.  Du**Données** menu, sélectionnez *Validation**. La boîte de dialogue de validation s'affichera.
1.  Clique le**Paramètres** et entrez les paramètres.

###  **Validation des données avec Aspose.Cells**

La validation des données est une fonctionnalité puissante pour valider les informations saisies dans les feuilles de calcul. Avec la validation des données, les développeurs peuvent fournir aux utilisateurs une liste de choix, restreindre les entrées de données à un type ou une taille spécifique, etc.
 Au Aspose.Cells, chacun[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la classe a un[**Validations**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/validations) propriété qui représente un ensemble de[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) objets. Pour configurer la validation, définissez certains des[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation)propriétés de la classe comme suit :

- Type – représente le type de validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies dans le[**Type de validation**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)énumération.
-  Opérateur – représente l'opérateur à utiliser dans la validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies dans le[**Type d'opérateur**](https://reference.aspose.com/cells/net/aspose.cells/operatortype)énumération.
- Formule1 – représente la valeur ou l'expression associée à la première partie de la validation des données.
- Formule2 – représente la valeur ou l'expression associée à la deuxième partie de la validation des données.

 Quand le[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation) les propriétés de l'objet ont été configurées, les développeurs peuvent utiliser le[**ZoneCellule**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)structure pour stocker des informations sur la plage de cellules qui sera validée à l’aide de la validation créée.

####  **Types de validation des données**

 Le[**Type de validation**](https://reference.aspose.com/cells/net/aspose.cells/validationtype)L'énumération comprend les membres suivants :

|**Nom de membre**|**Description**|
| :- | :- |
|De n'importe quelle valeur|Désigne une valeur de n’importe quel type.|
|Nombre entier|Désigne le type de validation pour les nombres entiers.|
|Décimal|Désigne le type de validation pour les nombres décimaux.|
|Liste|Indique le type de validation pour la liste déroulante.|
|Date|Désigne le type de validation pour les dates.|
|Temps|Désigne le type de validation pour l’heure.|
|Longueur du texte|Désigne le type de validation pour la longueur du texte.|
|Coutume|Désigne un type de validation personnalisé.|

#####  **Validation des données en nombres entiers**

Avec ce type de validation, les utilisateurs peuvent saisir uniquement des nombres entiers compris dans une plage spécifiée dans les cellules validées. Les exemples de code qui suivent montrent comment implémenter le type de validation WholeNumber. L'exemple crée la même validation de données en utilisant Aspose.Cells que celle que nous avons créée en utilisant Microsoft Excel ci-dessus.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-WholeNumberDataValidation-1.cs" >}}

#####  **Validation des données de liste**

Ce type de validation permet à l'utilisateur de saisir des valeurs dans une liste déroulante. Il fournit une liste : une série de lignes contenant des données. Dans l'exemple, une deuxième feuille de calcul est ajoutée pour contenir la source de la liste. Les utilisateurs peuvent uniquement sélectionner des valeurs dans la liste. La zone de validation est la plage de cellules A1:A5 dans la première feuille de calcul.

 Il est important ici de définir le[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)propriété à *true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-ListDataValidation-1.cs" >}}

#####  **Validation des données de dates**

Avec ce type de validation, les utilisateurs saisissent des valeurs de date dans une plage spécifiée ou répondant à des critères spécifiques dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des dates comprises entre 1970 et 1999. Ici, la zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-DateDataValidation-1.cs" >}}

#####  **Validation des données temporelles**

Avec ce type de validation, les utilisateurs peuvent saisir des heures comprises dans une plage spécifiée ou répondant à certains critères dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des heures entre 9h00 et 11h30. Ici, la zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TimeDataValidation-1.cs" >}}

#####  **Validation des données de longueur de texte**

Avec ce type de validation, les utilisateurs peuvent saisir des valeurs de texte d'une longueur spécifiée dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des valeurs de chaîne ne dépassant pas 5 caractères. La zone de validation est la cellule B1.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Processing-FilteringAndValidation-TextLengthDataValidation-1.cs" >}}

###  **Règles de validation des données**

 Lorsque des validations de données sont mises en œuvre, la validation peut être vérifiée en attribuant différentes valeurs dans les cellules.[**Cell.GetValidationValue**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidationvalue) peut être utilisé pour récupérer le résultat de la validation. L'exemple suivant illustre cette fonctionnalité avec différentes valeurs. L'exemple de fichier peut être téléchargé à partir du lien suivant pour le test :

[sampleDataValidationRules.xlsx](77496339.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-DataValidationRules-1.cs" >}}

##  **Vérifiez si la validation dans la cellule est une liste déroulante**

 Comme nous l'avons vu, de nombreux types de validations peuvent être implémentés au sein d'une cellule. Si vous souhaitez vérifier si la validation est déroulante ou non,[**Validation.InCellDropDown**](https://reference.aspose.com/cells/net/aspose.cells/validation/properties/incelldropdown)La propriété peut être utilisée pour tester cela. L'exemple de code suivant illustre l'utilisation de cette propriété. Un exemple de fichier à tester peut être téléchargé à partir du lien suivant :

[sampleValidation.xlsx](79527947.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckIfValidationInCellDropDown-1.cs" >}}

##  **Ajouter CellArea à la validation existante**

 Il peut y avoir des cas où vous souhaiterez peut-être ajouter[**ZoneCellule**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)à l'existant[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation). Quand tu ajoutes[**ZoneCellule**](https://reference.aspose.com/cells/net/aspose.cells/cellarea) en utilisant[**Validation.AddArea(CellArea cellArea)**](https://reference.aspose.com/cells/net/aspose.cells/validation/methods/addarea), Aspose.Cells vérifie toutes les zones existantes pour voir si la nouvelle zone existe déjà. Si le fichier comporte un grand nombre de validations, cela diminue les performances. Pour pallier à cela, le API met à disposition le[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) méthode. Le*checkIntersection* Le paramètre indique s’il faut vérifier l’intersection d’une zone donnée avec les zones de validation existantes. Le régler sur**FAUX** désactivera la vérification des autres zones. Le*vérifierBord*Le paramètre indique s’il faut vérifier les zones appliquées. Si la nouvelle zone devient la zone supérieure gauche, les paramètres internes sont reconstruits. Si vous êtes sûr que la nouvelle zone n'est pas la zone en haut à gauche, vous pouvez définir ce paramètre sur *false**.

L'extrait de code suivant illustre l'utilisation de[**Validation.AddAreaCellArea cellArea, bool checkIntersection, bool checkEdge)**](https://reference.aspose.com/cells/net/aspose.cells.validation/addarea/methods/1) méthode pour ajouter un nouveau[**ZoneCellule**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)à l'existant[**Validation**](https://reference.aspose.com/cells/net/aspose.cells/validation).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddValidationArea-1.cs" >}}

Les fichiers Excel source et de sortie sont joints pour référence.

[Fichier source](96928093.xlsx)

[Fichier de sortie](96928220.xlsx)


##  **Sujets avancés**
- [Obtenez la validation Cell dans les fichiers ODS](/cells/fr/net/get-cell-validation-in-ods-files/)
- [Obtenez une validation appliquée sur un Cell](/cells/fr/net/get-validation-applied-on-a-cell/)
- [Vérifiez que la valeur Cell satisfait aux règles de validation des données](/cells/fr/net/verify-that-cell-value-satisfies-data-validation-rules/)
