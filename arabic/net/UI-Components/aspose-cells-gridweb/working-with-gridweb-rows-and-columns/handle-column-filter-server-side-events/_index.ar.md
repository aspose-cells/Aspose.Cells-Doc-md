---
title: التعامل مع أحداث تصفية الأعمدة على الخادم
type: docs
weight: 90
url: /ar/net/aspose-cells-gridweb/handle-column-filter-server-side-events/
keywords: GridWeb,filter,OnBeforeColumnFilter,OnAfterColumnFilter
description: يقدم هذا المقال كيفية التعامل مع حدث تصفية الأعمدة في GridWeb.
---

{{% alert color="primary" %}} 

تصفية البيانات ربما تكون الوظيفة الأكثر استخدامًا في إكسل التي تتيح لك تصفية البيانات بناءً على معيار محدد. تعرض البيانات المصفاة فقط الصفوف التي تلبي الشرط عن طريق إخفاء الصفوف التي لا تفي بالمعايير.
يوفر GridWeb في Aspose.Cells.GridWeb القدرة على تنفيذ تصفية البيانات باستخدام واجهته. وبغرض توسيع قدراته، يوفر GridWeb في Aspose.Cells.GridWeb أيضاً حدثين يمكن أن يكونا كمرشدين لآلية التصفية المنجزة من خلال واجهة GridWeb.

{{% /alert %}} 
## **التعامل مع حدث جانب الخادم عند تطبيق تصفية الأعمدة**
هناك حدثين رئيسيين كما هو مفصل أدناه.

1. OnBeforeColumnFilter: يتم تشغيله قبل تطبيق التصفية على العمود.
1. OnAfterColumnFilter: يتم تشغيله بعد تطبيق التصفية على العمود.

إليك سيناريو ASPX من مكون Aspose.Cells.GridWeb لإضافة وتعيين الأحداث المذكورة سابقًا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents-HandleColumnFilterEvents.aspx" >}}



يمكن استخدام هذه الأحداث للحصول على معلومات مفيدة حول عملية التصفية مثل فهرس العمود والقيمة التي يجب تطبيق التصفية عليها. وفيما يلي مقتطف يوضح استخدام حدث OnBeforeColumnFilter لاسترداد فهرس العمود والقيمة التي اختارها المستخدم على واجهة GridWeb للتصفية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-BeforeColumnFilter.cs" >}}


من جهة أخرى، إذا كانت المتطلبات تتطلب الحصول على عدد الصفوف المصفاة بعد تطبيق التصفية، فيمكنك استخدام حدث OnAfterColumnFilter كما هو موضح أدناه.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-RowsAndColumns-HandleColumnFilterEvents.aspx-AfterColumnFilter.cs" >}}

{{% alert color="primary" %}} 

تحقق من مقدمة لجميع [العمل مع أحداث GridWeb](/cells/ar/net/aspose-cells-gridweb/working-with-gridweb-events/) جنبًا إلى جانب بعض التفاصيل حول كيفية التعامل مع هذه الأحداث.

{{% /alert %}}
