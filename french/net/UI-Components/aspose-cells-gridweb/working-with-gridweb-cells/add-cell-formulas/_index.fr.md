---
title: Ajouter des formules de cellule
type: docs
weight: 30
url: /fr/net/aspose-cells-gridweb/add-cell-formula/
keywords: GridWeb,formule
description: Cet article présente comment ajouter une formule dans une cellule dans GridWeb.
---

{{% alert color="primary" %}} 

La fonction la plus précieuse offerte par Aspose.Cells.GridWeb est le support des formules ou fonctions. Aspose.Cells.GridWeb possède son propre Moteur de Formules qui calcule les formules dans les feuilles de calcul. Aspose.Cells.GridWeb prend en charge les fonctions ou formules intégrées et définies par l'utilisateur. Ce sujet traite de l'ajout de formules aux cellules en utilisant l'API Aspose.Cells.GridWeb en détail.

{{% /alert %}} 
## **Ajout de formules aux cellules**
### **Comment Ajouter & Calculer une Formule ?**
Il est possible d'ajouter, d'accéder et de modifier des formules dans les cellules en utilisant la propriété Formule d'une cellule. Aspose.Cells.GridWeb prend en charge les formules définies par l'utilisateur allant de simples à complexes. Toutefois, un grand nombre de fonctions ou formules intégrées (similaires à Microsoft Excel) sont également fournies avec Aspose.Cells.GridWeb. Pour voir la liste complète des fonctions intégrées, veuillez vous référer à cette [liste des fonctions prises en charge.](/cells/fr/net/aspose-cells-gridweb/list-of-supported-functions/)

{{% alert color="primary" %}} 

La syntaxe des formules doit être compatible avec la syntaxe de Microsoft Excel. Par exemple, toutes les formules doivent commencer par un signe égal (=).

Pour ajouter une formule dynamiquement, Aspose.Cells.GridWeb la reconnaîtra en tant que formule même si vous n'utilisez pas de signe **=**, mais si les utilisateurs finaux travaillent dans l'interface graphique, ils doivent utiliser le signe "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Formule ajoutée à la cellule B3 mais non calculée par GridWeb** 

![todo:image_alt_text](add-cell-formulas_1.png)

Sur la capture d'écran ci-dessus, vous pouvez voir qu'une formule a été ajoutée à B3 mais n'a pas encore été calculée. Pour calculer toutes les formules, appelez la méthode CalculateFormula de la collection GridWorksheet du contrôle GridWeb après avoir ajouté des formules aux feuilles de calcul comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

Les utilisateurs peuvent également calculer des formules en cliquant sur **Soumettre**.

**Cliquez sur le bouton Soumettre de GridWeb** 

![todo:image_alt_text](add-cell-formulas_2.png)

**IMPORTANT** : Si un utilisateur clique sur les boutons **Enregistrer** ou **Annuler**, ou sur les onglets de feuille, toutes les formules sont calculées automatiquement par GridWeb.

**Résultat de la formule après le calcul** 

![todo:image_alt_text](add-cell-formulas_3.png)

{{% /alert %}} 
### **Référencer des cellules à partir d'autres feuilles de calcul**
En utilisant Aspose.Cells.GridWeb, il est possible de référencer des valeurs stockées dans différentes feuilles de calcul dans leurs formules, en créant des formules complexes.

La syntaxe pour référencer une valeur de cellule à partir d'une feuille de calcul différente est NomFeuille!NomCellule.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
