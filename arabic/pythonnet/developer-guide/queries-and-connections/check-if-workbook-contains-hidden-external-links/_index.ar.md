---
title: التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية
type: docs
weight: 230
url: /ar/python-net/check-if-workbook-contains-hidden-external-links/
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، يحتوي دفتر العمل على روابط خارجية مخفية ولا يمكن عرضها في Microsoft Excel. تسترجع Aspose.Cells لبايثون via .NET جميع الروابط الخارجية سواء كانت مرئية أو مخفية. ومع ذلك، يمكنك التحقق من الخاصية [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible) لمعرفة ما إذا كان الرابط الخارجي مرئيًا أم لا.

## **التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية**
الرمز التالي يحمّل ملف إكسل المصدر الذي يحتوي على روابط خارجية مخفية. لا يمكن عرض هذه الروابط في Microsoft Excel، لكنها موجودة داخل دفتر العمل. بعد طباعة الخاصية [ExternalLink.data_source](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/data_source) و[ExternalLink.is_referred](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_referred)، سيتم طباعة الخاصية [ExternalLink.is_visible](https://reference.aspose.com/cells/python-net/aspose.cells/externallink/is_visible). في المخرجات في وحدة التحكم أدناه، ترى أن جميع روابطه الخارجية غير مرئية.

### **الكود المثالي**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Connections-CheckHiddenExternalLinks.py" >}}

### **مخرجات الوحدة**
إليك مخرجات وحدة التحكم للكود العيني أعلاه عند تنفيذه مع [ملف Excel العيني المعطى](5115413.xlsx).



{{< highlight java >}}

 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}

