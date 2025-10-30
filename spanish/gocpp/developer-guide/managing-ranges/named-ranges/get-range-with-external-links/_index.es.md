---
title: Obtener rango con enlaces externos con Golang vía C++
linktitle: Obtener rango con enlaces externos
type: docs
weight: 120
url: /es/go-cpp/get-range-with-external-links/
description: Aprender cómo recuperar rangos con enlaces externos en archivos de Excel usando Aspose.Cells con Golang vía C++.
---

## **Obtener Rango con Vínculos Externos**

Muchas veces, los archivos de Excel acceden a datos de otros archivos de Excel usando enlaces externos. Aspose.Cells ofrece la opción de recuperar estos enlaces externos usando el método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/). El método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) devuelve una matriz del tipo [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). La clase [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) proporciona una propiedad [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) que devuelve el nombre del archivo externo. La clase [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) expone los siguientes miembros.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): La columna final del área
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): La fila final del área
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): Obtener el nombre del archivo externo si esta es una referencia externa
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): Indica si esto es un área
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): Indica si esto es un enlace externo
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): Indica en qué hoja está esta referencia
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): La columna inicial del área
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): La fila inicial del área

El código de ejemplo a continuación demuestra el uso del método [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) para obtener Rangos con enlaces externos.

## **Código de muestra**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
