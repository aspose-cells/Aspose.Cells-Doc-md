---
title: الوصول إلى كائن الارتباط التشعبي لـ GridWeb Cell
type: docs
weight: 60
url: /ar/java/access-hyperlink-object-of-the-gridweb-cell/
---
##  **سيناريوهات الاستخدام المحتملة**
يمكنك التحقق مما إذا كانت الخلية تحتوي على ارتباط تشعبي أم لا باستخدام الطريقتين التاليتين. ستُرجع هذه الطرق قيمة فارغة إذا كانت الخلية لا تحتوي على ارتباط تشعبي، وإذا كانت تحتوي على ارتباط تشعبي، فسوف تُرجع كائن GridHyperlink.

- GridHyperlinkCollection.getHyperlink(خلية GridCell)
- GridHyperlinkCollection.getHyperlink (صف int، عمود int)
##  **افتح الارتباط التشعبي في نافذة جديدة أو موجودة**
 إذا كان ملف Excel الخاص بك يحتوي على ارتباط تشعبي يرتبط ببعض عناوين URL مثل<http://wwww.aspose.com/> وقمت بتحميله في GridWeb، ثم سيتم عرض الارتباطات التشعبية مع تعيين السمة المستهدفة على _blank. وهذا يعني أنه عندما تقوم بالنقر فوق الارتباط التشعبي الموجود في خلية GridWeb، فسيتم فتحه في نافذة جديدة بدلاً من النافذة الحالية. علاوة على ذلك، إذا كنت تريد فتح الارتباط التشعبي في النافذة الحالية، فيرجى تعيين GridHyperlink.Target على _self.
##  **الوصول إلى كائن الارتباط التشعبي لـ GridWeb Cell**
نموذج التعليمات البرمجية التالي يصل إلى الارتباط التشعبي للخلية A1. إذا كانت الخلية A1 تحتوي على ارتباط تشعبي، فسوف تُرجع كائن GridHyperlink، وإلا فإنها ستعيد قيمة فارغة.
##  **عينة من الرموز**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
