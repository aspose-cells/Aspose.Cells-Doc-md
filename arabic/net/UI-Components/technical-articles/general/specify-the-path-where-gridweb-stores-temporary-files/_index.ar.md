---
title: حدد المسار حيث يقوم GridWeb بتخزين الملفات المؤقتة
type: docs
weight: 50
url: /ar/net/gridweb-cache-files/
keywords: cache,session,storage
---
###  حول ذاكرة التخزين المؤقت للملف
{{% alert color="primary" %}} 

عندما يكون وضع جلسة GridWeb هو ViewState ، فإنه يخزن ملفات الجلسة المؤقتة داخل دليل قاعدة التطبيق. في بعض الأحيان ، لا بأس من تخزين ملفات الجلسات المؤقتة هناك لأن Application Base Directory قد لا يكون لديه أذونات الكتابة عليه. في مثل هذه الحالات ، يطرح GridWeb مثل هذا الاستثناء

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]

{{< /highlight >}}

الحل للمشكلة أعلاه هو منح حق الوصول للكتابة إلى Application Base Directory أو تغيير مسار ملفات جلسة GridWeb المؤقتة التي لها حق الوصول للكتابة باستخدام خاصية GridWeb.SessionStorePath. يجب أن يكون هذا المسار متعلقًا بـ Application Base Directory.

{{% /alert %}} 
####  **حدد المسار حيث يقوم GridWeb بتخزين ملفات الجلسة المؤقتة**
يحدد نموذج التعليمات البرمجية التالي المسار حيث يخزن GridWeb ملفات جلسة العمل المؤقتة.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}

###  حول ذاكرة التخزين المؤقت للصور

عند وجود أشكال / صور في ورقة العمل ، سيحفظ GridWeb كل الأشكال / الصور في مسار ذاكرة التخزين المؤقت

 المسار الافتراضي لذاكرة التخزين المؤقت هو***System.Web.HttpContext.Current.Server.MapPath ("/ acwcache")***

 كما يمكننا استخدامها***GridWeb.PictureCachePath*** لتعيين هذا المسار إلى مسار محدد.

عندما نفتح صفحة ، فإن GridWeb سيحل عنوان url الخاص بالصورة للطلب ، ويحصل على دفق الصورة من ذاكرة التخزين المؤقت بواسطة معرف عنوان url.

 على سبيل المثال ، إذا كان عنوان صفحتك هو*http: //ip/mygridwebapp/test.aspx*  

عنوان url الخاص بطلب الصورة الذي تم إنشاؤه بواسطة GridWeb سيكون * http: //ip/mygridwebapp/test.aspx/acw_image/imageid*.

####  في بعض الأحيان لا يتم تحميل الأشكال / الصور عند الاستخدام[عنوان Url الودية](https://weblogs.asp.net/psheriff/using-friendly-urls-in-web-forms).

تحتاج إلى التحقق من طلب عنوان url للصورة.

 يجب أن يكون طلب الصورة العادي مثل:*http: //ip/mygridwebapp/test.aspx/acw_image/imageid*

لكن طلبك يذهب على النحو التالي: * http: // ip / mygridwebapp / test / acw_image / imageid *

إذا كنت تستخدم FriendlyUrl ، فأنت بحاجة إلى تصفية طلب عنوان url الخاص بالصورة لـ GridWeb.

وبالتالي يمكن لخادم التحكم في GridWeb الحصول على الطلب وحله والعثور على دفق الصورة من مسار ذاكرة التخزين المؤقت.

على سبيل المثال ، نفترض عنوان url لصفحتك مثل هذا: * http: //ip/mygridwebapp/test.aspx*

ثم الكود أدناه هو حل بديل لإصلاح هذه المشكلة.
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





