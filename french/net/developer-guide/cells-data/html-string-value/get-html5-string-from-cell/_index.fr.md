---
title: Obtenir la chaîne HTML5 à partir de la cellule
type: docs
weight: 90
url: /fr/net/get-html5-string-from-cell/
description: Apprenez comment obtenir une chaîne HTML5 de la cellule à travers l API Aspose.Cells for .NET.
keywords: Obtenir une chaîne HTML5 de la cellule, Obtenir une chaîne HTML5 de la cellule, Gérer une chaîne HTML5 de cellule
---

## **Scénarios d'utilisation possibles**

Aspose.Cells retourne la chaîne HTML de la cellule en utilisant la méthode [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) qui accepte un paramètre booléen. Si vous passez **false** en tant que paramètre, il renverra un HTML normal mais si vous passez **true** en tant que paramètre, il renverra une chaîne HTML5.

## **Obtenir une chaîne HTML5 à partir de la cellule**

Le code d'exemple suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille de calcul. Ensuite, il récupère la chaîne HTML normale et HTML5 de la cellule A1 à l'aide de la méthode [**GetHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) et les imprime dans la console.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

## **Sortie console**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
