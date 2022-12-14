---
title: تحكم في الموارد الخارجية باستخدام WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /ar/net/control-external-resources-using-workbooksetting-streamprovider/
---
## **سيناريوهات الاستخدام الممكنة**

في بعض الأحيان ، يحتوي ملف Excel الخاص بك على موارد خارجية ، مثل الصور المرتبطة ، وما إلى ذلك. يسمح لك Aspose.Cells بالتحكم في هذه الموارد الخارجية باستخدام[**المصنف.الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)يأخذ تنفيذ[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)واجهه المستخدم. كلما حاولت تقديم ورقة العمل الخاصة بك التي تحتوي على موارد خارجية ، مثل الصور المرتبطة ، فإن طرق[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)سيتم استدعاء الواجهة التي ستمكنك من اتخاذ الإجراءات المناسبة لمواردك الخارجية.

## **تحكم في الموارد الخارجية باستخدام WorkbookSetting.StreamProvider**

يشرح نموذج التعليمات البرمجية التالي استخدام ملف[**المصنف.الإعدادات**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) . يقوم بتحميل ملف[نموذج لملف Excel](61767863.xlsx) تحتوي على صورة مرتبطة. يستبدل الرمز الصورة المرتبطة بـ[Aspose الشعار](61767862.png) ويعرض الورقة بأكملها في صورة واحدة باستخدام[**عرض الورقة**](https://reference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) صف دراسي. تُظهر لقطة الشاشة التالية نموذج ملف Excel وامتداده[المقدمة صورة الإخراج](61767865.png) كمرجع. كما ترى ، يتم استبدال الصورة المرتبطة المكسورة بشعار Aspose.

![ما يجب القيام به: image_بديل_نص](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
