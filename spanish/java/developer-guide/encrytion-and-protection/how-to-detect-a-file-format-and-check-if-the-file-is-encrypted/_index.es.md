---
title: Cómo detectar un formato de archivo y comprobar si el archivo está cifrado
type: docs
weight: 2000
url: /es/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 A veces es necesario detectar el formato de un archivo antes de abrirlo porque la extensión del archivo no garantiza que el contenido del archivo sea apropiado. El archivo puede estar encriptado (un archivo protegido con contraseña) por lo que no se puede leer directamente, o no deberíamos leerlo. Aspose.Cells proporciona el[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)método estático y algunas API relevantes que puede usar para procesar documentos.

{{% /alert %}}

## **Código Java para detectar el formato de archivo y comprobar si el archivo está cifrado**

El siguiente código de ejemplo ilustra cómo detectar un formato de archivo (usando la ruta del archivo) y verificar su extensión. También puede determinar si el archivo está encriptado.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
