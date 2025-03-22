---
title: Manage Smart Art with C++
linktitle: Manage Smart Art
type: docs
weight: 200
url: /cpp/managing-smartart/
description: Manage and manipulate Smart Art shapes in Excel files using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells provides comprehensive tools for working with Smart Art shapes in Excel files programmatically. This guide demonstrates how to create, access, and modify Smart Art elements using C++.

{{% /alert %}}

Aspose.Cells for C++ provides the [**SmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.smartart/) namespace for working with Smart Art diagrams. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class contains a [**Shapes**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) collection that allows access to all graphical elements.

## **Adding Smart Art Shapes**
To add a Smart Art diagram to a worksheet:

1. Create a [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) object
2. Access the target worksheet using [**GetIWorksheets()->GetObjectByIndex()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/getobjectbyindex/)
3. Add Smart Art using [**GetIShapes()->AddSmartArt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addsmartart/)
4. Save the workbook with [**Save()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)

```cpp
// Create new workbook
intrusive_ptr<Aspose::Cells::IWorkbook> workbook = Factory::CreateIWorkbook();

// Access first worksheet
intrusive_ptr<Aspose::Cells::IWorksheet> worksheet = workbook->GetIWorksheets()->GetObjectByIndex(0);

// Add Smart Art diagram
intrusive_ptr<Aspose::Cells::Drawing::ISmartArtShape> smartArt = worksheet->GetIShapes()->AddSmartArt(0, 0, 400, 600, Aspose::Cells::Drawing::SmartArtLayoutType::BasicCycle);

// Save output
workbook->Save(u"output.xlsx");
```

## **Accessing Smart Art Properties**
Retrieve and modify Smart Art properties through the [**ISmartArt**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.smartart/ismartart/) interface:

```cpp
// Access existing Smart Art
intrusive_ptr<Aspose::Cells::Drawing::ISmartArt> smartArt = worksheet->GetIShapes()->GetObjectByIndex(0)->GetISmartArt();

// Modify properties
smartArt->SetColorStyle(Aspose::Cells::Drawing::SmartArtColorType::ColoredFillAccent1);
smartArt->SetQuickStyle(Aspose::Cells::Drawing::SmartArtQuickStyleType::SimpleFill);
```

## **Removing Smart Art Shapes**
Remove Smart Art elements by index or reference:

```cpp
// Remove first shape
worksheet->GetIShapes()->GetObjectByIndex(0)->Remove();
```

{{% alert color="warning" %}} 
Please note that you cannot instruct Aspose.Cells for C++ to change or remove Smart Art metadata from output documents.
{{% /alert %}}