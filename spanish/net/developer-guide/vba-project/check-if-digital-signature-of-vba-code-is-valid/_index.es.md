---
title: Verifica si la Firma Digital del Código VBA es Válida
type: docs
weight: 120
url: /es/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells te permite verificar si la firma digital del código VBA es válida usando la propiedad [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned). Devolverá **true** si la firma es válida, de lo contrario devolverá **false**. La firma digital del código VBA se vuelve inválida cuando se cambia el código VBA.

{{% /alert %}}

## **Verifica si la Firma Digital del Código VBA es Válida en C#**

El siguiente código demuestra el uso de esta propiedad utilizando el [archivo excel de muestra](5115030.xlsm) que puedes descargar desde el enlace proporcionado. El mismo archivo de Excel tiene una firma válida pero cuando modificamos su código VBA y guardamos el libro de trabajo y luego volvemos a verificar, encontramos que su firma se ha vuelto inválida.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
