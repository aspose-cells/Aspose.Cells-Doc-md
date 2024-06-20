---
title: الدخول إلى كائن الارتباط التشعبي في خلية GridWeb
type: docs
weight: 60
url: /ar/java/access-hyperlink-object-of-the-gridweb-cell/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك التحقق مما إذا كانت الخلية تحتوي على ارتباط تشعبي أم لا باستخدام الطريقتين التاليتين. ستعيد هذه الطرق قيمة فارغة إذا لم تحتوي الخلية على ارتباط تشعبي، وإذا حتوت على ارتباط تشعبي، ستعيد كائن GridHyperlink.

- GridHyperlinkCollection.getHyperlink(GridCell cell)
- GridHyperlinkCollection.getHyperlink(int row,int column)
## **فتح الرابط الفائق في نافذة جديدة أو موجودة**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of the existing window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.
## **الوصول إلى كائن الرابط الفائق لخلية GridWeb**
يقوم الكود النموذجي التالي بالوصول إلى الرابط الفائق للخلية A1. إذا كانت الخلية A1 تحتوي على رابط فائق ، فسيُرجع كائن GridHyperlink ، وإلا ، سيُرجع قيمة فارغة.
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
