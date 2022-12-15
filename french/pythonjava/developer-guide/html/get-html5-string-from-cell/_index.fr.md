---
title: Obtenir la chaîne HTML5 de Cell
type: docs
weight: 40
url: /fr/python-java/get-html5-string-from-cell/
---
## **Obtenir la chaîne HTML5 de Cell**
En utilisant Aspose.Cells for Python via Java, vous pouvez obtenir la chaîne HTML de la cellule. Ceci peut être réalisé en utilisant le[getHtmlString(booléen html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) méthode fournie par le API. Si vous réussissez**faux**en paramètre, il vous renverra du HTML normal mais si vous passez**vrai**en tant que paramètre, il renverra la chaîne HTML5.

L'exemple de code suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille de calcul. Il obtient ensuite la chaîne HTML normal et HTML5 de la cellule A1 à l'aide de la[getHtmlString(booléen html5)](https://reference.aspose.com/cells/python/asposecells.api/cell#getHtmlString\(boolean\)) et les imprime.
## **Exemple de code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-GetHTML5StringFromCell.py" >}}

Voici la sortie générée par l'extrait de code fourni ci-dessus.
## **Production**
{{< highlight "java" >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
