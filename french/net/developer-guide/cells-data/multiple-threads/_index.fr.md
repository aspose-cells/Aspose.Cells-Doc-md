---
title: Lecture des valeurs de cellule dans plusieurs threads simultanément
linktitle: Plusieurs threads
type: docs
weight: 1800
url: /fr/net/reading-cell-values-in-multiple-threads-simultaneously/
description: Apprenez à lire les valeurs de cellule dans plusieurs threads simultanément grâce à l API Aspose.Cells for .NET.
keywords: Lire les valeurs de cellule dans plusieurs threads simultanément, Aspose.Cells C# Multiple Threads, Lire des données dans plusieurs threads
---

{{% alert color="primary" %}}

La nécessité de lire les valeurs de cellule dans plusieurs threads simultanément est une exigence courante. Cet article explique comment utiliser Aspose.Cells à cette fin.

{{% /alert %}}

Pour lire les valeurs de cellule dans plus d'un thread simultanément, définissez [**Worksheet.Cells.MultiThreadReading**](https://reference.aspose.com/cells/net/aspose.cells/cells/properties/multithreadreading) sur **true**. Sinon, vous pourriez obtenir les mauvaises valeurs de cellule.

Le code suivant :

1. Crée un classeur.
1. Ajoute une feuille de calcul.
1. Remplit la feuille de calcul avec des valeurs de chaîne.
1. Crée ensuite deux threads qui lisent simultanément les valeurs de cellules aléatoires.
   Si les valeurs lues sont correctes, rien ne se passe. Si les valeurs lues sont incorrectes, un message est affiché.

Si vous commentez cette ligne :

{{< highlight java >}}

 testWorkbook.Worksheets[0].Cells.MultiThreadReading = true;

{{< /highlight >}}

alors le message suivant est affiché :

{{< highlight java >}}

 if (s != "R" + row + "C" + col)

{

    MessageBox.Show("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Sinon, le programme s'exécute sans afficher de message, ce qui signifie que toutes les valeurs lues dans les cellules sont correctes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ReadingCellValuesInMultipleThreadsSimultaneously-1.cs" >}}
