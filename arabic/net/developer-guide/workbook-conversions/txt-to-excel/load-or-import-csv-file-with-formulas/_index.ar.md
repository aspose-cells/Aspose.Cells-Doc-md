---
title: تحميل أو استيراد ملف CSV مع الصيغ
type: docs
weight: 350
url: /ar/net/load-or-import-csv-file-with-formulas/
---

{{% alert color="primary" %}} 

يحتوي ملف CSV بشكل عام على بيانات نصية ولا يحتوي على أي صيغ. ومع ذلك، في بعض الأحيان يحدث أن ملفات CSV تحتوي أيضًا على صيغ. يجب تحميل مثل هذه الملفات CSV عن طريق ضبط [TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) كـ **true**. بمجرد ضبط هذه الخاصية على **true**، فإن Aspose.Cells لن تعامل الصيغ كنص بسيط. سيتم التعامل معها على أنها صيغة وسيقوم محرك حساب صيغ Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}} 

يوضح الكود التالي كيف يمكنك تحميل واستيراد ملف CSV بالصيغ. يمكنك استخدام أي ملف CSV. لأغراض التوضيح، سنستخدم [ملف csv بسيط](5115034.csv) الذي يحتوي على هذه البيانات. كما ترون، يحتوي على صيغة.

{{< highlight java >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



يقوم الكود أولاً بتحميل ملف CSV، ثم استيراده مرة أخرى في الخلية D4. وأخيرًا، يقوم بحفظ كائن الورقة في تنسيق XSLX. [يبدو الملف XLSX الناتج](5115052.xlsx) مثل هذا. كما ترون، تحتوي الخلية C3 و F4 على صيغة ونتيجتها 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |

