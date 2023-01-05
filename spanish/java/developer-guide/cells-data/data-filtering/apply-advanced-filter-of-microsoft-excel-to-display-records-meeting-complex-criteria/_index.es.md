---
title: Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplen criterios complejos
type: docs
weight: 190
url: /es/java/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
---
## **Posibles escenarios de uso**
 Microsoft Excel te permite aplicar*Filtro avanzado* en los datos de la hoja de cálculo para mostrar registros que cumplen criterios complejos. Puede aplicar Filtro avanzado con Microsoft Excel a través de su*Datos > Avanzado*comando como se muestra en esta captura de pantalla.

![todo:imagen_alternativa_texto](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells también le permite aplicar el Filtro avanzado usando el[Hoja de trabajo.filtro avanzado()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#advancedFilter\(boolean,%20java.lang.String,%20java.lang.String,%20java.lang.String,%20boolean\)) método. Al igual que Microsoft Excel, acepta los siguientes parámetros.

**esFiltro**

Indica si se filtra la lista en su lugar.

**rango de lista**

El rango de la lista.

**Rango de criterio**

El rango de criterios.

**copiar a**

El rango donde se copian los datos.

**UniqueRecordOnly**

Solo mostrar o copiar filas únicas.
## **Aplicar filtro avanzado de Microsoft Excel para mostrar registros que cumplen criterios complejos**
El siguiente código de ejemplo aplica el filtro avanzado en el[Ejemplo de archivo de Excel](48496702.xlsx) y genera la[Archivo de Excel de salida](48496705.xlsx). La captura de pantalla muestra ambos archivos para comparar. Como puede ver dentro de la captura de pantalla, los datos se filtraron dentro del archivo de salida de Excel de acuerdo con criterios complejos.

![todo:imagen_alternativa_texto](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ApplyAdvancedFilterOfMicrosoftExcel.java" >}}
