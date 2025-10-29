---
title: الوصول وتحديث أجزاء النص الغني للخلية مع Golang عبر C++
linktitle: تنسيق النص الغني
type: docs
weight: 40
url: /ar/go-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: تعلم كيفية الوصول إلى وتحديث أجزاء النص الغني للخلية من خلال API Aspose.Cells for C++.
keywords: الوصول إلى وتحديث نص غني للخلية، الحصول على نص غني للخلية، تحرير نص غني للخلية، الوصول إلى نص غني للخلية، تحديث نص غني للخلية، تغيير نص غني للخلية
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بالوصول إلى وتحديث أجزاء النص الغني للخلية. لهذا الغرض، يمكنك استخدام [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) و [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) الأساليب. ستقوم هذه الأساليب بإرجاع وقبول مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) التي يمكنك استخدامها للوصول وتحديث خصائص مختلفة للخط مثل اسم الخط، لون الخط، السمك، الخ،

{{% /alert %}}

## **الوصول إلى وتحديث أجزاء النص الغني للخلية**

توضح الشفرة التالية استخدام طرق [**Cell->GetCharacters()**](https://reference.aspose.com/cells/go-cpp/cell/getcharacters/) و [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) باستخدام ملف إكسل المصدر ([ملف إكسل](5112369.xlsx)). يحتوي ملف إكسل المصدر على نص غني في الخلية A1 بثلاث أجزاء، كل جزء بتنسيق مختلف. تصل هذه الأجزاء وتحدث خط التنسيق الخاص بالجزء الأول إلى **"Arial"**. يتم حفظ المصنف المعدل كملف إكسل الناتج ([ملف إكسل المخرجات](5112366.xlsx)).

### كود ++C للوصول إلى أجزاء النص الغني وتحديثها

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RichFormattingText.go" >}}
### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي

إليك إخراج وحدة التحكم عند استخدام [ملف إكسل المصدر](5112369.xlsx):

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
