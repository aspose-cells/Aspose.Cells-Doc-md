---
title: Aplique el filtro avanzado de Excel Microsoft para mostrar registros que cumplan criterios complejos
type: docs
weight: 280
url: /es/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: Aprenda a aplicar el filtro avanzado de Microsoft Excel para mostrar registros que cumplan criterios complejos utilizando Aspose.Cells for .NET API.
keywords: Apply Advanced Filter, Set Advanced Filter, Add Advanced Filter, Create Advanced Filter, How to add Advanced Filter to a range 
---
##  **Posibles escenarios de uso**

 Microsoft Excel te permite aplicar*Filtro avanzado* en los datos de la hoja de cálculo para mostrar registros que cumplan criterios complejos. Puede aplicar el filtro avanzado con Microsoft Excel a través de su*Datos > Avanzado*comando como se muestra en esta captura de pantalla.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_1.png)

Aspose.Cells también le permite aplicar el filtro avanzado utilizando el[**Hoja de trabajo.Filtro avanzado()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/advancedfilter)método. Al igual que Microsoft Excel, acepta los siguientes parámetros.

**esfiltro**

Indica si se está filtrando la lista.

**listarango**

El rango de la lista.

**Rango de criterio**

Los criterios varían.

**copiar a**

El rango donde se copian los datos.

**únicoRecordOnly**

Solo mostrar o copiar filas únicas.

##  **Aplique el filtro avanzado de Excel Microsoft para mostrar registros que cumplan criterios complejos**

El siguiente código de muestra aplica el filtro avanzado en el[Archivo de Excel de muestra](48496692.xlsx) y genera el[Archivo de Excel de salida](48496691.xlsx). La captura de pantalla muestra ambos archivos para comparar. Como puede ver en la captura de pantalla, los datos se han filtrado dentro del archivo Excel de salida según criterios complejos.

![todo:image_alt_text](apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria_2.png)

##  **Código de muestra**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-ApplyAdvancedFilterOfMicrosoftExcel.cs" >}}
