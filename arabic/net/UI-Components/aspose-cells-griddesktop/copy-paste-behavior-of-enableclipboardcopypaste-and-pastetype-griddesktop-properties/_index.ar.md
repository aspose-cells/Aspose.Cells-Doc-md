---
title: سلوك النسخ واللصق لخصائص EnableClipboardCopyPaste وPasteType GridDesktop
type: docs
weight: 80
url: /ar/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **سيناريوهات الاستخدام المحتملة**
يوفر GridDesktop أنواعًا مختلفة من خيارات نوع النسخ واللصق باستخدام خاصية Aspose.Cells.GridDesktop.GridDesktop.PasteType. يتم تحديد هذه الخيارات باستخدام تعداد Aspose.Cells.GridDesktop.Data.GridPasteType. بعض هذه هي على النحو التالي

- GridPasteType.All

يقوم بنسخ ولصق كل شيء من الخلايا المصدر إلى الخلايا المستهدفة.

- GridPasteType.Formulas

يقوم بنسخ ولصق الصيغ من الخلايا المصدر إلى الخلايا المستهدفة.

- GridPasteType.Comments

يقوم بنسخ ولصق التعليقات من الخلايا المصدر إلى الخلايا المستهدفة.

- GridPasteType.RowHeights

يقوم بنسخ ولصق ارتفاعات الصفوف من الخلايا المصدر إلى الخلايا المستهدفة.

- GridPasteType.ColumnWidths

يقوم بنسخ ولصق عروض الأعمدة من الخلايا المصدر إلى الخلايا المستهدفة.

إلخ.
##  **قم بتعيين خاصية EnableClipboardCopyPaste إلى True لتمكين خاصية PasteType**
تعمل الخاصية Aspose.Cells.GridDesktop.GridDesktop.PasteType فقط إذا قمت بتعيين الخاصية Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste على أنها صحيحة كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **سلوك خصائص EnableClipboardCopyPaste وPasteType**
نظرًا لأن EnableClipboardCopyPaste هو خطأ وأن PasteType هو الكل، فإن لقطة الشاشة التالية توضح أنه عندما يتم نسخ الخلية B3 ولصقها في الخلية C5.

![ما يجب القيام به:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

نظرًا لأن EnableClipboardCopyPaste صحيح وأن PasteType هو الكل، فبعد نسخ الصورة من windows. توضح لقطة الشاشة التالية أنه عند نسخ الخلية B3 ولصقها في الخلية C5، فإنها تقوم أيضًا بنسخ الصورة إلى الخلية C5.

![ما يجب القيام به: هل نسخ الصورة](copyimage.png)

![ما يجب القيام به: بعد النسخ قم باللصق](aftercopy.png)


