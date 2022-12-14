---
title: تحقق مما إذا كان المصنف يحتوي على روابط خارجية مخفية
type: docs
weight: 230
url: /ar/net/check-if-workbook-contains-hidden-external-links/
---
## **سيناريوهات الاستخدام الممكنة**
في بعض الأحيان ، يحتوي المصنف على روابط خارجية مخفية ولا يمكن عرضها في Microsoft Excel. Aspose.Cells يقوم باسترجاع كل الوصلات الخارجية سواء كانت مرئية أو مخفية. ومع ذلك ، يمكنك التحقق من[ExternalLink.Is مرئي](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)للتحقق مما إذا كان الرابط الخارجي مرئيًا أم لا
## **تحقق مما إذا كان المصنف يحتوي على روابط خارجية مخفية**
 يقوم نموذج التعليمات البرمجية التالي بتحميل ملف[ملف اكسل المصدر](5115413.xlsx) الذي يحتوي على روابط خارجية مخفية. لا يمكن عرض هذه الارتباطات في Microsoft Excel ولكنها موجودة داخل المصنف. بعد الطباعة[ExternalLink.DataSource](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/datasource) و[رابط خارجي](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isreferred) الملكية ، فإنه يطبع ملف[ExternalLink.Is مرئي](https://reference.aspose.com/cells/net/aspose.cells/externallink/properties/isvisible)منشأه. في إخراج وحدة التحكم أدناه ، كما ترى ، جميع الروابط الخارجية غير مرئية.
### **عينة من الرموز**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CheckHiddenExternalLinks-CheckHiddenExternalLinks.cs" >}}
### **إخراج وحدة التحكم**
 هنا هو إخراج وحدة التحكم من نموذج التعليمات البرمجية أعلاه عند تنفيذه مع المعطى[نموذج ملف اكسل](5115413.xlsx).



{{< highlight "java" >}}

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
