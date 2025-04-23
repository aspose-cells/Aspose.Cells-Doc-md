---
title: Asignar y Validar Firmas Digitales
linktitle: Firma
type: docs
weight: 140
url: /es/net/assign-and-validate-digital-signatures/
description: Firma digital de archivos de Excel, verificación. Para proteger la autenticidad del contenido de un libro de trabajo de un archivo de Excel, puedes agregar una firma digital usando códigos C# con Aspose.Cells para .Net.
keywords: Firma digital del archivo de Excel, Agregar firma digital para Excel, Cómo validar firma digital.
---

{{% alert color="primary" %}}

Una firma digital proporciona garantía de que un archivo de libro de trabajo es válido y que nadie lo ha alterado. Puedes crear una firma digital personal usando el **Microsoft Selfcert.exe** u otra herramienta, o puedes comprar una firma digital. Después de crear una firma digital, debes adjuntarla a tu libro de trabajo. Adjuntar una firma digital es similar a sellar un sobre. Si un sobre llega sellado, tienes cierto nivel de seguridad de que nadie ha manipulado su contenido.

{{% /alert %}}

## **Introducción**

Utilice el cuadro de diálogo de Firma digital para adjuntar una firma digital. El cuadro de diálogo de Firma digital lista los certificados válidos. Puede usar el cuadro de diálogo de Firma digital para ver certificados y seleccionar el que desea utilizar. Si un libro tiene una firma digital, el nombre de la firma aparece en el campo **Nombre del certificado**. Si hace clic en el botón **Quitar** en el cuadro de diálogo de Firma digital, Microsoft Excel también quita la firma digital.

## **Cómo agregar firma digital para Excel**

Aspose.Cells proporciona el espacio de nombres [**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature) para realizar la tarea (asignar y validar firmas digitales). El espacio de nombres tiene algunas características útiles para agregar y validar firmas digitales.

Consulte el siguiente código de muestra que describe cómo puede realizar la tarea usando el API Aspose.Cells for .NET.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **Temas avanzados**
- [Agregar firma digital a un archivo de Excel ya firmado](/cells/es/net/add-digital-signature-to-an-already-signed-excel-file/)
- [Agregar línea de firma a la hoja de trabajo](/cells/es/net/add-signature-line/)
- [Soporte para firma XAdES](/cells/es/net/support-for-xades-signature/)
{{< app/cells/assistant language="csharp" >}}
