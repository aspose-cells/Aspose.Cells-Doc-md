---
title: Comment définir un point comme Total avec Python.NET
linktitle: Comment définir un point comme total
type: docs
weight: 72
url: /fr/python-net/how-to-set-point-as-total/
description: Apprenez comment configurer les points totaux dans les graphiques en cascade Excel en utilisant Aspose.Cells pour Python via .NET avec ce guide étape par étape.
---

## **Qu'est-ce que "Définir le point comme total" dans un graphique Excel**

Dans certains graphiques Excel comme les graphiques en cascade, certains points de données représentent la somme cumulative des valeurs précédentes. Cet article démontre comment configurer ces points totaux de manière programmatique à l'aide d'Aspose.Cells.

## **Graphique en cascade nécessitant des points totaux**

![todo:image_alt_text](set-as-total1.png)

Cet exemple de graphique en cascade montre quatre points de données "Total" qui doivent agréger les valeurs précédentes. Le point "Total 2024" en surbrillance démontre un état de total non configuré dans le fichier d'origine. Téléchargez le [fichier Excel d'exemple](SampleSheet.xlsx) pour suivre le processus.

## **Configurer les points totaux avec Aspose.Cells pour Python**

Le code suivant démontre une configuration correcte du point total :

```python
import aspose.cells as cells
from aspose.cells.charts import ChartType

# Load sample workbook
workbook = cells.Workbook("SampleSheet.xlsx")

try:
    # Access first worksheet and chart
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    # Verify chart type
    if chart.type == ChartType.WATERFALL:
        # Configure chart data range
        chart.set_data_range("A1:B8", True)

        # Customize series formatting
        chart.n_series.is_color_varied = True

        # Configure total points (0-based indices)
        total_points = [3, 5, 7]  # Points to mark as totals
        for i in total_points:
            point = chart.n_series.points[i]
            point.is_total = True

        # Save modified workbook
        workbook.save("output.xlsx")

except Exception as e:
    print(f"Error processing workbook: {str(e)}")
```

```python
import os
from aspose.cells import Workbook

file_path = ""
wb = Workbook(os.path.join(file_path, "SampleSheet.xlsx"))
worksheet = wb.worksheets[0]
chart = worksheet.charts.get("Graphiq5")

# Set some points as total column
# In this example, we set points 0, 4, 8, 12 as total
chart.n_series[0].layout_properties.subtotals = [0, 4, 8, 12]
wb.save(os.path.join(file_path, "output.xlsx"))
```

Le [fichier de sortie](output.xlsx) corrigé configure maintenant correctement les points totaux :

![todo:image_alt_text](set-as-total2.png)

Principaux détails de l'implémentation :
- Utiliser des indices 0-based pour les points de données
- Définir la propriété `is_total` sur les objets `ChartPoint`
- Assurer la bonne configuration de la plage de données
- Gérer la validation du type de graphique

Voir la [documentation de ChartPoint](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chartpoint/) pour des options de configuration avancées.
