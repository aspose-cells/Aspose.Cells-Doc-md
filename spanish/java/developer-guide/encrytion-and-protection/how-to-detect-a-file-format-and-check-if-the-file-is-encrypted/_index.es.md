---
title: Cómo Detectar el Formato de un Archivo y Verificar si el Archivo está Encriptado
type: docs
weight: 2000
url: /es/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

A veces necesitas detectar el formato de un archivo antes de abrirlo porque la extensión del archivo no garantiza que el contenido del archivo sea adecuado. El archivo podría estar encriptado (un archivo protegido con contraseña) por lo que no se puede leer directamente, o no deberíamos leerlo. Aspose.Cells proporciona el método estático [**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)) y algunas API relevantes que puedes usar para procesar documentos.

{{% /alert %}}

## **Código Java para Detectar el Formato de Archivo y Comprobar si el Archivo está Encriptado**

El siguiente código de ejemplo ilustra cómo detectar el formato de un archivo (usando la ruta del archivo) y verificar su extensión. También puedes determinar si el archivo está encriptado.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
