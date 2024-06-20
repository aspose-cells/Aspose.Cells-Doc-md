---
title: دمج وإلغاء دمج الخلايا
type: docs
weight: 60
url: /ar/net/aspose-cells-gridweb/merge-and-unmerge-cells/
keywords: GridWeb ، دمج ، إلغاء الدمج
description: يقدم هذا المقال كيفية دمج/إلغاء دمج الخلايا في GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb لديه ميزة أداة مفيدة تتيح لك دمج الخلايا في خلية كبيرة واحدة. يصف هذا الموضوع كيفية دمج الخلايا بطريقة برمجية.

{{% /alert %}} 
## **دمج الخلايا**
دمج عدة خلايا في ورقة العمل في خلية واحدة عن طريق استدعاء طريقة الدمج لمجموعة الخلايا. حدد مجموعة الخلايا التي ستدمج عند استدعاء طريقة الدمج.

{{% alert color="primary" %}} 

إذا قمت بدمج خلايا متعددة وكل خلية تحتوي على بيانات، يتم الاحتفاظ فقط بمحتوى أعلى الخلية اليسرى في المدى بعد الدمج. لا يتم فقدان البيانات في الخلايا الأخرى. إذا قمت بإلغاء دمج الخلايا، فإن كل خلية تستعيد بياناتها.

{{% /alert %}} 

**دمج أربع خلايا في واحدة** 

![todo:image_alt_text](merge-and-unmerge-cells_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-MergeCells.cs" >}}
## **إلغاء دمج الخلايا**
لإلغاء دمج الخلايا، استخدم طريقة إلغاء دمج Cells collection التي تأخذ نفس المعلمات كطريقة الدمج وتقوم بإلغاء دمج الخلايا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-MergeCells.aspx-UnmergeCells.cs" >}}
