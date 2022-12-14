---
title: Cómo detectar un formato de archivo y comprobar si el archivo está cifrado
type: docs
weight: 2700
url: /es/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 A veces es necesario detectar el formato de un archivo antes de abrirlo porque la extensión del archivo no garantiza que el contenido del archivo sea apropiado. El archivo puede estar encriptado (un archivo protegido con contraseña) por lo que no se puede leer directamente, o no deberíamos leerlo. Aspose.Cells proporciona el[**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) método estático y algunas API relevantes que puede usar para procesar documentos.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo detectar un formato de archivo (usando la ruta del archivo) y verificar su extensión. También puede determinar si el archivo está encriptado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
