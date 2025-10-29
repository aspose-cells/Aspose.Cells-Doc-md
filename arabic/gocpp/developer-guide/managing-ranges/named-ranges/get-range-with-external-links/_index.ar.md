---
title: الحصول على النطاق مع الروابط الخارجية باستخدام جولانج عبر C++
linktitle: الحصول على المدى مع الروابط الخارجية
type: docs
weight: 120
url: /ar/go-cpp/get-range-with-external-links/
description: تعلم كيف تسترجع النطاقات مع روابط خارجية في ملفات إكسل باستخدام Aspose.Cells مع جولانج عبر C++
---

## **الحصول على نطاق مع روابط خارجية**

كثيرًا ما تصل ملفات Excel إلى البيانات من ملفات أخرى باستخدام روابط خارجية. توفر Aspose.Cells خيار استرداد هذه الروابط الخارجية باستخدام طريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/). ترجع طريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) مصفوفة من النوع [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/). يوفر فئة [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) خاصية [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) التي تعيد اسم الملف الخارجي. تكشف فئة [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) عن الأعضاء التالية.

- [**GetEndColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendcolumn/): عمود النهاية للمنطقة
- [**GetEndRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getendrow/): الصف النهائي للمنطقة
- [**GetExternalFileName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getexternalfilename/): الحصول على اسم الملف الخارجي إذا كان هذا مرجع خارجي
- [**IsArea**](https://reference.aspose.com/cells/go-cpp/referredarea/isarea/): يشير إلى ما إذا كان هذا منطقة
- [**IsExternalLink**](https://reference.aspose.com/cells/go-cpp/referredarea/isexternallink/): يشير إلى ما إذا كان هذا ارتباط خارجي
- [**GetSheetName()**](https://reference.aspose.com/cells/go-cpp/referredarea/getsheetname/): يشير إلى الورقة التي يقع فيها هذا المرجع
- [**GetStartColumn()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartcolumn/): العمود الابتدائي للمنطقة
- [**GetStartRow()**](https://reference.aspose.com/cells/go-cpp/referredarea/getstartrow/): صف البداية للمنطقة

يوضح رمز النموذج المقدم أدناه استخدام طريقة [**Name.GetReferredAreas**](https://reference.aspose.com/cells/go-cpp/name/getreferredareas/) للحصول على النطاقات ذات الروابط الخارجية.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetRangeWithExternalLinks.go" >}}
