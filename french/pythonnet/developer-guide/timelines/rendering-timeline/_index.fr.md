---
title: Rendu de la chronologie
type: docs
weight: 40
url: /fr/python-net/rendering-timeline/
description: Gérer les chronologies des fichiers Excel avec Aspose.Cells pour Python via .NET.
keywords: Aspose.Cells for Python Excel, bibliothèque Excel Python, chronologie de rendu sans Excel, rendu de la chronologie en image en utilisant la bibliothèque Aspose.Cells pour Python.
---

## **Scénarios d'utilisation possibles**
Aspose.Cells for Python via .NET prend en charge le rendu de la forme de chronologie sans utiliser Office 2013, Office 2016, Office 2019 et Office 365. Si vous convertissez votre feuille de calcul en une image ou si vous enregistrez votre classeur aux formats PDF ou HTML, vous verrez que les chronologies sont rendues correctement.

## **Comment rendre la chronologie en utilisant la bibliothèque Aspose.Cells pour Python Excel**
Le code d'exemple suivant charge le [fichier Excel d'exemple](input.xlsx) qui contient une chronologie existante. Obtenez l'objet de forme selon le nom de la chronologie, puis rendez-le en image à travers la méthode Shape.to_image(). L'image résultante est la [image de sortie](out.png) qui montre la chronologie rendue. Comme vous pouvez le constater, la chronologie a été rendue correctement et ressemble à celle du fichier Excel d'exemple.

![todo:image_alt_text](out.png)
### **Code d'exemple**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-RenderingTimeline.py" >}}

