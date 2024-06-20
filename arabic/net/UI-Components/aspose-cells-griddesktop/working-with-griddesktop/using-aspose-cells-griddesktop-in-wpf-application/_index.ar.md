---
title: استخدام تحكم Aspose.Cells.GridDesktop في تطبيق WPF
type: docs
weight: 50
url: /ar/net/aspose-cells-griddesktop/use-aspose-cells-griddesktop-in-wpf-application/
keywords: GridDesktop,wpf
description: يقدم هذا المقال كيفية استخدام تحكم GridDesktop في تطبيق WPF.
---

{{% alert color="primary" %}} 

يوضح هذا المقال كيفية استخدام مصمم واجهة المستخدم لنظام التشغيل Windows (WPF) في برنامج Visual Studio لاستضافة تحكم Windows Forms مثل Aspose.Cells.GridDesktop في تطبيق WPF. 
سنستخدم Visual Studio 2015 لتوضيح العملية، ومع ذلك، يمكنك استخدام أي إصدار بما في ذلك Visual Studio 2008 أو الأحدث.

{{% /alert %}} 

سيرشدك هذا البرنامج التعليمي خلال عملية إضافة تحكم Aspose.Cells.GridDesktop إلى تطبيق WPF. تحتاج إلى أي إصدار من بيئة تطوير Visual Studio يدعم تطوير WPF من أجل تجربتها من جهتك.
## **إنشاء تطبيق WPF باستخدام Visual Studio**
أنشئ أولاً تطبيق WPF باستخدام بيئة تطوير Visual Studio. انقر على **فايل** >> **جديد** >> **مشروع** ثم حدد **تطبيق WPF** من القوالب، قم بتسمية المشروع وانقر على **موافق**. يمكنك توجيه مشروعك إلى أي إصدار من .NET Framework أعلى من 2.0، ولكن لا يمكن استخدام ملف تعريف العميل .NET Frameworks.
## **إضافة مراجع إلى مساحات الاسم المطلوبة**
أضف المراجع لتجميعات البرمجيات النهائية التالية بالنقر بزر الماوس الأيمن على المراجع من نافذة مستكشف الحلول وحدد القائمة إضافة مرجع.

- تجميع الدمج بين Windows (WindowsFormsIntegration.dll).
- تجميع النماذج Windows (System.Windows.Forms.dll).
- تجميع Aspose.Cells.GridDesktop (Aspose.Cells.GridDesktop.dll).

تضيف هذه الإجراءات التجميعات المطلوبة إلى التطبيق، أي تنسخ التجميعات إلى مجلد Bin للتطبيق.
## **إضافة مراجع إلى XAML**
بعد ذلك، انتقل إلى ملف XAML وأضف مساحات الاسم ومراجع التجميع التالية داخل الوسم الخاص بنوافذ.

{{< highlight java >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**سيكون العلامة النهائية لنظام التشغيل Windows مشابهة لما هو موضح أدناه.**

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **أضف تحكم Aspose.Cells.GridDesktop إلى XAML**
قم ببساطة بإضافة الكود أدناه داخل علامة Grid في XAML. تُستخدم علامة **WindowsFormsHost** لاستضافة تحكمات Windows Forms وتُمثل علامة **gridDesktop:GridDesktop** تحكم Aspose.Cells.GridDesktop. يمكنك أيضًا تسمية التحكم حتى يمكن الإشارة إليه بسهولة في الكود.

{{< highlight java >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**سيبدو الـ XAML النهائي كما يلي.** 

![todo:image_alt_text](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **استخدام Aspose.Cells.GridDesktop**
يمكننا الآن الوصول إلى Aspose.Cells.GridDesktop واستخدامه في ملف .cs كأي تطبيقات Windows Forms أخرى. من أجل إبقاء العرض بسيطًا، نقوم فقط بتحميل جدول بيانات عيني في تحكم Aspose.Cells.GridDesktop وحفظه. علاوة على ذلك، قمنا باستخدام حدث FrameworkElement_OnLoaded لتشغيل البيانات التالية.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **بناء وتشغيل**
الآن، يمكنك بناء وتشغيل التطبيق باستخدام زر **F5** أو زر **Start** في واجهة مستخدم Visual Studio.
