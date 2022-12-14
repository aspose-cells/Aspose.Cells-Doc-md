---
title: Tri des données de feuille de calcul
type: docs
weight: 80
url: /fr/net/sorting-worksheet-data/
---
{{% alert color="primary" %}} 

Le tri est une tâche de routine importante que nous utilisons principalement lors du traitement des données. Dans cette rubrique, nous discuterons à l'aide d'un exemple simple de la manière dont nous pouvons trier les données dans une feuille de calcul.

{{% /alert %}} 
## **Tri des données de feuille de calcul**
Pour trier les données dans une feuille de calcul à l'aide du API de Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous :

-  Créez d'abord un objet global de**CellRange** afin qu'il soit accessible n'importe où dans le cadre de votre classe
-  Créer un gestionnaire d'événements pour**SelectedCellRangeChanged** événement de**GrilleDesktop**. **SelectedCellRangeChanged** L'événement est déclenché chaque fois qu'une plage de cellules sélectionnée par un utilisateur est modifiée. Par exemple, si un utilisateur sélectionne des cellules (contenant des données à trier) alors chaque fois que sa plage de sélection changerait, cet événement serait déclenché.
-  Le gestionnaire d'événements fournit**CellRangeEventArgsCellRangeEventArgs** argument qui fournit en outre la plage de mise à jour des cellules (sélectionnée par l'utilisateur) sous la forme d'un**CellRange** objet. Donc, dans ce gestionnaire d'événements, nous assignerons ceci**CellRange** objet (contenant la plage de cellules mise à jour) au global**CellRange**objet afin qu'il puisse également être utilisé dans d'autres parties du code. Pour nous assurer que nous ne perdons pas la plage de cellules, nous écrirons le code du gestionnaire d'événements dans une condition
- Nous pouvons maintenant écrire du code pour trier les données de la feuille de travail. Tout d'abord, accédez à une feuille de calcul souhaitée
-  Créer un**TrierPlage** objet qui conservera la plage de cellules dont les données doivent être triées. Dans**TrierPlage** constructeur, nous pouvons spécifier la feuille de calcul, les indices de la ligne et de la colonne de départ, le nombre de lignes et de colonnes à trier, l'orientation du tri (comme de haut en bas ou de gauche à droite), etc.
-  Maintenant, nous pouvons appeler**Trier** méthode de**TrierPlage** objet pour effectuer le tri des données. Dans**Trier** méthode, nous pouvons spécifier l'index de la colonne ou de la ligne à trier et l'ordre de tri (qui peut être**Ascendant** ou**Descendant** selon vos besoins)
-  Enfin, on peut appeler**Invalider** méthode de**GrilleDesktop** pour redessiner les cellules.

Dans l'exemple ci-dessous, nous avons montré comment trier les données dans une colonne.

 Créez un objet global de CellRange et**SelectedCellRangeChanged**événement de GridDesktop. Maintenant, écrivez le code comme indiqué ci-dessous :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


 Maintenant, nous écrivons la méthode pour**Tri croissant** . Vous pouvez créer un bouton pour**Tri croissant** et écrivez le code ci-dessous à l'intérieur de son**Cliquez sur** Événement.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


 Enfin, nous écrivons du code pour réaliser**Tri décroissant** Fonctionnalité. Créer un**Tri décroissant** bouton et écrivez le code ci-dessous à l'intérieur de son**Cliquez sur** Événement.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
