---
title: Spécification du nombre de chiffres significatifs à stocker dans le fichier Excel avec Python.NET
linktitle: Spécification des chiffres significatifs
type: docs
weight: 30
url: /fr/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: Apprenez comment contrôler les chiffres significatifs stockés dans les fichiers Excel en utilisant l’API Aspose.Cells pour Python via .NET.
---

## **Scénarios d'utilisation possibles**

Par défaut, Aspose.Cells stocke 17 chiffres significatifs des valeurs doubles dans le fichier Excel, contrairement à MS-Excel qui en stocke seulement 15. Vous pouvez modifier ce comportement de 17 à 15 chiffres significatifs à l’aide de l’attribut [**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/).

## **Spécification des chiffres significatifs à stocker dans le fichier Excel**

Le code d’exemple ci-dessous force Aspose.Cells à utiliser 15 chiffres significatifs lors du stockage des valeurs doubles. Vérifiez le [fichier Excel de sortie](22774105.xlsx) (renommez l’extension en .zip pour inspecter les valeurs stockées). La capture d’écran ci-dessous montre comment ce paramètre influence les valeurs stockées :

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Code d'exemple**

```python
from aspose.cells import Workbook, CellsHelper
import aspose.cells
import os
import pytest

# Set significant digits to 15
CellsHelper.set_significant_digits(15)

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set value with extended precision
cell = worksheet.cells.get("A1")
cell.put_value(1234567890123456.001234567890123456)

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CellsHelper

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Set significant digits to 15 like MS-Excel
CellsHelper.set_significant_digits(15)

# Create workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Access cell A1
c = worksheet.cells.get("A1")

# Put double value with 15 significant digits
c.put_value(1234567890.123451711)

# Save the workbook
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "out_SignificantDigits.xlsx"))
```
