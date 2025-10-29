---
title: Générer des images de mise en forme conditionnelle DataBars
description: Aspose.Cells pour Python via .NET est une bibliothèque Python pour travailler avec des fichiers de feuilles de calcul. Elle supporte la génération de barres de données et d images formatées conditionnellement, permettant aux utilisateurs de personnaliser l affichage de la feuille en fonction de la valeur des cellules. Cet article présente comment utiliser la bibliothèque Aspose.Cells pour Python pour générer des barres de données et des images formatées conditionnellement.
keywords: Aspose.Cells pour Python via .NET, Mise en forme conditionnelle, Barres de données, Images, Feuilles de calcul
type: docs
weight: 40
url: /fr/python-net/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Parfois, vous devez générer des images de Barres de données de Mise en forme conditionnelle. Vous pouvez utiliser la méthode [**DataBar.to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) d'Aspose.Cells pour générer ces images. Cet article montre comment générer une image de barre de données en utilisant Aspose.Cells pour Python via .NET.

{{% /alert %}}

Le code d'exemple suivant génère l'image DataBar de la cellule C1. Tout d'abord, il accède à l'objet de condition de format de la cellule, puis à partir de cet objet, il accède à l'objet [**DataBar**](https://reference.aspose.com/cells/python-net/aspose.cells/databar) et utilise sa méthode [**to_image()**](https://reference.aspose.com/cells/python-net/aspose.cells/databar/to_image) pour générer l'image de la cellule. Enfin, il enregistre l'image sur le disque.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GenerateDatabarImage-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
