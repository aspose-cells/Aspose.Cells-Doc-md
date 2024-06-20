---
title: Obtenir la chaîne HTML5 à partir de la cellule
type: docs
weight: 90
url: /fr/python-net/get-html5-string-from-cell/
description: Apprenez comment obtenir une chaîne HTML5 à partir de la cellule grâce à la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Python Excel Library, Python Obtenez la chaîne HTML5 à partir de la cellule, Obtenez la chaîne HTML5 à partir de la cellule en utilisant Python, Gérez la chaîne HTML5 de la cellule en Python.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells for Python via .NET retourne la chaîne HTML de la cellule en utilisant la méthode [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) qui accepte un paramètre booléen. Si vous passez **false** en tant que paramètre, cela renverra le HTML normal mais si vous passez **true** en tant que paramètre, cela renverra la chaîne HTML5.

## **Obtenir une chaîne HTML5 à partir de la cellule**

Le code d'exemple suivant crée un objet classeur et ajoute du texte dans la cellule A1 de la première feuille de calcul. Ensuite, il récupère la chaîne HTML normale et HTML5 de la cellule A1 à l'aide de la méthode [**get_html_string(html5)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_html_string/#bool) et les imprime dans la console.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetHTML5StringFromCell.py" >}}

## **Sortie console**

{{< highlight java >}}

 Normal:

<Font Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</Font>

Html5:

<div Style="FONT-FAMILY: Arial;FONT-SIZE: 10pt;COLOR: #000000;">This is some text.</div>

{{< /highlight >}}
