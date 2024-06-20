---
title: Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplan criterios complejos
type: docs
weight: 280
url: /es/python-net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Aprende cómo aplicar el filtro avanzado de Microsoft Excel para mostrar registros que cumplen con criterios complejos usando la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Excel de Python, Aplicar Filtro Avanzado de Python, Establecer Filtro Avanzado de Python, Agregar Filtro Avanzado de Python, Crear Filtro Avanzado de Python, Cómo agregar Filtro Avanzado a un rango usando Python.
---

## **Escenarios de uso posibles**

Microsoft Excel te permite aplicar el *Filtro Avanzado* en los datos de la hoja de cálculo para mostrar registros que cumplan criterios complejos. Puedes aplicar el Filtro Avanzado en Microsoft Excel a través del comando *Datos > Avanzados* como se muestra en esta captura de pantalla.

![todo:image_alt_text](1.png)

Aspose.Cells for Python via .NET también te permite aplicar el Filtro Avanzado usando el método [**Worksheet.advancedFilter()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/advanced_filter/#bool-str-str-str-bool). Al igual que Microsoft Excel, acepta los siguientes parámetros.

**isFilter**

Indica si se está filtrando la lista en su lugar.

**listRange**

El rango de la lista.

**criteriaRange**

El rango de criterios.

**copyTo**

El rango donde se copian los datos.

**uniqueRecordOnly**

Solo muestra o copia filas únicas.

## **Aplicar Filtro Avanzado de Microsoft Excel para Mostrar Registros que Cumplen Criterios Complejos**

El siguiente código de ejemplo aplica el filtro avanzado en el [Archivo de Excel de Muestra](48496692.xlsx) y genera el [Archivo de Excel de Salida](48496691.xlsx). La captura de pantalla muestra ambos archivos para comparación. Como puede ver en la captura de pantalla, los datos se han filtrado dentro del archivo de Excel de salida de acuerdo a criterios complejos.

![todo:image_alt_text](2.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-ApplyAdvancedFilterOfMicrosoftExcel.py" >}}
