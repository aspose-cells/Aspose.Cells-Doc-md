---
title: Utilisation de Formules ou Fonctions pour Traiter les Données
type: docs
weight: 5
url: /fr/java/get-and-set-formula/
---

{{% alert color="primary" %}}

Une des fonctionnalités les plus attrayantes de Microsoft Excel est sa capacité à traiter les données avec des formules et des fonctions. Microsoft Excel fournit un ensemble de fonctions et de formules intégrées qui aident les utilisateurs à effectuer rapidement des calculs complexes. Aspose.Cells fournit également un vaste ensemble de fonctions et de formules intégrées qui aident les développeurs à calculer les valeurs facilement. Aspose.Cells prend également en charge les fonctions d'extension. De plus, Aspose.Cells prend en charge les formules matricielles et R1C1 dans Aspose.Cells.

{{% /alert %}}

## **Utilisation de Formules et de Fonctions**

Aspose.Cells fournit une classe, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), qui représente un fichier Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) contient une collection [**Worksheets**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) qui permet d'accéder à chaque feuille de calcul du fichier Excel. Une feuille de calcul est représentée par la classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). La classe [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) fournit une collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells). Chaque élément de la collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) représente un objet de la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

Il est possible d'appliquer des formules aux cellules en utilisant les propriétés et les méthodes offertes par la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell), discutée plus en détail ci-dessous.

- [Utilisation de fonctions intégrées](/cells/fr/java/using-formulas-or-functions-to-process-data/#using-built-in-functions).
- [Utilisation de fonctions d'extension](/cells/fr/java/using-formulas-or-functions-to-process-data/#using-add-in-functions).
- [Travailler avec des formules matricielles](/cells/fr/java/using-formulas-or-functions-to-process-data/#using-array-formula).
- [Créer une formule R1C1](/cells/fr/java/using-formulas-or-functions-to-process-data/#using-r1c1-formula).

## **Utilisation de Fonctions Intégrées**

Les fonctions intégrées ou formules sont fournies comme des fonctions prêtes à l'emploi pour réduire les efforts et le temps des développeurs. Consultez [une liste des fonctions intégrées](/cells/fr/java/supported-formula-functions/). Les fonctions sont répertoriées par ordre alphabétique. D'autres fonctions seront prises en charge à l'avenir.

Aspose.Cells prend en charge la plupart des formules ou fonctions offertes par Microsoft Excel. Les développeurs peuvent utiliser ces formules via l'API ou [tableur de concepteur](/cells/fr/java/what-is-a-designer-spreadsheet/). Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaînes, logiques, date/heure, statistiques, de base de données, de recherche et de référence.

Utiliser la propriété [**Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) de la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) pour ajouter une formule à une cellule. **Des formules complexes**, par exemple

{{< highlight java >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sont également prises en charge dans Aspose.Cells. Lors de l'application d'une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

Dans l'exemple ci-dessous, une formule complexe est appliquée à la première cellule de la collection [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Cells) d'une feuille de calcul. La formule utilise une **fonction SI** intégrée fournie par Aspose.Cells.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingBuiltinfunction-1.java" >}}

## **Utilisation de Fonctions d'Extension**

Nous pouvons avoir quelques formules définies par l'utilisateur que nous voulons inclure en tant qu'addon Excel. Lors de la définition de la fonction [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula), les fonctions intégrées fonctionnent bien, cependant il est nécessaire de définir les fonctions ou formules personnalisées à l'aide des fonctions de l'addon.

Aspose.Cells propose des fonctionnalités pour enregistrer des fonctions de complément à l'aide de [**Worksheets.RegisterAddInFunction()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#registerAddInFunction-java.lang.String-java.lang.String-boolean-). Ensuite, lorsque nous définissons [**Cell.Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#Formula) = anyFunctionFromAddIn, le fichier Excel de sortie contient la valeur calculée à partir de la fonction de complément.

Le fichier XLAM suivant doit être téléchargé pour enregistrer la fonction d'addon dans le code d'exemple ci-dessous. De même, le fichier de sortie "test_udf.xlsx" peut être téléchargé pour vérifier la sortie.

[TestUDF.xlam](TestUDF.xlam)

[test_udf.xlsx](test_udf.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Formulas-RegisterAndCallFuncFromAddIn-1.java" >}}

## **Utilisation de la formule matricielle**

Les formules matricielles sont des formules qui fonctionnent avec des matrices, au lieu de numéros individuels, en tant qu'arguments des fonctions qui constituent la formule. Lorsqu'une formule matricielle est affichée, elle est entourée d'accolades ({}) comme illustré ci-dessous.

**Définition d'une formule matricielle sur la cellule G2** 

![todo:image_alt_text](using-formulas-or-functions-to-process-data_1.png)

Certaines fonctions Microsoft Excel renvoient des tableaux de valeurs. Pour calculer plusieurs résultats avec une formule de tableau, entrez le tableau dans une plage de cellules avec le même nombre de lignes et de colonnes que les arguments du tableau.

Il est possible d'appliquer une formule de tableau à une cellule en appelant la méthode [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-) de la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell). La méthode [**setArrayFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setArrayFormula-java.lang.String-int-int-) prend les paramètres suivants :

- **Formule de tableau**, la formule de tableau.
- **Nombre de lignes**, le nombre de lignes pour remplir le résultat de la formule de tableau.
- **Nombre de colonnes**, le nombre de colonnes pour remplir le résultat de la formule matricielle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingArrayFunction-1.java" >}}

## **Utilisation de la formule R1C1**

Appliquer une formule de style de référence **R1C1** à une cellule avec la propriété [**setR1C1Formula**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#R1C1Formula) de la classe [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-formulas-ProcessDataUsingR1C1-1.java" >}}

{{< app/cells/assistant language="java" >}}
