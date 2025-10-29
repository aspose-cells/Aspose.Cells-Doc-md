---
title: تحميل أو استيراد ملف CSV مع صيغ باستخدام C++
linktitle: تحميل أو استيراد ملف CSV مع الصيغ
type: docs
weight: 350
url: /ar/go-cpp/load-or-import-csv-file-with-formulas/
description: تحميل أو استيراد ملف CSV يحتوي على صيغ باستخدام Aspose.Cells مع Golang عبر C++.
---

{{% alert color="primary" %}} 

عادةً تحتوي ملفات CSV على بيانات نصية ولا تتضمن عادةً أي صيغ. ومع ذلك، هناك حالات قد تحتوي فيها ملفات CSV على صيغ. يجب تحميل مثل هذه الملفات عن طريق تعيين [TxtLoadOptions.GetHasFormula()](https://reference.aspose.com/cells/go-cpp/txtloadoptions/gethasformula/) إلى **true**. بمجرد تعيين هذه الخاصية إلى **true**، لن يتعامل Aspose.Cells مع الصيغ كنص بسيط. ستعامل كصيغ، وسيقوم محرك حساب الصيغ في Aspose.Cells بمعالجتها كالمعتاد.

{{% /alert %}} 

يوضح الكود التالي كيف يمكنك تحميل واستيراد ملف CSV بصيغ. يمكنك استخدام أي ملف CSV. للأغراض التوضيحية، نستخدم ملف CSV بسيط يحتوي على هذه البيانات. كما ترى، فإنه يحتوي على صيغة.

{{< highlight cpp >}}
 300,500,=Sum(A1:B1)
{{< /highlight >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LoadOrImportCsvFileWithFormulas.go" >}}
يتم أولاً تحميل ملف CSV، ثم استيراده مرة أخرى في الخلية D4. وأخيراً، يتم حفظ مصنف العمل بصيغة XLSX. يبدو ملف XLSX الناتج هكذا. كما ترى، الخلية C3 و F4 تحتويان على صيغ ونتيجتهما 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|
| :- |
