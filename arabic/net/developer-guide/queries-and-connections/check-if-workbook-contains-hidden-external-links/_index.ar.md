---
title: التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية
type: docs
weight: 230
url: /ar/net/check-if-workbook-contains-hidden-external-links/
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، تحتوي مصفوفة العمل على روابط خارجية مخفية ولا يمكن رؤيتها في Microsoft Excel. تسترجع Aspose.Cells جميع الروابط الخارجية سواء كانت مرئية أم مخفية. ومع ذلك، يمكنك التحقق من خاصية [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible) للتحقق مما إذا كان الرابط الخارجي مرئيًا أم لا.
## **التحقق مما إذا كانت مصفوفة العمل تحتوي على روابط خارجية مخفية**
يقوم الكود النموذجي التالي بتحميل [ملف Excel المصدر](5115413.xlsx) الذي يحتوي على روابط خارجية مخفية. لا يمكن بصرها في Microsoft Excel ولكنها موجودة داخل مصفوفة العمل. بعد طباعة [ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) و [ExternalLink.IsReferred](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred)، يطبع خاصية [ExternalLink.IsVisible](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible). في مخرجات وحدة التحكم أدناه، ترى، أن جميع روابطه الخارجية غير مرئية.
### **الكود المثالي**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
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
{{< app/cells/assistant language="csharp" >}}
