---
title: Lecture simultanée de valeurs Cell dans plusieurs threads
linktitle: Plusieurs fils
type: docs
weight: 1800
url: /fr/net/reading-cell-values-in-multiple-threads-simultaneously/
---
{{% alert color="primary" %}}

La nécessité de lire simultanément les valeurs des cellules dans plusieurs threads est une exigence courante. Cet article explique comment utiliser Aspose.Cells à cette fin.

{{% /alert %}}

 Pour lire les valeurs des cellules dans plusieurs threads simultanément, définissez[**Feuille de travail.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) à**vrai**. Si vous ne le faites pas, vous risquez d'obtenir les mauvaises valeurs de cellule.

Le code suivant :

1. Crée un classeur.
1. Ajoute une feuille de calcul.
1. Remplit la feuille de calcul avec des valeurs de chaîne.
1. Il crée ensuite deux threads qui lisent simultanément des valeurs à partir de cellules aléatoires.
 Si les valeurs lues sont correctes, rien ne se passe. Si les valeurs lues sont incorrectes, alors un message s'affiche.

Si vous commentez cette ligne :

{{< highlight "java" >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

alors le message suivant s'affiche :

{{< highlight "java" >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Sinon, le programme s'exécute sans afficher de message, ce qui signifie que toutes les valeurs lues dans les cellules sont correctes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
