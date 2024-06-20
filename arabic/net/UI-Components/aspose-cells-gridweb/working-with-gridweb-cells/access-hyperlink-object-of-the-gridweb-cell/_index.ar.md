---
title: الدخول إلى كائن الارتباط التشعبي في خلية GridWeb
type: docs
weight: 100
url: /ar/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb، ارتباط تشعب
description: يقدم هذا المقال كيفية العمل مع ارتباط التشعب في GridWeb.
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك التحقق مما إذا كانت الخلية تحتوي على ارتباط تشعبي أم لا باستخدام الطريقتين التاليتين. ستعيد هذه الطرق قيمة فارغة إذا لم تحتوي الخلية على ارتباط تشعبي، وإذا حتوت على ارتباط تشعبي، ستعيد كائن GridHyperlink.

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **فتح الرابط الفائق في نافذة جديدة أو موجودة**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **الوصول إلى كائن الرابط الفائق لخلية GridWeb**
يقوم الكود النموذجي التالي بالوصول إلى الرابط الفائق للخلية A1. إذا كانت الخلية A1 تحتوي على رابط فائق ، فسيُرجع كائن GridHyperlink ، وإلا ، سيُرجع قيمة فارغة.
### **الكود المثالي**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}
