---
title: كيفية استخدام لوحة الألوان
type: docs
weight: 80
url: /ar/net/excel-color-palette/
description: كود C# لإضافة ألوان مخصصة إلى اللوحة واستخدام لوحة ألوان إكسل مع Aspose.Cells for .NET API
keywords: c# add custom colors to the palette, c# programmatically excel color palette, programmatically how to use color palette in workbook, c# how to use color palette in excel
---
##  **الألوان ولوحة**

اللوحة هي عدد الألوان المتاحة للاستخدام في إنشاء الصورة. يتيح استخدام لوحة موحدة في العرض التقديمي للمستخدم إنشاء مظهر متسق. يحتوي كل ملف Microsoft Excel (97-2003) على لوحة مكونة من 56 لونًا يمكن تطبيقها على الخلايا والخطوط وخطوط الشبكة والكائنات الرسومية والتعبئات والخطوط في المخطط.

مع Aspose.Cells، من الممكن ليس فقط استخدام الألوان الموجودة في اللوحة ولكن أيضًا الألوان المخصصة. قبل استخدام لون مخصص، قم بإضافته إلى اللوحة أولاً.

يناقش هذا الموضوع كيفية إضافة ألوان مخصصة إلى لوحة الألوان.

##  **أضف ألوانًا مخصصة إلى لوحة الألوان**

Aspose.Cells يدعم Microsoft لوحة ألوان Excel المكونة من 56 لونًا. لاستخدام لون مخصص غير محدد في لوحة الألوان، قم بإضافة اللون إلى لوحة الألوان.

 Aspose.Cells يوفر فئة،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) ، يمثل ملف Excel Microsoft. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يوفر الفصل أ[**تغيير لوحة**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/changepalette) الطريقة التي تأخذ المعلمات التالية لإضافة لون مخصص لتعديل اللوحة:

- اللون المخصص، اللون المخصص المراد إضافته.
- الفهرس، فهرس اللون الموجود في اللوحة الذي سيحل محله اللون المخصص. ينبغي أن يكون بين 0-55.

يضيف المثال أدناه لونًا مخصصًا (Orchid) إلى لوحة الألوان قبل تطبيقه على الخط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ColorsAndPalette-1.cs" >}}

{{% alert color="primary" %}}

تحتوي اللوحة على 56 لونًا فقط. عند إضافة لون مخصص إلى لوحة الألوان، يتم تغيير اللوحة وتغيير أي عنصر في الملف المنسق باللون السابق. لذا، عند تغيير لوحة الألوان، يرجى توخي الحذر الشديد. علاوة على ذلك، هذا هو القيد في تنسيق الملف XLS (Excel 97 - 2003) فقط حيث لا يوجد مثل هذا القيد على XLSX أو تنسيقات ملفات MS Excel المتقدمة الأخرى (2007/2010 أو 2013).

{{% /alert %}}