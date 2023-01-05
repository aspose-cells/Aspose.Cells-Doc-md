---
title: الوصول إلى وتعديل قيمة Cell
type: docs
weight: 20
url: /ar/net/accessing-and-modifying-the-value-of-a-cell/
---
{{% alert color="primary" %}} 

في موضوعنا السابق ، ناقشنا حول الوصول إلى خلايا ورقة العمل. في هذا الموضوع ، سنقوم ببساطة بتوسيع هذا الموضوع لنوضح للمطورين كيف يمكنهم الوصول إلى قيم الخلايا وتعديلها باستخدام API من Aspose.Cells.GridDesktop.

{{% /alert %}} 
## **قم بالوصول وتعديل قيمة Cell باستخدام Aspose.Cells.GridDesktop**
 قبل الوصول إلى قيمة الخلية وتعديلها ، يجب أن نعرف كيفية الوصول إلى الخلايا. هناك ثلاث طرق للوصول إلى خلايا ورقة العمل. لمزيد من التفاصيل حول هذه الأساليب الثلاثة ، من فضلك[الوصول إلى Cells في ورقة عمل.](/cells/ar/net/accessing-cells-in-a-worksheet/)

كل خلية لها خاصية تسمى القيمة. لذلك ، بمجرد الوصول إلى خلية ، يمكن للمطورين الوصول إلى محتويات خاصية القيمة وتعديلها من أجل الوصول إلى قيمة الخلية وتغييرها.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingValue.cs" >}}


**الأهمية:**يعد استخدام خاصية Value لخلية لتعديل قيمتها طريقة جيدة لتعيين قيمة خلية مفردة أو خلايا قليلة. إذا كنت بحاجة إلى تعيين قيم العديد من الخلايا ، فلن يكون أداء هذا النهج جيدًا. لذلك ، لتعيين قيم العديد من الخلايا ، يجب عليك استخدام**SetCellValue** طريقة الخلية لتحسين أداء تطبيقاتك. نسخة معدلة من مقتطف الشفرة أعلاه باستخدام**SetCellValue** الطريقة الموضحة أدناه.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-AccessAndModifyCells-UsingSetCellValue.cs" >}}
