---
title: تنشيط الأوراق وتنشيط خلية في ورقة العمل
type: docs
weight: 5
url: /ar/java/activating-sheets-and-activating-a-cell-in-worksheet/
---

{{% alert color="primary" %}}

أحيانًا، قد تحتاج إلى نشر ورقة عمل محددة وعرضها عندما يفتح المستخدم ملف Microsoft Excel في Excel. بالمثل، قد ترغب في تنشيط خلية معينة وضبط شريطي التمرير لعرض الخلية النشطة. يمكن لـ Aspose.Cells إجراء جميع هذه المهام كما هو موضح أدناه.

- الورقة النشطة هي الورقة التي تعمل عليها: يظهر اسم الورقة النشطة بالخط العريض افتراضيًا على علامة التبويب.
- **الخلية النشطة** هي الخلية المحددة، وهي الخلية التي يتم إدخال البيانات فيها عند بدء الكتابة. يتم تحديد خلية واحدة فقط في كل مرة. يتم تمييز الخلية النشطة بحدود سميكة.

{{% /alert %}}

## **تفعيل الأوراق وتفعيل خلية**

توفر Aspose.Cells استدعاءات API محددة لتفعيل ورقة وخلية. على سبيل المثال، تعتبر خاصية [**WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#ActiveSheetIndex) مفيدة لضبط الورقة النشطة في دفتر العمل. بالمثل، يمكن استخدام الخاصية [**Worksheet.ActiveCell**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ActiveCell) لضبط واسترجاع خلية نشطة في ورق العمل.

للتأكد من أن شريط التمرير الأفقي أو الرأسي عند الموضع الخاص بفهرس الصف والعمود الذي تريد عرض البيانات المحددة فيه، استخدم الخاصيتين [**Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleRow) و[**Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#FirstVisibleColumn).

يظهر المثال التالي كيفية تفعيل ورقة عمل وجعل خلية نشطة فيها. يتم إنشاء الإخراج التالي عند تنفيذ الكود. يتم تمرير شريطي التمرير لجعل الصف الثاني والعمود الثاني أول صف وعمود مرئيين لديهم.

**تعيين الخلية B2 كخلية نشطة**

![todo:image_alt_text](activating-sheets-and-activating-a-cell-in-worksheet_1.png)

## كود جافا لضبط ورقة عمل نشطة في إكسل

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ActivatingSheetsandActivatingCell-ActivatingSheetsandActivatingCell.java" >}}

{{% alert color="primary" %}}

في وضع **التقييم**، وهو؛ دون تعيين ترخيص صالح، ستكون الورقة النشطة دائمًا تحتوي على علامة العلامة التجريبية. يمكن تجاوز هذه السلوك بتعيين الترخيص في بداية التطبيق فقط.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
