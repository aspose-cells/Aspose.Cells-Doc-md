---
title: Cómo Detectar el Formato de un Archivo y Verificar si el Archivo está Encriptado
type: docs
weight: 2700
url: /es/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

A veces necesitas detectar el formato de un archivo antes de abrirlo porque la extensión del archivo no garantiza que el contenido del archivo sea apropiado. El archivo podría estar encriptado (un archivo protegido con contraseña) por lo que no se puede leer directamente, o no deberíamos leerlo. Aspose.Cells proporciona el método [**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) estático y algunas API relevantes que puedes usar para procesar documentos.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo detectar el formato de un archivo (usando la ruta del archivo) y verificar su extensión. También puedes determinar si el archivo está encriptado.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
{{< app/cells/assistant language="csharp" >}}
