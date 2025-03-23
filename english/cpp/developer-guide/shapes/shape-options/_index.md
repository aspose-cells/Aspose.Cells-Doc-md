---  
title: Manage Shape Options with C++  
linktitle: Manage Shape Options  
type: docs  
weight: 200  
url: /cpp/managing-shape-options/  
description: Manage shape options in Microsoft Excel files using Aspose.Cells with C++.  
---  

{{% alert color="primary" %}}  

Developers can easily manage shape options in Microsoft Excel files programmatically using Aspose.Cells' flexible API. This topic describes how to manipulate shape options in Microsoft Excel files.  

{{% /alert %}}  

Aspose.Cells provides a class [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) that represents a worksheet in an Excel file. You can use various shape classes in this API to work with graphics or drawing objects in Excel.

A shape is represented by the [Shape](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) class. The [Shape](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) class provides extensive properties and methods for managing shapes within an Excel worksheet.

## **Adding Shapes to a Worksheet**  
To add a shape to a worksheet:

1. Obtain a reference to the desired worksheet.
2. Create an instance of the [Shape](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/) class using the corresponding method in the worksheet.
3. Specify the shape's properties, such as its position and dimensions.
4. Append the shape to the worksheet.

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

void AddShapeToWorksheet()
{
    // Create a workbook
    SharedPtr<Workbook> workbook = MakeObject<Workbook>();
    
    // Obtain the first worksheet
    SharedPtr<Worksheet> worksheet = workbook->GetWorksheets()->Get(0);
    
    // Add a shape to the worksheet
    int shapeIndex = worksheet->GetShapes()->AddShape(ShapeType::Rectangle, 50, 50, 100, 100);
    SharedPtr<Shape> shape = worksheet->GetShapes()->Get(shapeIndex);
    
    // Set the fill color
    shape->GetFill()->SetSolidFill(Color::GetYellow());
    
    // Save the workbook
    workbook->Save(u"Shapes.xlsx");
}
```

## **Accessing Shape Options**  
To modify or access existing shape options:

1. Retrieve the shape object from the worksheet.
2. Access shape properties such as `GetFill()`, `GetLine()`, and `GetText()` to manipulate the shape's appearance and attributes.

```cpp
void ModifyShapeOptions(SharedPtr<Worksheet> worksheet)
{
    // Accessing the first shape
    SharedPtr<Shape> shape = worksheet->GetShapes()->Get(0);
    
    // Modify shape properties
    shape->GetFill()->SetSolidFill(Color::GetBlue());
    shape->GetLine()->SetStyle(LineStyleType::Solid);
}
```

## **Removing Shapes from a Worksheet**  
If you need to remove a shape, you can do so using the index or by retrieving the shape directly. Here's how to remove a shape using its index:

```cpp
void RemoveShape(SharedPtr<Worksheet> worksheet, int shapeIndex)
{
    worksheet->GetShapes()->RemoveAt(shapeIndex);
}
```

In this code snippet, the `RemoveAt` method removes the shape at the specified index. Make sure the index is valid to avoid runtime errors.

Please note that you cannot instruct Aspose.Cells for C++ to change or remove this information from output documents.