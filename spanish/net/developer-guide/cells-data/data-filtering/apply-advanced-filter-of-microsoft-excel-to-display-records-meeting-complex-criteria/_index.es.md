---
title: Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplan criterios complejos
type: docs
weight: 280
url: /es/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Aprenda cómo aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplen con criterios complejos utilizando la API Aspose.Cells for .NET.
keywords: Aplicar Filtro Avanzado, Establecer Filtro Avanzado, Agregar Filtro Avanzado, Crear Filtro Avanzado, Cómo agregar Filtro Avanzado a un rango 
---

## **Escenarios de uso posibles**

Microsoft Excel te permite aplicar el *Filtro Avanzado* en los datos de la hoja de cálculo para mostrar registros que cumplan criterios complejos. Puedes aplicar el Filtro Avanzado en Microsoft Excel a través del comando *Datos > Avanzados* como se muestra en esta captura de pantalla.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells también le permite aplicar el Filtro Avanzado usando el método [**Worksheet.AdvancedFilter()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter). Al igual que Microsoft Excel, acepta los siguientes parámetros.

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

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
