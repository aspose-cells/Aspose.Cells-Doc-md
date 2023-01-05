---
title: Gérer les formules des fichiers Excel
linktitle: Formules
type: docs
weight: 122
url: /fr/net/using-formulas-or-functions-to-process-data/
description: Aspose.Cells peut simplement obtenir, définir et calculer des formules de fichiers Excel.
---
## **Introduction**

L'une des caractéristiques convaincantes d'Excel Microsoft est sa capacité à traiter des données avec des formules et des fonctions. Microsoft Excel fournit un ensemble de fonctions et de formules intégrées qui aident les utilisateurs à effectuer rapidement des calculs complexes. Aspose.Cells fournit également un vaste ensemble de fonctions et de formules intégrées qui aident les développeurs à calculer facilement les valeurs. Aspose.Cells prend également en charge les fonctions complémentaires. De plus, Aspose.Cells prend en charge le tableau et les formules R1C1 dans Aspose.Cells.

## **Utiliser des formules et des fonctions**

 Aspose.Cells fournit une classe,[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , qui représente un fichier Excel Microsoft. Le[**Cahier**](https://reference.aspose.com/cells/net/aspose.cells/workbook) classe contient un[**Feuilles de travail**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) collection qui permet d'accéder à chaque feuille de calcul dans le fichier Excel. Une feuille de calcul est représentée par le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) classe. Le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la classe offre une[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/cells) le recueil. Chaque pièce de la collection Cells représente un objet de la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe.

 Il est possible d'appliquer des formules aux cellules en utilisant les propriétés et les méthodes offertes par le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe, discuté plus en détail ci-dessous.

- Utilisation des fonctions intégrées.
- Utilisation des fonctions complémentaires.
- Travailler avec des formules matricielles.
- Création d'une formule R1C1.

## **Utilisation des fonctions intégrées**

 Les fonctions ou formules intégrées sont fournies sous forme de fonctions prêtes à l'emploi pour réduire les efforts et le temps des développeurs. Voir[une liste de fonctions intégrées](/cells/fr/net/supported-formula-functions/) pris en charge par Aspose.Cells. Les fonctions sont répertoriées par ordre alphabétique. D'autres fonctions seront prises en charge à l'avenir.

 Aspose.Cells prend en charge la plupart des formules ou fonctions proposées par Microsoft Excel. Les développeurs peuvent utiliser ces formules via le API ou[feuille de calcul de concepteur](/cells/fr/net/what-is-a-designer-spreadsheet/). Aspose.Cells prend en charge un vaste ensemble de formules mathématiques, de chaîne, booléennes, de date/heure, statistiques, de base de données, de recherche et de référence.

 Utilisez le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**Formule**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/formula)propriété pour ajouter une formule à une cellule.**Formules complexes**, par exemple

{{< highlight "java" >}}

 = H7*(1+IF(P7 = $L$3,$M$3, (IF(P7=$L$4,$M$4,0))))

{{< /highlight >}}

, sont également pris en charge dans Aspose.Cells. Lorsque vous appliquez une formule à une cellule, commencez toujours la chaîne par un signe égal (=) comme vous le faites lors de la création d'une formule dans Microsoft Excel et utilisez une virgule (,) pour délimiter les paramètres de la fonction.

 Dans l'exemple ci-dessous, une formule complexe est appliquée à la première cellule d'une feuille de calcul[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) le recueil. La formule utilise une fonction intégrée**SI** fonction fournie par Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingBuiltinfunction-1.cs" >}}

## **Utilisation des fonctions complémentaires**

Nous pouvons avoir des formules définies par l'utilisateur que nous souhaitons inclure en tant que complément Excel. Lors de la définition de la fonction cell.Formula, les fonctions intégrées fonctionnent correctement, mais il est nécessaire de définir les fonctions ou formules personnalisées à l'aide des fonctions complémentaires.

 Aspose.Cells fournit des fonctionnalités pour enregistrer des fonctions supplémentaires à l'aide de[**Feuilles de calcul.RegisterAddInFunction()**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/registeraddinfunction/index). Ensuite, lorsque nous définissons cell.Formula = anyFunctionFromAddIn, le fichier Excel de sortie contient la valeur calculée à partir de la fonction AddIn.

Le fichier XLAM suivant doit être téléchargé pour enregistrer la fonction complémentaire dans l'exemple de code ci-dessous. De même, le fichier de sortie "test_udf.xlsx" peut être téléchargé pour vérifier la sortie.

[TestUDF.xlam](81920908.xlam)

[test_udf.xlsx](81920909.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-RegisterAndCallFuncFromAddIn-1.cs" >}}

## **Utilisation de la formule matricielle**

Les formules matricielles sont des formules qui prennent des tableaux, au lieu de nombres individuels, comme arguments des fonctions qui composent la formule. Lorsqu'une formule matricielle est affichée, elle est entourée d'accolades ({}).

Certaines fonctions Excel Microsoft renvoient des tableaux de valeurs. Pour calculer plusieurs résultats avec une formule matricielle, entrez le tableau dans une plage de cellules avec le même nombre de lignes et de colonnes que les arguments du tableau.

 Il est possible d'appliquer une formule matricielle à une cellule en appelant la[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) méthode. Le[**SetArrayFormula**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setarrayformula) méthode prend les paramètres suivants :

- **Formule matricielle**la formule matricielle.
- **Nombre de rangées**, le nombre de lignes à remplir résultat de la formule matricielle.
- **Le nombre de colonnes**le nombre de colonnes à remplir résultat de la formule matricielle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingArrayFunction-1.cs" >}}

## **Utilisation de la formule R1C1**

 Ajouter un**R1C1** formule de style de référence à une cellule avec le[**Cell**](https://reference.aspose.com/cells/net/aspose.cells/cell) classe'[**Formule R1C1**](https://reference.aspose.com/cells/net/aspose.cells/cell/properties/r1c1formula) la propriété.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formulas-ProcessDataUsingR1C1-1.cs" >}}

## **Sujets avancés**
- [Antécédents et personnes à charge](/cells/fr/net/precedents-and-dependents/)
- [Définir des liens externes dans les formules](/cells/fr/net/set-external-links-in-formulas/)
- [Propager automatiquement la formule dans le tableau ou l'objet de liste lors de la saisie de données dans de nouvelles lignes](/cells/fr/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/)
- [Définition de la formule pour la plage nommée](/cells/fr/net/setting-formula-for-named-range/)
- [Définition des formules - Avis pour les utilisateurs non anglophones](/cells/fr/net/setting-formulas-notice-for-non-english-users/)
- [Définition d'une formule partagée](/cells/fr/net/setting-shared-formula/)
- [Spécifier le nombre maximal de lignes de formule partagée](/cells/fr/net/specify-maximum-rows-of-shared-formula/)
- [Fonctions Excel prises en charge](/cells/fr/net/supported-formula-functions/)

