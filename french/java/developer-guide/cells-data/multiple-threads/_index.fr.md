---
title: Lecture des valeurs de cellule dans plusieurs threads simultanément
linktitle: Plusieurs threads
type: docs
weight: 1100
url: /fr/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Apprenez comment lire les valeurs des cellules simultanément dans plusieurs threads avec les API Aspose.Cells for Java.
keywords: Lecture des valeurs des cellules simultanément dans plusieurs threads en Java, plusieurs threads pour les API Aspose.Cells for Java.
---

{{% alert color="primary" %}}

La nécessité de lire les valeurs de cellule dans plusieurs threads simultanément est une exigence courante. Cet article explique comment utiliser Aspose.Cells à cette fin.

{{% /alert %}}

## **Comment lire les valeurs des cellules simultanément dans plusieurs threads avec Aspose.Cells for Java**

Pour lire les valeurs des cellules dans plus d'un thread simultanément, définissez [**Worksheet.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading) sur **true**. Sinon, vous pourriez obtenir les mauvaises valeurs de cellule. Veuillez noter que certaines fonctionnalités telles que la mise en forme des valeurs de cellules ne sont pas prises en charge pour les multithreads. Ainsi, MultiThreadReading vous permet uniquement d'accéder aux données originales des cellules. Dans un environnement multithread, si vous essayez d'obtenir la valeur formatée de la cellule, par exemple avec Cell.getStringValue() pour les valeurs numériques, vous pourriez obtenir un résultat inattendu ou une exception.

Le code suivant :

1. Crée un classeur.
1. Ajoute une feuille de calcul.
1. Remplit la feuille de calcul avec des valeurs de chaîne.
1. Crée ensuite deux threads qui lisent simultanément les valeurs de cellules aléatoires.
   Si les valeurs lues sont correctes, rien ne se passe. Si les valeurs lues sont incorrectes, un message est affiché.

Si vous commentez cette ligne :

{{< highlight java >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

alors le message suivant est affiché :

{{< highlight java >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Sinon, le programme s'exécute sans afficher de message, ce qui signifie que toutes les valeurs lues dans les cellules sont correctes.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
