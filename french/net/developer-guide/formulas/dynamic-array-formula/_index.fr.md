---
title: Définition de formules de tableau dynamique
description: Comment utiliser la bibliothèque Aspose.Cells pour calculer des formules matricielles dynamiques dans Excel Microsoft. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser la méthode fournie par Aspose.Cells pour calculer la formule matricielle dynamique et obtenir le résultat. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Dynamic Array Formulas, Dynamic Array Formulas in Excel, Set dynamic array formulas, Calculation of dynamic array formulas, operate dynamic array formulas of Excel.
type: docs
weight: 70
url: /fr/net/calculation-of-dynamic-array-formulas/
---
##  **Quelle est la formule du tableau Excel**
Dans Excel, une formule matricielle est un type spécial de formule qui vous permet d'effectuer des calculs sur des tableaux de données plutôt que sur des cellules individuelles. Les formules matricielles peuvent être utilisées pour effectuer des calculs complexes, manipuler des données et résoudre efficacement des problèmes spécifiques. Elles sont saisies différemment des formules classiques et nécessitent souvent l'utilisation de Ctrl + Maj + Entrée.

Voici quelques points clés sur les formules matricielles dans Excel :
1. Syntaxe:
<br>
Les formules matricielles sont écrites comme des formules normales mais impliquent des opérations sur des tableaux de valeurs. Ils sont entourés d'accolades { } pour indiquer qu'il s'agit de formules matricielles. Cependant, vous ne tapez pas ces accolades vous-même ; Excel les ajoute automatiquement lorsque vous saisissez correctement la formule.
1. Saisie de formules matricielles :
<br>
Pour saisir une formule matricielle, vous tapez la formule dans la barre de formule. Au lieu d’appuyer sur Entrée pour terminer, vous appuyez sur Ctrl + Maj + Entrée. Cela indique à Excel qu'il s'agit d'une formule matricielle. Lorsqu'elle est saisie correctement, Excel affiche la formule entre accolades dans la barre de formule pour indiquer qu'il s'agit d'une formule matricielle.
1. Cas d'utilisation :
<br>
Les formules matricielles sont utiles pour effectuer des calculs sur plusieurs cellules ou plages simultanément. Ils peuvent être utilisés pour des calculs mathématiques avancés, des opérations conditionnelles, le filtrage des données, etc.
1. Avantages:
<br>
Les formules matricielles vous permettent d'effectuer des calculs complexes dans une seule formule, ce qui peut améliorer l'efficacité et simplifier vos feuilles de calcul. Ils peuvent gérer de grands ensembles de données et effectuer des calculs qui nécessiteraient autrement plusieurs étapes intermédiaires.
1. Limites:
<br>
Les formules matricielles peuvent être plus difficiles à comprendre et à dépanner que les formules classiques. Ils peuvent ralentir les performances des feuilles de calcul, surtout s'ils sont utilisés de manière intensive ou avec de grands ensembles de données.
1. Exemples:
<br>
 Somme des valeurs dans une plage :**{=SOMME(A1:A5*B1:B5)}**
<br>
 Trouver la valeur maximale dans une plage :**{=MAX(A1:A5+B1:B5)}**
<br>
<image src="1.png" width="70%" />
<br>

N'oubliez pas que les formules matricielles doivent être utilisées judicieusement et qu'il est important de comprendre leur fonctionnement avant de les implémenter dans vos feuilles de calcul. Ils peuvent être de puissants outils d’analyse et de manipulation de données dans Excel.

##  **Quelle est la formule de tableau dynamique Excel**
Les formules matricielles dynamiques sont une nouvelle fonctionnalité introduite dans Excel 365 et Excel 2021. Elles vous permettent de travailler avec des tableaux de données de manière plus transparente et plus efficace que les formules matricielles traditionnelles. Les formules matricielles dynamiques diffusent automatiquement les résultats dans les cellules voisines, éliminant ainsi le besoin de Ctrl + Maj + Entrée et permettant une manipulation plus facile des données.

Points clés sur les formules matricielles dynamiques dans Excel :
1. Déversement automatique :
<br>
Les formules matricielles dynamiques répartissent automatiquement les résultats dans les cellules adjacentes en fonction de la taille des données de sortie. Cela signifie que vous n'avez pas besoin de sélectionner une plage de cellules avant de saisir la formule ou d'utiliser Ctrl + Maj + Entrée pour confirmer la formule.
1. Entrée unique-Cell :
<br>
Les formules matricielles dynamiques sont saisies dans une seule cellule et Excel remplit automatiquement les cellules voisines avec les résultats. Cela facilite la gestion et la compréhension des formules, car vous ne devez saisir la formule qu'une seule fois.
1. Nouvelles fonctions :
<br>
Les formules de tableau dynamique introduisent de nouvelles fonctions capables de gérer les tableaux de manière native, telles que *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** et *RANDARRAY**. Ces fonctions peuvent renvoyer plusieurs valeurs ou manipuler directement des tableaux, simplifiant ainsi les calculs complexes.
1. Gestion flexible de la plage :
<br>
Les formules matricielles dynamiques ajustent dynamiquement la taille de la plage déversée en fonction de la taille des données d'entrée ou du calcul effectué. Cette flexibilité permet une utilisation plus efficace de l'espace de la feuille de calcul et simplifie la création de formules.
1. Performance améliorée:
<br>
Les formules matricielles dynamiques peuvent améliorer les performances par rapport aux formules matricielles traditionnelles, en particulier lorsque vous travaillez avec des ensembles de données volumineux ou des calculs complexes.
1. Compatibilité:
<br>
Les formules matricielles dynamiques sont disponibles dans Excel 365 et Excel 2021. Elles peuvent ne pas être prises en charge dans les anciennes versions d'Excel.
1. Exemples de formules matricielles dynamiques :
<br>
*FILTER** : renvoie un tableau de valeurs qui répondent aux critères spécifiés.
<br>
*TRIER** : trie les valeurs dans une plage ou un tableau.
<br>
*UNIQUE** : renvoie des valeurs uniques à partir d'une liste ou d'une plage.
<br>
*SEQUENCE** : Génère une séquence de nombres ou de dates.
<br>
*RANDARRAY** : génère un tableau de nombres aléatoires.
<br>
<image src="2.png" width="70%" />
<br>

Les formules matricielles dynamiques offrent de puissantes fonctionnalités de manipulation et d'analyse des données dans Excel, facilitant ainsi l'utilisation de tableaux de données et l'exécution efficace de calculs complexes.

##  **Quelle est la différence entre les formules matricielles et les formules matricielles dynamiques dans Excel**
Dans Excel, les formules matricielles et les formules matricielles dynamiques sont utilisées pour effectuer des calculs sur plusieurs valeurs simultanément, mais elles présentent certaines différences en termes de fonctionnalités et de manière de les mettre en œuvre.

###  **Fonctionnalités des formules matricielles**
1. Les formules matricielles sont des formules traditionnelles dans Excel qui peuvent effectuer des calculs sur des tableaux de données.
1. Ils sont saisis en appuyant sur Ctrl + Maj + Entrée après avoir tapé la formule, ce qui indique à Excel qu'il s'agit d'une formule matricielle.
1. Les formules matricielles ont des limites en termes de capacité à diffuser les résultats dans les cellules adjacentes. Ils renvoient généralement un résultat 1. unique, bien que ce résultat puisse être un tableau de cellules.
1. Ils existent depuis longtemps et sont pris en charge dans toutes les versions d'Excel.

###  **Fonctionnalités des formules de tableaux dynamiques**
1. Les formules matricielles dynamiques sont une nouvelle fonctionnalité introduite dans Excel 365 (abonnement Office 365) et Excel 2021.
1. Ils diffusent automatiquement les résultats dans les cellules adjacentes en fonction de la taille des données d'entrée ou du calcul de la formule.
1. Les formules matricielles dynamiques ne nécessitent pas d'appuyer sur Ctrl + Maj + Entrée ; vous tapez simplement la formule dans une cellule et Excel remplit automatiquement les cellules adjacentes avec les résultats.
1. Ces formules ont la capacité de renvoyer plusieurs résultats (une plage de cellules) directement sans avoir besoin d'une formule matricielle ou de Ctrl + Maj + Entrée.
1. Ils ont de nouvelles fonctions comme *FILTER**, *SORT**, *UNIQUE**, etc., qui peuvent gérer les tableaux de manière native et renvoyer les résultats dans un format de tableau dynamique.
En résumé, les formules matricielles dynamiques constituent un moyen plus moderne et plus pratique de travailler avec des tableaux dans Excel, permettant une diffusion automatique des résultats et simplifiant le processus de travail avec des tableaux par rapport aux formules matricielles traditionnelles. Cependant, ils ne sont disponibles que dans les versions les plus récentes d'Excel prenant en charge les tableaux dynamiques.

##  **Comment définir et calculer des formules de tableau dynamique dans Excel**
 La configuration de formules matricielles dynamiques dans Excel implique l'utilisation de fonctions spécifiques conçues pour fonctionner avec des tableaux de données et permettre aux résultats de se propager automatiquement dans les cellules voisines.

Voici un guide étape par étape pour configurer des formules matricielles dynamiques :
1. Sélectionnez le Cell :
<br>
Choisissez la cellule dans laquelle vous souhaitez que les résultats de la formule matricielle dynamique apparaissent. Les formules matricielles dynamiques répartissent les résultats dans des cellules adjacentes, alors assurez-vous qu'il y a suffisamment d'espace pour la sortie déversée.
1. Entrez la formule :
<br>
Tapez la formule matricielle dynamique dans la barre de formule de la cellule sélectionnée. Utilisez l'une des fonctions de tableau dynamique disponibles dans Excel 365 et Excel 2021, telles que *FILTER**, *SORT**, *UNIQUE**, *SEQUENCE**, *SORTBY** ou *RANDARRAY**.
<br>
Par exemple, vous pouvez utiliser la fonction FILTER pour filtrer une liste de données en fonction de critères spécifiques : *=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.
<br>
<image src="3.png" width="70%" />
<br>
1. Appuyez sur Entrée:
<br>
Après avoir tapé la formule, appuyez simplement sur Entrée sur votre clavier. Contrairement aux formules matricielles traditionnelles, vous n'avez pas besoin d'appuyer sur Ctrl + Maj + Entrée.
1. Observez la plage déversée :
<br>
Excel répartit automatiquement les résultats de la formule dans les cellules voisines. La plage déversée s'ajuste dynamiquement en fonction de la taille des données de sortie ou du calcul effectué par la formule. Excel met en évidence la plage déversée avec une bordure et une icône de flèche diagonale pour indiquer qu'elle contient des données déversées.
1. Interagissez avec la gamme Spilled :
<br>
Vous pouvez interagir avec la plage déversée comme n’importe quelle autre plage de cellules dans Excel. Utilisez la plage renversée dans d'autres formules, effectuez des calculs dessus, formatez-la ou référencez-la dans des graphiques ou des tableaux.
1. Mettez à jour la formule :
<br>
Si vous devez modifier la formule matricielle dynamique, modifiez simplement la formule dans la cellule d'origine où elle a été saisie.
Après l'édition, appuyez à nouveau sur Entrée pour confirmer les modifications. Excel mettra automatiquement à jour la plage déversée si nécessaire.
1. Effacement de la zone déversée :
<br>
Si vous souhaitez effacer les données répandues, vous pouvez supprimer la formule de la cellule d'origine. Excel effacera également la plage déversée. Alternativement, vous pouvez supprimer directement la plage déversée en la sélectionnant et en appuyant sur la touche Suppr.
<br>

En suivant ces étapes, vous pouvez configurer des formules matricielles dynamiques dans Excel pour analyser et manipuler efficacement des tableaux de données, ce qui facilite les tâches d'analyse des données et de création de rapports.

##  **Comment définir et actualiser des formules de tableau dynamique à l'aide de Aspose.Cells**
 Veuillez consulter l'exemple de code suivant qui charge le[exemple de fichier Excel](dynamicArrayFormula.xlsx)qui contient des données factices. Après avoir chargé le fichier, appelez le[Cell.SetDynamicArrayFormula](https://reference.aspose.com/cells/net/aspose.cells/cell/setdynamicarrayformula/#setdynamicarrayformula)fonction pour définir la formule de tableau dynamique et[Workbook.RefreshDynamicArrayFormulas](https://reference.aspose.com/cells/net/aspose.cells/workbook/refreshdynamicarrayformulas/#refreshdynamicarrayformulas) fonction pour actualiser les formules matricielles dynamiques avant d'appeler le calcul de formule, et enfin enregistrer le classeur sous[sortie du fichier Excel](out.xlsx). 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Formulas-dynamic-array-formulas.cs" >}}

L'instantané de sortie :
<br>
<image src="4.png" width="70%" />