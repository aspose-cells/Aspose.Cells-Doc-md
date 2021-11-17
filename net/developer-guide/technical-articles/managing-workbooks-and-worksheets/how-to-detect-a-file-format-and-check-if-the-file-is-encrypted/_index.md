---
title: How to Detect a File Format and Check if the File is Encrypted
type: docs
weight: 270
url: /net/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
---

{{% alert color="primary" %}}

Sometimes you need to detect a file's format before opening it because the file extension does not guarantee that the file content is appropriate. The file might be encrypted (a password-protected file) so it can't be read it directly, or we should not read it. Aspose.Cells provides the [**FileFormatUtil.DetectFileFormat()**](https://apireference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/detectfileformat/index) static method and some relevant APIs that you can use to process documents.

{{% /alert %}}

The following sample code illustrates how to detect a file format (using the file path) and check its extension. You can also determine whether the file is encrypted.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DetectFileFormatAndEncryption-DetectFileFormatAndEncryption.cs" >}}
