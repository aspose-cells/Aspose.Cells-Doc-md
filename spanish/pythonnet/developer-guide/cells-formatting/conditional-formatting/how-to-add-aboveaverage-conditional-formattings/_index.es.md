---
title: Cómo agregar formateo condicional de valores por encima del promedio
description: Cómo usar la biblioteca Aspose.Cells para Python via .NET para aplicar formato condicional de Promedio Alto. Ajustando estos criterios, tienes más control sobre la apariencia de las celdas.
keywords: Aspose.Cells, Formato condicional de Promedio Alto, Python, Condicional, Formato
type: docs
weight: 70
url: /es/python-net/how-to-add-above-average-conditional-formatting/
---

## **Escenarios de uso posibles**
Usar formato condicional de por encima del promedio en herramientas como Microsoft Excel o Google Sheets es una manera rápida y visual de resaltar datos destacados—específicamente, valores que son mayores que el promedio en un rango. Aquí las razones para usarlo:
1. Detectar tendencias rápidamente: Te ayuda a identificar instantáneamente valores de alto rendimiento sin calcular manualmente los promedios o escanear números.
1. Simplificar análisis de datos: No necesitas calcular ni ingresar fórmulas, es una forma automática de aplicar formato basado en lógica, ahorrando tiempo.
1. Mejorar el atractivo visual: La codificación por colores ayuda a que tu hoja de cálculo sea más fácil de leer y visualmente más atractiva, especialmente durante presentaciones.
1. Apoyar la toma de decisiones: Identificar rápidamente valores por encima del promedio puede orientar acciones, como recompensar a los que rinden alto o investigar por qué ciertos productos superan a otros.

## **Cómo agregar formateo condicional de por encima del promedio usando Excel**
Para agregar formateo condicional de por encima del promedio en Excel, así es como puedes hacerlo paso a paso:

1. Selecciona el rango de celdas al que deseas aplicar el formato. Por ejemplo: A1:A20.
1. Ve a la pestaña Inicio en la cinta de opciones.
1. Haz clic en Formato condicional en el grupo Estilos.
1. Pasa el cursor sobre Reglas superiores/inferiores.
1. Haz clic en Por encima del promedio...
1. En el cuadro de diálogo que aparece: Detectará automáticamente "Formatar celdas que están POR ENCIMA del media." Puedes cambiar el estilo de formato haciendo clic en la flecha hacia abajo junto a (por ejemplo, elegir un color de relleno o formato personalizado).
1. Haz clic en Aceptar. Todas las celdas en tu rango seleccionado que estén por encima del promedio de ese rango serán resaltadas.


## **Cómo agregar formato condicional de Promedio Alto usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET soporta completamente el formato condicional proporcionado por Microsoft Excel 2007 y versiones posteriores en formato XLSX en tiempo de ejecución. Este ejemplo demuestra un ejercicio de formato condicional de Promedio Alto con diferentes conjuntos de atributos.

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
