---
title: قم بإزالة ورقة العمل
type: docs
weight: 30
url: /ar/net/remove-a-worksheet/
---
{{% alert color="primary" %}} 

يناقش هذا الموضوع إزالة أوراق العمل باستخدام عنصر تحكم Aspose.Cells.GridDesktop. هناك بعض الأساليب البسيطة لإنجاز هذه المهمة الأساسية.

{{% /alert %}} 
## **إزالة ورقة عمل**
لإزالة ورقة عمل باستخدام Aspose.Cells.GridDesktop control ، يرجى اتباع الخطوات التالية:

1. قم باضافة Aspose.Cells.GridDesktop control الى نموذج.
1. قم باستدعاء طريقة الإزالة الخاصة بمجموعة أوراق العمل في عنصر تحكم GridDesktop.
### **باستخدام فهرس ورقة العمل**
في هذا النهج ، ما عليك سوى تمرير فهرس ورقة العمل (في مجموعة أوراق العمل الخاصة بالشبكة) لورقة العمل المراد إزالتها.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingIndex.cs" >}}
### **استخدام اسم ورقة العمل**
إذا كان اسم ورقة العمل معروفًا ، فمن الممكن إزالة ورقة عمل معينة عن طريق تحديد اسمها.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-RemoveWorksheet-RemoveUsingName.cs" >}}

{{% alert color="primary" %}} 

الإزالة هي طريقة. استخدمها لإزالة ورقة العمل باستخدام الفهرس الخاص بها (في مجموعة أوراق العمل) أو استخدم طريقة RemoveAt لإزالة ورقة العمل باستخدام الفهرس / الاسم.

{{% /alert %}}
