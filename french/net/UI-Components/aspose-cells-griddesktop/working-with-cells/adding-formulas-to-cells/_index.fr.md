---
title: Ajouter une formule à une cellule
type: docs
weight: 30
url: /fr/net/aspose-cells-griddesktop/adding-formula-to-cell/
keywords: GridDesktop, formule
description: Cet article présente comment obtenir ou définir une formule dans la cellule de la feuille de calcul de GridDesktop.
---

{{% alert color="primary" %}} 

Une cellule peut contenir non seulement une valeur simple comme un chiffre ou du texte, mais aussi une formule comme sa valeur. Une formule est utilisée dans une cellule lorsque la valeur de la cellule doit être déterminée après quelques calculs. Dans ce sujet, nous discuterons de l'accès et de la modification d'une formule appliquée à une cellule.

{{% /alert %}} 
## **Ajouter une formule à une cellule**
Ajouter une formule à une cellule est similaire à définir la valeur d'une cellule comme nous l'avons discuté dans notre sujet précédent: [Accéder et modifier la valeur d'une cellule](/cells/fr/net/acceder-et-modifier-la-valeur-dune-cellule/) sauf que dans ce cas, nous ajoutons simplement des valeurs simples aux cellules. Maintenant, nous ajouterons des formules. Les développeurs peuvent utiliser la propriété Value d'une cellule pour accéder et modifier la formule ou sinon la méthode **SetCellValue** de la cellule peut également être utilisée pour ajouter ou modifier la formule dans une cellule.

**IMPORTANT :** La différence fondamentale entre l'utilisation de la propriété Value ou de la méthode **SetCellValue** d'une cellule est que la propriété Value invoque automatiquement la méthode **RunAllFormulas** de Grid pour recalculer les valeurs de toutes les formules, tandis que dans le cas de la méthode **SetCellValue**, les développeurs doivent appeler explicitement la méthode **RunAllFormulas** après avoir ajouté les formules aux cellules. En fait, lorsque nous utilisons la méthode **SetCellValue** d'une cellule, cette méthode définit la valeur de la cellule uniquement sur **FormulaType** et ne calcule pas la formule. De plus, appeler la méthode **RunAllFormulas** à chaque fois n'est pas nécessaire. Si vous souhaitez ajouter de nombreuses formules dans les cellules d'une feuille de calcul, vous pouvez appeler la méthode **RunAllFormulas** une seule fois à la fin.

Une formule est ajoutée à une cellule sous forme de valeur de chaîne. De plus, la structure de la formule doit être compatible avec la structure de la formule de MS Excel. Toutes les formules doivent commencer par un signe égal (=).

Dans l'exemple ci-dessous, nous avons ajouté une formule pour multiplier les valeurs de deux cellules de la feuille de calcul et stocker le résultat dans une autre cellule. La méthode **RunAllFormulas** est également invoquée à la fin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Maintenant, exécutez l'application. Si vous double-cliquez sur la cellule où la formule a été ajoutée, vous remarquerez que la valeur sera remplacée par la formule qui calcule réellement la valeur en arrière-plan.

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop prend en charge la plupart des fonctions couramment utilisées dans MS Excel. Pour plus de détails sur la liste des fonctions prises en charge, veuillez [cliquer ici.](/cells/fr/net/liste-des-fonctions-prise-en-charge/)

{{% /alert %}}
