---
title: استخراج كائنات OLE من ورقة العمل
type: docs
weight: 10
url: /ar/cpp/extracting-ole-objects-from-worksheet/
---
##  **سيناريوهات الاستخدام المحتملة**
 Aspose.Cells يسمح لك باستخراج كافة أنواع كائنات OLE من ورقة العمل. الرجاء استخدام[ورقة العمل->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) طريقة للوصول إلى كافة كائنات OLE داخل ورقة العمل. يحتوي كل كائن OLE على[معرف البرنامج](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) و[بيانات الكائن](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)الخصائص التي يمكن أن تساعدك في التعرف على نوع كائن OLE واستخراجه بنجاح.
##  **استخراج كائنات OLE من ورقة العمل**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[عينة من ملف إكسل](66519077.xlsx) الذي يحتوي على ثلاثة كائنات OLE. يحدد الكود أنواع كائنات OLE ويستخرجها واحدًا تلو الآخر كملفات التالية.

- [OutputExtractOleObject.pptx](66519080.pptx)
- [OutputExtractOleObject.pdf](66519079.pdf)
- [OutputExtractOleObject.docx](66519078.docx)
##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
