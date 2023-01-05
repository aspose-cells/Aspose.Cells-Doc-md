---
title: ورقة عمل الوصول Cells
type: docs
weight: 10
url: /ar/net/access-worksheet-cells/
---
{{% alert color="primary" %}} 

يناقش هذا الموضوع الخلايا ، بالنظر إلى Aspose.Cells. الميزة الأساسية لـGridWeb: الوصول إلى الخلايا.

{{% /alert %}} 
## **الوصول إلى Cells في ورقة عمل**
تحتوي كل ورقة عمل على خاصية باسم Cells وهي في الواقع مجموعة من كائنات GridCell حيث يمثل كائن GridCell خلية في Aspose.Cells.GridWeb. من الممكن الوصول إلى أي خلية باستخدام Aspose.Cells.GridWeb. هناك طريقتان مفضلتان ، تتم مناقشة كل منهما أدناه.


### **باستخدام Cell الاسم**
جميع الخلايا لها اسم فريد. على سبيل المثال ، A1 ، A2 ، B1 ، B2 إلخ. Aspose.Cells.GridWeb يسمح للمطورين بالوصول إلى أي خلية مرغوبة باستخدام اسم الخلية. ما عليك سوى تمرير اسم الخلية (كمؤشر) إلى المجموعة Cells من GridWorksheet.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByName.cs" >}}


### **استخدام فهارس الصفوف والعمود**
يمكن أيضًا التعرف على الخلية من خلال موقعها من حيث فهارس الصفوف والأعمدة. فقط قم بتمرير فهارس الصفوف والعمود الخاصة بالخلية إلى مجموعة Cells من GridWorksheet. هذا النهج أسرع من الأسلوب أعلاه.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCells.aspx-AccessCellByRowColumnIndex.cs" >}}
