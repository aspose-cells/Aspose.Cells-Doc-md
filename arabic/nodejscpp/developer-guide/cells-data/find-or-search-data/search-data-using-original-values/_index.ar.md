---  
title: البحث عن البيانات باستخدام القيم الأصلية
type: docs  
weight: 380  
url: /ar/nodejs-cpp/search-data-using-original-values/  
description: تعلم كيفية البحث عن البيانات باستخدام القيم الأصلية عبر واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.  
keywords: البحث عن البيانات باستخدام القيم الأصلية Node.js عبر C++، العثور على البيانات باستخدام القيم الأصلية Node.js عبر C++، البحث عن البيانات بواسطة القيم الأصلية Node.js عبر C++، العثور على البيانات بواسطة القيم الأصلية Node.js عبر C++.  
---  

{{% alert color="primary" %}}  

أحيانًا يكون قيمة البيانات مخفية لأنها مهيأة بطريقة ما. على سبيل المثال، لنفترض أن الخلية D4 لديها صيغة =Sum(A1:A2) وقيمتها 20 ولكنها مهيأة كما ---، عندها تكون القيمة 20 مخفية ولا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel. ومع ذلك، يمكنك العثور عليها باستخدام Aspose.Cells باستخدام [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype).  

{{% /alert %}}  

الشيفرة العينية التالية توضح النقطة السابقة. إنها تجد الخلية D4 التي لا يمكن العثور عليها باستخدام خيارات البحث في Microsoft Excel ولكن يمكن لـ Aspose.Cells العثور عليها باستخدام [**LookInType.OriginalValues**](https://reference.aspose.com/cells/nodejs-cpp/lookintype). يرجى قراءة التعليقات داخل الشيفرة لمزيد من المعلومات.  

## كود Node.js للبحث عن البيانات باستخدام القيم الأصلية  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SearchData-SearchDataUsingOriginalValues.js" >}}


## الناتج على واجهة الأوامر الناتجة عن الكود المثال  

فيما يلي مخرجات وحدة الإدخال الخاصة بالكود المصدري أعلاه.  

{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}  

