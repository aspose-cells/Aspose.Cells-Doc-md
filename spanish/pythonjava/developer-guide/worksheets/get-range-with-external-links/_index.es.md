---
title: Obtener rango con enlaces externos
type: docs
weight: 60
url: /es/python-java/get-range-with-external-links/
---
## **Obtener rango con enlaces externos**
Hay muchos casos en los que los archivos de Excel acceden a datos de otros archivos de Excel mediante el uso de enlaces externos. Aspose.Cells for Python via Java ofrece la opción de recuperar estos enlaces externos mediante el[Nombre.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) método. los[Nombre.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) método devuelve una matriz de tipo[Área referida](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). los[Área referida](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea)la clase proporciona un[Nombre de archivo externo](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName)propiedad que devuelve el nombre del archivo externo.

El siguiente fragmento de código muestra cómo obtener enlaces externos.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
