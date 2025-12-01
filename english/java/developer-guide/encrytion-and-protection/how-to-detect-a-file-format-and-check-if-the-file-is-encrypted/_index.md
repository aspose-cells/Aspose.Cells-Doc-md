---
title: How to Detect a File Format and Check if the File is Encrypted
type: docs
weight: 2000
url: /java/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you need to detect a file's format before opening it because the file extension does not guarantee that the file content is appropriate. The file might be encrypted (a password-protected file) so it can't be read it directly, or we should not read it. Aspose.Cells provides the [**FileFormatUtil.detectFileFormat()**](https://reference.aspose.com/cells/java/com.aspose.cells/fileformatutil#detectFileFormat-java.io.InputStream-) static method and some relevant APIs which you can use to process documents.

{{% /alert %}}

## **Java code to Detect File Format and Check if the File is Encrypted**

The following sample code illustrates how to detect a file format (using the file path) and check its extension. You can also determine whether the file is encrypted.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectFileFormatandCheckFileEncrypted-DetectFileFormatandCheckFileEncrypted.java" >}}
{{< app/cells/assistant language="java" >}}
