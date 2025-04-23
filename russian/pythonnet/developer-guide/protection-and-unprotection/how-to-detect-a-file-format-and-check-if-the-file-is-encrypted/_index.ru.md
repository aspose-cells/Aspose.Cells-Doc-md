---
title: Как определить формат файла и проверить, зашифрован ли файл
type: docs
weight: 2700
url: /ru/python-net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Иногда вам нужно определить формат файла перед его открытием, поскольку расширение файла не гарантирует, что содержимое файла соответствует. Файл может быть зашифрован (защищен паролем), поэтому его нельзя прочитать напрямую, или его не следует читать. Aspose.Cells for Python via .NET предоставляет статический метод [**FileFormatUtil.detect_file_format()**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/detect_file_format) и некоторые сопутствующие API, которые можно использовать для обработки документов.

{{% /alert %}}

В следующем образце кода показано, как определить формат файла (с использованием пути к файлу) и проверить его расширение. Вы также можете определить, зашифрован ли файл.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DetectFileFormatAndEncryption.py" >}}

