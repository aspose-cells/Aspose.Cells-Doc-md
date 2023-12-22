---
title: Ajuster automatiquement la hauteur de la ligne lors du chargement du fichier
type: docs
weight: 120
url: /fr/net/autofit-row-height/
description: Apprenez à ajuster les lignes dont la hauteur n'est pas personnalisée.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **Scénarios d'utilisation possibles**
 La hauteur de la ligne correspond automatiquement à la police du contenu, mais lorsque la hauteur de la ligne mise en cache ne correspond pas à la hauteur du contenu du fichier, MS Excel ajustera automatiquement la hauteur de la ligne lors du chargement du fichier, alors que Aspose.Cells ne le fera pas. ajustez-le automatiquement pour améliorer les performances. Si vous devez utiliser le programme Aspose.Cells pour faire correspondre automatiquement les hauteurs de ligne lors du chargement de fichiers, vous pouvez atteindre l'objectif via le paramètre[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

Veuillez vous référer aux données d'image suivantes. Nous pouvons observer que la hauteur de ligne du cache à la ligne 11 est de 15, mais Excel a automatiquement ajusté la hauteur de ligne lors du chargement du fichier.
<br>
<img src="1.png" width=70% />

##  **Ajustez la hauteur de la rangée à l'aide de Aspose.Cells**
Si vous chargez directement le fichier et l'enregistrez sous PDF, les données ne seront pas entièrement affichées dans PDF car la hauteur de sa ligne de cache n'est que de 15.
<br>
<img src="2.png" width=70% />
<br>
 Si vous définissez le paramètre[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) sur true lors du chargement du fichier, Aspose.Cells ajustera automatiquement la hauteur de ligne. La hauteur de ligne ajustée peut répondre efficacement aux exigences d'affichage du texte.
<br>
<img src="3.png" width=70% />

##  **C# Exemple de code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}