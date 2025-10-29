---
title: Ajuster automatiquement la hauteur de la ligne lorsque le fichier est chargé
type: docs
weight: 120
url: /fr/python-net/autofit-row-height/
description: Apprenez comment ajuster les lignes dont la hauteur n est pas personnalisée via l API Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel Python, Ajustement automatique de la hauteur de ligne en Python lors du chargement du fichier, Ajustement automatique de la hauteur de ligne en Python lors de l ouverture d un fichier Excel. 
---

## **Scénarios d'utilisation possibles**
La hauteur de la ligne correspond automatiquement à la police du contenu, mais lorsque la hauteur de la ligne mise en cache ne correspond pas à la hauteur du contenu dans le fichier, MS Excel ajustera automatiquement la hauteur de la ligne lors du chargement du fichier, tandis que Aspose.Cells pour Python via .NET ne l'ajustera pas automatiquement pour améliorer les performances. Si vous avez besoin d'utiliser le programme Aspose.Cells pour Python via .NET pour correspondre automatiquement aux hauteurs de ligne lors du chargement de fichiers, vous pouvez réaliser l'objectif en utilisant le paramètre [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/).

Veuillez vous référer aux données d'image suivantes. Nous pouvons observer que la hauteur de la ligne mise en cache dans la ligne 11 est de 15, mais Excel a ajusté automatiquement la hauteur de la ligne lors du chargement du fichier.
<br>
<img src="1.png" width=70% />

## **Ajuster la hauteur des lignes à l'aide de la bibliothèque Excel pour Python Aspose.Cells**
Si vous chargez directement le fichier et le sauvegardez en PDF, les données ne seront pas entièrement affichées dans le PDF car sa hauteur de ligne mise en cache est seulement de 15.
<br>
<img src="2.png" width=70% />
<br>
Si vous définissez le paramètre [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) à true lors du chargement du fichier, alors Aspose.Cells pour Python via .NET ajustera automatiquement la hauteur de la ligne. La hauteur de la ligne ajustée peut répondre efficacement aux exigences d'affichage du texte.
<br>
<img src="3.png" width=70% />

## **Code d'exemple Python**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
{{< app/cells/assistant language="python-net" >}}
