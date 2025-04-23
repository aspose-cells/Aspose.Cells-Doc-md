---
title: Spécifier les champs de formule lors de l importation de données dans une feuille de calcul avec Python via .NET
linktitle: Spécifiez les champs de formule lors de l importation de données dans la feuille de calcul
type: docs
weight: 300
url: /fr/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: Apprenez comment spécifier des champs de formule lors de l importation de données dans les feuilles de calcul en utilisant Aspose.Cells pour Python via .NET API.
keywords: Python spécifier les champs de formule lors de l importation de données, Python définir des colonnes de formule lors de l importation de données, Aspose.Cells Python importation de formule
---

## **Scénarios d'utilisation possibles**

Vous pouvez spécifier des champs de formule lors de l'importation de données dans votre feuille de calcul en utilisant la propriété [**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/). Cette propriété prend une liste booléenne où la valeur **True** indique que le champ est une formule. Par exemple, si le troisième champ est un champ de formule, le troisième élément de la liste sera **True**.

## **Spécifier les champs de formule lors de l'importation de données**

L'exemple suivant démontre comment spécifier des champs de formule lors de l'importation de données. Voir le fichier Excel de sortie généré ([output Excel file](61767838.xlsx)) et la capture d'écran montrant les résultats.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Code d'exemple**

```python
import os
from dataclasses import dataclass
from aspose.cells import Workbook, ImportTableOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

@dataclass
class DataItems:
    number1: int
    number2: int
    formula1: str
    formula2: str

def run():
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)

    dis = []
    dis.append(DataItems(2002, 3502, "=SUM(A2,B2)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2003, 3503, "=SUM(A3,B3)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2004, 3504, "=SUM(A4,B4)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2005, 3505, "=SUM(A5,B5)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))

    wb = Workbook()
    ws = wb.worksheets[0]

    opts = ImportTableOptions()
    opts.is_formulas = [False, False, True, True]

    ws.cells.import_custom_objects(dis, 0, 0, opts)

    wb.calculate_formula()
    ws.auto_fit_columns()

    output_path = os.path.join(output_dir, "outputSpecifyFormulaFieldsWhileImportingDataToWorksheet.xlsx")
    wb.save(output_path)

    print("SpecifyFormulaFieldsWhileImportingDataToWorksheet executed successfully.")

if __name__ == "__main__":
    run()
```
