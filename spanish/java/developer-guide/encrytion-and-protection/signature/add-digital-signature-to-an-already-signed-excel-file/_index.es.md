---
title: Agregar firma digital a un archivo de Excel ya firmado
type: docs
weight: 20
url: /es/java/add-digital-signature-to-an-already-signed-excel-file/
---
## **Posibles escenarios de uso**

Aspose.Cells proporciona el[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) que puede usar para agregar una firma digital a un archivo de Excel ya firmado.

{{% alert color="primary" %}}

Tenga en cuenta que al agregar una firma digital a un documento de Excel ya firmado, si el documento original es un documento generado por Aspose.Cells, funciona bien. Pero si el documento original es generado por otros motores (por ejemplo, Microsoft Excel, etc.), Aspose.Cells no puede mantener el archivo igual después de cargarlo y volver a guardarlo, esto hará que la firma original no sea válida.

{{% /alert %}}

## **Agregar firma digital a un archivo de Excel ya firmado**

El siguiente código de ejemplo explica cómo hacer uso de[**Workbook.addDigitalSignature(DigitalSignatureCollection digitalSignatureCollection)**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#addDigitalSignature(com.aspose.cells.DigitalSignatureCollection)) para agregar una firma digital a un archivo de Excel ya firmado. Por favor, checa el[ejemplo de archivo de Excel](50528287.xlsx)utilizado en este código. Este archivo ya está firmado digitalmente. Por favor, checa el[archivo de salida de Excel](50528288.xlsx)generado por el código. Hemos utilizado el certificado de demostración llamado[AsposePrueba.pfx](50528289.pfx)en este código que tiene una contraseña*suponer*La captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra después de la ejecución.

![todo:imagen_alternativa_texto](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AddDigitalSignatureToAnAlreadySignedExcelFile.java" >}}
