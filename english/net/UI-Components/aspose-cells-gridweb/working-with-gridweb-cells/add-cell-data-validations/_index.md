---
title: Add Cell Data Validations
type: docs
weight: 90
url: /net/aspose-cells-gridweb/add-cell-data-validations/
keywords: GridWeb,validation,data validation,GridValidation
description: This article introduces how to add data validation (GridValidation) in GridWeb.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb allows you to add **Data Validation** using the `GridWorksheet.Validations.Add()` method. Using this method, you must specify the **cell range**. However, if you want to create a data validation in a single GridCell, you can do it directly using the `GridCell.CreateValidation()` method. Similarly, you can remove **Data Validation** from a GridCell using the `GridCell.RemoveValidation()` method.

{{% /alert %}} 
## **Create Data Validation in a GridCell of GridWeb**
The following sample code creates a **Data Validation** in cell B3. If you enter any value that is not between 20 and 40, cell B3 will display a **validation error** in the form of **Red XXXX**, as shown in this screenshot.

![todo:image_alt_text](add-cell-data-validations_1.png)

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AddDataValidation.aspx-AddDataValidation.cs" >}}
