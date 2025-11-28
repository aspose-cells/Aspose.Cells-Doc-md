---
title: How to Print
description: Learn how to configure print settings in the GridJs, including page orientation, paper size, scaling options, page order, and visibility of images/shapes.
keywords: GridJs, print settings, page layout, orientation, scaling, paper size, print order
type: docs
weight: 195
url: /python-net/aspose-cells-gridjs/how-to-print/
aliases:
  - /python-net/aspose-cells-gridjs/print-settings/
  - /python-net/aspose-cells-gridjs/printing/
  - /python-net/aspose-cells-gridjs/print-configuration/
  - /python-net/aspose-cells-gridjs/print-layout/
---

{{% alert color="primary" %}}

The GridJs provides a built-in **Print Settings** modal that allows users to customize the layout and appearance of the worksheet before sending it to the printer or saving it as a PDF. This ensures that large datasets are presented readably on standard paper sizes.

{{% /alert %}}

## **Introduction**
Spreadsheets often contain data that exceeds the dimensions of a standard sheet of paper. To produce a professional-looking document, it is essential to control how the grid data flows across pages, how it is scaled, and what elements are included.

The **Print Settings** feature allows you to configure:
*   **Page Orientation:** Switch between Portrait and Landscape.
*   **Paper Size:** Support for standard ISO sizes (A3, A4, etc.).
*   **Scaling:** Options to fit content to a specific page count.
*   **Page Order:** Control the sequence in which pages are numbered and printed.
*   **Content Visibility:** Toggle images and shapes.

## **Accessing Print Settings**
To access the print settings:
1.  Click the **Print** icon on the toolbar (or select Print from the menu).
   ![Print Icon](print_icon.png)
2.  The **Settings** modal window will appear, presenting various configuration options.
   ![Print Settings Modal](print_setting.png)
3.  After adjusting settings, click **OK** to generate a preview and open the system print dialog.

## **Configuration Options**

The `ModalPrint` class provides the following configurable parameters. Below is a detailed explanation of each option:

### **1. Page Orientation**
Determines the layout direction of the paper.
*   **Landscape:** (Default) Orients the paper horizontally. Best for spreadsheets with many columns.
*   **Portrait:** Orients the paper vertically. Best for spreadsheets with many rows but fewer columns.

### **2. Paper Size**
Select the physical paper size for the output. The available options correspond to standard ISO paper sizes:
*   **A4:** (Default) The standard paper size used worldwide (210 x 297 mm).
*   **A3:** Larger size, suitable for extensive tables.
*   **A5:** Smaller size.
*   **B4, B5:** Additional standard sizes.

### **3. Scale**
Scaling is critical for fitting spreadsheet data onto physical pages.
*   **No Scaling:** (Default) Prints the data at 100% size. Data that doesn't fit will spill over to subsequent pages.
*   **Fit Sheet on One Page:** Shrinks the entire worksheet (width and height) to fit on a single sheet of paper. *Note: For very large datasets, this may make the text unreadably small.*
*   **Fit All Columns on One Page:** Scales the width of the data to fit the page width. Rows will spill over to subsequent pages as needed. This is the most common setting for wide tables.
*   **Fit All Rows on One Page:** Scales the height of the data to fit the page height. Columns will spill over to horizontal pages.

### **4. Page Order**
When a worksheet is too large to fit on a single page (and scaling is not set to fit on one page), it is split into multiple pages. The **Order** setting determines the sequence in which these pages are printed.

*   **Down, then over:** (Default) Prints pages from top to bottom first, then moves to the right to print the remaining columns. (N-pattern).
*   **Over, then down:** Prints pages from left to right first, then moves down to print the remaining rows. (Z-pattern).

### **5. Images/Shapes**
Controls the visibility of floating objects like charts, inserted images, and shapes during printing.
*   **Show:** (Default) All images and shapes are included in the print output.
*   **Hide:** Images and shapes are excluded, printing only the cell data and grid styles. This is useful for saving ink or producing data-only reports.

## **How it Works**

When the user confirms the settings in the `ModalPrint` dialog, the following internal process occurs:

1.  **Configuration Capture:** The selected options (Orientation, Size, Scale, Order, ImageShow) are captured from the UI form fields.
2.  **Preview Generation:** The application calculates the page breaks based on the selected **Paper Size** and **Scale**.
3.  **Rendering:**
    *   If **Scale** is set to `fitsheet`, `fitcolumns`, or `fitrows`, a transformation matrix is applied to the canvas to reduce the content size.
    *   If **Images/Shapes** is set to `hide`, the rendering loop skips drawing the `fabObjects` (fabric.js objects) on the canvas.
4.  **System Print:** The component triggers the browser's native `window.print()` method or opens a new window with the generated canvas image, allowing the user to select their physical printer or "Save as PDF".

