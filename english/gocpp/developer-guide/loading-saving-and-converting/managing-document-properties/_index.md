---
title: Managing Document Properties
type: docs
weight: 30
url: /go-cpp/managing-document-properties/
---

## **Possible Usage Scenario**

Aspose.Cells allows you to work with Built-In and Custom document properties. Here is the Microsoft Excel interface to open these *Document Properties*. Just click on the *Advanced Properties* as shown in this screenshot and view them.

![todo:image_alt_text](managing-document-properties_1.png)

## **Managing Document Properties**

The following sample code loads [sample Excel file](23166989.xlsx) and reads the built-in document properties, e.g., *Title and Subject*, and then changes them. Then, it also reads the custom document property, i.e., *MyCustom1* and then adds a new custom document property, i.e., *MyCustom5* and writes the [output Excel file](23166986.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file.

![todo:image_alt_text](managing-document-properties_2.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingDocumentProperties.go" >}}

## **Console Output**

This is the console output of the above sample code when executed with the provided [sample Excel file](23166989.xlsx).

{{< highlight java >}}

Title: Aspose Team

Subject: Aspose.Cells for Go via C++

MyCustom1: This is my custom one.

{{< /highlight >}}
