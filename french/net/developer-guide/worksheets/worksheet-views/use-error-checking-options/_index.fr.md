---
title: Utiliser les options de vérification des erreurs
type: docs
weight: 140
url: /fr/net/use-error-checking-options/
---
{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de définir des options et des règles de vérification des erreurs. Les utilisateurs voient souvent des contrôles d'erreur lors de la création de formules, un petit triangle dans le coin supérieur droit d'une cellule met en évidence lorsqu'il y a un problème avec une cellule. Excel fournit des informations qui aident les utilisateurs à corriger les problèmes courants.

{{% /alert %}}

## **Types d'erreurs**

Les erreurs qui signifient que la formule ne peut pas renvoyer de résultat, comme la division d'un nombre par zéro, nécessitent une attention immédiate et une valeur d'erreur s'affiche dans la cellule. Cliquer sur le triangle vert affiche un point d'exclamation, cliquer dessus ouvre une liste d'options.

L'erreur peut être résolue à l'aide des options ou être ignorée. Ignorer une erreur signifie que cette erreur n'apparaîtra pas dans les contrôles d'erreur ultérieurs.

 Aspose.Cells fournit des fonctionnalités d'option de vérification des erreurs. Le[**ErreurVérifierOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption) La classe gère différents types de contrôles d'erreur, par exemple, les nombres stockés sous forme de texte, les erreurs de calcul de formule et les erreurs de validation. Utilisez le[**ErreurVérifierType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype)énumération pour définir la vérification d'erreur souhaitée.

## **Numbers stocké sous forme de texte**

Parfois, les nombres peuvent être formatés et stockés dans des cellules sous forme de texte. Cela peut entraîner des problèmes de calcul ou produire des ordres de tri déroutants. Numbers formatés en tant que texte sont alignés à gauche au lieu d'être alignés à droite dans la cellule. Si une formule qui doit effectuer une opération mathématique sur des cellules ne renvoie pas de valeur, vérifiez l'alignement dans les cellules auxquelles la formule fait référence - certaines ou toutes ces cellules peuvent être des nombres au format texte.

Vous pouvez utiliser les options de vérification des erreurs pour convertir rapidement les nombres stockés sous forme de texte en nombres réels. Dans Excel Microsoft 2003 :

1.  Sur le**Outils** menu, cliquez sur**Choix**.
1. Sélectionnez l'onglet Vérification des erreurs.
   **Numéro stocké sous forme de texte** option est cochée par défaut.
1. Désactivez-le.

L'exemple de code suivant montre comment désactiver les nombres stockés en tant qu'option de vérification des erreurs de texte pour une feuille de calcul dans le fichier de modèle XLS à l'aide des API Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
