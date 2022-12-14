---
title: Asignar y Validar Firmas Digitales
linktitle: Firma
type: docs
weight: 140
url: /es/net/assign-and-validate-digital-signatures/
description: Archivo de Excel firma digital, verificación. Para proteger la autenticidad del contenido de un libro de trabajo de un archivo de Excel, puede agregar una firma digital usando los códigos C# con Aspose.Cells para .Net.
---
{{% alert color="primary" %}}

 Una firma digital garantiza que el archivo de un libro de trabajo es válido y que nadie lo ha alterado. Puede crear una firma digital personal utilizando el**Microsoft Selfcert.exe** o cualquier otra herramienta, o puede comprar una firma digital. Después de crear una firma digital, debe adjuntarla a su libro de trabajo. Adjuntar una firma digital es similar a sellar un sobre. Si un sobre llega sellado, tiene cierto nivel de seguridad de que nadie ha manipulado su contenido.

{{% /alert %}}

## **Introducción**

 Utilice el cuadro de diálogo Firma digital para adjuntar una firma digital. El cuadro de diálogo Firma digital enumera los certificados válidos. Puede usar el cuadro de diálogo Firma digital para ver los certificados y seleccionar el que desea usar. Si un libro de trabajo tiene una firma digital, el nombre de la firma aparece en el**Nombre del certificado** campo. Si hace clic en el**Remover** en el cuadro de diálogo Firma digital, Microsoft Excel también elimina la firma digital.

Aspose.Cells proporciona el[**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature)espacio de nombres para realizar el trabajo (asignar y validar firmas digitales). El espacio de nombres tiene algunas características útiles para agregar y validar firmas digitales.

Consulte el siguiente código de ejemplo que describe cómo puede realizar la tarea con Aspose.Cells for .NET API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **Temas avanzados**
- [Agregar firma digital a un archivo de Excel ya firmado](/cells/es/net/add-digital-signature-to-an-already-signed-excel-file/)
- [Agregar línea de firma a la hoja de trabajo](/cells/es/net/add-signature-line/)
- [Soporte para firma XAdES](/cells/es/net/support-for-xades-signature/)
