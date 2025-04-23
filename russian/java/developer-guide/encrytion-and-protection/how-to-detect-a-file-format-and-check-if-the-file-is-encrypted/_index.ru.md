---
title: Как определить формат файла и проверить, зашифрован ли файл
type: docs
weight: 2000
url: /ru/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Иногда перед открытием файла необходимо определить его формат, поскольку расширение файла не гарантирует, что содержимое файла соответствует. Файл может быть зашифрован (защищен паролем), поэтому его нельзя прочитать непосредственно, или его не следует читать. Aspose.Cells предоставляет статический метод [**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat-java.io.InputStream-) и соответствующие API, которые вы можете использовать для обработки документов.

{{% /alert %}}

## **Код на Java для обнаружения формата файла и проверки, зашифрован ли файл**

В следующем образце кода показано, как определить формат файла (с использованием пути к файлу) и проверить его расширение. Вы также можете определить, зашифрован ли файл.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
{{< app/cells/assistant language="java" >}}
