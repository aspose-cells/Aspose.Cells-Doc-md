---
title: الوصول وتحديث أجزاء النص الغني للخلية
linktitle: تنسيق النص الغني
type: docs
weight: 40
url: /ar/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: تعرف على كيفية الوصول إلى وتحديث أجزاء النص الغني للخلية من خلال واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: الوصول إلى وتحديث نص غني للخلية، الحصول على نص غني للخلية، تحرير نص غني للخلية، الوصول إلى نص غني للخلية، تحديث نص غني للخلية، تغيير نص غني للخلية
---

{{% alert color="primary" %}}

 يسمح لك Aspose.Cells for Node.js via C++ بالوصول إلى وتحديث أجزاء النص الغني للخلية. لهذا الغرض، يمكنك استخدام طرق [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) و [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). سترجع هذه الطرق وتقبل مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) والتي يمكنك استخدامها للوصول وتحديث خصائص الخط مثل اسم الخط، لون الخط، عريض، إلخ.

{{% /alert %}}

## **الوصول إلى وتحديث أجزاء النص الغني للخلية**

يوضح الكود التالي كيفية استخدام طرق [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) و [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) باستخدام ملف اكسل المصدر [ملف إكسل المصدر](5112369.xlsx) والذي يمكنك تنزيله من الرابط المقدم. يحتوي ملف إكسل المصدر على نص غني في الخلية A1. لديه 3 أجزاء وكل جزء يحتوي على خط مختلف. يتصل الكود التالي بهذه الأجزاء ويقوم بتحديث الجزء الأول باسم خط جديد. وأخيرًا، يحفظ المصنف باسم [ملف إكسل المخرجات](5112366.xlsx). عند فتحه، ستجد أن خط الجزء الأول من النص قد تغير إلى **"Arial"**.

### كود Nodejs للوصول وتحديث أجزاء النص الغني للخلية

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

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

{{< app/cells/assistant language="nodejs-cpp" >}}
