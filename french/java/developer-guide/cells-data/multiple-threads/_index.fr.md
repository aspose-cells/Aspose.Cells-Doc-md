---
title: Lecture simultanée des valeurs Cell dans plusieurs threads
linktitle: Plusieurs fils de discussion
type: docs
weight: 1100
url: /fr/java/reading-cell-values-in-multiple-threads-simultaneously/
description: Découvrez comment lire les valeurs Cell dans plusieurs threads simultanément avec les API Aspose.Cells for Java.
keywords: Java Read Cell Values in Multiple Threads Simultaneously, Multiple Threads for Aspose.Cells for Java APIs.
---
{{% alert color="primary" %}}

La nécessité de lire simultanément les valeurs des cellules dans plusieurs threads est une exigence courante. Cet article explique comment utiliser le Aspose.Cells à cet effet.

{{% /alert %}}

##  **Comment lire les valeurs Cell dans plusieurs threads simultanément avec Aspose.Cells for Java**

 Pour lire les valeurs des cellules dans plusieurs threads simultanément, définissez[**Feuille de travail.getCells().setMultiThreadReading()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MultiThreadReading)à *vrai**. Si vous ne le faites pas, vous risquez d'obtenir des valeurs de cellule erronées. Veuillez noter que certaines fonctionnalités telles que le formatage des valeurs de cellule ne sont pas prises en charge pour plusieurs threads. Ainsi, MultiThreadReading vous permet uniquement d'accéder aux données originales de la cellule. Dans un environnement à plusieurs threads, si vous essayez d'obtenir la valeur formatée de la cellule, par exemple avec Cell.getStringValue() pour les valeurs numériques, vous risquez d'obtenir un résultat ou une exception inattendue.

Le code suivant :

1. Crée un classeur.
1. Ajoute une feuille de calcul.
1. Remplit la feuille de calcul avec des valeurs de chaîne.
1. Il crée ensuite deux threads qui lisent simultanément les valeurs de cellules aléatoires.
 Si les valeurs lues sont correctes, rien ne se passe. Si les valeurs lues sont incorrectes, alors un message s'affiche.

Si vous commentez cette ligne :

{{< highlight "java" >}}

testWorkbook.getWorksheets().get(0).getCells().setMultiThreadReading(true);

{{< /highlight >}}

alors le message suivant s'affiche :

{{< highlight "java" >}}

if (s.equals("R" + row + "C" + col)!=true)

{

    System.out.println("This message box will show up when cells read values are incorrect.");

}

{{< /highlight >}}

Sinon, le programme s'exécute sans afficher aucun message, ce qui signifie que toutes les valeurs lues dans les cellules sont correctes.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ThreadProc-ThreadProc.java" >}}
