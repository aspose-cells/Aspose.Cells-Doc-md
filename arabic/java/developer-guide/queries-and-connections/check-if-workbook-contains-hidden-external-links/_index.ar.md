---
title: التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية
type: docs
weight: 950
url: /ar/java/check-if-workbook-contains-hidden-external-links/
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، يحتوي الدفتر على روابط خارجية مخفية ولا يمكن عرضها في Microsoft Excel. يقوم Aspose.Cells بإسترجاع جميع الروابط الخارجية سواء كانت مرئية أم مخفية. ومع ذلك، يمكنك التحقق من خاصية [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible) للتحقق مما إذا كانت الرابط الخارجي مرئيًا أم لا
## **التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية**
يقوم الكود العيني التالي بتحميل [ملف الإكسل المصدر](5472525.xlsx) الذي يحتوي على روابط خارجية مخفية. لا يمكن عرض هذه الروابط في Microsoft Excel لكنها موجودة داخل الدفتر. بعد طباعة [ExternalLink.DataSource](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#DataSource) و [ExternalLink.IsReferred](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsReferred)، يتم طباعة [ExternalLink.IsVisible](https://reference.aspose.com/cells/java/com.aspose.cells/externallink#IsVisible). في مخرجات الوحدة أدناه، يمكنك أن ترى أن جميع الروابط الخارجية ليست مرئية.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckWorkbookContainsHiddenExternalLinks-CheckWorkbookContainsHiddenExternalLinks.java" >}}
## **مخرجات الوحدة**
هذه هي مخرجات الوحدة للكود العيني أعلاه عند تنفيذه مع [ملف الإكسل عينة](5472525.xlsx).



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
{{< app/cells/assistant language="java" >}}
