---
title: تحديث عنصر التحكم ActiveX ComboBox
type: docs
weight: 900
url: /ar/java/update-activex-combobox-control/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك قراءة أو كتابة قيم عنصر التحكم ActiveX ComboBox باستخدام Aspose.Cells. يرجى الوصول إلى عنصر التحكم ActiveX عبر الخاصية [Shape.ActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/shape#ActiveXControl) والتحقق من نوعه عبر الخاصية [ActiveXControl.Type](https://reference.aspose.com/cells/java/com.aspose.cells/activexcontrol#Type)، يجب أن يعيد قيمة [ControlType.ComboBox](https://reference.aspose.com/cells/java/com.aspose.cells/controltype#COMBO_BOX) ومن ثم قم بتحويل النوع إلى [ComboBoxActiveXControl](https://reference.aspose.com/cells/java/com.aspose.cells/ComboBoxActiveXControl) وقراءة أو تعديل خصائصه المختلفة.

يرجى تنزيل [ملف الإكسل العيني](5473374.xlsx) المستخدم في الكود المثالي التالي و [ملف الإكسل الناتج](5473375.xlsx) الذي تم إنشاؤه به.
## **تحديث عنصر تحكم ActiveX ComboBox**
تظهر اللقطة الشاشية التالية تأثير الكود المثالي على [ملف الإكسل العيني](5473374.xlsx). كما يمكنك رؤية أن قيمة عنصر التحكم ActiveX ComboBox تم تحديثها إلى "هذا عنصر تحكم مربع الاختيار".

![todo:image_alt_text](update-activex-combobox-control_1.png)
## **الكود المثالي**
الكود النموذجي التالي يقوم بتحديث قيمة عنصر تحكم ActiveX ComboBox الموجود داخل [ملف الإكسل العيني](5473374.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UpdateActiveXComboBoxControl-UpdateActiveXComboBoxControl.java" >}}
