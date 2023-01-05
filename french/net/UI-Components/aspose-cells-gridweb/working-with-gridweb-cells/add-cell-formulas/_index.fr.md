---
title: Ajouter Cell Formules
type: docs
weight: 30
url: /fr/net/add-cell-formulas/
---
{{% alert color="primary" %}} 

La fonctionnalité la plus précieuse offerte par Aspose.Cells.GridWeb est la prise en charge des formules ou des fonctions. Aspose.Cells.GridWeb possède son propre moteur de formule qui calcule les formules dans les feuilles de calcul. Aspose.Cells.GridWeb prend en charge les fonctions ou formules intégrées et définies par l'utilisateur. Cette rubrique décrit en détail l'ajout de formules aux cellules à l'aide de Aspose.Cells.GridWeb API.

{{% /alert %}} 
## **Ajout de formules au Cells**
### **Comment ajouter et calculer une formule ?**
 Il est possible d'ajouter, d'accéder et de modifier des formules dans les cellules en utilisant la propriété Formule d'une cellule. Aspose.Cells.GridWeb prend en charge les formules définies par l'utilisateur allant du simple au complexe. Cependant, un grand nombre de fonctions ou de formules intégrées (similaires à Microsoft Excel) sont également fournies avec Aspose.Cells.GridWeb. Pour voir la liste complète des fonctions intégrées, veuillez vous référer à ce[liste des fonctions prises en charge.](/cells/fr/net/list-of-supported-functions/)

{{% alert color="primary" %}} 

La syntaxe de la formule doit être compatible avec la syntaxe Excel Microsoft. Par exemple, toutes les formules doivent commencer par un signe égal (=).

Pour ajouter une formule dynamiquement, Aspose.Cells.GridWeb la reconnaîtra comme une formule même si vous n'utilisez pas de signe **=**, mais si les utilisateurs finaux travaillent dans l'interface graphique, il doit utiliser le signe "=".

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddFormulas.cs" >}}



**Formule ajoutée à la cellule B3 mais non calculée par GridWeb** 

![tâche : image_autre_texte](add-cell-formulas_1.png)

Dans la capture d'écran ci-dessus, vous pouvez voir qu'une formule a été ajoutée à B3 mais n'a pas encore été calculée. Pour calculer toutes les formules, appelez la méthode CalculateFormula du contrôle GridWorksheetCollection après avoir ajouté des formules aux feuilles de calcul, comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-CalculateFormulas.cs" >}}

{{% alert color="primary" %}} 

 Les utilisateurs peuvent également calculer des formules en cliquant sur**Nous faire parvenir**.

**En cliquant sur le bouton Soumettre de GridWeb** 

![tâche : image_autre_texte](add-cell-formulas_2.png)

**IMPORTANT** : Si un utilisateur clique sur le**Sauver** ou alors**annuler** ou les onglets de la feuille, toutes les formules sont calculées automatiquement par GridWeb.

**Résultat de la formule après calcul** 

![tâche : image_autre_texte](add-cell-formulas_3.png)

{{% /alert %}} 
### **Référence Cells à partir d'autres feuilles de travail**
En utilisant Aspose.Cells.GridWeb, il est possible de référencer des valeurs stockées dans différentes feuilles de calcul dans leurs formules, créant ainsi des formules complexes.

La syntaxe pour référencer une valeur de cellule à partir d'une autre feuille de calcul est SheetName!CellName.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddFormulas.aspx-AddComplexFormulas.cs" >}}
