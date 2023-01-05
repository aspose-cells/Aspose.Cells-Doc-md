---
title: احصل على النطاق مع الروابط الخارجية
type: docs
weight: 140
url: /ar/java/get-range-with-external-links/
---
## **احصل على النطاق مع الروابط الخارجية**

في كثير من الأحيان ، تصل ملفات Excel إلى البيانات من ملفات Excel الأخرى باستخدام روابط خارجية. Aspose.Cells يوفر خيار استرجاع هذه الوصلات الخارجية باستخدام[**الاسم**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) طريقة. ال[**الاسم**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) تقوم بإرجاع مصفوفة من النوع[**إحالة**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). ال[**إحالة**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)فئة توفر[**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName)الخاصية التي تُرجع اسم الملف الخارجي. ال[**إحالة**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea)فئة يكشف الأعضاء التالية.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): عمود نهاية المنطقة
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): صف نهاية المنطقة
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): احصل على اسم الملف الخارجي إذا كان هذا مرجعًا خارجيًا
- [**جزيرة**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): يشير إلى ما إذا كانت هذه منطقة
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): يشير إلى ما إذا كان هذا ارتباطًا خارجيًا
- [**اسم الورقة**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): يشير إلى الورقة التي يوجد بها هذا المرجع
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): عمود البداية للمنطقة
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): صف البداية للمنطقة

يوضح نموذج التعليمات البرمجية الوارد أدناه استخدام[**الاسم**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) طريقة الحصول على النطاقات ذات الروابط الخارجية.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
