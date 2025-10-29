---
title: استخراج كائنات OLE من ورقة العمل
type: docs
weight: 10
url: /ar/cpp/extracting-ole-objects-from-worksheet/
---

## **سيناريوهات الاستخدام المحتملة**
يتيح Aspose.Cells لك استخراج جميع أنواع كائنات OLE من ورقة العمل. يرجى استخدام [Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) للوصول إلى جميع كائنات OLE داخل ورقة العمل. كل كائن OLE له خصائص [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) و [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) التي يمكن أن تساعدك في تحديد نوع كائن OLE واستخراجه بنجاح.
## **استخراج كائنات OLE من ورقة العمل**
يقوم الكود المثالي التالي بتحميل [ملف Excel عيني](66519077.xlsx) الذي يحتوي على ثلاث كائنات OLE. يحدد الكود أنواع الكائنات OLE ويستخرجها واحدة تلو الأخرى كما في الملفات التالية.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
