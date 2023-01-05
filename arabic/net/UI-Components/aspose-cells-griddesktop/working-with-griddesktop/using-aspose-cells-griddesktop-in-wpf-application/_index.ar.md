---
title: باستخدام Aspose.Cells.GridDesktop في تطبيق WPF
type: docs
weight: 50
url: /ar/net/using-aspose-cells-griddesktop-in-wpf-application/
---
{{% alert color="primary" %}} 

 توضح هذه المقالة كيفية استخدام مصمم Windows Presentation Foundation (WPF) لبرنامج Visual Studio لاستضافة عنصر تحكم نماذج Windows مثل Aspose.Cells.GridDesktop في تطبيق WPF.
سنستخدم Visual Studio 2015 لشرح العملية ، ومع ذلك ، يمكنك استخدام أي إصدار بما في ذلك Visual Studio 2008 أو ما بعده.

{{% /alert %}} 

سيرشدك هذا البرنامج التعليمي خلال عملية إضافة Aspose.Cells.GridDesktop control إلى تطبيق WPF. أنت بحاجة إلى أي إصدار من Visual Studio IDE يدعم تطوير WPF لتجربة ذلك من جانبك.
## **قم بإنشاء تطبيق WPF باستخدام Visual Studio**
 قم أولاً بإنشاء تطبيق WPF باستخدام Visual Studio IDE. انقر فوق**ملف** >> **جديد** >> **مشروع** القائمة وحدد**تطبيق WPF** من القوالب ، قم بتسمية المشروع وانقر**نعم**. يمكنك توجيه مشروعك إلى أي إطار .NET أعلى من 2.0 ، ومع ذلك ، لا يمكنك استخدام ملف تعريف العميل .NET Frameworks.
## **أضف مراجع إلى مساحات الأسماء المطلوبة**
أضف المراجع إلى التجميعات التالية بالنقر بزر الماوس الأيمن فوق نافذة المراجع من نافذة مستكشف الحلول وحدد إضافة قائمة مرجعية.

- تجميع WindowsFormsIntegration (WindowsFormsIntegration.dll).
- Windows تجميع النماذج (System.Windows.Forms.dll).
- Aspose.Cells.GridDesktop (Aspose.Cells.GridDesktop.dll).

يضيف هذا الإجراء التجميعات المطلوبة إلى التطبيق ، أي ؛ نسخ التجميعات إلى مجلد سلة التطبيق.
## **أضف مراجع إلى XAML**
بعد ذلك ، انتقل إلى ملف XAML وأضف مساحات الأسماء ومراجع التجميع التالية داخل علامة Windows.

{{< highlight "java" >}}

 xmlns:wf="clr-namespace:System.Windows.Forms;assembly=System.Windows.Forms"

xmlns:gridDesktop="clr-namespace:Aspose.Cells.GridDesktop;assembly=Aspose.Cells.GridDesktop">

{{< /highlight >}}

**ستبدو علامة Windows النهائية مشابهة لما هو موضح أدناه.**

![ما يجب القيام به: image_بديل_نص](using-aspose-cells-griddesktop-in-wpf-application_1.png)
## **أضف Aspose.Cells.GridDesktop control إلى XAML**
 ما عليك سوى إضافة الكود أدناه داخل علامة الشبكة في XAML. ال**WindowsFormsHost** تستخدم العلامة لاستضافة Windows نماذج التحكم و**الشبكة: GridDesktop** تمثل العلامة Aspose.Cells.GridDesktop control. يمكنك أيضًا تسمية عنصر التحكم بحيث يمكن الرجوع إليه بسهولة في التعليمات البرمجية.

{{< highlight "java" >}}

 <WindowsFormsHost Loaded="FrameworkElement_OnLoaded">

    <WindowsFormsHost.Child>

        <gridDesktop:GridDesktop x:Name="grid" />

    </WindowsFormsHost.Child>

</WindowsFormsHost>

{{< /highlight >}}

**سيبدو XAML النهائي على النحو التالي.** 

![ما يجب القيام به: image_بديل_نص](using-aspose-cells-griddesktop-in-wpf-application_2.png)
## **استخدم Aspose.Cells.GridDesktop**
يمكننا الآن الوصول إلى واستخدام Aspose.Cells.GridDesktop control في ملف .cs مثل أي تطبيقات Windows Forms أخرى. من أجل الحفاظ على العرض التوضيحي بسيطًا ، نقوم فقط بتحميل نموذج جدول بيانات في Aspose.Cells.GridDesktop control وحفظه مرة أخرى. علاوة على ذلك ، استخدمنا الحدث FrameworkElement_OnLoaded لتشغيل العبارات التالية.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-UsingGridDesktopInWpf-MainWindow.xaml-UsingGridDesktopInWpf.cs" >}}
## **بناء وتشغيل**
 الآن ، قم ببناء وتشغيل التطبيق باستخدام**F5** أو**بداية** زر في Visual Studio UI.
