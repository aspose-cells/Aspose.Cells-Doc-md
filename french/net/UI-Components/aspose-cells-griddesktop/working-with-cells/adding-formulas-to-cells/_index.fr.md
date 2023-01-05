---
title: Ajout de formules au Cells
type: docs
weight: 30
url: /fr/net/adding-formulas-to-cells/
---
{{% alert color="primary" %}} 

Une cellule ne peut pas seulement contenir une simple valeur comme un chiffre ou du texte, mais nous pouvons également insérer une formule dans une cellule comme valeur. Une formule est utilisée dans une cellule lorsque la valeur d'une cellule doit être déterminée après certains calculs. Dans cette rubrique, nous verrons comment accéder et modifier une formule appliquée sur une cellule.

{{% /alert %}} 
## **Ajouter une formule à un Cell**
 Ajouter une formule à une cellule revient à définir la valeur d'une cellule, comme nous l'avons vu dans notre sujet précédent :[Accès et modification de la valeur d'un Cell](/cells/fr/net/accessing-and-modifying-the-value-of-a-cell/) sauf que dans ce cas, nous avons simplement ajouté des valeurs simples aux cellules. Maintenant, nous allons ajouter des formules. Les développeurs peuvent utiliser la propriété Value d'une cellule pour accéder et modifier la formule ou autrement**DéfinirValeurCellule** La méthode de la cellule peut également être utilisée pour ajouter ou modifier la formule dans une cellule.

**IMPORTANT:** La différence fondamentale entre l'utilisation de la propriété Value ou**DéfinirValeurCellule** méthode d'une cellule est que la propriété Value appelle**ExécuterToutesFormules** méthode de Grille automatiquement pour recalculer les valeurs de toutes les formules où, comme dans le cas de**DéfinirValeurCellule** les développeurs de méthodes doivent appeler**ExécuterToutesFormules** méthode explicitement après que les formules ont été ajoutées aux cellules. En fait, lorsque nous utilisons**DéfinirValeurCellule** méthode d'une cellule, cette méthode définit la valeur de la cellule sur**Type de formule** seulement et ne calculez pas la formule. De plus, appeler**ExécuterToutesFormules**méthode à chaque fois n'est pas nécessaire. Si vous souhaitez ajouter de nombreuses formules dans les cellules d'une feuille de calcul, vous pouvez appeler**ExécuterToutesFormules** méthode une seule fois à la fin.

 Une formule est ajoutée à une cellule en tant que valeur de chaîne. De plus, la structure de formule doit être compatible avec la structure de formule de MS Excel. Toutes les formules doivent commencer par un**Signe égal (=)**.

 Dans l'exemple ci-dessous, nous avons ajouté une formule pour multiplier les valeurs de deux cellules de la feuille de calcul et stocker le résultat dans une autre cellule.**ExécuterToutesFormules** La méthode est également invoquée à la fin.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AddingCellFormulas-1.cs" >}}



Exécutez maintenant l'application. Si vous double-cliquez sur la cellule où la formule a été ajoutée, vous remarquerez que la valeur sera remplacée par la formule qui calcule réellement la valeur sur le back-end.

{{% alert color="primary" %}} 

 Aspose.Cells.GridDesktop prend en charge la plupart des fonctions couramment utilisées de MS Excel. Pour plus de détails sur la liste des fonctions prises en charge, veuillez[Cliquez ici.](/cells/fr/net/list-of-supported-functions/)

{{% /alert %}}
