---
title: Obtenir la chaîne HTML5 à partir de la cellule
type: docs
weight: 40
url: /fr/python-java/get-html5-string-from-cell/
---

## **Obtenir une chaîne HTML5 à partir de la cellule**
En utilisant Aspose.Cells pour Python via Java, vous pouvez obtenir la chaîne HTML à partir de la cellule. Cela peut être réalisé en utilisant la méthode [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)). Si vous passez **false** comme paramètre, cela vous renverra un HTML normal, mais si vous passez **true** comme paramètre, cela vous renverra une chaîne HTML5.

Le code d'exemple suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille de calcul. Il obtient ensuite la chaîne HTML normale et HTML5 de la cellule A1 en utilisant la méthode [getHtmlString(boolean html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) et les affiche.
## **Code d'exemple**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Ce qui suit est la sortie générée par l'extrait de code fourni ci-dessus.
## **Sortie**
{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
