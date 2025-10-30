---  
title: Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplan criterios complejos
type: docs  
weight: 280  
url: /es/nodejs-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/  
description: Aprende cómo aplicar filtros avanzados de Microsoft Excel para mostrar registros que cumplen criterios complejos usando la API Aspose.Cells for Node.js via C++.  
keywords: Aplicar Filtro Avanzado con Node.js vía C++, Configurar Filtro Avanzado con Node.js vía C++, Añadir Filtro Avanzado con Node.js vía C++, Crear Filtro Avanzado con Node.js vía C++, Cómo agregar filtro avanzado a un rango con Node.js vía C++  
---  

## **Escenarios de uso posibles**  

Microsoft Excel permite aplicar *Filtro Avanzado* en datos de hojas de cálculo para mostrar registros que cumplen criterios complejos. Puedes aplicar Filtro Avanzado con Microsoft Excel usando su comando *Datos > Avanzadas* como se muestra en esta captura.  

![todo:image_alt_text](1.png)  

Aspose.Cells for Node.js via C++ también permite aplicar el Filtro Avanzado usando el método [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). Igual que Microsoft Excel, admite los siguientes parámetros.  

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

![todo:image_alt_text](2.png)  

## **Código de muestra**  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Autofilter-AdvancedFilter.js" >}}


{{< app/cells/assistant language="nodejs-cpp" >}}
