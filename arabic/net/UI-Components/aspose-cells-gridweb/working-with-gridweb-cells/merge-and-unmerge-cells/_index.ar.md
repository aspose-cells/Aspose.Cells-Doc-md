---
title: دمج وفك دمج Cells
type: docs
weight: 60
url: /ar/net/merge-and-unmerge-cells/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb له ميزة مفيدة تتيح لك دمج الخلايا في خلية واحدة كبيرة. يصف هذا الموضوع كيفية دمج الخلايا برمجيًا.

{{% /alert %}} 
## **دمج Cells**
دمج خلايا متعددة في ورقة عمل في خلية واحدة عن طريق استدعاء أسلوب دمج المجموعة Cells. حدد نطاق الخلايا المراد دمجها عند استدعاء أسلوب الدمج.

{{% alert color="primary" %}} 

إذا قمت بدمج عدة خلايا وكانت كل خلية تحتوي على بيانات ، فسيتم الاحتفاظ فقط بمحتوى الخلية العلوية اليسرى في النطاق بعد الدمج. لا تضيع البيانات الموجودة في الخلايا الأخرى. إذا قمت بإلغاء دمج الخلايا ، تستعيد كل خلية بياناتها.

{{% /alert %}} 

**تم دمج أربع خلايا في واحدة** 

![ما يجب القيام به: image_بديل_نص](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **اندماج Cells**
لإلغاء دمج الخلايا ، استخدم أسلوب UnMerge الخاص بالمجموعة Cells الذي يأخذ نفس المعلمات مثل أسلوب الدمج وينفذ إلغاء دمج الخلايا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
