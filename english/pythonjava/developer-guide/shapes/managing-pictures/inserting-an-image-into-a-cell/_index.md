---
title: Inserting an Image into a Cell
description: Aspose.Cells for Python via Java is a library for working with spreadsheet files. This article explains how to fit a picture exactly to a single cell size using two different approaches: placing a floating picture over the cell, or embedding the image directly into the cell.
keywords: Aspose.Cells, Python via Java library, spreadsheet, insert image, embed image, picture in cell, fit image to cell, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /python-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells provides two distinct ways to associate an image with a single cell. A floating picture is a shape on the worksheet drawing layer that visually overlays a cell range, while an embedded image is stored inside the cell itself and scales automatically to the cell's display area. Choose the approach that best matches your layout requirements.

{{% /alert %}}

## **Introduction**

Fitting a picture exactly to a single cell is a common requirement when designing spreadsheets that act as visual reports, product catalogs, employee directories, dashboards, or inventory lists. Rather than stretching an image across many cells or placing it loosely on a worksheet, you may want a clean, cell-bound image that stays aligned with the cell that owns it.

Aspose.Cells supports this scenario in two complementary ways:

- **Approach 1 — Place a floating picture over a cell.** Add a `Picture` to the worksheet, set its `setPlacement` to `MOVE_AND_SIZE`, and adjust its anchor cells (`setUpperLeftRow`, `setUpperLeftColumn`, `setLowerRightRow`, `setLowerRightColumn`) so the picture covers exactly one cell.
- **Approach 2 — Embed an image directly in a cell.** Assign image bytes to the cell's `setEmbeddedImage` property. The image automatically scales to fit the cell's display area and travels with the cell.

The rest of this article walks through both approaches, explains the relevant APIs, and shows how to use them in code.

## **Approach 1: Place a Picture Over a Cell**

A floating picture is a `Picture` object that lives on the worksheet drawing layer. Although it is not part of any single cell, it is anchored to a cell range. The picture's anchor cells — its upper-left and lower-right corners — determine its visual extent on the worksheet. By default, a freshly added picture spans several cells.

To make a floating picture cover **exactly one cell**, you need to:

1. Add the picture using `Worksheet.getPictures().add(int row, int column, InputStream stream)`, which anchors the new picture to the given cell.
2. Set the four anchor properties so the picture's bounding rectangle coincides with the target cell.
3. Set `Picture.setPlacement` to `PlacementType.MOVE_AND_SIZE` so the picture moves and resizes with the underlying cell when the user changes the column width or row height.

### **Anchoring the Picture to a Single Cell**

The picture's anchor is defined by four zero-based index properties:

- `setUpperLeftRow` — the row index of the picture's top edge.
- `setUpperLeftColumn` — the column index of the picture's left edge.
- `setLowerRightRow` — the row index of the picture's bottom edge. To make the picture's bottom edge sit at the bottom of row `r`, set this to `r + 1`.
- `setLowerRightColumn` — the column index of the picture's right edge. To make the picture's right edge sit at the right of column `c`, set this to `c + 1`.

For example, to fit the picture exactly into cell **C6** (row index `5`, column index `2`), set `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, and `setLowerRightColumn(3)`.

{{% alert color="primary" %}}

Row and column indices in Aspose.Cells are **zero-based**. Cell C6 has row index 5 and column index 2. Off-by-one errors on the lower-right anchor are the most common source of pictures that appear to overlap into an adjacent cell.

{{% /alert %}}

### **Controlling Placement Behavior**

`getPlacement` is an enum of type `PlacementType` that controls how the picture behaves when the user resizes the row or column beneath it. The recommended value for a single-cell picture is `PlacementType.MOVE_AND_SIZE`, which causes the picture to move and resize together with its underlying cell, preserving the exact fit.

### **Step-by-Step Instructions**

1. Create a new `Workbook` (or open an existing one).
2. Access the target `Worksheet` from `workbook.getWorksheets().get(0)`.
3. Open the image file from disk into an `InputStream` (typically a `FileInputStream`) so the stream is closed properly.
4. Call `worksheet.getPictures().add(5, 2, stream)` to add a picture anchored to cell C6. Capture the returned `Picture` reference.
5. Set the four anchor coordinates so the picture covers only cell C6: `setUpperLeftRow(5)`, `setUpperLeftColumn(2)`, `setLowerRightRow(6)`, `setLowerRightColumn(3)`.
6. Set `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` to keep the picture aligned with C6 when the column or row is resized.
7. Optionally add sample text to surrounding cells to demonstrate that only cell C6 contains the picture.
8. Save the workbook to disk as an `.xlsx` file.

The following code demonstrates the complete approach.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, SaveFormat, PlacementType

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

FileInputStream = jpype.JClass("java.io.FileInputStream")
fs = FileInputStream("logo.png")
try:
    picIndex = worksheet.getPictures().add(5, 2, fs)
    picture = worksheet.getPictures().get(picIndex)
    picture.setUpperLeftRow(5)
    picture.setUpperLeftColumn(2)
    picture.setLowerRightRow(6)
    picture.setLowerRightColumn(3)
    picture.setPlacement(PlacementType.MoveAndSize)
finally:
    fs.close()

workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Approach 2: Embed an Image Directly in a Cell**

Aspose.Cells also exposes a simpler mechanism for cell-bound images: the `Cell.setEmbeddedImage` property. Assigning image bytes to this property attaches the image to the cell itself, as if it were inline content.

### **How Embedded Images Work**

- The image is stored as part of the cell content rather than as a shape on the drawing layer.
- The image automatically scales to fit inside the cell's rendered boundaries. No anchor coordinates or placement settings are required.
- The cell remains a real cell with a real address that can be referenced by formulas, sorted as part of a row, or used in other cell-level operations.

This makes `Cell.setEmbeddedImage` the most concise option when your goal is simply "an image that lives inside this cell."

### **Step-by-Step Instructions**

1. Create a new `Workbook` (or open an existing one).
2. Access the target `Worksheet` from `workbook.getWorksheets().get(0)`.
3. Read the image file from disk into a `byte[]` array (for example, by using a `Files.readAllBytes` call from `java.nio.file.Files`).
4. Get a reference to the target cell — either through `worksheet.getCells().get("C6")` or `worksheet.getCells().get(5, 2)`.
5. Assign the byte array to the cell's `setEmbeddedImage` property.
6. Optionally adjust the row height and column width of the target row and column to give the embedded image a more prominent appearance.
7. Save the workbook to disk as an `.xlsx` file.

The following code demonstrates the complete approach.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

workbook = Workbook()
worksheet = workbook.getWorksheets().get(0)

# Get the target cell C6
cell = worksheet.getCells().get("C6")

# Read the image file into a byte array
imageData = open("logo.png", "rb").read()

# Embed the image directly into the cell
cell.setEmbeddedImage(imageData)

# Optionally adjust row height and column width so the embedded image is more visible
worksheet.getCells().setColumnWidth(2, 30)   # Column C (index 2)
worksheet.getCells().setRowHeight(5, 100)    # Row 6 (index 5)

# Save the resulting workbook as an .xlsx file
workbook.save("output.xlsx", SaveFormat.Xlsx)

jpype.shutdownJVM()
```

## **Choosing the Right Approach**

Both approaches produce a picture that fits inside a single cell, but they differ in how the picture is stored and how it behaves:

- **Use a floating picture (Approach 1) when:**
  - You need finer control over placement, layering, or alignment with other drawing objects.
  - You want the picture to behave as a shape that can be selected, reordered, or grouped with other shapes.
  - You require legacy compatibility with code that already works with `PictureCollection`.
  - You need to compute anchor coordinates dynamically based on worksheet layout.

- **Use an embedded image (Approach 2) when:**
  - You want the simplest possible insertion of an image into a cell.
  - The image should travel with the cell like any other cell content.
  - You do not need to manipulate the image as a shape.

{{% alert color="primary" %}}

Both approaches can coexist in the same workbook. You can place floating pictures over one set of cells and embed images directly into other cells, as the two mechanisms use different storage layers in the file.

{{% /alert %}}

{{< app/cells/assistant language="python" >}}