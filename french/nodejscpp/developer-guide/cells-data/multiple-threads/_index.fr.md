---
title: Lecture des valeurs de cellule dans plusieurs threads simultanément
linktitle: Plusieurs threads
type: docs
weight: 1800
url: /fr/nodejs-cpp/reading-cell-values-in-multiple-threads-simultaneously/
description: Apprenez comment lire les valeurs des cellules dans plusieurs threads simultanément via l’API Aspose.Cells for Node.js via C++.
keywords: Lecture des valeurs de cellules dans plusieurs threads simultanément via Node.js en C++, Aspose.Cells C++ Multithreads, Lecture des données dans plusieurs threads
---

{{% alert color="primary" %}}

La nécessité de lire les valeurs de cellule dans plusieurs threads simultanément est une exigence courante. Cet article explique comment utiliser Aspose.Cells à cette fin.

{{% /alert %}}

Pour lire les valeurs des cellules dans plus d’un thread simultanément, définissez [**Cells.setMultiThreadReading(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setMultiThreadReading-boolean-) sur **true**. Sinon, vous risquez d’obtenir des mauvaises valeurs de cellules.

Le code suivant :

1. Crée un classeur.
1. Ajoute une feuille de calcul.
1. Remplit la feuille de calcul avec des valeurs de chaîne.
1. Crée ensuite deux threads qui lisent simultanément les valeurs de cellules aléatoires.
   Si les valeurs lues sont correctes, rien ne se passe. Si les valeurs lues sont incorrectes, un message est affiché.

Si vous commentez cette ligne :

{{< highlight javascript >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

alors le message suivant est affiché :

{{< highlight javascript >}}

if (s !== "R" + row + "C" + col)
{
    console.log("This message box will show up when cells read values are incorrect.");
}

{{< /highlight >}}

Sinon, le programme s'exécute sans afficher de message, ce qui signifie que toutes les valeurs lues dans les cellules sont correctes.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-multiple-threads.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
