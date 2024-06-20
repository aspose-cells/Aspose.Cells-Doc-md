---
title: التحكم في الموارد الخارجية باستخدام WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /ar/java/control-external-resources-using-workbooksetting-streamprovider/
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، يحتوي ملف Excel الخاص بك على موارد خارجية مثل الصور المرتبطة، إلخ. تسمح Aspose.Cells لك بالتحكم في هذه الموارد الخارجية باستخدام [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider) الذي يأخذ تنفيذ [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) واجهة. كلما حاولت استعراض ورقة العمل الخاصة بك التي تحتوي على موارد خارجية مثل الصور المرتبطة، ستتم استدعاء طرق واجهة [IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider) والتي ستمكنك من اتخاذ إجراءات مناسبة للموارد الخارجية.
## **التحكم في الموارد الخارجية باستخدام WorkbookSetting.StreamProvider**
الرمز المصدري التالي يشرح استخدام [Workbook.Settings.StreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). يحمل [ملف Excel المثال](61767877.xlsx) الذي يحتوي على صورة مرتبطة. يستبدل الرمز المصدري الصورة المرتبطة بـ [شعار Aspose](61767874.png) ويقوم بعرض الورقة بأكملها في صورة واحدة باستخدام فئة [SheetRender](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender). تُظهر اللقطة الشاشية التالية ملف Excel المثال و[صورة الإخراج المُقدمة](61767874.png) للإشارة. كما يمكنك رؤية استبدال الصورة المرتبطة المعطوبة بشعار Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
