---
title: Verificar si la firma digital del código VBA es válida con Golang vía C++
linktitle: Verifica si la Firma Digital del Código VBA es Válida
type: docs
weight: 120
url: /es/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Aprenda cómo verificar la validez de una firma digital en código VBA usando Aspose.Cells con Golang vía C++.
---

{{% alert color="primary" %}}

Aspose.Cells te permite verificar si la firma digital del código VBA es válida usando la propiedad [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/). Retornará **true** si la firma es válida; de lo contrario, retornará **false**. La firma digital del código VBA se vuelve inválida cuando cambias el código VBA.

{{% /alert %}}

## **Verifica si la firma digital del código VBA es válida en C++**

El siguiente código demuestra el uso de esta propiedad con el [archivo de Excel de ejemplo](5115030.xlsm) que puedes descargar del enlace proporcionado. El mismo archivo de Excel tiene una firma válida, pero cuando modificamos su código VBA y guardamos el libro de trabajo y luego volvemos a verificar, encontramos que su firma se volvió inválida.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
