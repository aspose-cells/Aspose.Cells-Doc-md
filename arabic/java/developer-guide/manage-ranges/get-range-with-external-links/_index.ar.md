---
title: الحصول على المدى مع الروابط الخارجية
type: docs
weight: 140
url: /ar/java/get-range-with-external-links/
---

## **الحصول على نطاق مع روابط خارجية**

غالبًا ما يقوم ملفات Excel بالوصول إلى بيانات من ملفات Excel أخرى باستخدام روابط خارجية. توفر Aspose.Cells الخيار لاسترداد هذه الروابط الخارجية باستخدام الطريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)). تقوم الطريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) بإرجاع مصفوفة من النوع [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea). توفر الفئة [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) خاصية [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName) التي ترجع اسم الملف الخارجي. تكشف الفئة [**ReferredArea**](https://reference.aspose.com/cells/java/com.aspose.cells/ReferredArea) التالية الأعضاء التالية.

- [**EndColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndColumn): العمود النهائي للمنطقة
- [**EndRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#EndRow): الصف النهائي للمنطقة
- [**ExternalFileName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#ExternalFileName): احصل على اسم الملف الخارجي إذا كانت هذه مرجعًا خارجيًا
- [**IsArea**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsArea): يشير ما إذا كانت هذه منطقة
- [**IsExternalLink**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#IsExternalLink): يشير ما إذا كانت هذه رابطًا خارجيًا
- [**SheetName**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#SheetName): يشير إلى الورقة التي يكون فيها هذا المرجع
- [**StartColumn**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartColumn): عمود بداية المنطقة
- [**StartRow**](https://reference.aspose.com/cells/java/com.aspose.cells/referredarea#StartRow): صف بداية المنطقة

يوضح الشفرة النموذجية التالية كيفية استخدام طريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/java/com.aspose.cells/name#getReferredAreas(boolean)) للحصول على نطاقات مع روابط خارجية.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-GetRangeWithExternalLinks-1.java" >}}
