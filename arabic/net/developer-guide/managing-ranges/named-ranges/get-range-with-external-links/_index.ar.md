---
title: الحصول على المدى مع الروابط الخارجية
type: docs
weight: 120
url: /ar/net/get-range-with-external-links/
---

## **الحصول على نطاق مع روابط خارجية**

غالبًا ما تقوم ملفات Excel بالوصول إلى البيانات من ملفات Excel أخرى باستخدام روابط خارجية. توفر Aspose.Cells الخيار لاسترداد هذه الروابط الخارجية باستخدام الطريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas). تُرجع الطريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) مصفوفة من النوع [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea). توفر فئة [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) خاصية [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename) التي تُرجع اسم الملف الخارجي. تكشف الفئة [**ReferredArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea) عن الأعضاء التالية.

- [**EndColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endcolumn): العمود النهائي للمنطقة
- [**EndRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/endrow): الصف النهائي للمنطقة
- [**ExternalFileName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/externalfilename): احصل على اسم الملف الخارجي إذا كانت هذه مرجعًا خارجيًا
- [**IsArea**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isarea): يشير ما إذا كانت هذه منطقة
- [**IsExternalLink**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/isexternallink): يشير ما إذا كانت هذه رابطًا خارجيًا
- [**SheetName**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/sheetname): يشير إلى الورقة التي يكون فيها هذا المرجع
- [**StartColumn**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startcolumn): عمود بداية المنطقة
- [**StartRow**](https://reference.aspose.com/cells/net/aspose.cells/referredarea/properties/startrow): صف بداية المنطقة

الكود المثالي أدناه يبرز استخدام الطريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/net/aspose.cells/name/methods/getreferredareas) للحصول على النطاقات مع روابط خارجية.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-GetRangeWithExternalLinks-1.cs" >}}
