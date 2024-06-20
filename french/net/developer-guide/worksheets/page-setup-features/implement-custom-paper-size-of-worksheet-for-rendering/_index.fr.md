---
title: Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu
type: docs
weight: 70
url: /fr/net/implement-custom-paper-size-of-worksheet-for-rendering/
description: Cet article explique comment utiliser le code d exemple de l API C# ou de la bibliothèque .NET pour définir une taille de papier personnalisée de vos feuilles de calcul souhaitées lors du rendu d un fichier Excel au format PDF de manière programmable.
keywords: Définir une taille de papier personnalisée lors du rendu d Excel en PDF en c#
---

## **Scénarios d'utilisation possibles**

Il n'existe pas d'option directe pour créer des tailles de papier personnalisées dans MS Excel, cependant, vous pouvez définir une taille de papier personnalisée de vos feuilles de calcul souhaitées lors du rendu d'un fichier Excel au format PDF. Ce document explique comment définir une taille de papier personnalisée d'une feuille de calcul en utilisant les API Aspose.Cells.

## **Implémenter une taille de papier personnalisée de la feuille de calcul pour le rendu**

Aspose.Cells vous permet de mettre en œuvre la taille de feuille de calcul souhaitée. Vous pouvez utiliser la méthode [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) de la classe [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) pour spécifier une taille de page personnalisée. Le code d'exemple suivant illustre comment spécifier une taille de papier personnalisée pour la première feuille de calcul dans le classeur. Veuillez également consulter le [PDF généré](45056028.pdf) avec le code suivant pour une référence.

## **Capture d'écran**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
