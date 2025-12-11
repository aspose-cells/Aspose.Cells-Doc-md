---
title: Managing Document Properties
type: docs
weight: 30
url: /cpp/managing-document-properties/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenario**
Aspose.Cells allows you to work with built‑in and custom document properties. Here is the Microsoft Excel interface for opening these document properties. Just click on **Advanced Properties** as shown in this screenshot to view them.

![todo:image_alt_text](managing-document-properties_1.png)

## **Managing Document Properties**
The following sample code loads the [sample Excel file](23166989.xlsx) and reads the built‑in document properties, e.g., *Title* and *Subject*, and then changes them. It also reads the custom document property, i.e., *MyCustom1*, and then adds a new custom document property, i.e., *MyCustom5*, and writes the [output Excel file](23166986.xlsx). The following screenshot shows the effect of the sample code on the sample Excel file.

![todo:image_alt_text](managing-document-properties_2.png)

## **Sample Code**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}

## **Console Output**
This is the console output of the above sample code when executed with the provided [sample Excel file](23166989.xlsx).

{{< highlight java >}}
Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.
{{< /highlight >}}

{{< app/cells/assistant language="cpp" >}}
