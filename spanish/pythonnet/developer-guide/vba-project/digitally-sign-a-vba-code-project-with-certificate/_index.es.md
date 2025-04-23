---
title: Firmar digitalmente un proyecto de código VBA con un certificado
type: docs
weight: 110
url: /es/python-net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Puedes firmar digitalmente tu proyecto de código VBA usando Aspose.Cells para Python via .NET con su método [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature). Por favor, sigue estos pasos para verificar si tu archivo de Excel está firmado digitalmente con un certificado.

- Haga clic en **Visual Basic** desde la pestaña **Desarrollador** para abrir **Visual Basic para Aplicaciones IDE**
- Haz clic en **Herramientas** > **Firmas Digitales...** del **IDE de Visual Basic for Applications**

y mostrará el **Formulario de Firma Digital** que muestra si el documento está firmado digitalmente con un certificado o no.

{{% /alert %}} 

## **Firmar digitalmente un proyecto de código VBA con certificado en Python**

El siguiente código de muestra ilustra cómo utilizar el método [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature). Aquí están los archivos de entrada y salida del código de muestra. Puedes usar cualquier archivo de Excel y cualquier certificado para probar este código.

- [Archivo de Excel de origen](5115028.xlsm) utilizado en el código de ejemplo.
- [Archivo pfx de ejemplo](5115039.pfx) para crear la Firma Digital. Por favor, instálelo en su computadora para ejecutar este código. Su contraseña es 1234.
- [Archivo de Excel de salida](5115029.xlsm) generado por el código de ejemplo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-DigitallySignVbaProjectWithCertificate-1.py" >}}

