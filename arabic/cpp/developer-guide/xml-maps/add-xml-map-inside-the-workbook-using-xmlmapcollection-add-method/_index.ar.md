---
title: إضافة خريطة XML داخل ملف العمل باستخدام طريقة XmlMapCollection.Add مع C++
linktitle: إضافة خريطة XML داخل الدفتر باستخدام طريقة XmlMapCollection.Add
type: docs
weight: 10
url: /ar/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/
description: إضافة خريطة XML داخل ملف العمل باستخدام طريقة XmlMapCollection.Add مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells الطريقة [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) التي يمكنك استخدامها لاستيراد خريطة XML داخل مصنف العمل.

## **إضافة خريطة XML داخل الكتيب باستخدام طريقة XmlMapCollection.Add**

يقوم الكود العيني بإضافة خريطة XML داخل مصنف العمل باستخدام الطريقة [**XmlMapCollection.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/xmlmapcollection/add/) ويحفظه كملف إكسل [output excel file](5115434.xlsx). تظهر اللقطة الشاشية خريطة XML التي تم استيرادها من [sample.xml](5115433.xml) داخل ملف إكسل الناتج.

![add-xml-map](add-xml-map.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input XML file
    U16String inputXmlMap = srcDir + u"sample.xml";

    // Create workbook object
    Workbook workbook;

    // Add XML map found inside the sample.xml inside the workbook
    workbook.GetWorksheets().GetXmlMaps().Add(inputXmlMap);

    // Save the workbook in xlsx format
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully as xlsx format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
