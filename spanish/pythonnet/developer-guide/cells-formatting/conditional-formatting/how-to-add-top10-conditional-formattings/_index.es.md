---
title: Cómo agregar formato condicional Top10
description: Cómo usar la biblioteca Aspose.Cells para Python via .NET para aplicar formato condicional Top10. Ajustando estos criterios, tienes más control sobre cómo se ven y aparecen las celdas.
keywords: Aspose.Cells, Formato condicional Top10, Python, Condicional, Formato
type: docs
weight: 70
url: /es/python-net/how-to-add-top10-conditional-formatting/
---

## **Escenarios de uso posibles**
Usar el formato condicional Top 10 en Excel ayuda a resaltar rápidamente los valores de mayor rendimiento en un conjunto de datos — no solo los 10 valores principales literales, sino también los N principales o N% superior (¡puedes elegir!).

1. Detectar tendencias y valores atípicos: identifica instantáneamente los mejores (por ejemplo, los 10 mejores vendedores, las mejores calificaciones, los meses de mayor ingreso). Facilita el análisis sin ordenar los datos.
1. Visualización de datos: Agrega señales de color que hacen que los puntos de datos importantes destaquen visualmente. Ayuda a los usuarios de la hoja de cálculo a entender los valores clave de un vistazo.
1. Comparaciones rápidas: Útil en tableros y reportes donde quieres destacar la excelencia o puntos máximos.
1. Actualizaciones dinámicas: Si tus datos cambian, el formato condicional se actualiza automáticamente para reflejar los nuevos valores principales.

## **Cómo agregar formato condicional Top10 usando Excel**
Así es como puedes agregar formato condicional Top10 en Excel, paso a paso:

1. Selecciona el rango de celdas que deseas analizar. Por ejemplo: selecciona B2:B100, si trabajas con puntuaciones o números de ventas.
1. Ve a la pestaña Inicio en la cinta de opciones de Excel.
1. Haz clic en Formato condicional en el grupo Estilos.
1. Pasa el cursor sobre Reglas de los últimos/top en el menú desplegable.
1. Haz clic en Último 10 elementos...
1. Aparecerá un cuadro de diálogo: Dirá: Formatear celdas que se encuentren en el top 10. Puedes cambiar el número (por ejemplo, Top 5, Top 3, etc.). Elige un formato (como relleno rojo claro, texto en negrita, o haz clic en Formato personalizado para más opciones).
1. Haz clic en Aceptar


## **Cómo agregar formato condicional Top10 usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET soporta completamente el formato condicional proporcionado por Microsoft Excel 2007 y versiones posteriores en formato XLSX en tiempo de ejecución. Este ejemplo demuestra un ejercicio para el formato condicional Top 10 con diferentes conjuntos de atributos.

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
