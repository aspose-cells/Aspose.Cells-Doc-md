---
title: الوصول وتحديث أجزاء النص الغني للخلية
linktitle: تنسيق النص الغني
type: docs
weight: 40
url: /ar/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: تعلم كيفية الوصول وتحديث أجزاء النص الغني للخلية من خلال واجهة برمجة التطبيقات Aspose.Cells for Python via .NET.
keywords: مكتبة Python لـ Excel، الوصول والتحديث لنص الغني للخلية بلغة Python، الحصول على نص غني للخلية بلغة Python، تحرير نص غني للخلية بلغة Python، الوصول لنص غني للخلية بلغة Python، تحديث نص غني للخلية بلغة Python، تغيير نص غني للخلية بلغة Python.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET تتيح لك الوصول وتحديث أجزاء النص الغني للخلية. لهذا الغرض، يمكنك استخدام الطرق [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) و [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list). ستقوم هذه الطرق بإرجاع وقبول مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) التي يمكنك استخدامها للوصول وتحديث خصائص مختلفة من الخط مثل اسم الخط، لون الخط، السمك، إلخ.

{{% /alert %}}

## **الوصول إلى وتحديث أجزاء النص الغني للخلية**

الشيفرة التالية توضح استخدام الطرق [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) و [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) باستخدام [ملف Excel المصدر] (5112369.xlsx) الذي يمكنك تنزيله من الرابط المقدم. يحتوي ملف Excel المصدر على نص غني في الخلية A1. يحتوي على 3 أجزاء ولكل جزء خط مختلف. تقوم الشيفرة التالية بالوصول إلى هذه الأجزاء وتحديث الجزء الأول بخط جديد. أخيرًا، تقوم بحفظ دفتر العمل كـ [ملف Excel الناتج] (5112366.xlsx). عند فتحه، ستجد أن خط الجزء الأول من النص قد تغير إلى **"Arial"**.

### الشيفرة C# للوصول وتحديث أجزاء النص الغني للخلية

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي

 هنا يعرض الناتج على واجهة الطباعة لرمز العينة أعلاه باستخدام [ملف الإكسل المصدر](5112369.xlsx).

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

