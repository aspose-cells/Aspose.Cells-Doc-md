---
title: Ajuster automatiquement la hauteur de la ligne lorsque le fichier est chargé
type: docs
weight: 120
url: /fr/net/autofit-row-height/
description: Apprenez à ajuster les lignes dont la hauteur n est pas personnalisée.
keywords: Ajuster automatiquement la hauteur de la ligne lors du chargement du fichier, ajuster automatiquement la hauteur de la ligne lors de l ouverture du fichier Excel. 
---

## **Scénarios d'utilisation possibles**
La hauteur de la ligne correspond automatiquement à la police du contenu, mais lorsque la hauteur de la ligne mise en cache ne correspond pas à la hauteur du contenu dans le fichier, MS Excel ajustera automatiquement la hauteur de la ligne lors du chargement du fichier, tandis qu'Aspose.Cells ne l'ajustera pas automatiquement pour améliorer les performances. Si vous avez besoin d'utiliser le programme Aspose.Cells pour ajuster automatiquement les hauteurs de ligne lors du chargement des fichiers, vous pouvez atteindre cet objectif en utilisant le paramètre [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Veuillez vous référer aux données d'image suivantes. Nous pouvons observer que la hauteur de la ligne mise en cache dans la ligne 11 est de 15, mais Excel a ajusté automatiquement la hauteur de la ligne lors du chargement du fichier.
<br>
<img src="1.png" width=70% />

## **Ajuster la hauteur de la ligne en utilisant Aspose.Cells**
Si vous chargez directement le fichier et le sauvegardez en PDF, les données ne seront pas entièrement affichées dans le PDF car sa hauteur de ligne mise en cache est seulement de 15.
<br>
<img src="2.png" width=70% />
<br>
Si vous définissez le paramètre [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) sur true lors du chargement du fichier, alors Aspose.Cells ajustera automatiquement la hauteur de la ligne. La hauteur de la ligne ajustée peut répondre efficacement aux exigences d'affichage du texte.
<br>
<img src="3.png" width=70% />

## **Code d'exemple C#**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
