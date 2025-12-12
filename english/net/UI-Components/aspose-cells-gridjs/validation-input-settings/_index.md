---
title: Validation Input Settings
description: This guide explains how to configure data validation rules in Aspose.Cells GridJs, covering toolbar access, modal options for criteria, input messages, error alerts, and the available client‑side JavaScript API.
keywords: GridJs, Data Validation, Input Message, Error Alert, Validation Rules, Front‑end, Spreadsheet
type: docs
weight: 210
url: /net/aspose-cells-gridjs/validation-input-settings/
aliases:
  - /net/aspose-cells-gridjs/gridjs-validation-settings/
  - /net/aspose-cells-gridjs/data-validation-settings/
  - /net/aspose-cells-gridjs/validation-rules-configuration/
  - /net/aspose-cells-gridjs/setting-up-data-validation/
  - /net/aspose-cells-gridjs/validation-input-configuration/
---

{{% alert color="primary" %}}
Data validation helps ensure that users enter only allowed values in cells. GridJs provides a full‑featured modal dialog where you can define the rule type, specify the target range, and customize helpful messages and error alerts.
{{% /alert %}}

## Overview
The **Validation Input Settings** feature is accessed entirely in the browser. A dedicated **Data Validation** button on the toolbar (or the context/menubar) opens a modal dialog with three tabs:

1. **Criteria** – Choose the rule type and define the allowed values/ranges.  
2. **Input Message** – Optional tip shown when the cell is selected.  
3. **Error Alert** – Message displayed when a user tries to enter an invalid value.

All configuration is stored in the sheet model, and the component validates edits automatically.

## UI Operations

### Opening the Validation Dialog
right‑click a cell (or a selected range) and choose **Data Validation…**, or use **Data → Validation** from the menubar.  
![](contextmenu.png)
![](menubar_data.png)


### Criteria Tab
1. In the **Allow** dropdown, select the rule type (e.g., *Whole Number*, *Decimal*, *List*, *Date*, etc.).  
2. Based on the chosen type, the dialog shows the relevant fields:  
   * **Value1** and **Value2** inputs (each ~70 % width).  
   * **Operator** dropdown (e.g., *between*, *equal to*).  
   * For **List**, toggle **In‑cell dropdown** to display a drop‑down list directly in the grid.  
3. To define the target cell range, click the range‑select icon next to **Value2**.  
![](modal_criteriaTab.png)

### Range‑Selection Page
1. The spreadsheet UI (sheet tabs, footer, context menu) is temporarily hidden and the background is masked.  
2. The validation modal moves to the top‑right corner.  
3. An input box shows the current range (e.g., `A1:B10`). Edit it manually or click cells in the grid to pick a range.  
4. Click the **Return** (back‑arrow) button to confirm the selection or cancel to keep the previous range.  
![](modal_rangeSelection.png)

### Input Message Tab
1. Switch **Show Input Message** on/off.  
2. Fill **Title** and **Message** fields with the text you want users to see when the cell becomes active.  
3. Choose an icon (Stop, Warning, Information) that appears alongside the message.  
![](modal_inputMessage.png)

### Error Alert Tab
1. Switch **Show Error Alert** on/off.  
2. Pick an **Alert Style**:  
   * **Stop** – red “X” (blocks the entry).  
   * **Warning** – yellow “!” (allows entry after confirmation).  
   * **Information** – blue “i” (informational only).  
3. Provide **Title** and **Error Text** that will be displayed when a user violates the rule.  
4. Click **Apply** to save the rule, or **Cancel** to discard changes.  
![](modal_errorAlert.png)

### Saving & Applying
* Press **Apply** on any tab to commit the validation rule to the selected range.  
* The rule is now active; any subsequent edit to cells in that range triggers automatic validation.



## Tips & Best Practices
* **Choose the narrowest rule needed.** Using *Whole Number* with a *between* operator reduces the chance of accidental invalid entries.  
* **Enable In‑cell dropdowns** for list‑type rules to give users a visual selection list.  
* **Provide a helpful Input Message** – it appears before the user types, reducing validation errors.  
* **Select the appropriate Error Alert style:**  
  * *Stop* for critical data (e.g., IDs).  
  * *Warning* when you want to allow the entry after user confirmation.  

---