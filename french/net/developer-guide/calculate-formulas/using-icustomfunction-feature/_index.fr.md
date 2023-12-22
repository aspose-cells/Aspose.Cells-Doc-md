---
title: Utilisation de la fonctionnalité ICustomFunction
description: Cet article décrit comment créer une fonction personnalisée dans Excel Microsoft à l'aide de la fonctionnalité ICustomFunction de la bibliothèque Aspose.Cells. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour définir et enregistrer des fonctions personnalisées et obtenir les résultats. Enfin, nous enregistrons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions
type: docs
weight: 30
url: /fr/net/using-icustomfunction-feature/
---
{{% alert color="primary" %}} 

Cet article fournit une compréhension détaillée de la façon d’utiliser la fonctionnalité ICustomFunction pour implémenter des fonctions personnalisées avec les API Aspose.Cells.

L'interface ICustomFunction permet d'ajouter des fonctions de calcul de formule personnalisées pour étendre le moteur de calcul de base Aspose.Cells' afin de répondre à certaines exigences. Cette fonctionnalité est utile pour définir des fonctions personnalisées (définies par l'utilisateur) dans un fichier modèle ou dans du code où la fonction personnalisée peut être implémentée et évaluée à l'aide des API Aspose.Cells comme toute autre fonction Excel Microsoft par défaut.

 Attention, cette interface a été remplacée par[RésuméCalculMoteur](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) et sera supprimé à l'avenir. Quelques articles/exemples techniques sur le nouveau API :[ici](/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) et[ici](/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
##  **Création et évaluation d'une fonction définie par l'utilisateur**
 Cet article montre l'implémentation de l'interface ICustomFunction pour écrire une fonction personnalisée et l'utiliser dans la feuille de calcul pour obtenir les résultats. Nous définirons une fonction personnalisée par son nom**MaFonction** qui acceptera 2 paramètres avec les détails suivants.

- Le 1er paramètre fait référence à une seule cellule
- Le 2ème paramètre fait référence à une plage de cellules

La fonction personnalisée ajoutera toutes les valeurs de la plage de cellules spécifiée comme 2ème paramètre et divisera le résultat avec la valeur du 1er paramètre.

Voici comment nous avons implémenté la méthode CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Voici comment utiliser la fonction nouvellement définie dans une feuille de calcul



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
##  **Aperçu**
Les API Aspose.Cells placent simplement l'objet ReferredArea dans la "paramsList" lorsque le paramètre correspondant est une référence ou que son résultat calculé est une référence. Si vous avez besoin de la référence elle-même, vous pouvez utiliser directement ReferredArea. Si vous avez besoin d'obtenir la valeur d'une seule cellule à partir de la référence correspondant à la position de la formule, vous pouvez utiliser la méthode ReferredArea.GetValue(rowOffset, int colOffset). Si vous avez besoin d'un tableau de valeurs de cellules pour toute la zone, vous pouvez utiliser la méthode ReferredArea.GetValues.

Comme les API Aspose.Cells donnent la ReferredArea dans "paramsList", la ReferredAreaCollection dans "contextObjects" ne sera plus nécessaire (dans les anciennes versions, il n'était pas toujours possible de donner une carte un à un aux paramètres de la fonction personnalisée), donc il a été supprimé des "contextObjects".

{{< highlight "java" >}}

 public object CalculateCustomFunction(string functionName, ArrayList paramsList, ArrayList contextObjects)

{

    ...

    object o = paramsList[i];

    if(o is ReferredArea) //fetch data from reference

    {

        ReferredArea ra = (ReferredArea)o;

        if(ra.IsArea)

        {

            o = ra.GetValues();

        }

        else

        {

            o = ra.GetValue(0, 0);

        }

    }

    if (o is Array)

    {

        ...

    }

    else if...

    ...

}

{{< /highlight >}}
