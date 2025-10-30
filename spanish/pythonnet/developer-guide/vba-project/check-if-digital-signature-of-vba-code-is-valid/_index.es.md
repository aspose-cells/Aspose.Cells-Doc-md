---
title: Verifica si la Firma Digital del Código VBA es Válida
type: docs
weight: 120
url: /es/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells para Python via .NET te permite verificar si la firma digital del código VBA es válida usando la propiedad [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed). Retornará **true** si la firma es válida, de lo contrario retornará **false**. La firma digital del código VBA se vuelve inválida cuando cambias el código VBA.

{{% /alert %}}

## **Verifica si la firma digital del código VBA es válida en Python**

El siguiente código demuestra el uso de esta propiedad utilizando el [archivo excel de muestra](5115030.xlsm) que puedes descargar desde el enlace proporcionado. El mismo archivo de Excel tiene una firma válida pero cuando modificamos su código VBA y guardamos el libro de trabajo y luego volvemos a verificar, encontramos que su firma se ha vuelto inválida.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

{{< app/cells/assistant language="python-net" >}}
