---
title: Comment ajouter un formatage conditionnel avec barres de données
description: Comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour appliquer la mise en forme conditionnelle avec des barres de données. En ajustant ces critères, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, Mise en forme conditionnelle avec barres de données, Python, Conditionnel, Mise en forme
type: docs
weight: 70
url: /fr/python-net/how-to-add-databars-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
Utiliser des barres de données dans le formatage conditionnel est un moyen puissant (et visuel !) de comprendre vos données en un coup d'œil.

1. Comparaison visuelle des valeurs : Les barres de données transforment les nombres en barres horizontales, facilitant la comparaison côte à côte — comme un mini graphique à barres dans vos cellules !
1. Reconnaissance immédiate de modèles : Vous pouvez instantanément voir les points hauts, les points bas et les valeurs aberrantes sans trier ou examiner les chiffres.
1. Meilleure lisibilité : Particulièrement utile dans de longues tables — cela réduit la charge cognitive et vous aide à saisir rapidement les tendances clés.
1. Dynamique & en temps réel : À mesure que les valeurs changent, les barres se mettent à jour automatiquement — idéal pour suivre des métriques en direct, des progrès ou des KPI.
1. Tableau de bord d'aspect professionnel : Ajoute un aspect propre, moderne et soigné aux rapports ou tableaux de bord.

## **Comment ajouter un formatage conditionnel avec barres de données en utilisant Excel**
Pour ajouter un formatage conditionnel avec barres de données dans Excel, voici comment faire étape par étape :

1. Sélectionnez votre plage de données, par exemple : C2:C20 — cela pourrait être des ventes, des scores ou des valeurs de progression.
1. Allez à l'onglet Accueil dans le ruban.
1. Cliquez sur Formatage conditionnel dans le groupe Styles.
1. Survolez les Barres de données.
1. Choisissez un style : Remplissage en dégradé (les barres s’estompent de la gauche vers la droite) et Remplissage uni (les barres ont une couleur unie).
1. Cliquez sur le style qui vous plaît — et c’est terminé !

## **Comment ajouter une mise en forme conditionnelle avec barres de données en utilisant Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET supporte entièrement la mise en forme conditionnelle fournie par Microsoft Excel 2007 et versions ultérieures au format XLSX sur les cellules en temps réel. Cet exemple démontre un exercice pour la mise en forme conditionnelle avec des barres de données utilisant différents ensembles d’attributs.

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

        self.add_data_bar1()
        self.add_data_bar2()

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)    

    def add_data_bar2(self):
        conds = self.get_format_condition("E3:G4", Color.light_green)
        idx = conds.add_condition(FormatConditionType.DATA_BAR)
        cond = conds[idx]
        cond.data_bar.color = Color.orange
        cond.data_bar.min_cfvo.type = FormatConditionValueType.PERCENTILE
        cond.data_bar.min_cfvo.value = 30.78
        cond.data_bar.show_value = False

    def add_data_bar1(self):
        conds = self.get_format_condition("E1:G2", Color.yellow_green)
        idx = conds.add_condition(FormatConditionType.DATA_BAR)
        cond = conds[idx]

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

```

{{< app/cells/assistant language="python-net" >}}
