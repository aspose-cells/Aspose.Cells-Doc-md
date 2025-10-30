---
title: Cómo Detectar el Formato de un Archivo y Verificar si el Archivo está Encriptado
type: docs
weight: 2700
url: /es/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

A veces, necesitas detectar el formato de un archivo antes de abrirlo porque la extensión del archivo no garantiza que el contenido del mismo sea apropiado. El archivo podría estar cifrado (con protección por contraseña) por lo que no se puede leer directamente, o simplemente no deberíamos leerlo. Aspose.Cells para Python via .NET proporciona el método estático [**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format) y algunas APIs relevantes que puedes usar para procesar documentos.

{{% /alert %}}

El siguiente código de ejemplo ilustra cómo detectar el formato de un archivo (usando la ruta del archivo) y verificar su extensión. También puedes determinar si el archivo está encriptado.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

{{< app/cells/assistant language="python-net" >}}
