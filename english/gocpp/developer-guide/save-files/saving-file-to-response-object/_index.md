---
title: Saving File to Response Object with Golang via C++
linktitle: Saving File to Response Object
type: docs
weight: 50
url: /go-cpp/saving-file-to-response-object/
description: Learn how to save files dynamically and send them directly to a client browser using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells makes it possible to manipulate files. This article explains the various ways in which files can be saved to a response object.

{{% /alert %}}

## **Saving File to Response Object**

It is also possible to generate a file dynamically and send it directly to a client browser. In order to do so, use a special overloaded version of the [**Save**](https://reference.aspose.com/cells/go-cpp/workbook/save_string_saveformat/) method that accepts the following parameters:

- **HttpResponse** object.  
- File name.  
- [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/), the content‑disposition type of the output file.  
- [**SaveOptions**](https://reference.aspose.com/cells/go-cpp/saveoptions/), the file format type.

The [**ContentDisposition**](https://reference.aspose.com/cells/go-cpp/contentdisposition/) enumeration determines whether the file being sent to the browser provides the option to open directly in the browser or in an application associated with .xls/.xlsx or another extension.

The enumeration contains the following pre‑defined save types:

| **Type** | **Description** |
| :- | :- |
| Attachment | Sends the spreadsheet to the browser and opens it in an application as an attachment associated with .xls/.xlsx or other extensions |
| Inline | Sends the document to the browser and presents an option to save the spreadsheet to disk or open it inside the browser |

### **XLS Files**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject.go" >}}

### **XLSX Files**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-1.go" >}}

### **PDF Files**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-2.go" >}}

### **Note**

Due to the object **System.Web.HttpResponse** not being included in .NET 5 and .NET Standard, this function does not exist in Aspose.Cells .NET 5 and .NET Standard versions. You can refer to the following code to save the file to a stream and then operate on the stream.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SavingFileToResponseObject-3.go" >}}