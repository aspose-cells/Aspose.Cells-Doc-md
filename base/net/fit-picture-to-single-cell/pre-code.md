

---
title: Fit Picture to Single Cell Size
description: Aspose.Cells is a .NET library for working with spreadsheet files that allows you to insert and fit images exactly to a single cell. This article will demonstrate how to use Aspose.Cells to place a picture so that it covers exactly one cell, using two different approaches.
keywords: Aspose.Cells, .NET library, spreadsheet, picture, image, cell size, embed image, PictureCollection, EmbeddedImage, PlacementType
type: docs
weight: 195
url: /net/fit-picture-to-single-cell/
---

{{% alert color="primary" %}}

Aspose.Cells supports fitting a picture exactly to a single cell size in a worksheet. There are two approaches available depending on your use case: placing a floating picture over the cell with `PictureCollection.Add` and configuring its placement and dimensions, or embedding an image directly inside a cell using the `Cell.EmbeddedImage` property.

{{% /alert %}}
## **Introduction**
Sometimes you need to insert an image into a worksheet that fits perfectly into a single cell — for example, product thumbnails, employee photos, icons, or item illustrations. Aspose.Cells provides two methods to accomplish this task: placing a floating picture over the cell (Approach 1) or embedding an image directly inside a cell (Approach 2).

{{% alert color="primary" %}}

Approach 1 gives full control over positioning and sizing, and the picture moves and resizes with the cell when rows or columns are resized. Approach 2 is simpler and automatically sizes the embedded image to fill the cell, but offers less control over the picture's behavior.

{{% /alert %}}
## **Approach 1 — Place Picture Over a Cell**
### **Concept Explanation**
This approach uses a floating picture from the `PictureCollection` and positions it so its boundaries align exactly with a target cell. The key APIs involved are:

- **`PictureCollection.Add(int upperLeftRow, int upperLeftColumn, Stream stream)`** — Adds a picture at the specified cell location by providing a stream containing the image data.
- **`Picture.Placement`** — Property of type `PlacementType`. Setting it to `PlacementType.MoveAndSize` makes the picture move and resize together with the underlying cell when the row height or column width changes.
- **`Picture.UpperLeftRow`**, **`Picture.UpperLeftColumn`**, **`Picture.LowerRightRow`**, **`Picture.LowerRightColumn`** — These four integer properties define the picture's bounding rectangle. To fit exactly into one cell, the `LowerRightRow` must equal `UpperLeftRow + 1` and the `LowerRightColumn` must equal `UpperLeftColumn + 1`.

{{% alert color="primary" %}}

When `PlacementType.MoveAndSize` is set, the picture stays locked to the cell's size and position even when the worksheet layout changes, such as when the row height or column width is modified.

{{% /alert %}}
### **Step-by-Step Instructions**
The following steps describe how to fit a picture exactly over a single cell using `PictureCollection`:

1. Create or open a `Workbook` and access the target `Worksheet`.
2. Open the image file as a `Stream` (e.g., from a file path on disk).
3. Call `worksheet.Pictures.Add(upperLeftRow, upperLeftColumn, stream)` to add a picture anchored to a specific cell.
4. Set the returned `Picture` object's `Placement` property to `PlacementType.MoveAndSize`.
5. Set `UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, and `LowerRightColumn` on the picture so that it spans exactly one cell (for example, set `UpperLeftRow=5`, `UpperLeftColumn=2`, `LowerRightRow=6`, `LowerRightColumn=3` to cover cell C6).
6. Save the workbook to disk.
### **Code Example — Place Picture Over a Cell**
The following example demonstrates how to create a workbook, add a picture anchored to a specific cell, configure its placement so it moves and resizes with the cell, and adjust its bounding rectangle so the picture exactly covers one cell.

<!-- CODE_BLOCK:0:Create a new Workbook instance and access the first worksheet via Workbook.Worksheets[0]. Open an image file named "sample.png" from the current directory by reading it into a FileStream and copying it into a MemoryStream so the picture can be added independently of the file lock. Call worksheet.Pictures.Add(5, 2, stream) to add a picture anchored at row 5, column 2 (cell C6 in 1-based terms). Retrieve the newly added picture from the collection (e.g., worksheet.Pictures[0]). Set picture.Placement = PlacementType.MoveAndSize so the picture moves and resizes with the cell. Set picture.UpperLeftRow = 5, picture.UpperLeftColumn = 2, picture.LowerRightRow = 6, picture.LowerRightColumn = 3 so the picture exactly covers cell C6. Save the workbook to the output file "fitpicture.out.xlsx" using Workbook.Save. Dispose of the streams properly. Declare string dataDir = "./" at the top. Include the standard comment header "For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET". -->

After running this example, the resulting `.xlsx` file will contain the image positioned exactly over cell C6, and the picture will move and resize together with the cell whenever row heights or column widths are changed.
## **Approach 2 — Embed Image Inside a Cell**
### **Concept Explanation**
This approach uses the `Cell.EmbeddedImage` property to directly attach an image to a cell. The image is stored as part of the cell's data and automatically renders at the cell's full size when opened in Microsoft Excel or rendered with Aspose.Cells. The key API is:

- **`Cell.EmbeddedImage`** — A property of type `byte[]`. Assigning image data (as a byte array) to this property embeds the image inside the cell. The image will be automatically scaled to fill the cell.

{{% alert color="primary" %}}

The embedded image is bound to the cell itself, so the image scales to match the cell's dimensions automatically. There is no need to manually configure placement or size, which makes this approach the simplest option when you just want an image to appear inside a cell.

{{% /alert %}}
### **Step-by-Step Instructions**
The following steps describe how to embed an image directly into a cell using the `Cell.EmbeddedImage` property:

1. Create or open a `Workbook` and access the target `Worksheet`.
2. Read the image file from disk into a `byte[]` array (e.g., using `File.ReadAllBytes`).
3. Access the target cell (e.g., `worksheet.Cells[5, 2]` for cell C6).
4. Assign the byte array to the cell's `EmbeddedImage` property.
5. Save the workbook to disk.
### **Code Example — Embed Image in a Cell**
The following example demonstrates how to create a workbook, read an image file into a byte array, and assign it directly to a cell so the image becomes embedded within that cell.

<!-- CODE_BLOCK:1:Create a new Workbook instance and access the first worksheet via Workbook.Worksheets[0]. Read the image file named "sample.png" from the current directory into a byte[] array using System.IO.File.ReadAllBytes. Access the target cell at row 5, column 2 (cell C6 in 1-based terms) via worksheet.Cells[5, 2]. Assign the byte array to worksheet.Cells[5, 2].EmbeddedImage so the image is embedded directly inside the cell. Save the workbook to the output file "embeddedimage.out.xlsx" using Workbook.Save. Declare string dataDir = "./" at the top. Include the standard comment header "For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET". -->

After running this example, the resulting `.xlsx` file will contain the image embedded inside cell C6, automatically rendered at the cell's full size when viewed in Microsoft Excel.
## **Summary**
Both approaches produce a worksheet in which the image fits exactly to a single cell:

- **Approach 1 (PictureCollection + MoveAndSize)** is best when you need explicit control over the picture's position and want the picture to resize together with the cell when columns or rows are resized. It uses floating picture semantics, which is ideal when the image is a visual overlay rather than part of the cell's stored data.
- **Approach 2 (Cell.EmbeddedImage)** is best for simple use cases where you simply want an image to appear inside a cell, sized automatically with no manual placement configuration.

Both approaches are supported across the XLSX file format, and the resulting files are fully compatible with Microsoft Excel.

## **Related Articles**
- [Merging and Unmerging Cells](/cells/net/merging-and-unmerging-cells/)
{{< app/cells/assistant language="csharp" >}}