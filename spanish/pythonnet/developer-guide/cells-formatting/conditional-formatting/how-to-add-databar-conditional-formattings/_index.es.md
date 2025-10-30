---
title: Cómo agregar formato condicional de Barras de Datos
description: Cómo usar la biblioteca Aspose.Cells para Python via .NET para aplicar formato condicional de Barras de Datos. Ajustando estos criterios, tienes más control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional de Barras de Datos, Python, Condicional, Formato
type: docs
weight: 70
url: /es/python-net/how-to-add-databars-conditional-formatting/
---

## **Escenarios de uso posibles**
Usar Barras de Datos en formato condicional es una forma poderosa (¡y visual!) de entender tus datos de un vistazo.

1. Comparación Visual de Valores: Las barras de datos convierten los números en barras horizontales, facilitando mucho la comparación de valores uno al lado del otro — ¡como un mini gráfico de barras dentro de tus celdas!
1. Reconocimiento Inmediato de Patrones: Puedes ver instantáneamente los picos, valles y valores atípicos sin ordenar o escanear números.
1. Mejor Legibilidad: Especialmente útil en tablas largas — reduce la carga cognitiva y te ayuda a captar rápidamente las tendencias clave.
1. Dinámico y en Tiempo Real: A medida que cambian los valores, las barras se actualizan automáticamente — ideal para monitorear métricas en vivo, progreso o KPI.
1. Paneles de Control de Aspecto Profesional: Añade un aspecto limpio, moderno y pulido a informes o paneles.

## **Cómo agregar formato condicional de Barras de Datos usando Excel**
Para agregar formato condicional de Barras de Datos en Excel, así es como puedes hacerlo paso a paso:

1. Selecciona tu rango de datos, por ejemplo: C2:C20 — esto podría ser ventas, puntuaciones o valores de progreso.
1. Ve a la pestaña Inicio en la cinta de opciones.
1. Haz clic en Formato condicional en el grupo Estilos.
1. Pasa el cursor sobre Barras de Datos.
1. Elige un estilo: Relleno con Degradado (las barras se desvanecen de izquierda a derecha) y Relleno Sólido (las barras tienen un color sólido).
1. Haz clic en el estilo que deseas — ¡y listo!

## **Cómo agregar formato condicional de Barras de Datos usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET soporta completamente el formato condicional proporcionado por Microsoft Excel 2007 y versiones posteriores en formato XLSX en tiempo de ejecución. Este ejemplo demuestra un ejercicio para el formato condicional de Barras de Datos con diferentes conjuntos de atributos.

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
