---
title: Activer les propriétés CSS personnalisées lors de l’enregistrement en HTML avec Python.NET
linktitle: Activer les propriétés CSS personnalisées lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/python-net/enable-css-custom-properties-while-saving-to-html/
description: Apprenez comment activer les propriétés CSS personnalisées lors de l’enregistrement de fichiers Excel en HTML en utilisant l’API Aspose.Cells pour Python via .NET.
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML, pour les scénarios où il y a plusieurs occurrences d’une image en base64, l’utilisation des propriétés CSS personnalisées permet d’enregistrer une seule fois les données de l’image. Cela améliore les performances du HTML résultant. Utilisez l’attribut [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/) et définissez-le sur **True** lors de l’enregistrement en HTML.

![todo:image_alt_text](enable-css-custom-properties-while-saving-to-html-1.jpg)

## **Activer les propriétés personnalisées CSS lors de l'enregistrement en HTML**

Le code d’exemple suivant montre comment utiliser l’attribut [**HtmlSaveOptions.enable_css_custom_properties**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/enable_css_custom_properties/). La capture d’écran montre l’effet lorsque cette propriété n’est pas réglée sur True. Téléchargez le [fichier Excel d’exemple](50528260.xlsx) utilisé dans ce code et le [HTML de sortie](50528261.zip) généré pour référence.

## **Code d'exemple**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

# Load sample workbook
wb = Workbook(os.path.join(source_dir, "sampleEnableCssCustomProperties.xlsx"))

# Configure HTML save options
opts = HtmlSaveOptions()
opts.export_images_as_base64 = True
opts.enable_css_custom_properties = True

# Save the workbook in HTML
wb.save(os.path.join(output_dir, "outputEnableCssCustomProperties.html"), opts)
```
