---
title: Appliquer un ombrage à des lignes et des colonnes alternatives avec une mise en forme conditionnelle
description: Comment utiliser la bibliothèque Aspose.Cells dans C# pour appliquer des ombres de mise en forme conditionnelle pour alterner les lignes et les colonnes. En ajustant ces critères, vous avez plus de contrôle sur l’apparence et l’apparence des cellules.
keywords: Aspose.Cells, Conditional Formatting, C#, Alternate Rows, Alternate Columns, Shadows
type: docs
weight: 30
url: /fr/net/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---
{{% alert color="primary" %}}

 Aspose.Cells Les API fournissent les moyens d'ajouter et de manipuler des règles de formatage conditionnel pour le[**Feuille de travail**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)objet. Ces règles peuvent être adaptées de plusieurs manières pour obtenir le formatage souhaité en fonction de conditions ou de règles. Cet article démontrera l'utilisation des API Aspose.Cells for .NET pour appliquer un ombrage à des lignes et des colonnes alternées à l'aide de règles de mise en forme conditionnelle et des fonctions intégrées d'Excel.

{{% /alert %}}

Cet article utilise les fonctions intégrées d'Excel telles que ROW, COLUMN et MOD. Voici quelques détails de ces fonctions pour une meilleure compréhension de l'extrait de code fourni ci-dessus.

- **ROW()** La fonction renvoie le numéro de ligne d'une référence de cellule. Si le paramètre de référence est omis, il suppose que la référence est l'adresse de cellule dans laquelle la fonction ROW a été saisie.
- **COLUMN()**La fonction renvoie le numéro de colonne d’une référence de cellule. Si le paramètre de référence est omis, il suppose que la référence est l'adresse de cellule dans laquelle la fonction COLONNE a été saisie.
- **MOD()** La fonction renvoie le reste après qu'un nombre est divisé par un diviseur, où le premier paramètre de la fonction est la valeur numérique dont vous souhaitez trouver le reste et le deuxième paramètre est le nombre utilisé pour diviser en paramètre numérique. Si le diviseur est 0, alors il renverra le #DIV/0 ! erreur.

Commençons par écrire du code pour atteindre cet objectif avec l'aide de Aspose.Cells for .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageConditionalFormatting-ApplyShadingToAlternateRowsColumns-1.cs" >}}

L'instantané suivant montre la feuille de calcul résultante chargée dans l'application Excel.

|![tâche : image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

 Afin d'appliquer l'ombrage aux colonnes alternatives, il suffit de changer la formule**=MOD(LIGNE(),2)=0** comme *=MOD(COLUMN(),2)=0**, c'est-à-dire ; au lieu d'obtenir l'index de ligne, modifiez la formule pour récupérer l'index de colonne.
La feuille de calcul résultante, dans ce cas, ressemblera à ceci.

|![tâche : image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
