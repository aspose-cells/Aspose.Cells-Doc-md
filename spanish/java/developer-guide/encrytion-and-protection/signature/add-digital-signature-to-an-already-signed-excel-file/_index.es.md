---
title: Agregar Firma Digital a un archivo de Excel que ya está firmado
type: docs
weight: 20
url: /es/java/add-digital-signature-to-an-already-signed-excel-file/
---

## **Escenarios de uso posibles**

Aspose.Cells proporciona el método [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) que se puede utilizar para agregar una firma digital a un archivo de Excel que ya ha sido firmado.

{{% alert color="primary" %}}

Ten en cuenta que al agregar una firma digital a un documento de Excel que ya está firmado, si el documento original es generado por otros motores (por ejemplo, Microsoft Excel, etc.), Aspose.Cells no puede mantener el archivo igual después de cargarlo y volver a guardarlo, lo que hará que la firma original sea inválida.

{{% /alert %}}

## **Agregar firma digital a un archivo de Excel ya firmado**

El siguiente código de muestra explica cómo hacer uso del método [**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature-com.aspose.cells.DigitalSignatureCollection-) para agregar una firma digital a un archivo de Excel que ya ha sido firmado. Por favor, revise el archivo de Excel de muestra utilizado en este código. Este archivo ya está firmado digitalmente. Por favor, revise el archivo de Excel de salida generado por el código. Hemos utilizado el certificado de demostración llamado [AsposeTest.pfx](50528289.pfx) en este código que tiene una contraseña *aspose*. La captura de pantalla muestra el efecto del código de ejemplo en el archivo de Excel de muestra después de la ejecución.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
{{< app/cells/assistant language="java" >}}
