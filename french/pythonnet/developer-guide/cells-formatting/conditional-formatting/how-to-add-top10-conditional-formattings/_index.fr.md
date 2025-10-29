---
title: Comment ajouter un formatage conditionnel Top10
description: Comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour appliquer la mise en forme Top10 conditionnelle. En ajustant ces critères, vous avez plus de contrôle sur l’apparence des cellules.
keywords: Aspose.Cells, Mise en forme Top10 conditionnelle, Python, Conditionnel, Mise en forme
type: docs
weight: 70
url: /fr/python-net/how-to-add-top10-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
L'utilisation du Top 10 en mise en forme conditionnelle dans Excel permet de mettre en évidence rapidement les valeurs les plus performantes dans un jeu de données — pas seulement les 10 valeurs les plus élevées, mais souvent les N premières ou les N% (vous pouvez choisir !).

1. Repérer les tendances et les valeurs aberrantes : Identifier instantanément les meilleurs performeurs (par exemple, les 10 meilleurs représentants commerciaux, les meilleures notes, les mois de chiffre d'affaires le plus élevé).Facilite l'analyse sans trier les données.
1. Visualisation des données : Ajoute des repères couleur qui font ressortir visuellement les points de données importants.Aide les lecteurs du tableau à comprendre rapidement les valeurs clés.
1. Comparaisons rapides : Utile dans les tableaux de bord et rapports où vous souhaitez mettre en évidence l'excellence ou les pics.
1. Mises à jour dynamiques : Si vos données changent, la mise en forme conditionnelle se met à jour automatiquement pour refléter les nouvelles valeurs principales.

## **Comment ajouter la mise en forme conditionnelle Top10 dans Excel**
Voici comment ajouter la mise en forme conditionnelle Top10 dans Excel, étape par étape :

1. Sélectionnez la plage de cellules que vous souhaitez analyser. Par exemple : Sélectionnez B2:B100 si vous travaillez avec des scores ou des chiffres de ventes.
1. Allez dans l'onglet Accueil du ruban Excel.
1. Cliquez sur Mise en forme conditionnelle dans le groupe Styles.
1. Survolez Règles Top/Bottom dans le menu déroulant.
1. Cliquez sur Top 10…
1. Une boîte de dialogue apparaîtra : Elle dira : Mettre en forme les cellules qui occupent le rang des 10 premiers. Vous pouvez modifier le nombre (par exemple, Top 5, Top 3, etc.). Choisissez un format (comme un remplissage rouge clair, du texte en gras, ou cliquez sur Format personnalisé pour plus d'options).
1. Cliquez sur OK


## **Comment ajouter une mise en forme Top10 conditionnelle en utilisant Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET supporte entièrement la mise en forme conditionnelle fournie par Microsoft Excel 2007 et versions ultérieures au format XLSX sur les cellules en temps réel. Cet exemple démontre un exercice pour la mise en forme Top 10 avec différents ensembles d’attributs.

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

        self.add_top10_1()
        self.add_top10_2()
        self.add_top10_3()
        self.add_top10_4()

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

    def add_top10_1(self):
        conds = self.get_format_condition("A17:C20", Color.gray)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID

    def add_top10_2(self):
        conds = self.get_format_condition("A21:C24", Color.green)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.is_bottom = True

    def add_top10_3(self):
        conds = self.get_format_condition("A25:C28", Color.orange)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.blue
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.is_percent = True

    def add_top10_4(self):
        conds = self.get_format_condition("A29:C32", Color.gold)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.green
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.rank = 3
```

{{< app/cells/assistant language="csharp" >}}
{{< app/cells/assistant language="python-net" >}}
