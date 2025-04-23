---
title: تحميل أو استيراد ملف CSV مع الصيغ
type: docs
weight: 500
url: /ar/java/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

يحتوي ملف CSV بشكل عام على بيانات نصية ولا يحتوي على أي معادلات. ومع ذلك، في بعض الأحيان يحدث أن ملفات CSV تحتوي أيضًا على معادلات. يجب تحميل مثل تلك الملفات CSV عن طريق ضبط [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) إلى **true**. عندما يتم تعيين هذه الخاصية إلى **true**، فإن Aspose.Cells لن تعامل المعادلة على أنها نص بسيط. سيتم معاملتهم كمعادلة وسيقوم محرك حساب معادلات Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}} 
## **تحميل أو استيراد ملف CSV بالصيغ**
الكود التالي يوضح كيفية تحميل واستيراد ملف CSV مع الصيغ. يمكنك استخدام أي ملف CSV. لأغراض التوضيح، نستخدم [ملف CSV بسيط](5472505.csv) الذي يحتوي على هذه البيانات. كما ترى أنه يحتوي على صيغة.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

يقوم الكود أولاً بتحميل ملف CSV، ثم يقوم بإستيراده مرة أخرى في الخانة D4. وأخيراً، يحفظ كائن المصنف في تنسيق XSLX. [ملف XLSX الناتج](5472503.xlsx) يبدو مثل هذا. كما ترى أن الخانة C3 و F4 تحتوي على صيغة ونتيجتها 800.

![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
{{< app/cells/assistant language="java" >}}
