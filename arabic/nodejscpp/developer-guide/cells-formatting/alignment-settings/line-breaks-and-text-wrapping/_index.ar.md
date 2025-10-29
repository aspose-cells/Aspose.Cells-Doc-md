---  
title: كسر الأسطر وتضمين النص
linktitle: كسر الأسطر وتضمين النص  
description: كيفية تنفيذ التفاف النص والتفاف الكلمة باستخدام مكتبة Aspose.Cells في Node.js عبر C++. باستخدام مكتبة Aspose.Cells، يمكنك بسهولة إدراج النص في الخلايا وتعيين طريقة التفاف النص، مثل التفاف كلمة يدوي، التفاف كلمة، إلخ. يوضح هذا المستند كيفية تنفيذ هذه الميزات ويوفر رمزًا نمطيًا للرجوع إليه.  
keywords: Aspose.Cells، فواصل الأسطر، التفاف النص، تخطيط النص Node.js عبر C++  
type: docs  
weight: 60  
url: /ar/nodejs-cpp/line-breaks-and-text-wrapping/  
---  

{{% alert color="primary" %}}  
لضمان قراءة النص في خلية معينة يمكن تطبيق كسرات الأسطر الصريحة وتضمين النص. يحول تضمين النص سطرًا واحدًا إلى عدة أسطر داخل خلية، بينما تضع كسرات الأسطر الصريحة فواصل تمامًا حيث تريدها.  
{{% /alert %}}  

## **لتضمين النص في خلية**  
لف التفاف النص في خلية، استخدم الطريقة [**Aspose.Cells.Style.setIsTextWrapped(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/style/#setIsTextWrapped-boolean-).  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-WrapTextInCell.js" >}}


## **للاستخدام كسرات الأسطر الصريحة**  
يمكنك استخدام '\n' في JavaScript لإدخال فواصل سطر واضحة في الخلية.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AlignSettings-UseExplicitLineBreaks.js" >}}



{{< app/cells/assistant language="nodejs-cpp" >}}
