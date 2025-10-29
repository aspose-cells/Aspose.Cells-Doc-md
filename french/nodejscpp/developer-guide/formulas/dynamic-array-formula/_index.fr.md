---  
title: Configuration des formules de tableau dynamique avec Node.js via C++  
linktitle: Définir les formules de tableau dynamiques  
description: Comment utiliser la bibliothèque Aspose.Cells pour calculer les formules de tableau dynamique dans Excel en utilisant Node.js via C++. Charger, calculer et enregistrer facilement des fichiers Excel.  
keywords: Formules de tableau dynamique, Formules de tableau dynamique dans Excel, Définir des formules de tableau dynamique Node.js via C++, Calcul des formules de tableau dynamique Node.js via C++, gérer des formules de tableau dynamique Excel.  
type: docs  
weight: 70  
url: /fr/nodejs-cpp/calculation-of-dynamic-array-formulas/  
---  
## **Qu'est-ce que la formule de tableau Excel**  
Dans Excel, une formule de tableau est un type spécial de formule qui vous permet d'effectuer des calculs sur des tableaux de données plutôt que sur des cellules individuelles. Les formules de tableau peuvent être utilisées pour effectuer des calculs complexes, manipuler des données et résoudre des problèmes spécifiques de manière efficace. Elles sont saisies différemment des formules régulières et nécessitent souvent l'utilisation de Ctrl + Maj + Entrée.

Voici quelques points clés sur les formules de tableau dans Excel:  
1. Syntaxe:  
<br>  
Les formules de tableau sont écrites comme des formules régulières mais impliquent des opérations sur des tableaux de valeurs. Elles sont contenues entre des accolades { } pour indiquer qu'elles sont des formules de tableau. Cependant, vous ne tapez pas ces accolades vous-même; Excel les ajoute automatiquement lorsque vous saisissez correctement la formule.  
2. Entrée des formules de tableau :  
<br>  
 Pour entrer une formule de tableau, tapez la formule dans la barre de formule. Au lieu d'appuyer sur Entrée pour terminer, appuyez sur Ctrl + Shift + Entrée. Cela indique à Excel qu'il s'agit d'une formule de tableau. Lorsque la formule est correctement entrée, Excel affiche la formule entre accolades dans la barre de formule pour indiquer qu'il s'agit d'une formule de tableau.  
3. Cas d'utilisation :  
<br>  
Les formules de tableau sont utiles pour effectuer des calculs sur plusieurs cellules ou plages simultanément. Elles peuvent être utilisées pour des calculs mathématiques avancés, des opérations conditionnelles, le filtrage des données, et plus encore.  
4. Avantages :  
<br>  
Les formules matricielles vous permettent d'effectuer des calculs complexes dans une seule formule, ce qui peut améliorer l'efficacité et simplifier vos feuilles de calcul. Elles peuvent gérer de grands ensembles de données et effectuer des calculs qui nécessiteraient autrement de multiples étapes intermédiaires.  
5. Limitations :  
<br>  
Les formules matricielles peuvent être plus difficiles à comprendre et à dépanner que les formules classiques. Elles peuvent ralentir les performances de la feuille de calcul, en particulier si elles sont utilisées de manière intensive ou avec de grands ensembles de données.  
6. Exemples :  
<br>  
Additionner les valeurs dans une plage : **{=SUM(A1:A5*B1:B5)}**  
<br>  
Trouver la valeur maximale dans une plage : **{=MAX(A1:A5+B1:B5)}**  
<br>  
<image src="1.png" width="70%" />  
<br>  

Rappelez-vous que les formules matricielles doivent être utilisées judicieusement et qu'il est important de comprendre comment elles fonctionnent avant de les implémenter dans vos feuilles de calcul. Elles peuvent être des outils puissants pour l'analyse et la manipulation des données dans Excel.

## **Quelle est la formule de tableau dynamique Excel**  
Les formules de tableau dynamique sont une nouvelle fonctionnalité introduite dans Excel 365 et Excel 2021. Elles vous permettent de travailler avec des tableaux de données de manière plus transparente et efficace par rapport aux formules matricielles traditionnelles. Les formules de tableau dynamique éclaboussent automatiquement les résultats dans les cellules adjacentes, éliminant ainsi le besoin de Ctrl + Maj + Entrée et permettant une manipulation plus facile des données.

Points clés concernant les formules de tableau dynamique dans Excel:  
1. Éclaboussures automatiques:  
<br>  
Les formules de tableau dynamique éclaboussent automatiquement les résultats dans les cellules adjacentes en fonction de la taille des données de sortie. Cela signifie que vous n'avez pas besoin de sélectionner une plage de cellules avant d'entrer la formule ou d'utiliser Ctrl + Maj + Entrée pour confirmer la formule.  
2. Entrée d'une seule cellule :  
<br>  
Les formules de tableau dynamique sont entrées dans une seule cellule, et Excel remplit automatiquement les cellules voisines avec les résultats. Cela facilite la gestion et la compréhension des formules, car vous n'avez besoin d'entrer la formule qu'une seule fois.  
3. Nouvelles fonctions :  
<br>  
Les formules de tableau dynamique introduisent de nouvelles fonctions qui peuvent manipuler des tableaux de manière native, telles que **FILTRE**, **TRIER**, **UNIQUE**, **SÉQUENCE**, **TRIERPAR** et **SÉQUENCEHAZARD**. Ces fonctions peuvent renvoyer plusieurs valeurs ou manipuler directement des tableaux, simplifiant les calculs complexes.  
4. Gestion flexible des plages :  
<br>  
Les formules de tableau dynamique ajustent dynamiquement la taille de la plage éclaboussée en fonction de la taille des données d'entrée ou du calcul effectué. Cette flexibilité permet une utilisation plus efficace de l'espace de la feuille de calcul et simplifie la création de formules.  
5. Performance améliorée :  
<br>  
Les formules de tableau dynamique peuvent améliorer les performances par rapport aux formules de tableau traditionnelles, notamment lors de travaux avec de grands ensembles de données ou des calculs complexes.  
6. Compatibilité :  
<br>  
Les formules de tableau dynamique sont disponibles dans Excel 365 et Excel 2021. Elles peuvent ne pas être prises en charge dans les anciennes versions d'Excel.  
7. Exemples de formules de tableau dynamique:  
<br>  
**FILTRE**: Renvoie un tableau de valeurs répondant à des critères spécifiques.  
<br>  
**TRIER**: Trie les valeurs dans une plage ou un tableau.  
<br>  
**UNIQUE**: Renvoie des valeurs uniques d'une liste ou d'une plage.  
<br>  
**SÉQUENCE**: Génère une séquence de nombres ou de dates.  
<br>  
**MATRANDE**: Génère un tableau de nombres aléatoires.  
<br>  
<image src="2.png" width="70%" />  
<br>  

Les formules de tableau dynamique offrent des capacités puissantes pour la manipulation et l'analyse des données dans Excel, facilitant le travail avec des tableaux de données et l'exécution de calculs complexes de manière efficace.

## **Quelle est la différence entre les Formules de tableau et les Formules de tableau dynamique dans Excel**  
Dans Excel, les formules de tableau et les formules de tableau dynamique sont utilisées pour effectuer des calculs sur plusieurs valeurs simultanément, mais elles présentent des différences en termes de fonctionnalité et de mise en œuvre.

### **Fonctionnalités des Formules de tableau**  
1. Les formules de tableau sont des formules traditionnelles dans Excel qui peuvent effectuer des calculs sur des tableaux de données.  
2. Elles sont saisies en appuyant sur Ctrl + Shift + Entrée après avoir tapé la formule, ce qui indique à Excel qu'il s'agit d'une formule matricielle.  
3. Les formules matricielles ont des limitations en termes de leur capacité à déverser les résultats dans les cellules adjacentes. Elles renvoient généralement un seul résultat, bien que ce résultat puisse être un tableau de cellules.  
4. Elles existent depuis longtemps et sont prises en charge dans toutes les versions d'Excel.

### **Fonctionnalités des Formules de tableau dynamique**  
1. Les formules de tableau dynamique sont une nouvelle fonctionnalité introduite dans Excel 365 (abonnement Office 365) et Excel 2021.  
2. Elles déversent automatiquement les résultats dans les cellules adjacentes en fonction de la taille des données d'entrée ou du calcul de la formule.  
3. Les formules de tableau dynamiques ne nécessitent pas d'appuyer sur Ctrl + Shift + Entrée ; vous tapez simplement la formule dans une cellule, et Excel remplit automatiquement les cellules adjacentes avec les résultats.  
4. Ces formules ont la capacité de renvoyer plusieurs résultats (une plage de cellules) directement sans avoir besoin d'une formule matricielle ou de Ctrl + Shift + Entrée.  
5. Elles disposent de nouvelles fonctions comme **FILTER**, **SORT**, **UNIQUE**, etc., qui peuvent gérer les tableaux de manière native et renvoyer des résultats au format de tableau dynamique.  
En résumé, les formules de tableau dynamique sont un moyen plus moderne et pratique de travailler avec des tableaux dans Excel, offrant un étalement automatique des résultats et simplifiant le processus de travail avec des tableaux par rapport aux formules de tableau traditionnelles. Cependant, elles ne sont disponibles que dans les versions plus récentes d'Excel prenant en charge les tableaux dynamiques.

## **Comment définir et calculer des formules de tableau dynamique dans Excel**  
La mise en place de formules de tableau dynamique dans Excel implique l'utilisation de fonctions spécifiques conçues pour travailler avec des tableaux de données et permettre aux résultats de s'épancher automatiquement dans les cellules voisines. 

Voici un guide étape par étape pour la mise en place de formules de tableau dynamique :  
1. Sélectionnez la Cellule :  
<br>  
Choisissez la cellule où vous voulez que les résultats de la formule de tableau dynamique apparaissent. Les formules de tableau dynamique épanchent les résultats dans les cellules adjacentes, assurez-vous donc qu'il y a suffisamment d'espace pour la sortie épanchée.  
2. Entrer la formule :  
<br>  
Tapez la formule de tableau dynamique dans la barre de formule de la cellule sélectionnée. Utilisez l'une des fonctions de tableau dynamique disponibles dans Excel 365 et Excel 2021, telles que **FILTRE**, **TRIER**, **UNIQUE**, **SEQUENCE**, **TRIERPAR**, ou **ALEA.TABLEAU**.  
<br>  
Par exemple, vous pourriez utiliser la fonction FILTRE pour filtrer une liste de données en fonction de critères spécifiques : **=FILTRE(A2:C15,(A2:A15=F4)*(C2:C15=G4),"")**.  
<br>  
<image src="3.png" width="70%" />  
<br>  
3. Appuyer sur Entrée :  
<br>  
Après avoir tapé la formule, appuyez simplement sur Entrée sur votre clavier. Contrairement aux formules de tableau traditionnelles, vous n'avez pas besoin d'appuyer sur Ctrl + Maj + Entrée.  
4. Observer la plage déversée :  
<br>  
Excel épanche automatiquement les résultats de la formule dans les cellules voisines. La plage épanchée s'ajuste dynamiquement en fonction de la taille des données de sortie ou du calcul effectué par la formule. Excel met en surbrillance la plage épanchée avec une bordure et une icône de flèche diagonale pour indiquer qu'elle contient des données épanchées.  
5. Interagir avec la plage déversée :  
<br>  
Vous pouvez interagir avec la plage épanchée comme avec n'importe quelle autre plage de cellules dans Excel. Utilisez la plage épanchée dans d'autres formules, effectuez des calculs dessus, formatez-la, ou référencez-la dans des graphiques ou des tableaux.  
6. Mettre à jour la formule :  
<br>  
Si vous devez modifier la formule de tableau dynamique, il suffit de modifier la formule dans la cellule d'origine où elle a été saisie. Après modification, appuyez de nouveau sur Entrée pour confirmer les changements. Excel mettra automatiquement à jour la plage déversée si nécessaire.  
7. Effacer la plage déversée :  
<br>  
Si vous voulez effacer les données étendues, vous pouvez supprimer la formule de la cellule d'origine. Excel effacera également la plage étendue. Autrement, vous pouvez supprimer directement la plage étendue en la sélectionnant et en appuyant sur la touche Supprimer.  
<br>  

En suivant ces étapes, vous pouvez configurer des formules de tableau dynamique dans Excel pour analyser et manipuler efficacement des tableaux de données, permettant une analyse de données et des tâches de reporting plus faciles.

## **Comment définir et actualiser les formules de tableau dynamique en utilisant Aspose.Cells**  
Veuillez consulter l'exemple de code ci-dessous qui charge le [fichier Excel d'exemple](dynamicArrayFormula.xlsx) contenant des données fictives. Après avoir chargé le fichier, appelez la fonction [Cell.setDynamicArrayFormula(string, FormulaParseOptions, boolean)](https://reference.aspose.com/cells/nodejs-cpp/cell/#setDynamicArrayFormula-string-formulaparseoptions-boolean-) pour définir la formule de tableau dynamique et la fonction [Workbook.refreshDynamicArrayFormulas(boolean)](https://reference.aspose.com/cells/nodejs-cpp/workbook/#refreshDynamicArrayFormulas-boolean-) pour rafraîchir les formules de tableau dynamique avant de calculer la formule, puis enregistrez enfin le classeur en tant que [fichier Excel de sortie](out.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "dynamicArrayFormula.xlsx");

// Instantiate an Workbook object
const wb = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const ws = wb.getWorksheets().get(0);

// Getting the F16 
const f16 = ws.getCells().get("F16");

// Set dynamic array formula
f16.setDynamicArrayFormula("=FILTER(A2:C15,(A2:A15=F4)*(C2:C15=25),\"\")", new AsposeCells.FormulaParseOptions(), false);

// Refresh the dynamic array formulas
wb.refreshDynamicArrayFormulas(true);

wb.calculateFormula();
wb.save("out.xlsx");
```

La capture d'écran de sortie :  
<br>  
<image src="4.png" width="70%" />  

{{< app/cells/assistant language="nodejs-cpp" >}}
