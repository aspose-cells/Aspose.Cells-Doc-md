---
title: Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplan criterios complejos
type: docs
weight: 190
url: /es/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---

## **Escenarios de uso posibles**
Microsoft Excel te permite aplicar el *Filtro Avanzado* en los datos de la hoja de cálculo para mostrar registros que cumplan criterios complejos. Puedes aplicar el Filtro Avanzado en Microsoft Excel a través del comando *Datos > Avanzados* como se muestra en esta captura de pantalla.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells también te permite aplicar el Filtro Avanzado utilizando el método [Worksheet.advancedFilter()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)). Al igual que Microsoft Excel, acepta los siguientes parámetros.

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
El siguiente código de muestra aplica el filtro avanzado en el [Archivo de Excel de Muestra](48496702.xlsx) y genera el [Archivo de Excel de Salida](48496705.xlsx). La captura de pantalla muestra ambos archivos para comparación. Como se puede ver en la captura de pantalla, los datos han sido filtrados dentro del archivo de Excel de salida de acuerdo con criterios complejos.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
