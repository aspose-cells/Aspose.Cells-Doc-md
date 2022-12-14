---
title: تحميل أو استيراد ملف CSV مع الصيغ
type: docs
weight: 350
url: /ar/net/load-or-import-csv-file-with-formulas/
---
{{% alert color="primary" %}} 

 يحتوي ملف CSV في الغالب على بيانات نصية ولا يحتوي على أي صيغ. ومع ذلك ، يحدث أحيانًا أن تحتوي ملفات CSV أيضًا على صيغ. يجب تحميل ملفات CSV هذه عن طريق تعيين الامتداد[TxtLoadOptions.HasFormula](https://reference.aspose.com/cells/net/aspose.cells/txtloadoptions/properties/hasformula) كما**حقيقي** . بمجرد تعيين هذه الخاصية**حقيقي**، Aspose.Cells لن يتعامل مع الصيغة كنص بسيط. سيتم التعامل معها كصيغة وسيقوم محرك حساب الصيغة Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}} 

 يوضح الكود التالي كيف يمكنك تحميل واستيراد ملف CSV مع الصيغ. يمكنك استخدام أي ملف CSV. لغرض التوضيح ، نستخدم[ملف CSV بسيط](5115034.csv) الذي يحتوي على هذه البيانات. كما ترى يحتوي على صيغة.

{{< highlight "java" >}}

 300,500,=Sum(A1:B1)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportCSVWithFormulas-ImportCSVWithFormulas.cs" >}}



 يقوم الرمز أولاً بتحميل ملف CSV ، ثم استيراده مرة أخرى في الخلية D4. أخيرًا ، يحفظ كائن المصنف بتنسيق XSLX. ال[إخراج ملف XLSX](5115052.xlsx) يشبه هذا. كما ترى ، تحتوي الخلية C3 و F4 على صيغة ونتائجها 800.

|![ما يجب القيام به: image_بديل_نص](load-or-import-csv-file-with-formulas_1.png)|
|:- |

