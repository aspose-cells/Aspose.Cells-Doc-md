---
title: Comment rendre une série invisible avec Python.NET
linktitle: Comment définir une série comme invisible
type: docs
weight: 74
url: /fr/python-net/how-to-set-series-invisible/
description: Apprenez comment masquer les séries de graphiques dans Excel en utilisant Aspose.Cells pour Python via .NET avec ce guide étape par étape.
keywords: Python excel chart, cacher série, propriété is_filtered, Aspose.Cells Python
---

## **Comment rendre une série invisible dans un graphique Excel**

Dans un graphique Excel, vous pouvez faire un clic droit sur un graphique, cliquer sur "Sélectionner les données" et, dans la fenêtre pop-up, définir si une série est visible en cochant ou décochant la case correspondante.
Vous pouvez télécharger le [fichier d'exemple](SeriesFiltered.xlsx) suivant et l'utiliser dans Excel comme illustré dans la figure pour réaliser cette fonction. Ensuite, nous vous montrerons comment accomplir cela en utilisant la bibliothèque Aspose.Cells pour Python via .NET.

![todo:image_alt_text](series-invisible.png)

## **Comment rendre une série invisible avec Aspose.Cells**

Utilisez le code suivant pour rendre une série invisible avec Aspose.Cells pour Python via .NET :

```python
import os
from aspose.cells import Workbook

current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Load sample workbook
workbook = Workbook(os.path.join(data_dir, "SeriesFiltered.xlsx"))

# Access charts from first worksheet
charts = workbook.worksheets[0].charts
chart = charts.get("Chart 1")

# Get series collections
n_series_filtered = chart.filtered_n_series
n_series = chart.n_series

# Filter series by marking them as filtered
n_series[1].is_filtered = True
n_series[0].is_filtered = True

# Save modified workbook
workbook.save(os.path.join(data_dir, "output.xlsx"))
```

Vous pouvez obtenir le [Fichier d'entrée](SeriesFiltered.xlsx) et le [Fichier de sortie](output.xlsx).

Comme indiqué dans la figure ci-dessous, les deux premières séries qui étaient initialement visibles sont devenues invisibles dans le fichier de sortie.
![todo:image_alt_text](output.png)
