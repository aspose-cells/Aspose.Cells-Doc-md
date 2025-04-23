---
title: الحصول على فهرس الخلايا
type: docs
weight: 600
url: /ar/nodejs-cpp/get-cells-index/
description: تعلم كيفية الحصول على صف أو عمود بواسطة اسم الصف، العمود أو الخلايا. تحويل اسم الخلية إلى فهرس صف وعمود بنظام العد القائم على الصفر.
keywords: الحصول على فهرس الصف والعمود بواسطة اسم الخلية، الحصول على فهرس العمود بواسطة اسم العمود، الحصول على فهرس الصف بواسطة اسم الصف، الحصول على الفهرس بواسطة اسم الخلية. 
---

{{% alert color="primary" %}}
العرض الافتراضي لإكسل هو إعادة النظر في نمط A1 المرجعي، حيث يتم تعريف كل عمود بأحرف A وB وC...، وتسمى الخلايا A1 وB2 وC3... وهكذا.
قد ترغب في معرفة الصف والعمود الذي يحتوي هذه الخلية فيه.

{{% /alert %}}


## **سيناريوهات الاستخدام المحتملة**
عندما تحتاج إلى تعديل بيانات معينة على ورقة العمل بواسطة مؤشر الصف والعمود فقط، تحتاج إلى معرفة مؤشر الصف والعمود لتلك الخلية المحددة. 
يقدم Aspose.Cells for Node.js via C++ هذه الميزة للحصول على فهرس الصف والعمود بناءً على اسم الصف، العمود، والخلية. 
تقدم Aspose.Cells for Node.js via C++ الخصائص والطرق التالية لمساعدتك على تحقيق أهدافك.
- [**CellsHelper.cellNameToIndex(string)**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#cellNameToIndex-string-)
- [**CellsHelper.columnIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnIndexToName-number-)
- [**CellsHelper.columnNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#columnNameToIndex-string-)
- [**CellsHelper.rowIndexToName**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowIndexToName-number-)
- [**CellsHelper.rowNameToIndex**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#rowNameToIndex-string-)

ملاحظة: الفهرسة تعتمد على الصفر في Aspose.Cells for Node.js via C++، لكن معرّف الصف هو واحدي في MS Excel.

## **الحصول على فهارس الخلايا باستخدام Aspose.Cells for Node.js via C++**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل وإضافة بعض البيانات.
1. العثور على الخلية المحددة في الورقة العمل الأولى.
1. الحصول على مؤشر الصف والعمود بواسطة اسم الخلية.
1. الحصول على مؤشر العمود بواسطة اسم العمود.
1. الحصول على مؤشر الصف بواسطة اسم الصف.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-get-index.js" >}}
