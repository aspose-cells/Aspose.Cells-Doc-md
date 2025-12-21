---
title: Add Group function in Aspose.Cells for Reporting Services Client
linktitle: Group Data
type: docs
weight: 120
url: /reportingservices/add-group-function-in-aspose-cells-for-reporting-services-client/
ai_search_scope: cells_reportingservices
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Overview

The **Add Group** function lets you set the grouping attributes of a table‑report item directly from the **Modify Attributes** dialog of Aspose.Cells for Reporting Services.  
You can control four properties:

| Parameter | Description |
|-----------|-------------|
| **Type**  | The group type – either **Row Group** or **Column Group**. |
| **Name**  | The identifier you want to assign to the group. |
| **Level** | The hierarchical level of the group (0 = top‑most). |
| **Hide**  | `true` / `false` – determines whether the group is hidden in the rendered report. |

## Steps to Add / Modify a Group

1. **Open the Modify Report dialog**  
   Click **Modify Report** in the toolbar, then switch to the **Outline** tab.  

   ![Modify Report dialog – Outline tab](add-group-function-in-aspose-cells-for-reporting-services-client_1.jpg)

2. **Configure the group**  
   * Press the **Modify** button.  
   * In the pop‑up, set the desired values for **Type**, **Name**, **Level**, and **Hide**.  
   * For this walkthrough we only change the **Hide** flag, but any of the four fields can be edited.  

   ![Modify button – edit Hide configuration](add-group-function-in-aspose-cells-for-reporting-services-client_2.jpg)

3. **Commit the changes**  
   Click **Commit** to apply the modifications and close the dialog.  

   ![Commit button – save hide configuration](add-group-function-in-aspose-cells-for-reporting-services-client_3.jpg)

4. **Save the report**  
   After committing, remember to save the report file (`*.rdl`) to persist the new group settings.
