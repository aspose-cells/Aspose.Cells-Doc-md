---
title: استيراد بيانات من مستند
type: docs
weight: 20
url: /ar/net/import-data-from-document/
---

البيانات هي مجموعة من الحقائق الخام ونقوم بإنشاء مستند جداول بيانات أو تقارير لعرض هذه الحقائق الخام بطريقة أكثر معنى. عادةً ما نضيف البيانات إلى جداول بيانات بأنفسنا ولكن في بعض الأحيان، نحتاج إلى إعادة استخدام مصادر البيانات الموجودة وهنا يأتي دور استيراد البيانات إلى جداول البيانات من مصادر بيانات مختلفة. في هذا الموضوع، سنناقش بعض التقنيات لاستيراد البيانات إلى أوراق العمل من مصادر بيانات مختلفة.

**استيراد البيانات باستخدام Aspose.Cells** 
عند استخدام **Aspose.Cells** لفتح ملف Excel، يتم استيراد جميع البيانات في الملف تلقائيًا ولكن Aspose.Cells يدعم أيضًا استيراد البيانات من مصادر البيانات المختلفة. يُذكر بعض هذه المصادر أدناه:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells توفر فئة، **Workbook** التي تمثل ملف Excel. تحتوي فئة Workbook على مجموعة Worksheets تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة Worksheet. توفر فئة Worksheet مجموعة Cells.

توفر مجموعة Cells طرقًا مفيدة جدًا لاستيراد البيانات من مصادر بيانات مختلفة.

تحتوي هذه القسم على المواضيع التالية:

- [استيراد من مصفوفة](/cells/ar/net/importing-from-array/)
- [استيراد من ArrayList](/cells/ar/net/importing-from-arraylist/)
- [استيراد من الكائنات المخصصة](/cells/ar/net/importing-from-custom-objects/)
- [استيراد من DataTable](/cells/ar/net/importing-from-datatable/)
{{< app/cells/assistant language="csharp" >}}
