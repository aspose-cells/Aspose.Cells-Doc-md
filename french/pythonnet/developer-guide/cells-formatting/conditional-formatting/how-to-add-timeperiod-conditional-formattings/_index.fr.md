---
title: Comment ajouter un formatage conditionnel pour les périodes de temps
description: Comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour appliquer la mise en forme conditionnelle par périodes de temps. En ajustant ces critères, vous avez plus de contrôle sur l’apparence des cellules.
keywords: Aspose.Cells, Mise en forme conditionnelle par périodes de temps, Python, Conditionnel, Mise en forme
type: docs
weight: 70
url: /fr/python-net/how-to-add-time-periods-conditional-formatting/
---

## **Scénarios d'utilisation possibles**
L'utilisation du formatage conditionnel pour les périodes de temps dans Excel est très utile lorsque vous travaillez avec des dates — cela vous aide à suivre et à gérer visuellement rapidement les données liées au temps.
1. Aperçu instantané des données basées sur le temps : mettez en évidence rapidement des tâches d'aujourd'hui, des ventes du mois dernier, des échéances à venir, des rendez-vous de la semaine prochaine.
1. Meilleur gestion du temps : vous aide à respecter les dates limites, les événements ou les éléments expirants. Idéal pour les chronologies de projet, les factures ou les emplois du temps.
1. Mises à jour automatiques : se met à jour dynamiquement. Si la date d'aujourd'hui change, Excel mettra à jour le formatage sans que vous ayez à intervenir.

1. Clarté visuelle : met en évidence les informations sensibles au temps à l'aide de couleurs ou de styles en gras — afin qu'elles ne soient pas manquées.

## **Comment ajouter un formatage conditionnel pour les périodes de temps en utilisant Excel**
Voici comment vous pouvez ajouter un formatage conditionnel pour les périodes de temps dans Excel — très utile pour mettre en évidence des dates comme aujourd'hui, la semaine dernière, le mois prochain, etc.

Étapes pour ajouter un formatage conditionnel pour les périodes de temps :
1. Sélectionnez la plage de cellules de date que vous souhaitez formater. Exemple : A2:A50.
1. Allez à l'onglet Accueil dans le ruban.
1. Cliquez sur Mise en forme conditionnelle dans le groupe Styles.
1. Survolez les règles de mise en surbrillance des cellules.
1. Cliquez sur Une date apparaissant...
1. Dans la boîte de dialogue qui apparaît : utilisez le menu déroulant pour sélectionner une période (Aujourd'hui, Hier, Demain, 7 derniers jours, La semaine dernière, Le mois prochain, etc.).
1. Choisissez le format (par défaut, remplissage rouge clair avec texte rouge foncé, ou cliquez sur Format personnalisé pour choisir le vôtre).
1. Cliquez sur OK.


## **Comment ajouter une mise en forme conditionnelle par périodes de temps en utilisant Aspose.Cells pour Python via .NET**

Aspose.Cells pour Python via .NET supporte entièrement la mise en forme conditionnelle fournie par Microsoft Excel 2007 et versions ultérieures au format XLSX sur les cellules en temps réel. Cet exemple démontre un exercice pour la mise en forme conditionnelle par périodes de temps avec différents ensembles d’attributs.

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

        self.add_time_period_1()
        self.add_time_period_2()
        self.add_time_period_3()
        self.add_time_period_4()
        self.add_time_period_5()
        self.add_time_period_6()
        self.add_time_period_7()
        self.add_time_period_8()
        self.add_time_period_9()
        self.add_time_period_10()

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_time_period_10(self):
        conds = self.get_format_condition("I19:K20", Color.medium_sea_green)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.YESTERDAY
        c = self._sheet.cells.get("I19")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 30))
        c = self._sheet.cells.get("K20")
        c.put_value(datetime(2008, 8, 3))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I20").put_value("Yesterday")

    def add_time_period_9(self):
        conds = self.get_format_condition("I17:K18", Color.medium_purple)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.TOMORROW
        c = self._sheet.cells.get("I17")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 8, 1))
        c = self._sheet.cells.get("K18")
        c.put_value(datetime(2008, 8, 3))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I18").put_value("Tomorrow")

    def add_time_period_8(self):
        conds = self.get_format_condition("I15:K16", Color.medium_orchid)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.THIS_WEEK
        c = self._sheet.cells.get("I15")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 28))
        c = self._sheet.cells.get("K16")
        c.put_value(datetime(2008, 8, 3))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I16").put_value("ThisWeek")

    def add_time_period_7(self):
        conds = self.get_format_condition("I13:K14", Color.medium_blue)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.THIS_MONTH
        c = self._sheet.cells.get("I13")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 5))
        c = self._sheet.cells.get("K14")
        c.put_value(datetime(2008, 5, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I14").put_value("ThisMonth")

    def add_time_period_6(self):
        conds = self.get_format_condition("I11:K12", Color.medium_aquamarine)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.NEXT_WEEK
        c = self._sheet.cells.get("I11")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 8, 5))
        c = self._sheet.cells.get("K12")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I12").put_value("NextWeek")

    def add_time_period_5(self):
        conds = self.get_format_condition("I9:K10", Color.maroon)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.NEXT_MONTH
        c = self._sheet.cells.get("I9")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 8, 25))
        c = self._sheet.cells.get("K10")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I10").put_value("NextMonth")

    def add_time_period_4(self):
        conds = self.get_format_condition("I7:K8", Color.linen)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.LAST_WEEK
        c = self._sheet.cells.get("I7")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 25))
        c = self._sheet.cells.get("K8")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I8").put_value("LastWeek")

    def add_time_period_3(self):
        conds = self.get_format_condition("I5:K6", Color.linen)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.LAST_MONTH
        c = self._sheet.cells.get("I5")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 6, 26))
        c = self._sheet.cells.get("K6")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I6").put_value("LastMonth")

    def add_time_period_2(self):
        conds = self.get_format_condition("I3:K4", Color.light_steel_blue)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.LAST7DAYS
        c = self._sheet.cells.get("I3")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 26))
        c = self._sheet.cells.get("K4")
        c.put_value(datetime(2008, 8, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I4").put_value("Last7Days")

    def add_time_period_1(self):
        conds = self.get_format_condition("I1:K2", Color.light_slate_gray)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.TODAY
        c = self._sheet.cells.get("I1")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime.today())
        c = self._sheet.cells.get("K2")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I2").put_value("Today")


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
