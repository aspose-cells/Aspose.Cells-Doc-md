---
title: Convertir des dates en dates japonaises avec Python.NET
linktitle: Convertir les dates en dates japonaises
type: docs
weight: 350
url: /fr/python-net/convert-dates-to-japanese-dates/
description: Apprenez à convertir des dates grégoriennes en dates japonaises dans les fichiers Excel en utilisant Aspose.Cells pour Python via .NET.
---

{{% alert color="primary" %}} 

Dans le calendrier japonais, une nouvelle ère commence avec le règne d’un nouveau empereur. Le 1er mai 2019, un nouveau empereur est monté sur le trône, marquant la fin de l’ère Heisei et le début de l’ère Reiwa.

{{% /alert %}} 

Aspose.Cells fournit un moyen de convertir les dates grégoriennes en dates japonaises en tenant compte des changements d’ère. Le fragment de code suivant montre comment convertir un fichier Excel source contenant des dates grégoriennes en un PDF avec des dates japonaises :

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

```python
import os
from aspose.cells import Workbook, LoadOptions, LoadFormat, SaveFormat, CountryCode

# Source directory
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Create output directory if not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize load options with XLSX format
options = LoadOptions(LoadFormat.XLSX)
options.region = CountryCode.JAPAN

# Load workbook with Japanese regional settings
workbook = Workbook(os.path.join(source_dir, "JapaneseDates.xlsx"), options)

# Save as PDF
workbook.save(os.path.join(output_dir, "JapaneseDates.pdf"), SaveFormat.PDF)
```

**Conversion Python.NET :**


Remarque : Assurez-vous que la prise en charge de la langue japonaise est activée dans votre environnement pour des conversions d’ère précises. La classe [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) et les [Options d’enregistrement en PDF](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) offrent les fonctionnalités nécessaires à cette conversion.
