---
title: حدد المسار الذي يخزن فيه GridWeb الملفات المؤقتة.
type: docs
weight: 50
url: /ar/net/aspose-cells-gridweb/gridweb-cache-files/
keywords: GridWeb, الخزن المؤقت, الجلسة, التخزين.
description: يصف هذا المقال التخزين في GridWeb.
---
### حول التخزين المؤقت للملف
{{% alert color="primary" %}} 

عندما يكون وضع جلسة GridWeb هو ViewState، تقوم بتخزين ملفات الجلسة المؤقتة داخل دليل قاعدة التطبيق. في بعض الأحيان، قد لا تكون مخزن ملفات الجلسة المؤقتة هناك مقبولة لأن قاعدة التطبيق قد لا تحتوي على أذونات كتابة فيها. في مثل هذه الحالات، يتسبب GridWeb في إلقاء استثناء من هذا القبيل.

{{< highlight java >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

الحل للمشكلة أعلاه هو منح الوصول إلى كتابة دليل قاعدة التطبيق أو تغيير مسار ملفات الجلسة المؤقتة في GridWeb بحيث يكون لها وصول للكتابة باستخدام خاصية GridWeb.SessionStorePath. يجب أن يكون هذا المسار نسبيًا لدليل قاعدة التطبيق.

{{% /alert %}} 
#### **حدد المسار الذي يخزن فيه GridWeb ملفات الجلسة المؤقتة.**
يحدد الكود العينة التالي المسار الذي يخزن فيه GridWeb ملفات الجلسة المؤقتة.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

### حول التخزين المؤقت للصور

عندما تحتوي الصفحة على أشكال / صور في ورقة العمل، فإن GridWeb سيقوم بحفظ جميع الأشكال / الصور في مسار تخزين مؤقت.

المسار التخزين المؤقت الافتراضي هو ***System.Web.HttpContext.Current.Server.MapPath("/acwcache")***.

كما يمكننا استخدام ***GridWeb.PictureCachePath*** لتعيين هذا المسار إلى مسار محدد.

عند فتح صفحة، سيقوم GridWeb بحل عنوان URL الصورة المطلوبة، والحصول على تيار الصورة من التخزين المؤقت بواسطة معرف URL.

على سبيل المثال، إذا كان عنوان صفحتك هو *http://ip/mygridwebapp/test.aspx*  

سيتم إنشاء عنوان URL الصورة بواسطة GridWeb على النحو التالي *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

#### أحيانًا لا تتم تحميل الأشكال / الصور عند استخدام [Friendly Url](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

يجب عليك التحقق من عنوان URL الصورة المطلوبة.

ويجب أن يكون طلب الصورة العادية مثل: *http://ip/mygridwebapp/test.aspx/acw_image/imageid*.

ولكن يذهب طلبك بهذا الشكل: *http://ip/mygridwebapp/test/acw_image/imageid*.

في حال استخدام FriendlyUrl ، يجب عليك تصفية طلب عنوان URL للصورة لـ GridWeb.

بهذه الطريقة ، يمكن لخادم تحكم GridWeb الحصول على الطلب وحله والعثور على تدفق الصورة من مسار الذاكرة المؤقتة.

على سبيل المثال ، نفترض أن عنوان URL الخاص بصفحتك كالتالي: *http://ip/mygridwebapp/test.aspx*

ثم الكود أدناه هو حل مؤقت لإصلاح مثل هذه المشكلة.
```csharp
//write your custom url resolver:MyWebFormsFriendlyUrlResolver
public class MyWebFormsFriendlyUrlResolver : WebFormsFriendlyUrlResolver
{
public MyWebFormsFriendlyUrlResolver() { }

    public override string ConvertToFriendlyUrl(string path)
    {
        if (!string.IsNullOrEmpty(path))
        {//filter your GridWeb related page,here we use 'mygridwebapp' to identify as we assume your page is:http://ip/mygridwebapp/test.aspx
            if (path.ToLower().Contains("mygridwebapp"))
            { // Here the filter code
                return path;
            }
        }
        return base.ConvertToFriendlyUrl(path);
    }
}
//in RoutConfig.cs set the custom url resolver:MyWebFormsFriendlyUrlResolver
public static class RouteConfig
{
    public static void RegisterRoutes(RouteCollection routes)
    {
        var settings = new FriendlyUrlSettings();
        settings.AutoRedirectMode = RedirectMode.Permanent;
        routes.EnableFriendlyUrls(settings, new IFriendlyUrlResolver[] {
                             new MyWebFormsFriendlyUrlResolver() });
    }
}
```





