---
title: سلوك النسخ واللصق في EnableClipboardCopyPaste and PasteType GridDesktop Properties
type: docs
weight: 80
url: /ar/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
## **سيناريوهات الاستخدام الممكنة**
يوفر GridDesktop أنواعًا مختلفة من خيارات نوع لصق النسخ مع خاصية Aspose.Cells.GridDesktop.GridDesktop.PasteType. تم تحديد هذه الخيارات باستخدام تعداد Aspose.Cells.GridDesktop.Data.GridPasteType. بعض هذه على النحو التالي

- GridPasteType.All

يقوم بنسخ ولصق كل شيء من الخلايا المصدر إلى الخلايا المستهدفة.

- GridPasteType. الصيغ

يقوم بنسخ ولصق الصيغ من الخلايا المصدر إلى الخلايا المستهدفة.

- GridPasteType.Comments. تعليقات

يقوم بنسخ ولصق التعليقات من الخلايا المصدر إلى الخلايا المستهدفة.

- GridPasteType.RowHeights

يقوم بنسخ ولصق ارتفاعات الصفوف من الخلايا المصدر إلى الخلايا المستهدفة.

- GridPasteType.ColumnWidths

يقوم بنسخ ولصق عرض الأعمدة من الخلايا المصدر إلى الخلايا المستهدفة.

إلخ.
## **قم بتعيين خاصية EnableClipboardCopyPaste True لتمكين خاصية PasteType**
Aspose.Cells.GridDesktop.GridDesktop.PasteType تعمل الخاصية فقط إذا قمت بتعيين Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste صحيحة كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **سلوك EnableClipboardCopyPaste و PasteType الخصائص**
بالنظر إلى أن EnableClipboardCopyPaste خاطئ وأن PasteType هو الكل ، توضح لقطة الشاشة التالية أنه عند نسخ الخلية B3 ولصقها في الخلية C5 ، لا يتم نسخ تنسيق الخلية ويتم نسخ محتوى الخلية B3 فقط.

![ما يجب القيام به: image_بديل_نص](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_2.png)

بالنظر إلى أن EnableClipboardCopyPaste صحيح وأن PasteType هو All ، توضح لقطة الشاشة التالية أنه عند نسخ الخلية B3 ولصقها في الخلية C5 ، فإنها تنسخ أيضًا تنسيق الخلية B3 إلى الخلية C5.

![ما يجب القيام به: image_بديل_نص](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)


