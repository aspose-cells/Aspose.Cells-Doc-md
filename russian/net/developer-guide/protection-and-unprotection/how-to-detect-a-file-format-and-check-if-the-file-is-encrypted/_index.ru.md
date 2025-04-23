---
title: Как определить формат файла и проверить, зашифрован ли файл
type: docs
weight: 2700
url: /ru/net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Иногда вам может потребоваться определить формат файла перед его открытием, потому что расширение файла не гарантирует соответствие содержимого файла. Файл может быть зашифрован (защищен паролем), поэтому его нельзя прочитать непосредственно, или его не следует читать. Aspose.Cells предоставляет статический метод [**FileFormatUtil.DetectFileFormat()**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) и некоторые связанные API, которые вы можете использовать для обработки документов.

{{% /alert %}}

В следующем образце кода показано, как определить формат файла (с использованием пути к файлу) и проверить его расширение. Вы также можете определить, зашифрован ли файл.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
{{< app/cells/assistant language="csharp" >}}
