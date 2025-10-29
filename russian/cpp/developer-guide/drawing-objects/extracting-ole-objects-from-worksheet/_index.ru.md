---
title: Извлечение объектов OLE из листа
type: docs
weight: 10
url: /ru/cpp/extracting-ole-objects-from-worksheet/
---

## **Возможные сценарии использования**
Aspose.Cells позволяет извлекать все типы объектов OLE из листа. Используйте метод [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) для доступа ко всем объектам OLE внутри листа. У каждого объекта OLE есть свойства [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) и [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/), которые могут помочь вам определить тип объекта OLE и успешно извлечь его.
## **Извлечение объектов OLE из листа**
Следующий образец кода загружает [образец файла Excel](66519077.xlsx), содержащий три объекта OLE. Код определяет типы объектов OLE и извлекает их поочередно в виде следующих файлов.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
