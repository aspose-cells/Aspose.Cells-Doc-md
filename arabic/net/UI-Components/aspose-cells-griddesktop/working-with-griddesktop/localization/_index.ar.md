---
title: الترجمة المخصصة
type: docs
weight: 40
url: /ar/net/griddesktop-localization/
keywords: custom,localization,translation,globalization
---
{{% alert color="primary" %}} 

إذا كنا بحاجة إلى ترجمة جميع القوائم/نصائح الرسائل وما إلى ذلك في GridDesktop، فيمكننا تحديد ملف المورد واستخدام GridDesktop.SetCustomResourceManager لتحميل هذا المورد.

{{% /alert %}} 
##  **مثال**

قم أولاً بإضافة ملف مورد جديد: customtest.resx


![الموارد المخصصة](managing-griddesktops-custom-res.png)

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.Designer.cs" >}}

{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-customtest.resx" >}}

```csharp
//suppose your application with name space: myapp
   ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
   gridDesktop1.SetCustomResourceManager(rm);
```

بعد تنفيذ الكود أعلاه، تظهر عناصر القائمة:

![قائمة العرض](managing-griddesktops-show-custom.png)
 