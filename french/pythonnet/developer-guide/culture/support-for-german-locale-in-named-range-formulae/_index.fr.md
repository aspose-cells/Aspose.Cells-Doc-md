---
title: Prise en charge de la traduction des noms de plages dans la formule des plages nommées avec Python.NET
linktitle: Prise en charge de l allemand dans les formules de plage nommée
type: docs
weight: 60
url: /fr/python-net/support-for-german-locale-in-named-range-formulae/
description: Apprenez comment gérer les paramètres de localisation allemande pour les formules de plage nommée dans Excel en utilisant Aspose.Cells pour Python via .NET.
---

Les formules en anglais sont écrites dans des régions nommées. Ce fichier Excel peut être ouvert dans un environnement où la configuration système est réglée sur la locale allemande, et la formule en anglais sera traduite en allemand. Cet exemple nécessite Excel installé avec les paramètres de langue allemands et la locale système configurée sur l’allemand.

Le fichier d'exemple pour tester cette fonctionnalité peut être téléchargé depuis :  
[sampleNamedRangeTest.xlsm](73990165.xlsm)

```python
import os
from aspose.cells import Workbook

source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

name = "HasFormula"
value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))"

wb_source = Workbook(os.path.join(source_dir, "sampleNamedRangeTest.xlsm"))
ws_col = wb_source.worksheets

name_index = ws_col.names.add(name)
named_range = ws_col.names[name_index]
named_range.refers_to = value

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb_source.save(os.path.join(output_dir, "sampleOutputNamedRangeTest.xlsm"))
```
