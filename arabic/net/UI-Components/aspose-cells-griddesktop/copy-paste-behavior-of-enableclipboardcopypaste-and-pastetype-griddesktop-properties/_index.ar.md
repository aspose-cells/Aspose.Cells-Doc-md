---
title: سلوك نسخ ولصق من خصائص GridDesktop EnableClipboardCopyPaste و PasteType
type: docs
weight: 80
url: /ar/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: نسخ، لصق، GridPasteType
description: يقوم هذا المقال بشرح كيفية استخدام GridPasteType للقيام بعملية نسخ لصق في GridDesktop.
---

## **سيناريوهات الاستخدام المحتملة**
يوفر GridDesktop أنواعًا مختلفة من خيارات نوع النسخ واللصق مع خاصية Aspose.Cells.GridDesktop.GridDesktop.PasteType. تُحدد بعض هذه بتعداد Aspose.Cells.GridDesktop.Data.GridPasteType. بعض هذه الخيارات هي كما يلي

- GridPasteType.All

ينسخ وي لصق كل شيء من الخلايا المصدر إلى الخلايا الهدف.

- GridPasteType.Formulas

ينسخ وي لصق الصيغ من الخلايا المصدر إلى الخلايا الهدف.

- GridPasteType.Comments

ينسخ ويلصق التعليقات من الخلايا المصدر إلى الخلايا الهدف.

- GridPasteType.RowHeights

ينسخ وي لصق ارتفاعات الصفوف من الخلايا المصدر إلى الخلايا الهدف.

- GridPasteType.ColumnWidths

ينسخ وي لصق أعراض الأعمدة من الخلايا المصدر إلى الخلايا الهدف.

إلخ.
## **قم بتعيين خاصية EnableClipboardCopyPaste إلى True لتمكين خاصية PasteType**
يعمل خاصية PasteType لـ Aspose.Cells.GridDesktop.GridDesktop فقط إذا قمت بتعيين خاصية Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste إلى true كما هو موضح في هذا اللقطة الشاشة.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **سلوك خصائص EnableClipboardCopyPaste وPasteType**
بناءً على أن EnableClipboardCopyPaste هو خاصية كاذبة و PasteType هو All، يظهر اللقطة الشاشية التالية عندما يتم نسخ الخلية B3 ولصقها في الخلية C5.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

بناءً على أن EnableClipboardCopyPaste هو صحيح و PasteType هو All، بعد نسخ صورة من نظام التشغيل ويندوز، تظهر اللقطة الشاشية التالية عند نسخ الخلية B3 ولصقها في الخلية C5، حيث تنسخ الصورة أيضًا إلى الخلية C5.

![لمرة أخرى: نسخ الصورة](copyimage.png)

![لمرة أخرى: بعد النسخ قم باللصق](aftercopy.png)


