---
title: Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul
type: docs
weight: 50
url: /fr/python-net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Vous découvrirez dans cet article comment obtenir la largeur et la hauteur du papier de la configuration de la page de la feuille Excel en utilisant du code Python avec l API ou la bibliothèque Aspose.Cells pour Python via .NET.
keywords: Bibliothèque Excel en Python, largeur du papier dans la configuration de la page Excel, hauteur du papier dans la configuration de la page Excel en Python.
---

## **Scénarios d'utilisation possibles**

Parfois, vous devez connaître la largeur et la hauteur du format de papier tel qu'il a été défini dans la configuration de page de la feuille de calcul. Veuillez utiliser les propriétés [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) et [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height) à cet effet.

## **Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul**

Le code d'exemple suivant explique l'utilisation des propriétés [**PageSetup.paper_width**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_width) et [**PageSetup.paper_height**](https://reference.aspose.com/cells/python-net/aspose.cells/pagesetup/paper_height). Il modifie d'abord la taille du papier en *A2*, puis trouve la largeur et la hauteur du papier, et la modifie en *A3*, *A4*, *Lettres* tout en trouvant la largeur et la hauteur respectives du papier.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-PageSetupFeatures-GetPageDimensions.py" >}}

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
