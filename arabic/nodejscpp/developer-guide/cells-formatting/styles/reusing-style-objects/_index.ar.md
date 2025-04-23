---  
title: إعادة استخدام كائنات النمط
linktitle: إعادة استخدام كائنات النمط  
description: في Aspose.Cells for Node.js via C++، من خلال إنشاء واستخدام كائنات أنماط قابلة لإعادة الاستخدام، يمكنك تبسيط إدارة الأنماط وتحسين كفاءة الكود. ستساعدك أدلتنا على الاستفادة من مزايا الكائنات القابلة لإعادة الاستخدام وتنفيذها في تطبيقك.  
keywords: Aspose.Cells for Node.js via C++، إعادة استخدام كائنات النمط، إدارة النمط، كفاءة الكود، أنماط قابلة لإعادة الاستخدام، تطوير التطبيق، مرجع API، مثال على الكود، التحميل، الدعم.  
type: docs  
weight: 3000  
url: /ar/nodejs-cpp/reusing-style-objects/  
---  

{{% alert color="primary" %}}  
يمكن لإعادة استخدام كائنات النمط توفير الذاكرة وجعل البرنامج أسرع.  
{{% /alert %}}  

لتطبيق بعض التنسيق على مجموعة كبيرة من الخلايا في ورقة العمل:

1. إنشاء كائن النمط.
1. تحديد السمات.
1. تطبيق النمط على الخلايا في النطاق.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-Styles-ReusingStyleObjects.js" >}}


{{% alert color="primary" %}}  
نظرًا لأن نهج [**Cell.getStyle()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) / [**Cell.setStyle(Style)**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) يستخدم ذاكرة أقل بكثير، وهو أكثر كفاءة، تم إزالة خاصية Cell.style القديمة التي كانت تستهلك الكثير من الذاكرة غير الضرورية مع إصدار Aspose.Cells 7.1.0.  
{{% /alert %}}  

