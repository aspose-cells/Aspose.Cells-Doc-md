---
title: Вставка объектов OLE в лист
type: docs
weight: 20
url: /ru/cpp/inserting-ole-objects-into-the-worksheet/
---

## **Возможные сценарии использования**
Aspose.Cells позволяет вставлять объект OLE в лист. Используйте метод [Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/) для этой цели. Вам потребуется массив байтов изображения, который будет использоваться для вставки объекта OLE в лист, и байты данных объекта OLE, которые будут вашим фактическим объектом для вставки в лист. 
## **Вставка объектов OLE в лист**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Логотип Aspose</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
