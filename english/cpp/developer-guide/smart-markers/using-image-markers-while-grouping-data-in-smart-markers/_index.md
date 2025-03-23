---
title: Using Image Markers while Grouping Data in Smart Markers with C++
linktitle: Using Image Markers while Grouping Data in Smart Markers
type: docs
weight: 30
url: /cpp/using-image-markers-while-grouping-data-in-smart-markers/
description: Learn how to use image markers while grouping data in smart markers with Aspose.Cells for C++.
---

## **Using Image Markers while Grouping Data in Smart Markers**
The following sample creates a workbook and then adds the following smart marker tags in cells D2, E2, and F2 respectively.

{{< highlight java >}}
&=Person.Name(group:normal,skip:1)
&=Person.City
&=Person.Photo(Picture:FitToCell)
{{< /highlight >}}

```cpp
#include <iostream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class Person
{
private:
    U16String m_Name;
    U16String m_City;
    std::vector<uint8_t> m_Photo;

public:
    Person(const U16String& name, const U16String& city, const std::vector<uint8_t>& photo)
        : m_Name(name), m_City(city), m_Photo(photo) {}

    U16String GetName() const { return m_Name; }
    void SetName(const U16String& value) { m_Name = value; }

    U16String GetCity() const { return m_City; }
    void SetCity(const U16String& value) { m_City = value; }

    std::vector<uint8_t> GetPhoto() const { return m_Photo; }
    void SetPhoto(const std::vector<uint8_t>& value) { m_Photo = value; }
};

void Run()
{
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Get the images
    std::vector<uint8_t> photo1 = System::IO::File::ReadAllBytes(srcDir + u"moon.png");
    std::vector<uint8_t> photo2 = System::IO::File::ReadAllBytes(srcDir + u"moon2.png");

    // Create a new workbook and access its worksheet
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the standard row height to 35
    worksheet.GetCells().SetStandardHeight(35);

    // Set column widths of D, E and F
    worksheet.GetCells().SetColumnWidth(3, 20);
    worksheet.GetCells().SetColumnWidth(4, 20);
    worksheet.GetCells().SetColumnWidth(5, 40);

    // Add the headings in columns D, E and F
    worksheet.GetCells().Get(u"D1").PutValue(u"Name");
    Style st = worksheet.GetCells().Get(u"D1").GetStyle();
    st.GetFont().SetIsBold(true);
    worksheet.GetCells().Get(u"D1").SetStyle(st);

    worksheet.GetCells().Get(u"E1").PutValue(u"City");
    worksheet.GetCells().Get(u"E1").SetStyle(st);

    worksheet.GetCells().Get(u"F1").PutValue(u"Photo");
    worksheet.GetCells().Get(u"F1").SetStyle(st);

    // Add smart marker tags in columns D, E, F
    worksheet.GetCells().Get(u"D2").PutValue(u"&=Person.Name(group:normal,skip:1)");
    worksheet.GetCells().Get(u"E2").PutValue(u"&=Person.City");
    worksheet.GetCells().Get(u"F2").PutValue(u"&=Person.Photo(Picture:FitToCell)");

    // Create Persons objects with photos
    std::vector<Person> persons;
    persons.push_back(Person(u"George", u"New York", photo1));
    persons.push_back(Person(u"George", u"New York", photo2));
    persons.push_back(Person(u"George", u"New York", photo1));
    persons.push_back(Person(u"George", u"New York", photo2));
    persons.push_back(Person(u"Johnson", u"London", photo2));
    persons.push_back(Person(u"Johnson", u"London", photo1));
    persons.push_back(Person(u"Johnson", u"London", photo2));
    persons.push_back(Person(u"Simon", u"Paris", photo1));
    persons.push_back(Person(u"Simon", u"Paris", photo2));
    persons.push_back(Person(u"Simon", u"Paris", photo1));
    persons.push_back(Person(u"Henry", u"Sydney", photo2));
    persons.push_back(Person(u"Henry", u"Sydney", photo1));
    persons.push_back(Person(u"Henry", u"Sydney", photo2));

    // Create a workbook designer
    WorkbookDesigner designer(workbook);

    // Set the data source and process smart marker tags
    designer.SetDataSource(u"Person", persons);
    designer.Process();

    // Save the workbook
    workbook.Save(outDir + u"UsingImageMarkersWhileGroupingDataInSmartMarkers.xlsx", SaveFormat::Xlsx);
}

int main()
{
    Aspose::Cells::Startup();
    Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```