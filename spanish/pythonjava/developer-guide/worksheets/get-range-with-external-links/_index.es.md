---
title: Obtener rango con enlaces externos
type: docs
weight: 60
url: /es/python-java/get-range-with-external-links/
---

## **Obtener Rango con Vínculos Externos**
Hay muchas instancias donde los archivos de Excel acceden a datos de otros archivos de Excel mediante el uso de enlaces externos. Aspose.Cells for Python via Java proporciona la opción de recuperar estos enlaces externos mediante el uso del método [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)). El método [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) devuelve una matriz del tipo [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). La clase [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) proporciona una propiedad [ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) que devuelve el nombre del archivo externo.

El siguiente fragmento de código muestra cómo obtener enlaces externos.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
