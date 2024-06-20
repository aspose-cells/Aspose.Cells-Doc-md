---
title: Asignar y Validar Firmas Digitales
linktitle: Firma
type: docs
weight: 100
url: /es/java/assign-and-validate-digital-signatures/
description: Firma digital de archivos de Excel, verificación. Para proteger la autenticidad del contenido de un libro de trabajo de un archivo de Excel, puedes agregar una firma digital usando códigos C# con Aspose.Cells para .Net.
---

{{% alert color="primary" %}}

Una firma digital garantiza que un archivo de libro es válido y que nadie lo ha alterado. Puede crear una firma digital personal utilizando la herramienta **SELFCERT** incluida con el paquete de Microsoft Office u otra herramienta. Incluso puede adquirir una firma digital. Después de crear o adquirir una firma digital, debe adjuntarla a su libro. Adjuntar una firma digital es similar a sellar un sobre. Si un sobre llega sellado, tiene cierto nivel de garantía de que nadie ha manipulado su contenido.

La API Aspose.Cells for Java proporciona las clases [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) y [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) para firmar las hojas de cálculo, así como para validarlas.

{{% /alert %}}

## **Firmar las hojas de cálculo**

El proceso de firma requiere un certificado, como se discutió anteriormente. Junto con el certificado, uno también debe conocer su contraseña para firmar correctamente las hojas de cálculo utilizando la API de Aspose.Cells.

La siguiente muestra de código demuestra el uso de la API Aspose.Cells for Java para firmar una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

En caso de que la contraseña especificada no coincida con la contraseña del certificado, se generará una excepción del tipo *javax.crypto.BadPaddingException*.

{{% /alert %}}

## **Validar las hojas de cálculo**

La siguiente muestra de código demuestra el uso de la API Aspose.Cells for Java para validar la hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
