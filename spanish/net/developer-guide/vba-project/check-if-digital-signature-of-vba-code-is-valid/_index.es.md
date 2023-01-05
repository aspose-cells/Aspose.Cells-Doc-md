---
title: Compruebe si la firma digital del código VBA es válida
type: docs
weight: 120
url: /es/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

 Aspose.Cells le permite verificar si la firma digital del código VBA es válida usando el[**Libro de trabajo.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) propiedad. regresará**verdadero** si la firma es válida de lo contrario volverá**falso**. La firma digital del código VBA deja de ser válida cuando cambia el código VBA.

{{% /alert %}}

## **Compruebe si la firma digital del código VBA es válida en C#**

 El siguiente código demuestra el uso de esta propiedad usando el[ejemplo de archivo de Excel](5115030.xlsm)que puede descargar desde el enlace proporcionado. El mismo archivo de Excel tiene una firma válida, pero cuando modificamos su código VBA y guardamos el libro de trabajo y luego volvemos a verificar, encontramos que su firma no es válida.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
