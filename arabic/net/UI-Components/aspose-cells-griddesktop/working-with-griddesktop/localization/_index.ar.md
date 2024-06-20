---
title: التعريب المخصص
type: docs
weight: 40
url: /ar/net/aspose-cells-griddesktop/griddesktop-localization/
keywords: GridDesktop ، مخصصة ، تعريب ، ترجمة ، عولمة
description: يقدم هذا المقال كيفية تخصيص التعريب في GridDesktop.
---

{{% alert color="primary" %}} 

إذا كنا بحاجة إلى عمل تعريب لجميع القوائم / نصائح الرسائل إلخ في GridDesktop ، يمكننا تحديد ملف الموارد ، واستخدام GridDesktop.SetCustomResourceManager لتحميل هذا المورد.

{{% /alert %}} 
## **مثال**

أولاً قم بإضافة ملف مورد جديد: customtest.resx


![custom-resource](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

بعد تنفيذ الكود أعلاه، يتم عرض عناصر القائمة:

![show menu](managing-griddesktops-show-custom.png)

