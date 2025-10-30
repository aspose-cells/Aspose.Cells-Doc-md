---
title: Agregar Firma Digital a un archivo de Excel que ya está firmado
type: docs
weight: 20
url: /es/python-net/add-digital-signature-to-an-already-signed-excel-file/
description: Este artículo describe cómo agregar una firma digital a un archivo de Excel ya firmado usando códigos en C# con Aspose.Cells para Python via .NET.
keywords: Agregar una firma digital a un archivo de Excel ya firmado, Cómo agregar una firma digital a un documento de Excel ya firmado.
---

## **Escenarios de uso posibles**

Aspose.Cells para Python via .NET proporciona el método [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) que puedes usar para agregar una firma digital a un archivo de Excel ya firmado.

{{% alert color="primary" %}}

Ten en cuenta que al agregar una firma digital a un documento de Excel ya firmado, si el documento original es generado por Aspose.Cells para Python via .NET, funciona bien. Pero si el documento original es generado por otros motores (por ejemplo, Microsoft Excel, etc.), Aspose.Cells para Python via .NET no puede mantener el archivo igual después de cargarlo y volver a guardarlo, esto hará que la firma original sea inválida.

{{% /alert %}}

## **Cómo agregar una firma digital a un archivo de Excel ya firmado**

El siguiente código de muestra demuestra cómo usar el método [**Workbook.add_digital_signature**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/add_digital_signature) para agregar firma digital a un archivo de Excel que ya está firmado. Por favor, verifica el [archivo de Excel de muestra](50528280.xlsx) utilizado en este código. Este archivo ya está firmado digitalmente. Revisa el [archivo de Excel de salida](50528281.xlsx) generado por el código. Hemos utilizado el certificado de demostración llamado [AsposeDemo.pfx](50528279.pfx) en este código que tiene la contraseña **aspose**. La captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de muestra después de la ejecución.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Código de muestra**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AddDigitalSignatureToAnAlreadySignedExcelFile.py" >}}

{{< app/cells/assistant language="python-net" >}}
