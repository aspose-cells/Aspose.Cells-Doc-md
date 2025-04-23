---
title: التحكم في الموارد الخارجية باستخدام WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /ar/net/control-external-resources-using-workbooksetting-streamprovider/
---

## **سيناريوهات الاستخدام المحتملة**

في بعض الأحيان، يحتوي ملف الإكسيل الخاص بك على موارد خارجية مثل الصور المرتبطة وما إلى ذلك. تتيح Aspose.Cells لك التحكم في هذه الموارد الخارجية باستخدام [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) الذي يأخذ تنفيذ واجهة [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider). عندما تحاول عرض ورقة العمل الخاصة بك المحتوية على موارد خارجية مثل الصور المرتبطة، سيتم استدعاء طرق واجهة [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) مما سيمكنك من اتخاذ إجراءات مناسبة للموارد الخارجية الخاصة بك.

## **التحكم في الموارد الخارجية باستخدام WorkbookSetting.StreamProvider**

يوضح الكود العيني التالي استخدام [**Workbook.Settings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider). يحمل ملف الإكسيل العيني المرفق المحتوي على صورة مرتبطة. يقوم الكود بتعويض الصورة المرتبطة بـ [Aspose Logo](61767862.png) ويقوم بعرض الورقة ككاملة في صورة واحدة باستخدام فئة [**SheetRender**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender). تُظهر اللقطة الشاشة التالية بمثال الإكسيل العيني و [صورة الإخراج المقروءة](61767865.png) للإشارة. كما يمكنك رؤية، تم استبدال الصورة المرتبطة التالفة بشعار Aspose.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
