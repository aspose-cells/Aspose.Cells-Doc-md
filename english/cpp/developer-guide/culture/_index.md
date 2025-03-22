---
title: Globalization and Localization with C++
linktitle: Globalization and Localization
type: docs
weight: 235
url: /cpp/globalization-and-localization/
description: Learn how to handle globalization and localization in Aspose.Cells for C++ to support multiple languages and regional settings.
---

## **Introduction**
Globalization and localization are essential aspects of software development that ensure applications can support multiple languages and regional settings. Aspose.Cells for C++ provides robust features to handle these requirements effectively.

## **Setting the Culture**
To set the culture for your application, you can use the `CultureInfo` class in C++. This allows you to specify the language and regional settings for your application.

```cpp
#include <system/globalization/culture_info.h>

void SetCulture() {
    // Set the culture to French (France)
    System::Globalization::CultureInfo culture("fr-FR");
    System::Threading::Thread::CurrentThread->CurrentCulture = culture;
    System::Threading::Thread::CurrentThread->CurrentUICulture = culture;
}
```

## **Localizing Cell Data**
Aspose.Cells allows you to localize cell data by formatting it according to the specified culture. For example, you can format dates, numbers, and currencies based on the user's locale.

```cpp
#include <Aspose.Cells.h>

void LocalizeCellData() {
    // Create a new workbook
    System::SharedPtr<Aspose::Cells::Workbook> workbook = System::MakeObject<Aspose::Cells::Workbook>();
    
    // Access the first worksheet
    System::SharedPtr<Aspose::Cells::Worksheet> worksheet = workbook->GetWorksheets()->Get(0);
    
    // Set the value of a cell
    System::SharedPtr<Aspose::Cells::Cell> cell = worksheet->GetCells()->Get("A1");
    cell->PutValue(12345.6789);
    
    // Format the cell as currency using the current culture
    System::SharedPtr<Aspose::Cells::Style> style = cell->GetStyle();
    style->SetCustom("C2");
    cell->SetStyle(style);
    
    // Save the workbook
    workbook->Save("output.xlsx");
}
```

## **Handling Multiple Languages**
Aspose.Cells supports multiple languages for text within cells. You can set the text in different languages and ensure that it is displayed correctly based on the user's locale.

```cpp
#include <Aspose.Cells.h>

void SetMultilingualText() {
    // Create a new workbook
    System::SharedPtr<Aspose::Cells::Workbook> workbook = System::MakeObject<Aspose::Cells::Workbook>();
    
    // Access the first worksheet
    System::SharedPtr<Aspose::Cells::Worksheet> worksheet = workbook->GetWorksheets()->Get(0);
    
    // Set text in different languages
    worksheet->GetCells()->Get("A1")->PutValue("Hello"); // English
    worksheet->GetCells()->Get("A2")->PutValue("Bonjour"); // French
    worksheet->GetCells()->Get("A3")->PutValue("Hola"); // Spanish
    
    // Save the workbook
    workbook->Save("multilingual.xlsx");
}
```

## **Conclusion**
By leveraging the globalization and localization features in Aspose.Cells for C++, you can create applications that are adaptable to various languages and regional settings. This ensures a better user experience for a global audience.