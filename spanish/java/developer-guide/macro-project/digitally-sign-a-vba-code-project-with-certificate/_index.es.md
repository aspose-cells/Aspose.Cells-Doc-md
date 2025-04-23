---
title: Firmar digitalmente un proyecto de código VBA con un certificado
type: docs
weight: 110
url: /es/java/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Puede firmar digitalmente su proyecto de código VBA usando Aspose.Cells con su método [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-). Siga estos pasos para verificar si su archivo de Excel está firmado digitalmente con un certificado.

- Haga clic en **Visual Basic** desde la pestaña **Desarrollador** para abrir **Visual Basic para Aplicaciones IDE**
- Haga clic en **Herramientas** > **Firmas Digitales...** de  **Visual Basic para Aplicaciones IDE**

y mostrará el **Formulario de Firma Digital** que muestra si el documento está firmado digitalmente con un certificado o no.

{{% /alert %}} 

## **Firmar digitalmente un proyecto de código VBA con un certificado en C#**

El siguiente código de ejemplo ilustra cómo hacer uso del método [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign-com.aspose.cells.DigitalSignature-). Aquí están los archivos de entrada y salida del código de ejemplo. Puede usar cualquier archivo de Excel y cualquier certificado para probar este código.

- [Archivo de Excel de origen](5115028.xlsm) utilizado en el código de ejemplo.
- [Archivo pfx de ejemplo](5115039.pfx) para crear la Firma Digital. Por favor, instálelo en su computadora para ejecutar este código. Su contraseña es 1234.
- [Archivo de Excel de salida](5115029.xlsm) generado por el código de ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
{{< app/cells/assistant language="java" >}}
