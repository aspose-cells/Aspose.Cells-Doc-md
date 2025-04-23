---
title: Appliquer un ombrage aux lignes et colonnes alternées avec une mise en forme conditionnelle
description: Comment utiliser la bibliothèque Aspose.Cells en C# pour appliquer des ombres en utilisant une mise en forme conditionnelle pour les lignes et colonnes alternées. En ajustant ces critères, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, Mise en forme conditionnelle, C#, Lignes Alternées, Colonnes Alternées, Ombres
type: docs
weight: 30
url: /fr/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

Les API Aspose.Cells offrent les moyens d'ajouter et de manipuler des règles de mise en forme conditionnelle pour l'objet [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). Ces règles peuvent être adaptées de différentes manières pour obtenir la mise en forme souhaitée en fonction de conditions ou de règles. Cet article démontrera l'utilisation des API Aspose.Cells for .NET pour appliquer un ombrage aux lignes et colonnes alternées avec l'aide de règles de mise en forme conditionnelle et de fonctions intégrées à Excel.

{{% /alert %}}

Cet article utilise des fonctions intégrées à Excel telles que ROW, COLUMN & MOD. Voici quelques détails sur ces fonctions pour une meilleure compréhension de l'extrait de code fourni ci-après.

- La fonction **ROW()** renvoie le numéro de ligne d'une référence de cellule. Si le paramètre de référence est omis, il suppose que la référence est l'adresse de la cellule dans laquelle la fonction ROW a été saisie.
- La fonction **COLUMN()** renvoie le numéro de colonne d'une référence de cellule. Si le paramètre de référence est omis, il suppose que la référence est l'adresse de la cellule dans laquelle la fonction COLUMN a été saisie.
- La fonction **MOD()** retourne le reste après la division d'un nombre par un diviseur, où le premier paramètre de la fonction est la valeur numérique dont vous souhaitez trouver le reste et le deuxième paramètre est le nombre utilisé pour diviser le paramètre de nombre. Si le diviseur est 0, alors il retournera l'erreur #DIV/0!.

Commençons à écrire du code pour accomplir cet objectif avec l'aide de l'API Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

La capture d'écran suivante montre la feuille de calcul résultante chargée dans l'application Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Pour appliquer l'ombrage aux colonnes alternatives, il vous suffit de changer la formule **=MOD(ROW(),2)=0** en **=MOD(COLUMN(),2)=0**, c'est-à-dire; au lieu d'obtenir l'index de ligne, modifier la formule pour récupérer l'index de colonne. 
La feuille de calcul résultante, dans ce cas, ressemblera comme suit.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
{{< app/cells/assistant language="csharp" >}}
