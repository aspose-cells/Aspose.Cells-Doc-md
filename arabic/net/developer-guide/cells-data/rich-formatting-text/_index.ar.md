---
title: الوصول وتحديث أجزاء النص الغني للخلية
linktitle: تنسيق النص الغني
type: docs
weight: 40
url: /ar/net/access-and-update-the-portions-of-rich-text-of-cell/
description: تعلم كيفية الوصول إلى وتحديث أجزاء النص الغني للخلية من خلال واجهة برمجة التطبيقات Aspose.Cells for .NET.
keywords: الوصول إلى وتحديث نص غني للخلية، الحصول على نص غني للخلية، تحرير نص غني للخلية، الوصول إلى نص غني للخلية، تحديث نص غني للخلية، تغيير نص غني للخلية
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بالوصول إلى وتحديث أجزاء النص الغني للخلية. لهذا الغرض، يمكنك استخدام [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) و [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) الأساليب. ستقوم هذه الأساليب بإرجاع وقبول مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting) التي يمكنك استخدامها للوصول وتحديث خصائص مختلفة للخط مثل اسم الخط، لون الخط، السمك، الخ،

{{% /alert %}}

## **الوصول إلى وتحديث أجزاء النص الغني للخلية**

الشيفرة التالية تُظهر استخدام [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) و [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) بتستخدام [ملف الإكسل المصدر](5112369.xlsx) الذي يمكنك تحميله من الرابط المُقدم. ملف الإكسل المصدر يَحتوي على نص غني في الخلية A1. يَحتوي على 3 أجزاء وكل جزء يَحتوي على خط مختلف. كُود الشيفرة التالي يصل إلى هذه الأجزاء ويُحدث الجزء الأول بخط جديد. أخيرًا، يُحفظ المصنف كـ [ملف إكسل الناتج](5112366.xlsx). عند فتحه، ستجد أن خط الجزء الأول من النص قد تغير إلى **"Arial"**.

### الشيفرة C# للوصول وتحديث أجزاء النص الغني للخلية

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

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

{{< app/cells/assistant language="csharp" >}}
