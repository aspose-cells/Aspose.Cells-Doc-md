---
title: تحكم في الموارد الخارجية باستخدام WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /ar/java/control-external-resources-using-workbooksetting-streamprovider/
---
## **سيناريوهات الاستخدام الممكنة**
في بعض الأحيان ، يحتوي ملف Excel الخاص بك على موارد خارجية ، مثل الصور المرتبطة ، وما إلى ذلك. يسمح لك Aspose.Cells بالتحكم في هذه الموارد الخارجية باستخدام[المصنف.الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider)الذي يأخذ تنفيذ[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)واجهه المستخدم. كلما حاولت تقديم ورقة العمل الخاصة بك التي تحتوي على موارد خارجية ، مثل الصور المرتبطة ، وطرق[IStreamProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)سيتم استدعاء الواجهة التي ستمكنك من اتخاذ الإجراءات المناسبة لمواردك الخارجية.
## **تحكم في الموارد الخارجية باستخدام WorkbookSetting.StreamProvider**
يشرح نموذج التعليمات البرمجية التالي استخدام[المصنف.الإعدادات](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#StreamProvider). يقوم بتحميل ملف[نموذج لملف Excel](61767877.xlsx)تحتوي على صورة مرتبطة. يستبدل الرمز الصورة المرتبطة بـ[Aspose الشعار](61767874.png)ويعرض الورقة بأكملها في صورة واحدة باستخدام[عرض الورقة](https://reference.aspose.com/cells/java/com.aspose.cells/SheetRender)صف دراسي. تُظهر لقطة الشاشة التالية نموذج ملف Excel وامتداده[المقدمة صورة الإخراج](61767874.png)كمرجع. كما ترى ، يتم استبدال الصورة المرتبطة المكسورة بشعار Aspose.

![ما يجب القيام به: image_بديل_نص](control-external-resources-using-workbooksetting-streamprovider_1.png)
## **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.java" >}}
