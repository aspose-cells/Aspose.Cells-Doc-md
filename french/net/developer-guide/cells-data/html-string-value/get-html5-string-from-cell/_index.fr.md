---
title: Obtenez la chaîne HTML5 du Cell
type: docs
weight: 90
url: /fr/net/get-html5-string-from-cell/
description: Découvrez comment obtenir une chaîne HTML5 du Cell au Aspose.Cells for .NET API.
keywords: Get HTML5 string from Cell, Obtain HTML5 string from Cell, Manage HTML5 string of Cell
---
##  **Scénarios d'utilisation possibles**

Aspose.Cells renvoie la chaîne HTML de la cellule en utilisant le[**ObtenirHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring) méthode qui accepte un paramètre booléen. Si tu réussis**FAUX** en paramètre, il renverra Normal HTML mais si vous passez**vrai** en tant que paramètre, il renverra une chaîne HTML5.

##  **Obtenez la chaîne HTML5 du Cell**

L'exemple de code suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille de calcul. Il obtient ensuite la chaîne Normal HTML et HTML5 de la cellule A1 en utilisant le[**ObtenirHtmlString**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/gethtmlstring)et les imprime sur la console.

##  **Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-GetHTML5StringFromCell.cs" >}}

##  **Sortie console**

{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
