---
title: الوصول وتعديل قيمة الخلية
type: docs
weight: 20
url: /ar/net/aspose-cells-griddesktop/accessing-and-modifying-the-value-of-a-cell/
keywords: GridDesktop,cell,modify cell,get cell,modify cell value,get cell value
description: يقدم هذا المقال كيفية الحصول على قيمة الخلية وتعديلها في GridDesktop.
---

{{% alert color="primary" %}} 

في موضوعنا السابق، تحدثنا حول الوصول إلى الخلايا في ورقة العمل. في هذا الموضوع، سنوسع ببساطة تلك الموضوع لنعرض للمطورين كيف يمكنهم الوصول وتعديل قيم الخلايا باستخدام واجهة برمجة التطبيقات (API) لـ Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **الوصول وتعديل قيمة الخلية باستخدام Aspose.Cells.GridDesktop**
قبل الوصول وتعديل قيمة الخلية، يجب أن نعرف كيفية الوصول إلى الخلايا. هناك ثلاثة طرق للوصول إلى الخلايا في ورقة العمل. لمزيد من التفاصيل حول هذه الطرق الثلاثة، يرجى [الوصول إلى الخلايا في ورقة العمل.](/cells/ar/net/accessing-cells-in-a-worksheet/)

لكل خلية خاصية تسمى القيمة. لذلك، بمجرد الوصول إلى الخلية، يمكن للمطورين الوصول وتعديل محتويات خاصية القيمة للوصول إلى قيمة الخلية وتغييرها.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**مهم:** استخدام خاصية القيمة للخلية لتعديل قيمتها هو نهج جيد لتعيين قيمة خلية واحدة أو قليلة. إذا كنت بحاجة إلى تعيين قيم العديد من الخلايا، فإن أداء هذا النهج لن يكون جيدًا. لذا، لتعيين قيم العديد من الخلايا، يجب عليك استخدام طريقة **SetCellValue** للخلية لتحسين أداء تطبيقاتك. تُظهر النسخة المعدلة من مقتطف الكود أعلاه باستخدام طريقة **SetCellValue** كمثال فيما يلي.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
