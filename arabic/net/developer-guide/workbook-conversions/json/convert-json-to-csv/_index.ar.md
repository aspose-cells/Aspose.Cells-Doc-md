---
title: تحويل JSON إلى CSV
type: docs
weight: 210
url: /ar/net/convert-json-to-csv/
---
## **تحويل JSON إلى CSV**

يدعم Aspose.Cells تحويل JSON البسيط والمتداخل إلى CSV. لهذا ، يوفر API**[JsonLayoutOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)** و**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)** الطبقات. ال**[JsonLayoutOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**توفر فئة خيارات تنسيق JSON مثل**[IgnoreArrayTitle] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/ignorearraytitle)**(يتجاهل العنوان إذا كانت المصفوفة خاصية لكائن) أو**[ArrayAsTable] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions/properties/arrayastable)**(يعالج المصفوفة كجدول). ال**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**يقوم class بمعالجة JSON باستخدام خيارات التخطيط التي تم تعيينها باستخدام**[JsonLayoutOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**صف دراسي.

يوضح نموذج التعليمات البرمجية التالي استخدام**[JsonLayoutOptions] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonlayoutoptions)**و**[JsonUtility] (https://reference.aspose.com/cells/net/aspose.cells.utility/jsonutility)**فئات لتحميل[ملف JSON المصدر](104398869.json) ويولد ال[إخراج ملف CSV](104398870.csv).

### **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertJsonToCsv-1.cs" >}}
