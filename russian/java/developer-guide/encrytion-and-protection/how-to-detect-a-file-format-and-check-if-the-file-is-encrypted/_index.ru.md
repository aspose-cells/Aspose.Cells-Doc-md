---
title: Как определить формат файла и проверить, зашифрован ли файл
type: docs
weight: 2000
url: /ru/java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Иногда вам нужно определить формат файла перед его открытием, потому что расширение файла не гарантирует, что содержимое файла подходит. Файл может быть зашифрован (файл, защищенный паролем), поэтому его нельзя прочитать напрямую, или мы не должны его читать. Aspose.Cells обеспечивает[**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat(java.io.InputStream)статический метод и некоторые соответствующие API, которые можно использовать для обработки документов.

{{% /alert %}}

## **Код Java для определения формата файла и проверки того, зашифрован ли файл**

В следующем примере кода показано, как определить формат файла (используя путь к файлу) и проверить его расширение. Вы также можете определить, зашифрован ли файл.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
