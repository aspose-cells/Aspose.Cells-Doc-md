---
title: استخراج كائنات OLE من ورقة العمل
type: docs
weight: 10
url: /ar/cpp/extracting-ole-objects-from-worksheet/
---
## **سيناريوهات الاستخدام الممكنة**
 يسمح لك Aspose.Cells باستخراج كافة أنواع كائنات OLE من ورقة العمل. الرجاء استخدام[IWorksheet-> GetIOleObjects ()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728) طريقة للوصول إلى كافة كائنات OLE داخل ورقة العمل. كل كائن OLE له[معرف البرنامج](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752) و[بيانات الكائن](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)الخصائص التي يمكن أن تساعدك في تحديد نوع كائن OLE واستخراجه بنجاح.
## **استخراج كائنات OLE من ورقة العمل**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[نموذج لملف Excel](66519077.xlsx) الذي يحتوي على ثلاثة كائنات OLE. يحدد الكود أنواع كائنات OLE ويستخرجها واحدة تلو الأخرى على أنها الملفات التالية.

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
