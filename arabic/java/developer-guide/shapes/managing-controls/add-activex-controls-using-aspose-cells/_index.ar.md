---
title: إضافة عناصر التحكم ActiveX باستخدام Aspose.Cells
type: docs
weight: 720
url: /ar/java/add-activex-controls-using-aspose-cells/
---

{{% alert color="primary" %}} 

يمكنك إضافة عناصر تحكم ActiveX باستخدام Aspose.Cells باستخدام طريقة [ShapeCollection.addActiveXControl()](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addActiveXControl-int-int-int-int-int-int-int-). تتطلب هذه الطريقة معلمة [ControlType](https://reference.aspose.com/cells/java/com.aspose.cells/ControlType) التي تخبر نوع عنصر ActiveX الذي يجب إضافته داخل ورقة العمل. تحتوي على القيم التالية.

- [CHECK_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#CHECK-BOX)
- [COMBO_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO-BOX)
- [COMMAND_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMMAND-BUTTON)
- [IMAGE](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#IMAGE)
- [LABEL](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LABEL)
- [LIST_BOX](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#LIST-BOX)
- [RADIO_BUTTON](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#RADIO-BUTTON)
- [SCROLL_BAR](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SCROLL-BAR)
- [زر التحديد](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#SPIN-BUTTON)
- [مربع نص](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TEXT-BOX)
- [زر تبديل](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#TOGGLE-BUTTON)
- [غير معروف](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#UNKNOWN)

بمجرد أن تضيف عنصر تحكم ActiveX داخل مجموعة الأشكال، يمكنك الوصول بعد ذلك إلى كائن عنصر تحكم ActiveX عبر خاصية [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) ثم ضبط خصائصه المختلفة.

{{% /alert %}} 
## **إضافة عنصر تحكم زر التبديل ActiveX باستخدام Aspose.Cells**
يلي كود العينة إضافة عنصر تحكم زر التبديل ActiveX باستخدام Aspose.Cells. الرجاء تنزيل [ملف الإكسل الناتج](5473427.xlsx) المُنشأ باستخدام هذا الكود للاطلاع عليه.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddActiveXControl-AddActiveXControl.java" >}}
{{< app/cells/assistant language="java" >}}
