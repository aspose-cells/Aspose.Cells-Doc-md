---
title: Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplen criterios complejos con Golang a través de C++
linktitle: Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplan criterios complejos
type: docs
weight: 280
url: /es/go-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Aprenda cómo aplicar el filtro avanzado de Microsoft Excel para mostrar registros que cumplen criterios complejos usando la API Aspose.Cells for C++.
keywords: Aplicar Filtro Avanzado, Establecer Filtro Avanzado, Agregar Filtro Avanzado, Crear Filtro Avanzado, Cómo agregar Filtro Avanzado a un rango
---

## **Escenarios de uso posibles**

Microsoft Excel permite aplicar *Filtro Avanzado* en datos de hojas de cálculo para mostrar registros que cumplen criterios complejos. Puedes aplicar Filtro Avanzado con Microsoft Excel usando su comando *Datos > Avanzadas* como se muestra en esta captura.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells también permite aplicar el filtro avanzado usando el método [**GetAdvancedFilter()**](https://reference.aspose.com/cells/go-cpp/worksheet/getadvancedfilter/). Al igual que en Microsoft Excel, acepta los siguientes parámetros.

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

El siguiente código de ejemplo aplica el filtro avanzado en el [Archivo de Excel de muestra](48496692.xlsx) y genera el [Archivo de Excel de salida](48496691.xlsx). La captura de pantalla muestra ambos archivos para comparación. Como puedes ver en la captura, los datos han sido filtrados en el archivo de Excel de salida de acuerdo con criterios complejos.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ApplyAdvancedFilterOfMicrosoftExcelToDisplayRecordsMeetingComplexCriteria.go" >}}
