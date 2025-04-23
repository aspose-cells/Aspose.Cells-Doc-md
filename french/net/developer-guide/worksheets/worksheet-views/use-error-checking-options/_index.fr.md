---
title: Utiliser les options de vérification des erreurs
type: docs
weight: 140
url: /fr/net/use-error-checking-options/
description: Dans cet article, vous trouverez un code d exemple qui utilisera de manière programmée les options de vérification des erreurs des feuilles de calcul Excel, par exemple les nombres stockés sous forme de texte à l aide de l API C# ou de la bibliothèque .NET.
keywords: stocker le numéro en tant que texte dans Excel en utilisant c#, vérifier les options Excel c#
---

{{% alert color="primary" %}}

Microsoft Excel permet aux utilisateurs de définir des options et des règles de vérification des erreurs. Les utilisateurs voient souvent des vérifications d'erreur lors de la création de formules, un petit triangle en haut à droite d'une cellule met en évidence un problème. Excel fournit des informations pour aider les utilisateurs à corriger les problèmes courants.

{{% /alert %}}

## **Types d'erreurs**

Les erreurs qui signifient que la formule ne peut pas renvoyer un résultat - comme diviser un nombre par zéro - nécessitent une attention immédiate et une valeur d'erreur est affichée dans la cellule. En cliquant sur le triangle vert apparaît un point d'exclamation, en cliquant dessus ouvre une liste d'options.

L'erreur peut être résolue à l'aide des options ou être ignorée. Ignorer une erreur signifie que cette erreur n'apparaîtra pas dans d'autres vérifications d'erreur.

Aspose.Cells fournit des fonctionnalités d'options de vérification des erreurs. La classe [**ErrorCheckOption**](https://reference.aspose.com/cells/net/aspose.cells/errorcheckoption) gère différents types de vérifications d'erreur, par exemple les nombres stockés sous forme de texte, les erreurs de calcul de formule et les erreurs de validation. Utilisez l'énumération [**ErrorCheckType**](https://reference.aspose.com/cells/net/aspose.cells/errorchecktype) pour définir la vérification d'erreur souhaitée.

## **Nombres stockés sous forme de texte**

Parfois, les nombres peuvent être formatés et stockés dans des cellules sous forme de texte. Cela peut causer des problèmes avec les calculs ou produire des ordres de tri confus. Les nombres formatés comme du texte sont alignés à gauche au lieu de droite dans la cellule. Si une formule qui devrait effectuer une opération mathématique sur des cellules ne renvoie pas de valeur, vérifiez l'alignement dans les cellules auxquelles la formule se réfère, certaines ou toutes ces cellules pourraient être des nombres formatés comme du texte.

Vous pouvez utiliser les options de vérification des erreurs pour convertir rapidement les nombres stockés sous forme de texte en nombres réels. Dans Microsoft Excel 2003 :

1. Dans le menu **Outils**, cliquez sur **Options**.
1. Sélectionnez l'onglet Vérification des erreurs.
   L'option **Nombre stocké comme texte** est activée par défaut.
1. Désactivez-la.

Le code d'exemple suivant montre comment désactiver l'option de vérification des erreurs pour les nombres stockés sous forme de texte pour une feuille de calcul dans le fichier XLS modèle à l'aide des API Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ErrorCheckingOptions-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
