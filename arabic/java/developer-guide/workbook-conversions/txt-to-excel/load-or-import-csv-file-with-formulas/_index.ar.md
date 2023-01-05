---
title: قم بتحميل أو استيراد ملف CSV باستخدام الصيغ
type: docs
weight: 500
url: /ar/java/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 يحتوي ملف CSV في الغالب على بيانات نصية ولا يحتوي على أي صيغ. ومع ذلك ، يحدث أحيانًا أن تحتوي ملفات CSV أيضًا على صيغ. يجب تحميل هذه الملفات CSV عن طريق تحديد الامتداد[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/java/com.aspose.cells/txtloadoptions#HasFormula) إلى**حقيقي** . بمجرد تعيين هذه الخاصية إلى**حقيقي**، Aspose.Cells لن يتعامل مع الصيغة كنص بسيط. سيتم التعامل معها كصيغة وسيقوم محرك حساب الصيغة Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}} 
## **قم بتحميل أو استيراد ملف CSV باستخدام الصيغ**
 يوضح الكود التالي كيف يمكنك تحميل واستيراد ملف CSV مع الصيغ. يمكنك استخدام أي ملف CSV. لغرض التوضيح ، نستخدم[ملف CSV بسيط](5472505.csv) الذي يحتوي على هذه البيانات. كما ترى يحتوي على صيغة.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

يقوم الرمز أولاً بتحميل الملف CSV ، ثم استيراده مرة أخرى في الخلية D4. أخيرًا ، يحفظ كائن المصنف بتنسيق XSLX. ال[ملف الإخراج XLSX](5472503.xlsx) يشبه هذا. كما ترى ، تحتوي الخلية C3 و F4 على صيغة ونتائجها 800.

![ما يجب القيام به: image_بديل_نص](load-or-import-csv-file-with-formulas_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadOrImportCSVFile-LoadOrImportCSVFile.java" >}}
