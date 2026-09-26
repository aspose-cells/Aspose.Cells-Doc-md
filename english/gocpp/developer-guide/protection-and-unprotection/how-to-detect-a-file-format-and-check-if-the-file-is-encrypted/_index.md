---  
title: How to Detect a File Format and Check if the File is Encrypted with Golang via C++  
linktitle: How to Detect a File Format and Check if the File is Encrypted  
type: docs  
weight: 2700  
url: /go-cpp/how-to-detect-a-file-format-and-check-if-the-file-is-encrypted/  
description: Learn how to detect a file's format and check if it is encrypted using Aspose.Cells with Golang via C++.  
---  

{{% alert color="primary" %}}

Sometimes you need to detect a file's format before opening it because the file extension does not guarantee that the file content is appropriate. The file might be encrypted (a password‑protected file), so it can't be read directly, or you should not read it. Aspose.Cells provides the [**FileFormatUtil::DetectFileFormat()**](https://reference.aspose.com/cells/go-cpp/fileformatutil/fileformatutil_detectfileformat_stream/) static method and some relevant APIs that you can use to process documents.

{{% /alert %}}

The following sample code illustrates how to detect a file format (using the file path) and check its extension. You can also determine whether the file is encrypted.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToDetectAFileFormatAndCheckIfTheFileIsEncrypted.go" >}}  
{{< app/cells/assistant language="go" >}}
