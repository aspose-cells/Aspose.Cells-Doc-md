---
title: Trier les données de la feuille de calcul
type: docs
weight: 80
url: /fr/net/aspose-cells-griddesktop/sorting-worksheet-data/
keywords: GridDesktop, tri, trier, trier les données, tri de données
description: Cet article présente comment trier les données dans une feuille de calcul dans GridDesktop.
---

{{% alert color="primary" %}} 

Le tri est une tâche routine importante que nous utilisons principalement lors du traitement de données. Dans ce sujet, nous discuterons à l'aide d'un exemple simple comment nous pouvons trier les données dans une feuille de calcul.

{{% /alert %}} 
## **Trier les données de la feuille de calcul**
Pour trier les données dans une feuille de calcul en utilisant l'API d'Aspose.Cells.GridDesktop, veuillez suivre les étapes ci-dessous:

- Tout d'abord, créez un objet global de **CellRange** pour qu'il puisse être accédé n'importe où dans le contexte de votre classe
- Créez un gestionnaire d'événements pour l'événement **SelectedCellRangeChanged** de **GridDesktop**. L'événement **SelectedCellRangeChanged** est déclenché à chaque fois qu'une plage de cellules sélectionnée par un utilisateur change. Par exemple, si un utilisateur sélectionne des cellules (contenant des données à trier), alors à chaque fois que sa plage de sélection changera, cet événement sera déclenché.
- Le gestionnaire d'événements fournit un argument **CellRangeEventArgs** qui fournit en outre la plage de mise à jour des cellules (sélectionnées par l'utilisateur) sous forme d'un objet **CellRange**. Ainsi, dans ce gestionnaire d'événements, nous attribuerons cet objet **CellRange** (contenant la plage de cellules mise à jour) à l'objet global **CellRange** afin qu'il puisse également être utilisé dans d'autres parties du code. Pour nous assurer que nous ne perdons pas la plage de cellules, nous écrirons le code du gestionnaire d'événements à l'intérieur d'une condition
- Maintenant, nous pouvons écrire du code pour trier les données de la feuille de calcul. Tout d'abord, accédez à une feuille de calcul souhaitée
- Créez un objet **SortRange** qui gardera la plage de cellules dont les données doivent être triées. Dans le constructeur **SortRange**, nous pouvons spécifier la feuille de calcul, les indices de la ligne et de la colonne de début, le nombre de lignes et de colonnes à trier, l'orientation du tri (comme de haut en bas ou de gauche à droite) etc.
- Maintenant, nous pouvons appeler la méthode **Trier** de l'objet **SortRange** pour effectuer le tri des données. Dans la méthode **Trier**, nous pouvons spécifier l'indice de la colonne ou de la ligne à trier et l'ordre de tri (qui peut être **Croissant** ou **Décroissant** selon vos besoins)
- Enfin, nous pouvons appeler la méthode **Invalider** de **GridDesktop** pour redessiner les cellules.

Dans l'exemple donné ci-dessous, nous avons démontré comment trier les données dans une colonne.

Créez un objet global de CellRange et l'événement **SelectedCellRangeChanged** de GridDesktop. Maintenant, écrivez le code comme indiqué ci-dessous :



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-CheckingCellRange.cs" >}}


Maintenant, nous écrivons la méthode pour le **Tri Croissant**. Vous pouvez créer un bouton pour le **Tri Croissant** et écrire le code ci-dessous à l'intérieur de son événement **Click**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-AscendingSort.cs" >}}


Enfin, nous écrivons du code pour obtenir la fonctionnalité de **Tri Décroissant**. Créez un bouton **Tri Décroissant** et écrivez le code ci-dessous à l'intérieur de son événement **Click**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-SortData-DescendingSort.cs" >}}
