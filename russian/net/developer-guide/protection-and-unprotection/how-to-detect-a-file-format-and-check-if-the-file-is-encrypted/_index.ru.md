---
title: Как определить формат файла и проверить, зашифрован ли файл
type: docs
weight: 2700
url: /ru/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---
{{% alert color="primary" %}}

 Иногда вам нужно определить формат файла перед его открытием, потому что расширение файла не гарантирует, что содержимое файла подходит. Файл может быть зашифрован (файл, защищенный паролем), поэтому его нельзя прочитать напрямую, или мы не должны его читать. Aspose.Cells обеспечивает[**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) статический метод и некоторые соответствующие API, которые можно использовать для обработки документов.

{{% /alert %}}

В следующем примере кода показано, как определить формат файла (используя путь к файлу) и проверить его расширение. Вы также можете определить, зашифрован ли файл.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
