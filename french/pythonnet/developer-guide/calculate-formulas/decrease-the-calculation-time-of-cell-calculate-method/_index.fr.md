---
title: Diminuer le temps de calcul de la méthode Cell.Calculate avec Python.NET
linktitle: Diminuer le temps de calcul de Cell.Calculate
type: docs
weight: 100
url: /fr/python-net/decrease-the-calculation-time-of-cell-calculate-method/
description: Apprenez comment optimiser la performance de calcul des cellules Excel en utilisant Aspose.Cells pour Python via .NET. Réduisez le temps de calcul avec les paramètres CalculationOptions.
keywords: calcul Excel en Python, optimisation du calcul de cellule, Aspose.Cells Python, performance du calcul, options de calcul récursif
---

## **Scénarios d'utilisation possibles**

 Normalement, nous recommandons aux utilisateurs d'appeler la méthode [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) une fois, puis d'obtenir les valeurs calculées des cellules individuelles. Lorsqu'on travaille avec des calculs de cellules uniques, vous pouvez utiliser la propriété [**calculation_options.recursive**](https://reference.aspose.com/cells/python-net/aspose.cells/calculationoptions/recursive/) pour réduire considérablement le temps de calcul. La définir à `False` empêche de recalculer les cellules dépendantes lors des appels suivants.

## ** Optimisation des performances de calcul des cellules**

 L'exemple suivant démontre l'utilisation de la propriété récursive. Utilisez le [fichier Excel d'exemple](5113710.xlsx) fourni pour tester la différence de performance. Le code montre comment le fait de définir `recursive=False` réduit le temps de calcul en évitant de recalculer les cellules dépendantes redondantes.

```python
# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
# Test calculation time after setting recursive true
test_calc_time_recursive(True)

# Test calculation time after setting recursive false
test_calc_time_recursive(False)
```

```python
import os
import time
from aspose.cells import Workbook, CalculationOptions

def test_calc_time_recursive(rec):
    """
    Tests calculation time with recursive option and prints elapsed seconds
    """
    # The path to the documents directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")

    # Load sample workbook
    wb = Workbook(os.path.join(data_dir, "sample.xlsx"))

    # Access first worksheet
    ws = wb.worksheets[0]

    # Set calculation options
    opts = CalculationOptions()
    opts.recursive = rec

    # Start timing
    start_time = time.perf_counter()

    # Calculate cell A1 one million times
    for _ in range(1000000):
        ws.cells.get("A1").calculate(opts)

    # Calculate elapsed time
    elapsed_time = int(time.perf_counter() - start_time)

    # Print results
    print(f"Recursive {rec}: {elapsed_time} seconds")
```

## ** Résultats du benchmark de performance**

 La sortie typique lors de l'exécution du code optimisé avec le fichier d'exemple montre une réduction notable du temps :

{{< highlight text >}}
Recursive True: 96 seconds
Recursive False: 42 seconds
{{< /highlight >}}
