---
title: Obtenir la chaîne HTML5 à partir de la cellule
type: docs
weight: 90
url: /fr/nodejs-cpp/get-html5-string-from-cell/
description: Apprenez comment obtenir la chaîne HTML5 d une cellule via l API Aspose.Cells for Node.js via C++.
keywords: Obtenez la chaîne HTML5 d une cellule Node.js via C++, Obtenez la chaîne HTML5 d une cellule Node.js via C++, Gérez la chaîne HTML5 d une cellule Node.js via C++
---

## **Scénarios d'utilisation possibles**

Aspose.Cells renvoie la chaîne HTML de la cellule en utilisant la méthode [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) qui accepte un paramètre booléen. Si vous passez **false** comme paramètre, il renverra le HTML normal mais si vous passez **true**, il renverra la chaîne HTML5.

## **Obtenir une chaîne HTML5 à partir de la cellule**

Le code d'exemple suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille. Il récupère ensuite la chaîne HTML normal et la chaîne HTML5 de la cellule A1 en utilisant la méthode [**Cell.getHtmlString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getHtmlString-boolean-) et les affiche dans la console.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-HtmlStringValue-GetHtml5String.js" >}}


## **Sortie console**

{{< highlight javascript >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
