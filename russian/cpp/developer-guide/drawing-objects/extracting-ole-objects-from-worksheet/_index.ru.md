---
title: Извлечение объектов OLE из рабочего листа
type: docs
weight: 10
url: /ru/cpp/extracting-ole-objects-from-worksheet/
---
## **Возможные сценарии использования**
 Aspose.Cells позволяет извлекать из рабочего листа все типы OLE-объектов. Пожалуйста, используйте[IWorksheet->GetIOleObjects()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728) метод для доступа ко всем объектам OLE внутри рабочего листа. Каждый объект OLE имеет[Идентификатор программы](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752) а также[ObjectData](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)свойства, которые помогут определить тип объекта OLE и успешно его извлечь.
## **Извлечение объектов OLE из рабочего листа**
 Следующий пример кода загружает[образец файла Excel](66519077.xlsx) который имеет три объекта OLE. Код определяет типы объектов OLE и извлекает их один за другим в виде следующих файлов.

- [выводExtractOleObject.pptx](66519080.pptx)
- [выводExtractOleObject.pdf](66519079.pdf)
- [выводExtractOleObject.docx](66519078.docx)
## **Образец кода**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
