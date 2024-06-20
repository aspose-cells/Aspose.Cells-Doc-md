---
title: الحصول على المدى مع الروابط الخارجية
type: docs
weight: 60
url: /ar/python-java/get-range-with-external-links/
---

## **الحصول على نطاق مع روابط خارجية**
هناك العديد من الحالات التي يتم فيها لكم ملفات الإكسيل الوصول إلى البيانات من ملفات إكسيل أخرى باستخدام الروابط الخارجية. يوفر Aspose.Cells for Python via Java الخيار لاسترداد هذه الروابط الخارجية باستخدام الطريقة [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)). تُرجع الطريقة [Name.GetReferredAreas](https://reference.aspose.com/cells/python/asposecells.api/name#getReferredAreas\(boolean\)) مصفوفة من النوع [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea). الفئة [ReferredArea](https://reference.aspose.com/cells/python/asposecells.api/ReferredArea) توفر خاصية [ExternalFileName](https://reference.aspose.com/cells/python/asposecells.api/referredarea#ExternalFileName) التي ترجع اسم الملف الخارجي.

يُظهر مقتطف الكود التالي كيفية الحصول على الروابط الخارجية.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-GetRangeWithExternalLinks.py" >}}
