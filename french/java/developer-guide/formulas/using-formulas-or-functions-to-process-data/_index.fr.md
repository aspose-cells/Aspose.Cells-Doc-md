---
title: Utilisation de formules ou de fonctions pour traiter des données
type: docs
weight: 5
url: /fr/java/get-and-set-formula/
---
{{% alert color="primary" %}}

L'une des caractéristiques convaincantes d'Excel Microsoft est sa capacité à traiter des données avec des formules et des fonctions. Microsoft Excel fournit un ensemble de fonctions et de formules intégrées qui aident les utilisateurs à effectuer rapidement des calculs complexes. Aspose.Cells fournit également un vaste ensemble de fonctions et de formules intégrées qui aident les développeurs à calculer facilement les valeurs. Aspose.Cells prend également en charge les fonctions complémentaires. De plus, Aspose.Cells prend en charge le tableau et les formules R1C1 dans Aspose.Cells.

{{% /alert %}}

## **Utiliser des formules et des fonctions**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , qui représente un fichier Excel Microsoft. La[**Cahier**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) classe contient un[**Des feuilles de calcul**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) classer. La[**Feuille de travail**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) le recueil. Chaque élément de la[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) collection représente un objet de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classer.

 Il est possible d'appliquer des formules aux cellules en utilisant les propriétés et les méthodes offertes par le[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)classe, discuté plus en détail ci-dessous.

- [Utilisation des fonctions intégrées](/cells/fr/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Utilisation des fonctions complémentaires](/cells/fr/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Travailler avec des formules matricielles](/cells/fr/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Création d'une formule R1C1](/cells/fr/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Utilisation des fonctions intégrées**

 Les fonctions ou formules intégrées sont fournies sous forme de fonctions prêtes à l'emploi pour réduire les efforts et le temps des développeurs. Voir[une liste de fonctions intégrées](/cells/fr/java/supported-formula-functions/). Les fonctions sont listées par ordre alphabétique. D'autres fonctions seront prises en charge à l'avenir.

 Aspose.Cells prend en charge la plupart des formules ou fonctions proposées par Microsoft Excel. Les développeurs peuvent utiliser ces formules via le API ou[feuille de calcul de concepteur](/cells/fr/java/what-is-a-designer-spreadsheet/). Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaîne, booléennes, de date/heure, statistiques, de base de données, de recherche et de référence.

 Utilisez le[**Formule**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula)propriété de la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classe pour ajouter une formule à une cellule.**Formules complexes**, par exemple

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sont également pris en charge dans Aspose.Cells. Lorsque vous appliquez une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

 Dans l'exemple ci-dessous, une formule complexe est appliquée à la première cellule d'une feuille de calcul[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) le recueil. La formule utilise une fonction intégrée**SI** fonction fournie par Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Utilisation des fonctions complémentaires**

 Nous pouvons avoir des formules définies par l'utilisateur que nous souhaitons inclure en tant que complément Excel. Lors du réglage du[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) Les fonctions intégrées de la fonction fonctionnent correctement, mais il est nécessaire de définir les fonctions ou formules personnalisées à l'aide des fonctions complémentaires.

 Aspose.Cells fournit des fonctionnalités pour enregistrer des fonctions supplémentaires à l'aide de[**Feuilles de calcul.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction(java.lang.String,%20java.lang.String,%20boolean)). Ensuite, quand nous avons mis[**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) anyFunctionFromAddIn, le fichier Excel de sortie contient la valeur calculée à partir de la fonction AddIn.

Ensuite, le fichier XLAM doit être téléchargé pour enregistrer la fonction complémentaire dans l'exemple de code ci-dessous. De même, le fichier de sortie "test_udf.xlsx" peut être téléchargé pour vérifier la sortie.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Utilisation de la formule matricielle**

Les formules matricielles sont des formules qui fonctionnent avec des tableaux, au lieu de nombres individuels, comme arguments des fonctions qui composent la formule. Lorsqu'une formule matricielle est affichée, elle est entourée d'accolades ({}) comme indiqué ci-dessous.

**Définition d'une formule matricielle sur la cellule G2** 

![tâche : image_autre_texte](using-formulas-or-functions-to-process-data_1.png)

Certaines fonctions Excel Microsoft renvoient des tableaux de valeurs. Pour calculer plusieurs résultats avec une formule matricielle, entrez le tableau dans une plage de cellules avec le même nombre de lignes et de colonnes que les arguments du tableau.

 Il est possible d'appliquer une formule matricielle à une cellule en appelant la[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classer'[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int) ) méthode. La[**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula(java.lang.String,%20int,%20int)) prend les paramètres suivants :

- **Formule matricielle**, la formule matricielle.
- **Nombre de rangées**le nombre de lignes à remplir résultat de la formule matricielle.
- **Le nombre de colonnes**, le nombre de colonnes pour remplir le résultat de la formule matricielle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Utilisation de la formule R1C1**

 Appliquer un**R1C1** formule de style de référence à une cellule avec le[**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) classer'[**setR1C1Formule**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula)propriété.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

