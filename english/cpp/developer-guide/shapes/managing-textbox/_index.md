---
title: Managing TextBox of Excel files with C++
linktitle: Managing TextBox
type: docs
weight: 50
url: /cpp/managing-textbox-of-excel/
description: Learn how to manage TextBox in Excel files using Aspose.Cells with C++.
---

{{% alert color="primary" %}}

In Excel, a TextBox is a floating object that can be used to add text or graphical objects. Aspose.Cells allows developers to manipulate TextBoxes in Excel files programmatically. This article explains how to add, modify, and remove TextBoxes in an Excel worksheet using Aspose.Cells for C++.

{{% /alert %}}

### **Adding a TextBox to a Worksheet**
To add a TextBox to a worksheet:

1. Create an instance of the [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class.
2. Access the [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) where you want to add a TextBox.
3. Create a TextBox shape and set its properties like location and size.
4. Add the TextBox to the worksheet's shapes collection.
5. Save the workbook.

```cpp
#include <aspose.cells.h>

void AddTextBox() {
    // Create a workbook instance
    System::SharedPtr<Aspose::Cells::Workbook> workbook = System::MakeObject<Aspose::Cells::Workbook>();
    
    // Access the first worksheet
    System::SharedPtr<Aspose::Cells::Worksheet> worksheet = workbook->GetWorksheets()->GetItem(0);

    // Add a TextBox shape
    System::SharedPtr<Aspose::Cells::Drawing::TextBox> textBox = worksheet->GetShapes()->AddTextBox(2, 2, 100, 50);
    textBox->SetText(L"Hello, TextBox!");

    // Save the workbook
    workbook->Save(u"TextBoxExample.xlsx");
}
```

### **Modifying a TextBox**
To modify an existing TextBox in a worksheet:

1. Access the [Shapes](https://reference.aspose.com/cells/cpp/aspose.cells/drawing/shape/) collection of the worksheet.
2. Retrieve the TextBox shape using its index.
3. Change the properties of the TextBox as needed.

```cpp
#include <aspose.cells.h>

void ModifyTextBox() {
    // Load the workbook
    System::SharedPtr<Aspose::Cells::Workbook> workbook = System::MakeObject<Aspose::Cells::Workbook>(u"TextBoxExample.xlsx");
    
    // Access the first worksheet
    System::SharedPtr<Aspose::Cells::Worksheet> worksheet = workbook->GetWorksheets()->GetItem(0);

    // Access the TextBox shape
    System::SharedPtr<Aspose::Cells::Drawing::TextBox> textBox = System::DynamicCast<Aspose::Cells::Drawing::TextBox>(worksheet->GetShapes()->GetItem(0));
    
    // Modify the TextBox properties
    textBox->SetText(L"Text modified!");
    textBox->SetTextHorizontalAlignment(Aspose::Cells::Drawing::TextAlignmentType::Center);

    // Save the modified workbook
    workbook->Save(u"ModifiedTextBoxExample.xlsx");
}
```

### **Removing a TextBox from a Worksheet**
To remove a TextBox from a worksheet:

1. Access the [Shapes](https://reference.aspose.com/cells/cpp/aspose.cells/drawing/shape/) collection of the worksheet.
2. Use the [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/shapecollection/removeat) method to remove the TextBox by its index.

```cpp
#include <aspose.cells.h>

void RemoveTextBox() {
    // Load the workbook
    System::SharedPtr<Aspose::Cells::Workbook> workbook = System::MakeObject<Aspose::Cells::Workbook>(u"ModifiedTextBoxExample.xlsx");

    // Access the first worksheet
    System::SharedPtr<Aspose::Cells::Worksheet> worksheet = workbook->GetWorksheets()->GetItem(0);

    // Remove the TextBox shape
    worksheet->GetShapes()->RemoveAt(0);

    // Save the changes
    workbook->Save(u"TextBoxRemovedExample.xlsx");
}
```

Please note that you cannot instruct Aspose.Cells for C++ to change or remove this information from output Documents.