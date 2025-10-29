---
title: Comment ajouter un format conditionnel au dessus de la moyenne
description: Comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour appliquer une mise en forme conditionnelle Supérieur à la moyenne. En ajustant ces critères, vous avez plus de contrôle sur l apparence et l aspect des cellules. 
keywords: Aspose.Cells, mise en forme conditionnelle supérieure à la moyenne, Python, Conditionnel, Mise en forme 
type: docs
weight: 70
url: /fr/python-net/how-to-add-above-average-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
L'utilisation du formatage conditionnel au-dessus de la moyenne dans des outils comme Microsoft Excel ou Google Sheets est un moyen rapide et visuel de mettre en évidence des données qui se démarquent — notamment, des valeurs supérieures à la moyenne dans une plage. Voici pourquoi vous pourriez l'utiliser :
1. Identifier rapidement les tendances : Il vous aide à repérer instantanément les valeurs performantes sans calculs manuels ni balayage numérique.
1. Simplifier l'analyse des données : Vous n'avez pas besoin de calculer ou d'entrer des formules — c'est une manière automatique d'appliquer une mise en forme basée sur une logique, ce qui fait gagner du temps.
1. Améliorer l'attrait visuel : La coloration aide à rendre votre feuille de calcul plus facile à lire et plus attrayante visuellement, notamment lors de présentations.
1. Soutenir la prise de décision : Identifier rapidement les valeurs supérieures à la moyenne peut conduire à des actions, comme récompenser les meilleurs ou enquêter sur les raisons pour lesquelles certains produits surpassent les autres.

## **Comment ajouter un formatage conditionnel au-dessus de la moyenne avec Excel**
Pour ajouter un formatage conditionnel au-dessus de la moyenne dans Excel, voici comment procéder étape par étape :

1. Sélectionnez la plage de cellules à laquelle vous souhaitez appliquer le formatage. Par exemple : A1:A20.
1. Allez à l'onglet Accueil dans le ruban.
1. Cliquez sur Mise en forme conditionnelle dans le groupe Styles.
1. Survolez Règles supérieur/inferieur.
1. Cliquez sur « Au-dessus de la moyenne... »
1. Dans la boîte de dialogue qui apparaît : Elle détectera automatiquement « Mettre en forme les cellules qui sont AU-DESSUS de la moyenne ». Vous pouvez modifier le style de mise en forme en cliquant sur la liste déroulante à côté (par exemple, choisir un fond de couleur ou un format personnalisé).
1. Cliquez sur OK. Toutes les cellules de votre plage sélectionnée qui sont supérieures à la moyenne de cette plage seront mises en évidence.


## **Comment ajouter une mise en forme conditionnelle supérieure à la moyenne avec Aspose.Cells pour Python via .NET **

Aspose.Cells pour Python via .NET prend en charge intégralement la mise en forme conditionnelle fournie par Microsoft Excel 2007 et versions ultérieures au format XLSX sur les cellules en temps réel. Cet exemple démontre un exercice de mise en forme conditionnelle supérieure à la moyenne avec différents ensembles d'attributs.

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_above_average()
        self.add_above_average2()
        self.add_above_average3()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)



    def get_format_condition(self, cell_area_name, color):
        index = self._sheet.conditional_formattings.add()
        format_conditions = self._sheet.conditional_formattings[index]
        area = self.get_cell_area_by_name(cell_area_name)
        format_conditions.add_area(area)
        self.fill_cell(cell_area_name, color)
        return format_conditions

    def fill_cell(self, cell_area_name, color):
        area = self.get_cell_area_by_name(cell_area_name)
        k = 0
        for i in range(area.start_column, area.end_column + 1):
            for j in range(area.start_row, area.end_row + 1):
                c = self._sheet.cells.get(j, i)
                if color != Color.empty:
                    s = c.get_style()
                    s.foreground_color = color
                    s.pattern = BackgroundType.SOLID
                    c.set_style(s)
                value = j + i + k
                c.put_value(value)
                k += 1

    @staticmethod
    def get_cell_area_by_name(s):
        area = CellArea()
        str_cell_range = s.replace("$", "").split(':')
        start_row, start_col = CellsHelper.cell_name_to_index(str_cell_range[0])
        area.start_row = start_row
        area.start_column = start_col
        if len(str_cell_range) == 1:
            area.end_row = start_row
            area.end_column = start_col
        else:
            end_row, end_col = CellsHelper.cell_name_to_index(str_cell_range[1])
            area.end_row = end_row
            area.end_column = end_col
        return area

    def add_above_average(self):
        conds = self.get_format_condition("A11:C12", Color.tomato)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

    def add_above_average2(self):
        conds = self.get_format_condition("A13:C14", Color.empty)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.above_average.is_above_average = False
        cond.above_average.is_equal_average = True
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

    def add_above_average3(self):
        conds = self.get_format_condition("A15:C16", Color.empty)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.above_average.is_above_average = False
        cond.above_average.is_equal_average = True
        cond.above_average.std_dev = 3
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

```
{{< app/cells/assistant language="python-net" >}}
