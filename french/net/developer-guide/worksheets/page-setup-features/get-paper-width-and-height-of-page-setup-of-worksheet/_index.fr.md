---
title: Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul
type: docs
weight: 50
url: /fr/net/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Dans cet article, vous découvrirez comment obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul Excel à l aide du code C# de manière programmable avec une API ou une bibliothèque .NET.
keywords: excel page setup paper width c#, excel page setup paper height c#
---

## **Scénarios d'utilisation possibles**

Parfois, vous devez connaître la largeur et la hauteur du format de papier tel qu'il a été défini dans la configuration de page de la feuille de calcul. Veuillez utiliser les propriétés [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) et [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight) à cet effet.

## **Obtenir la largeur et la hauteur du papier de la configuration de page de la feuille de calcul**

Le code d'exemple suivant explique l'utilisation des propriétés [**PageSetup.PaperWidth**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperwidth) et [**PageSetup.PaperHeight**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/properties/paperheight). Il modifie d'abord la taille du papier en *A2*, puis trouve la largeur et la hauteur du papier, puis le change en *A3*, *A4*, *Letter* et trouve respectivement la largeur et la hauteur du papier.

### **Code d'exemple**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-GetPageDimensions.cs" >}}

### **Sortie console**

Voici la sortie de la console du code d'exemple ci-dessus.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
