---
title: Obtenir la chaîne HTML5 de Cell
type: docs
weight: 90
url: /fr/java/get-html5-string-from-cell/
---
## **Scénarios d'utilisation possibles**

Aspose.Cells renvoie la chaîne HTML de la cellule à l'aide de la[**getHtmlString(booléen html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)méthode. Si vous passez**faux**en paramètre, il vous renverra du HTML normal mais si vous passez**vrai**en tant que paramètre, il renverra la chaîne HTML5.

## **Obtenir la chaîne HTML5 de Cell**

L'exemple de code suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille de calcul. Il obtient ensuite la chaîne HTML normal et HTML5 de la cellule A1 à l'aide de la[**getHtmlString(booléen html5)**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#HtmlString)méthode et les imprime sur la console.

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-GetHTML5StringFromCell.java" >}}

## **Sortie console**

{{< highlight "java" >}}

Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
