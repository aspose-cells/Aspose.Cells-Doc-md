---
title: تحديث عنصر التحكم ActiveX ComboBox
type: docs
weight: 170
url: /ar/python-net/update-activex-combobox-control/
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك قراءة أو كتابة قيم تحكم ComboBox الخاص بـ ActiveX باستخدام Aspose.Cells لـ Python via .NET. يرجى الوصول إلى تحكم ActiveX عبر الخاصية [Shape.active_x_control](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/active_x_control) والتحقق من نوعه عبر الخاصية [ActiveXControl.type](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/activexcontrolbase/type/)، يجب أن تُرجع القيمة [ControlType.COMBO_BOX](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/controltype) ثم تحويل نوعها إلى [ComboBoxActiveXControl](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol) وقراءة أو تعديل خصائصها المختلفة.

يرجىتنزيل[ملف الإكسل العيني](5115124.xlsx) المستخدمفيالكود العينيالتالي.
## **تحديث عنصر تحكم ActiveX ComboBox**
الصورة التي تلي تظهر تأثير كود العينة على [ملف الإكسل عينة](5115124.xlsx). كما يمكنك رؤية أن قيمة عنصر التحكم ComboBox في ActiveX تم تحديثها إلى "هذا عنصر التحكم في مربع القائمة"

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **الكود المثالي**
تحديث قيمة عنصر التحكم في مربع القائمة ActiveX داخل [ملف الإكسل عينة](5115124.xlsx).



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-UpdateActiveXComboBoxControl.py" >}}
