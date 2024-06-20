---
title: إضافة عناصر التحكم ActiveX باستخدام Aspose.Cells
type: docs
weight: 720
url: /ar/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

يمكنك إضافة عناصر التحكم ActiveX باستخدام Aspose.Cells باستخدام الطريقة [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl\(int,%20int,%20int,%20int,%20int,%20int,%20int\)). تأخذ هذه الطريقة معامل [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) الذي يقول أي نوع من عناصر التحكم ActiveX يجب إضافته داخل ورقة العمل. لديها القيم التالية.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK_BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND_BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST_BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO_BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL_BAR)
- [زر التحديد](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN_BUTTON)
- [مربع نص](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT_BOX)
- [زر تبديل](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE_BUTTON)
- [غير معروف](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

بمجرد أن تضيف عنصر تحكم ActiveX داخل مجموعة الأشكال، يمكنك الوصول بعد ذلك إلى كائن عنصر تحكم ActiveX عبر خاصية [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) ثم ضبط خصائصه المختلفة.

{{% /alert %}} 
## **إضافة عنصر تحكم زر التبديل ActiveX باستخدام Aspose.Cells**
يلي كود العينة إضافة عنصر تحكم زر التبديل ActiveX باستخدام Aspose.Cells. الرجاء تنزيل [ملف الإكسل الناتج](5473427.xlsx) المُنشأ باستخدام هذا الكود للاطلاع عليه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
