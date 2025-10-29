---
title: Désactiver CSS lors de l enregistrement en HTML avec Python.NET
linktitle: Désactiver CSS lors de l enregistrement en HTML
type: docs
weight: 320
url: /fr/python-net/disable-css-while-saving-to-html/
description: Apprenez comment désactiver les styles CSS lors de la sauvegarde de fichiers Excel au format HTML en utilisant l API Aspose.Cells pour Python via .NET.
---

## **Scénarios d'utilisation possibles**

Lorsque vous enregistrez votre fichier Excel en HTML d'une seule page, généralement, les éléments CSS seront intégrés dans le fichier HTML et situés dans la section HEAD. Si vous attachez ce fichier comme contenu/corps d'un email, la plupart des clients de messagerie supprimeront les éléments CSS, ce qui entraînera un rendu incorrect. L'API Aspose.Cells pour Python via .NET propose une option qui permet de désactiver optionnellement le CSS, permettant aux styles d'être appliqués directement dans les éléments HTML eux-mêmes. Si vous souhaitez définir le HTML comme contenu/corps de l'email, utilisez la propriété [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/) et réglez-la sur **True**.

## **Désactiver CSS lors de l'enregistrement en HTML**

Le code d'exemple suivant montre l'utilisation de la propriété [**HtmlSaveOptions.disable_css**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_css/).

## **Code d'exemple**

```python
import os
from aspose.cells import Workbook, HtmlSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

# Load sample workbook
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "source")
output_dir = os.path.join(current_dir, "output")

wb = Workbook(os.path.join(source_dir, "sampleDisableCss.xlsx"))

# Disable CSS
opts = HtmlSaveOptions()
opts.disable_css = True

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Save the workbook in html
wb.save(os.path.join(output_dir, "outputDisable.html"), opts)
```
{{< app/cells/assistant language="python-net" >}}
