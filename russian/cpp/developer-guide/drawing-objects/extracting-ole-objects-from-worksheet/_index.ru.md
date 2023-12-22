---
title: Извлечение объектов OLE из рабочего листа
type: docs
weight: 10
url: /ru/cpp/extracting-ole-objects-from-worksheet/
---
##  **Возможные сценарии использования**
 Aspose.Cells позволяет извлекать из рабочего листа все типы объектов OLE. Пожалуйста, используйте[Рабочий лист->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) метод для доступа ко всем объектам OLE внутри листа. Каждый OLE-объект имеет[ПрогИД](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) и[Объектданные](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)свойства, которые могут помочь вам определить тип объекта OLE и успешно извлечь его.
##  **Извлечение объектов OLE из рабочего листа**
 Следующий пример кода загружает[образец файла Excel](66519077.xlsx) который имеет три объекта OLE. Код определяет типы объектов OLE и извлекает их один за другим в виде следующих файлов.

- [выводExtractOleObject.pptx](66519080.pptx)
- [выводExtractOleObject.pdf](66519079.pdf)
- [выводExtractOleObject.docx](66519078.docx)
##  **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
