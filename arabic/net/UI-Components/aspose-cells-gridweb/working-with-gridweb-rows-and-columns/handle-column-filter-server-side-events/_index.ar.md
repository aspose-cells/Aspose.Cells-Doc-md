---
title: التعامل مع الأحداث الجانبية لخادم عامل تصفية العمود
type: docs
weight: 90
url: /ar/net/handle-column-filter-server-side-events/
---
{{% alert color="primary" %}} 

من المحتمل أن تكون تصفية البيانات هي أكثر ميزات Excel استخدامًا والتي تسمح لك بتصفية البيانات بناءً على معايير محددة. تعرض البيانات التي تمت تصفيتها الصفوف التي تفي بالشرط فقط عن طريق إخفاء الصفوف التي لا تفي بالمعايير.
Aspose.Cells. يوفر مكونGridWeb القدرة على إجراء تصفية البيانات باستخدام واجهته. من أجل توسيع قدراته ، يوفر المكون Aspose.Cells.GridWeb أيضًا حدثين يمكن أن يكونا بمثابة رد اتصال لآلية التصفية التي تتم من خلال GridWeb UI.

{{% /alert %}} 
## **معالجة حدث جانب الخادم عند تطبيق عامل تصفية العمود**
هناك حدثان رئيسيان على النحو المفصل أدناه.

1. OnBeforeColumnFilter: حرائق قبل تطبيق المرشح على عمود.
1. OnAfterColumnFilter: الحرائق بعد تطبيق المرشح على عمود.

فيما يلي نص ASPX الخاص بمكون Aspose.Cells.GridWeb لإضافة الأحداث المذكورة أعلاه وتعيينها.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



يمكن استخدام هذه الأحداث للحصول على معلومات مفيدة حول عملية التصفية مثل فهرس العمود والقيمة التي يجب تطبيق عامل التصفية عليها. فيما يلي المقتطف الذي يوضح استخدام حدث OnBeforeColumnFilter لاسترداد فهرس العمود والقيمة التي حددها المستخدم في GridWeb UI للتصفية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


من ناحية أخرى ، إذا كان المتطلب هو الحصول على عدد الصفوف التي تمت تصفيتها بعد تطبيق الفلتر ، فيمكنك استخدام حدث OnAfterColumnFilter كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

 تحقق من المقدمة للجميع[العمل مع أحداث GridWeb](/cells/ar/net/working-with-gridweb-events/) بالإضافة إلى بعض التفاصيل حول كيفية التعامل مع هذا الحدث.

{{% /alert %}}
