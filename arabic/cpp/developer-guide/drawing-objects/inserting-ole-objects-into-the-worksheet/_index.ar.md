---
title: إدراج كائنات OLE في ورقة العمل
type: docs
weight: 20
url: /ar/cpp/inserting-ole-objects-into-the-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**
يتيح Aspose.Cells لك إدراج كائن OLE داخل ورقة العمل. يرجى استخدام [Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/) لهذا الغرض. ستحتاج إلى مصفوفة بايتات صورة ستُستخدم لإدراج كائن OLE داخل ورقة العمل وبايتات بيانات الكائن Ole التي ستكون كائنك الفعلي لإدراج كائن Ole داخل ورقة العمل. 
## **إدراج كائنات OLE في ورقة العمل**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">شعار Aspose</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
