---
title: Utilisation de la fonction ICustomFunction
description: Cet article décrit comment créer une fonction personnalisée dans Microsoft Excel en utilisant la fonction ICustomFunction dans la bibliothèque Aspose.Cells. En chargeant un fichier Excel existant ou en créant un nouveau fichier Excel, nous pouvons utiliser les méthodes fournies par Aspose.Cells pour définir et enregistrer des fonctions personnalisées et obtenir les résultats. Enfin, nous sauvegardons le fichier Excel modifié sur le disque.
keywords: Aspose.Cells, Excel, fonctionnalités ICustomFunction, fonctions personnalisées
type: docs
weight: 30
url: /fr/net/using-icustomfunction-feature/
---

{{% alert color="primary" %}} 

Cet article offre une compréhension détaillée de l'utilisation de la fonction ICustomFunction pour implémenter des fonctions personnalisées avec les API Aspose.Cells.

L'interface ICustomFunction permet d'ajouter des fonctions de calcul de formule personnalisées pour étendre le moteur de calcul central d'Aspose.Cells afin de répondre à certaines exigences. Cette fonctionnalité est utile pour définir des fonctions personnalisées (définies par l'utilisateur) dans un fichier modèle ou dans un code où la fonction personnalisée peut être mise en œuvre et évaluée à l'aide des API Aspose.Cells comme toute autre fonction par défaut d'Excel.

Veuillez noter que cette interface a été remplacée par [AbstractCalculationEngine](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine/) et sera supprimée ultérieurement. Quelques articles/ exemples techniques sur la nouvelle API : [ici](/cells/fr/net/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) et [ici](/cells/fr/net/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 
## **Création et évaluation d'une fonction définie par l'utilisateur**
Cet article présente la mise en œuvre de l'interface ICustomFunction pour écrire une fonction personnalisée et l'utiliser dans la feuille de calcul pour obtenir les résultats. Nous définirons une fonction personnalisée nommée **MyFunc** qui acceptera 2 paramètres avec les détails suivants.

- Le 1er paramètre fait référence à une seule cellule
- Le 2ème paramètre fait référence à une plage de cellules

La fonction personnalisée ajoutera toutes les valeurs de la plage de cellules spécifiée en tant que 2ème paramètre et divisera le résultat par la valeur du 1er paramètre.

Voici comment nous avons implémenté la méthode CalculateCustomFunction.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-ICustomFunction.cs" >}}


Voici comment utiliser la nouvelle fonction définie dans une feuille de calcul



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-UsingICustomFunctionfeature-UsingICustomFunctionFeature.cs" >}}
## **Vue d'ensemble**
Les API Aspose.Cells placent simplement l'objet ReferredArea dans la "paramsList" lorsque le paramètre correspondant est une référence ou que son résultat calculé est une référence. Si vous avez besoin de la référence elle-même, vous pouvez utiliser directement ReferredArea. Si vous avez besoin d'obtenir la valeur d'une seule cellule à partir de la référence correspondant à la position de la formule, vous pouvez utiliser la méthode ReferredArea.GetValue(rowOffset, int colOffset). Si vous avez besoin d'un tableau de valeurs de cellules pour l'ensemble de la zone, vous pouvez utiliser la méthode ReferredArea.GetValues.

Comme les API Aspose.Cells fournissent ReferredArea dans "paramsList", la collection ReferredArea dans "contextObjects" ne sera plus nécessaire (dans les anciennes versions, elle n'était pas toujours capable de donner une correspondance un à un avec les paramètres de la fonction personnalisée) et a donc été supprimée des "contextObjects".

{{< highlight java >}}

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
