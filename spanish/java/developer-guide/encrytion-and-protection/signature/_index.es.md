---
title: Asignar y Validar Firmas Digitales
linktitle: Firma
type: docs
weight: 100
url: /es/java/assign-and-validate-digital-signatures/
description: Archivo de Excel firma digital, verificación. Para proteger la autenticidad del contenido de un libro de trabajo de un archivo de Excel, puede agregar una firma digital usando los códigos C# con Aspose.Cells para .Net.
---
{{% alert color="primary" %}}

 Una firma digital garantiza que el archivo de un libro de trabajo es válido y que nadie lo ha alterado. Puede crear una firma digital personal utilizando el**CERTIFICACIÓN AUTOMÁTICA** herramienta enviada con el paquete de Office Microsoft o cualquier otra herramienta. Incluso puede comprar una firma digital. Después de crear o adquirir una firma digital, debe adjuntarla a su libro de trabajo. Adjuntar una firma digital es similar a sellar un sobre. Si un sobre llega sellado, tiene cierto nivel de seguridad de que nadie ha manipulado su contenido.

 Aspose.Cells for Java API proporcionar el[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) clases para firmar las hojas de cálculo y validarlas.

{{% /alert %}}

## **Firmar las hojas de cálculo**

El proceso de firma requiere un certificado como se mencionó anteriormente. Junto con el certificado, también debe tener su contraseña para firmar con éxito las hojas de cálculo utilizando el Aspose.Cells API.

El siguiente fragmento de código demuestra el uso de Aspose.Cells for Java API para firmar una hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

 En caso de que la contraseña especificada no coincida con la contraseña del certificado, entonces una excepción de tipo*javax.crypto.BadPaddingException* será arrojado.

{{% /alert %}}

## **Validación de las hojas de cálculo**

El siguiente fragmento de código demuestra el uso de Aspose.Cells for Java API para validar la hoja de cálculo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
