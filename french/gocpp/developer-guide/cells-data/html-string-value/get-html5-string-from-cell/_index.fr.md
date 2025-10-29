---
title: Obtenir la chaîne HTML5 à partir d une cellule avec Golang via C++
linktitle: Obtenir la chaîne HTML5 de la cellule
type: docs
weight: 90
url: /fr/go-cpp/get-html5-string-from-cell/
description: Apprenez comment obtenir la chaîne HTML5 d une cellule en utilisant l API Aspose.Cells for C++.
keywords: Obtenir une chaîne HTML5 de la cellule, Obtenir une chaîne HTML5 de la cellule, Gérer une chaîne HTML5 de cellule
---

## **Scénarios d'utilisation possibles**

Aspose.Cells retourne la chaîne HTML de la cellule en utilisant la méthode [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) qui accepte un paramètre booléen. Si vous passez **false** en paramètre, il retournera le HTML Normal mais si vous passez **true**, il retournera la chaîne HTML5.

## **Obtenir la chaîne HTML5 de la cellule**

Le code d'exemple suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille de calcul. Ensuite, il récupère la chaîne HTML normale et HTML5 de la cellule A1 à l'aide de la méthode [**GetHtmlString**](https://reference.aspose.com/cells/go-cpp/cell/gethtmlstring/) et les imprime dans la console.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetHtml5StringFromCell.go" >}}
## **Sortie console**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
