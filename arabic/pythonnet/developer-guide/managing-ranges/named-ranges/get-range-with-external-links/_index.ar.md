---
title: الحصول على المدى مع الروابط الخارجية
type: docs
weight: 120
url: /ar/python-net/get-range-with-external-links/
description: يوضح هذا المقال كيفية الحصول على النطاقات مع الروابط الخارجية باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Excel باللغة Python، الحصول على النطاقات مع الروابط الخارجية في Python.
---

## **الحصول على نطاق مع روابط خارجية**

غالبًا ما تقوم ملفات Excel بالوصول إلى البيانات من ملفات Excel أخرى باستخدام روابط خارجية. توفر Aspose.Cells for Python via .NET الخيار لاسترجاع هذه الروابط الخارجية باستخدام الطريقة [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool). تُرجع الطريقة [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) مصفوفة من النوع [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea). يوفر الفئة [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) خاصية [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/) التي تُرجع اسم الملف الخارجي. تكشف الفئة [**ReferredArea**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea) عن الأعضاء التالية.

- [**end_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_column/): العمود النهائي للمنطقة
- [**end_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/end_row/): الصف النهائي للمنطقة
- [**external_file_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/external_file_name/): احصل على اسم الملف الخارجي إذا كانت هذه مرجعًا خارجيًا
- [**is_area**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_area/): يشير ما إذا كانت هذه منطقة
- [**is_external_link**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/is_external_link/): يشير ما إذا كانت هذه رابطًا خارجيًا
- [**sheet_name**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/sheet_name/): يشير إلى الورقة التي يكون فيها هذا المرجع
- [**start_column**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_column): عمود بداية المنطقة
- [**start_row**](https://reference.aspose.com/cells/python-net/aspose.cells/referredarea/start_row): صف بداية المنطقة

الكود المثالي أدناه يبرز استخدام الطريقة [**Name.get_referred_areas**](https://reference.aspose.com/cells/python-net/aspose.cells/name/get_referred_areas/#bool) للحصول على النطاقات مع روابط خارجية.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-Worksheets-GetRangeWithExternalLinks-1.py" >}}
