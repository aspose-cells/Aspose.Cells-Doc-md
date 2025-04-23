---  
title: Validation de données
type: docs  
weight: 90  
url: /fr/nodejs-cpp/data-validation/  
description: Découvrez comment ajouter une validation de données via l API Aspose.Cells for Node.js via C++.  
keywords: Ajoutez une validation de données Node.js via C++, récupérez la valeur de validation Node.js via C++, ajoutez une validation de nombre entier Node.js via C++, ajoutez une validation de liste Node.js via C++, ajoutez une validation de date Node.js via C++, ajoutez une validation de temps Node.js via C++, ajoutez une validation de longueur de texte Node.js via C++, ajoutez une CellArea à la validation existante Node.js via C++, vérifiez si la validation dans la cellule est un menu déroulant Node.js via C++, ajoutez une validation personnalisée Node.js via C++  
---  

{{% alert color="primary" %}}  
Microsoft Excel offre certaines bonnes fonctionnalités pour la validation automatique ou la validation de données de la feuille de calcul. Aspose.Cells prend entièrement en charge les fonctionnalités de validation de données et de filtre automatique de Microsoft Excel. Cet article explique comment utiliser ces fonctionnalités dans Microsoft Excel et comment les coder avec Aspose.Cells for Node.js via C++.  
{{% /alert %}}  

## **Types de validation des données et exécution**  

La validation des données est la capacité de définir des règles relatives aux données saisies dans une feuille de calcul. Par exemple, utilisez la validation pour vous assurer qu'une colonne étiquetée DATE ne contient que des dates, ou qu'une autre colonne ne contient que des chiffres. Vous pourriez même vous assurer qu'une colonne étiquetée DATE ne contient que des dates dans une certaine plage. Avec la validation des données, vous pouvez contrôler ce qui est saisi dans les cellules de la feuille de calcul.  

Microsoft Excel prend en charge plusieurs types de validation des données. Chaque type est utilisé pour contrôler le type de données entrées dans une cellule ou une plage de cellules. Ci-dessous, des extraits de code illustrent comment valider que:  

- Les chiffres sont des entiers, c'est-à-dire qu'ils n'ont pas de partie décimale.  
- Les nombres décimaux suivent la structure correcte. L'exemple de code définit qu'une plage de cellules doit avoir deux décimales.  
- Les valeurs sont restreintes à une liste de valeurs. La validation de liste définit une liste distincte de valeurs qui peuvent s'appliquer à une cellule ou une plage de cellules.  
- Les dates se trouvent dans une plage spécifique.  
- Une heure se situe dans une plage spécifique.  
- Un texte a une longueur de caractères donnée.  

### **Validation des données avec Microsoft Excel**  

Pour créer des validations avec Microsoft Excel:  

1. Dans une feuille de calcul, sélectionnez les cellules auxquelles vous voulez appliquer la validation.  
1. Dans le menu **Données**, sélectionnez **Validation**. La boîte de dialogue de validation s'affichera.  
1. Cliquez sur l'onglet **Paramètres** et saisissez les paramètres.  

### **Validation de données avec Aspose.Cells for Node.js via C++**  

La validation des données est une fonctionnalité puissante pour valider les informations saisies dans les feuilles de calcul. Avec la validation des données, les développeurs peuvent fournir aux utilisateurs une liste de choix, restreindre les saisies de données à un type ou une taille spécifique, etc.  
Dans Aspose.Cells for Node.js via C++, chaque classe [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) possède une méthode [**getValidations()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getValidations--) qui représente une collection d'objets [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation). Pour configurer la validation, définissez certaines propriétés de la classe [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) comme suit:  

- Type – représente le type de validation, qui peut être spécifié en utilisant l'une des valeurs prédéfinies dans l’énumération [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype).  
- Opérateur – représente l’opérateur à utiliser dans la validation, qui peut être spécifié en utilisant l’une des valeurs prédéfinies dans l’énumération [**OperatorType**](https://reference.aspose.com/cells/nodejs-cpp/operatortype).  
- Formule1 : représente la valeur ou l'expression associée à la première partie de la validation des données.  
- Formule2 : représente la valeur ou l'expression associée à la deuxième partie de la validation des données.  

Lorsque les propriétés de l’objet [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) ont été configurées, les développeurs peuvent utiliser la structure [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) pour stocker des informations sur la plage de cellules qui sera validée à l’aide de la validation créée.  

#### **Types de validation des données**  

L’énumération [**ValidationType**](https://reference.aspose.com/cells/nodejs-cpp/validationtype) a les membres suivants :  

|**Nom du membre**|**Description**|  
| :- | :- |  
|AnyValue|Désigne une valeur de n'importe quel type.|  
|WholeNumber|Indique le type de validation pour les nombres entiers.|  
|Decimal|Indique le type de validation pour les nombres décimaux.|  
|List|Indique le type de validation pour la liste déroulante.|  
|Date|Indique le type de validation pour les dates.|  
|Time|Indique le type de validation pour l'heure.|  
|TextLength|Indique le type de validation pour la longueur du texte.|  
|Custom|Indique le type de validation personnalisée.|  

##### **Validation de données pour les nombres entiers**  

Avec ce type de validation, les utilisateurs ne peuvent entrer que des nombres entiers dans une plage spécifiée dans les cellules validées. Les exemples de code qui suivent montrent comment implémenter le type de validation NombreEntier. L’exemple crée la même validation de données en utilisant Aspose.Cells for Node.js via C++ que celle que nous avons créée avec Microsoft Excel ci-dessus.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-WholeNumber.js" >}}


##### **Validation de données par liste**  

Ce type de validation permet à l'utilisateur d'entrer des valeurs à partir d'une liste déroulante. Il fournit une liste: une série de lignes contenant des données. Dans l'exemple, une deuxième feuille de calcul est ajoutée pour contenir la source de la liste. Les utilisateurs ne peuvent sélectionner que des valeurs dans la liste. La zone de validation est la plage de cellules A1:A5 dans la première feuille de calcul.  

Il est important ici de définir la propriété [**Validation.setInCellDropDown(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#setInCellDropDown-boolean-) sur **true**.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ListData.js" >}}


##### **Validation de données pour les dates**  

Avec ce type de validation, les utilisateurs saisissent des valeurs de date dans une plage spécifiée, ou répondant à des critères spécifiques, dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des dates entre 1970 et 1999. Ici, la zone de validation est la cellule B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DateData.js" >}}

##### **Validation des données de temps**  

Avec ce type de validation, les utilisateurs peuvent saisir des heures dans une plage spécifiée, ou répondant à certains critères, dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des heures entre 09h00 et 11h30. Ici, la zone de validation est la cellule B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TimeData.js" >}}


##### **Validation de la longueur du texte**  

Avec ce type de validation, les utilisateurs peuvent saisir des valeurs textuelles d'une longueur spécifiée dans les cellules validées. Dans l'exemple, l'utilisateur est limité à saisir des valeurs de chaîne ne dépassant pas 5 caractères. La zone de validation est la cellule B1.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-TextLengthData.js" >}}


### **Règles de validation des données**  

 Lors de l’implémentation des validations, la validation peut être vérifiée en assignant différentes valeurs dans les cellules. [**Cell.getValidationValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidationValue--) peut être utilisé pour récupérer le résultat de la validation. L’exemple suivant montre cette fonctionnalité avec différentes valeurs. Le fichier d’échantillon peut être téléchargé via le lien suivant pour test :  

[sampleDataValidationRules.xlsx](77496339.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-DataValidationRules.js" >}}


## **Vérifier si la validation dans la cellule est une liste déroulante**  

Comme nous l’avons vu, il existe de nombreux types de validations qui peuvent être implémentés dans une cellule. Si vous souhaitez vérifier si la validation est un menu déroulant ou non, la méthode [**Validation.getInCellDropDown()**](https://reference.aspose.com/cells/nodejs-cpp/validation/#getInCellDropDown--) peut être utilisée pour tester cela. Le code d’échantillon ci-dessous montre l’utilisation de cette propriété. Un fichier d’échantillon pour tester peut être téléchargé via le lien suivant :  

[sampleValidation.xlsx](79527947.xlsx)  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-CheckValidationIsDropDown.js" >}}


## **Ajouter une CellArea à une validation existante**  

Il peut y avoir des cas où vous souhaitez ajouter [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) à [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) existantes. Lorsque vous ajoutez [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) en utilisant [**Validation.addArea(CellArea)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-), Aspose.Cells vérifie toutes les zones existantes pour voir si la nouvelle zone existe déjà. Si le fichier contient un grand nombre de validations, cela impacte la performance. Pour éviter cela, l’API fournit la méthode [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-). Le paramètre *checkIntersection* indique s’il faut vérifier l’intersection d’une zone donnée avec les zones de validation existantes. La mise à false désactivera la vérification des autres zones. Le paramètre *checkEdge* indique s’il faut vérifier les zones appliquées. Si la nouvelle zone devient la zone en haut à gauche, les paramètres internes sont reconstruit. Si vous êtes certain que la nouvelle zone n’est pas en haut à gauche, vous pouvez définir ce paramètre sur **false**.  

Le code suivant illustre l’utilisation de la méthode [**Validation.addArea(CellArea, boolean, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/validation/#addArea-cellarea-boolean-boolean-) pour ajouter un [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea) à [**Validation**](https://reference.aspose.com/cells/nodejs-cpp/validation) existants.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-AddCellAreaToExistingValidation.js" >}}

Les fichiers Excel source et de sortie sont joints pour référence.  

[Fichier source](96928093.xlsx)  

[Fichier de sortie](96928220.xlsx)  

## **Sujets avancés**  
- [Obtenir la validation de la cellule dans les fichiers ODS](/cells/fr/nodejs-cpp/get-cell-validation-in-ods-files/)  
- [Obtenir la validation appliquée sur une cellule](/cells/fr/nodejs-cpp/get-validation-applied-on-a-cell/)  
- [Vérifier que la valeur de la cellule satisfait aux règles de validation des données](/cells/fr/nodejs-cpp/verify-that-cell-value-satisfies-data-validation-rules/)  

