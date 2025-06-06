---
title: كيفية إدراج صورة في الخلية باستخدام C++
linktitle: كيفية إدراج صورة في الخلية
type: docs
weight: 130
url: /ar/cpp/how-to-insert-picture-in-cell/
description: تعلم كيفية إدراج صورة في خلية باستخدام Aspose.Cells باستخدام C++.
keywords: كيفية إدراج صورة في الخلية، إدراج الصورة فوق الخلايا، وضع الصورة في الخلية، وضع الصورة فوق الخلايا، كيفية وضع الصورة في الخلية، كيفية وضع الصورة فوق الخلايا، التبديل بين الصورة في الخلية والصورة فوق الخلايا، التبديل بين الوضع في الخلية والوضع فوق الخلايا.
---

## **سيناريوهات الاستخدام المحتملة**
تضيف الصورة لمسة من الإشراق إلى ورقة العمل الخاصة بك وتوفر تمثيلاً بصريًا للمحتوى. كما أنها تسهل عليك فهم البيانات والتوصل إلى رؤى. على الرغم من أنك كنت قادرًا على استخدام الصور في Excel لسنوات عديدة، إلا أن ميزة جعل الصور قيم خلايا فعلية لم تُتاح إلا مؤخرًا. حتى إذا تم تعديل تنسيق الرسمة، فستظل ملحقة بالبيانات. يمكنك استخدامها في الجداول، والفرز، والتصفية، وتضمينها في الصيغ، وغيرها!

## **كيفية إدراج الصورة في خلية باستخدام Excel**
حول كيفية إدراج صورة في خلية في Excel، اتبع هذه الخطوات:

1. انتقل إلى علامة التبويب الإدراج وانقر على خيار الصور.
2. حدد **وضع في الخلية**. حدد أحد المصادر التالية من القائمة المنسدلة إدراج صورة من(**هذا الجهاز**، **صور الأسهم** و **صور عبر الإنترنت**). هذا الجهاز لإدراج الصورة من جهازك. صور الأسهم لإدراج صورة من صور الأسهم. صور عبر الإنترنت لإدراج صورة من الويب.
<br>
<img src="1.png" width=60% />
3. حدد الصورة وأدرجها في خلية.
<br>
<img src="8.png" width=60% />

## **كيفية إدراج الصورة فوق الخلايا باستخدام Excel**
حول كيفية إدراج صورة فوق الخلايا في Excel، اتبع هذه الخطوات:

1. انتقل إلى علامة التبويب الإدراج وانقر على خيار الصور.
2. حدد **وضع فوق الخلايا**. حدد أحد المصادر التالية من القائمة المنسدلة إدراج صورة من(**هذا الجهاز**، **صور الأسهم** و **صور عبر الإنترنت**). هذا الجهاز لإدراج الصورة من جهازك. صور الأسهم لإدراج صورة من صور الأسهم. صور عبر الإنترنت لإدراج صورة من الويب.
<br>
<img src="2.png" width=60% />
3. حدد الصورة وأدرجها فوق الخلايا.
<br>
<img src="3.png" width=60% />

## **كيفية التبديل من الصورة في الخلية إلى الصورة فوق الخلايا باستخدام Excel**
يمكنك بسهولة التبديل من **الصورة في الخلية** إلى **الصورة فوق الخلايا**. يرجى اتباع هذه الخطوات:
1. انقر بزر الماوس الأيمن على الخلية وحدد **الصورة في الخلية** > **وضع فوق الخلايا**. 
<br>
<img src="4.png" width=60% />
2. النتيجة بعد التبديل كما يلي:
<br>
<img src="5.png" width=60% />

## **كيفية التبديل من الصورة فوق الخلايا إلى الصورة في الخلية باستخدام Excel**
يمكنك بسهولة التبديل من **الصورة فوق الخلايا** إلى **الصورة في الخلية**. يرجى اتباع هذه الخطوات:
1. انقر بزر الماوس الأيمن على الصورة وحدد **وضع في الخلية**. 
<br>
<img src="6.png" width=60% />
2. النتيجة بعد التبديل كما يلي:
<br>
<img src="7.png" width=60% />

## **كيفية إدراج صورة في خلية باستخدام C++**
إدراج صورة في الخلية باستخدام Aspose.Cells. يرجى الاطلاع على الكود المثالي التالي. بعد تنفيذ كود العينة، سيتم إدراج صورة في خلية.
1. استدعِ كائن دفتر العمل. 
2. احصل على الخلية التي ترغب في إدراج الصورة فيها.
3. ضبط خاصية الصورة المضمنة في الخلية. 
4. أخيرًا، يحفظ الدفتر بتنسيق [XLSX الناتج](out.xlsx). 

## **الكود المثالي**

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get cell D8
    Cell d8 = worksheet.GetCells().Get(u"D8");

    // Read image file into byte vector
    std::ifstream file("aspose.png", std::ios::binary);
    std::vector<uint8_t> imageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    // Convert to Aspose's Vector and set embedded image in cell D8
    d8.SetEmbeddedImage(Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
