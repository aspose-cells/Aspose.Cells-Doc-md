---  
title: Remove Unused Styles inside the Workbook with Golang via C++  
linktitle: Remove Unused Styles inside the Workbook  
type: docs  
weight: 340  
url: /go-cpp/remove-unused-styles-inside-the-workbook/  
description: Remove unused styles in an Excel workbook using Aspose.Cells with Golang via C++.  
---  

{{% alert color="primary" %}}  

Unused styles in Excel files not only take up space but also cause performance issues while converting to different formats such as PDF, HTML, etc. Aspose.Cells provides the [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/) to remove all unused styles from the workbook.  

{{% /alert %}}  

The following code demonstrates the usage of [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/). The code loads the [template Excel file](5115520.xlsx) which you can download from the provided link. It contains an unused style named **AsposeStyle**; this style and all other unused styles will be removed after the execution of the code.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemoveUnusedStylesInsideTheWorkbook.go" >}}