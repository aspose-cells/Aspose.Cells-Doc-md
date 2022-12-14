---
title: كيفية تشغيل Aspose.Cells في Docker
type: docs
description: قم بتشغيل Aspose.Cells في حاوية Docker لنظام التشغيل Linux و Windows Server وأي نظام تشغيل.
weight: 139
url: /ar/net/how-to-run-aspose-cells-in-docker/
---
تتيح الخدمات المصغرة ، جنبًا إلى جنب مع النقل بالحاويات ، إمكانية الجمع بين التقنيات بسهولة. يتيح لك Docker دمج وظائف Aspose.Cells بسهولة في تطبيقك ، بغض النظر عن التكنولوجيا الموجودة في حزمة التطوير الخاصة بك.

في حال كنت تستهدف الخدمات المصغرة ، أو إذا كانت التقنية الرئيسية في مجموعتك ليست .NET أو C++ أو Java ، لكنك تحتاج إلى وظيفة Aspose.Cells ، أو إذا كنت تستخدم Docker بالفعل في مكدسك ، فقد تكون مهتمًا باستخدام Aspose.Cells في Docker وعاء.

## المتطلبات الأساسية

- يجب تثبيت Docker على نظامك. للحصول على معلومات حول كيفية تثبيت Docker على Windows أو Mac ، راجع الروابط الموجودة في قسم "انظر أيضًا".

- لاحظ أيضًا أنه يتم استخدام Visual Studio 2019 ، .NET Core 3.1 SDK في المثال الموضح أدناه.


## تطبيق Hello World

في هذا المثال ، تقوم بإنشاء تطبيق وحدة تحكم Hello World بسيط يقوم بإنشاء "Hello World!" المستند ويحفظه بجميع تنسيقات الحفظ المدعومة. يمكن بعد ذلك بناء التطبيق وتشغيله في Docker.

### إنشاء تطبيق وحدة التحكم

لإنشاء برنامج Hello World ، اتبع الخطوات التالية:
1. بمجرد تثبيت Docker ، تأكد من أنه يستخدم حاويات Linux (افتراضي). إذا لزم الأمر ، حدد خيار التبديل إلى حاويات Linux من قائمة Docker Desktops.
1. في Visual Studio ، قم بإنشاء تطبيق وحدة تحكم .NET Core.<br>
![ما يجب القيام به: image_بديل_نص](create-a-new-project.png)<br>
1. قم بتثبيت أحدث إصدار Aspose.Cells من NuGet. سيتم تثبيت System.Drawing.Common و System.Text.Encoding.CodePages كعنصر تابع Aspose.Cells.<br>
![ما يجب القيام به: image_بديل_نص](nuget-aspose-cells.png)<br>
1. نظرًا لأنه سيتم تشغيل التطبيق على Linux ، يجب تثبيت أصول Linux الأصلية المناسبة. ابدأ بالصورة الأساسية dotnet core sdk 3.1 وقم بتثبيت libgdiplus libc6-dev.
1. عند إضافة جميع التبعيات المطلوبة ، اكتب برنامجًا بسيطًا يقوم بإنشاء "Hello World!" المصنف ويحفظه بجميع تنسيقات الحفظ المدعومة:<br>
**.NET**<br>
{{< highlight "csharp" >}}
using System;
namespace Aspose.Cells.Docker
{
    class Program
    {
        static void Main(string[] args)
        {
            Workbook workbook = new Workbook();
            workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
            foreach (SaveFormat sf in Enum.GetValues(typeof(SaveFormat)))
            {
                if (sf != SaveFormat.Unknown)
                {
                    try
                    {
                        // The folder specified will be mounted as a volume when run the application in Docker image.
                        var fileName = string.Format("out{0}", FileFormatUtil.SaveFormatToExtension(sf));
                        workbook.Save(fileName, sf);
                        Console.WriteLine("Saving {0}\t\t[OK]", sf);
                    }
                    catch
                    {
                        Console.WriteLine("Saving {0}\t\t[FAILED]", sf);
                    }
                }
            }
        }
    }
}

{{< /highlight >}}

لاحظ أنه تم تحديد مجلد "TestOut" كمجلد إخراج لحفظ مستندات الإخراج. عند تشغيل التطبيق في Docker ، سيتم تثبيت مجلد على الجهاز المضيف في هذا المجلد في الحاوية. سيمكنك هذا من عرض المخرجات التي تم إنشاؤها بواسطة Aspose.Cells في حاوية Docker بسهولة.

### تكوين Dockerfile

الخطوة التالية هي إنشاء ملف Docker وتكوينه.

1. قم بإنشاء Dockerfile ووضعه بجوار ملف الحل للتطبيق الخاص بك. احتفظ باسم الملف هذا بدون امتداد (الافتراضي).
1. في Dockerfile ، حدد:

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
COPY fonts/* /usr/share/fonts/
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

ما سبق هو ملف Dockerfile بسيط يحتوي على التعليمات التالية:

- صورة SDK المراد استخدامها. ها هي صورة .Net Core SDK 3.1. سيقوم Docker بتنزيله عند تشغيل الإصدار. تم تحديد إصدار SDK كعلامة.
- تثبيت الخطوط لأن صورة SDK تحتوي على عدد قليل جدًا من الخطوط. يقوم الأمر بنسخ ملفات الخط من صورة محلية إلى صورة عامل إرساء. تأكد من أن لديك دليل "خطوط" محلي يحتوي على جميع الخطوط التي تحتاج إلى تثبيتها. في هذا المثال ، يتم وضع دليل "الخطوط" المحلي في نفس الدليل مثل Dockerfile.
- دليل العمل المحدد في السطر التالي.
- الأمر لنسخ كل شيء إلى الحاوية ونشر التطبيق وتحديد نقطة الدخول.
- يتم تشغيل أمر تثبيت libgdiplus في الحاوية. هذا مطلوب من قبل System.Drawing.Common.

### إنشاء التطبيق وتشغيله في Docker

الآن يمكن بناء التطبيق وتشغيله في Docker. افتح موجه الأوامر المفضل لديك ، وقم بتغيير الدليل إلى المجلد الذي يحتوي على التطبيق (المجلد حيث يتم وضع ملف الحل وملف Dockerfile) وقم بتشغيل الأمر التالي:

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

قد يستغرق الأمر وقتًا أطول في المرة الأولى التي يتم فيها تنفيذ هذا الأمر ، نظرًا لأن Docker يحتاج إلى تنزيل الصور المطلوبة. بمجرد اكتمال الأمر السابق ، قم بتشغيل الأمر التالي:

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}

{{% alert color="primary" %}} 

انتبه إلى وسيطة التحميل ، لأنه ، كما ذكرنا سابقًا ، يتم تثبيت مجلد على الجهاز المضيف في مجلد الحاوية ، لرؤية نتائج تنفيذ التطبيق بسهولة. المسارات في Linux حساسة لحالة الأحرف.

{{% /alert %}}

## دعم الصور Aspose.Cells

- Aspose.Cells for .NET القياسي لا يدعم EMF و TIFF على Linux.


## مزيد من الأمثلة

***1. لتشغيل التطبيق في Windows Server 2019***

- ملف Dockerfile

{{< highlight "plain" >}}
FROM microsoft/dotnet-framework:4.7.2-sdk-windowsservercore-ltsc2019
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.dll"]{{< /highlight >}}

- بناء صورة عامل ميناء

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- تشغيل صورة Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Temp,target=c:\TestOut --rm actest from Docker
{{< /highlight >}}


***2. لتشغيل التطبيق في لينكس***

- اكتب برنامجًا بسيطًا يضبط مجلد الخطوط ، ينشئ "Hello World!" المصنف ويحفظه.

{{< highlight "csharp" >}}
namespace Aspose.Cells.Docker.Fonts
{
    using System;
    using System.IO;

    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                // Set font folders on linux.
                string[] fonts = { "/Fonts" };
                FontConfigs.SetFontFolders(fonts, true);
                // build workbook
                Workbook workbook = new Workbook();
                MemoryStream memoryStream = new MemoryStream();
                workbook.Worksheets[0].Cells[0, 0].PutValue("Hello from Aspose.Cells!!!");
                Style style = workbook.CreateStyle();
                style.Font.Name = "Arial";
                style.Font.Size = 16;
                workbook.Worksheets[0].Cells[0, 0].SetStyle(style);
                workbook.Save("/TestOut/TestFontsOut.xlsx");
            }
            catch (Exception e)
            {
                Console.WriteLine("Saving outfonts.xlsx\t\t[FAILED],{0}", e.Message);
            }
           
        }
    }
}

{{< /highlight >}}
- ملف Dockerfile

{{< highlight "plain" >}}
FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster 
WORKDIR /app
COPY . ./
RUN apt-get update && \
    apt-get install -y --allow-unauthenticated libgdiplus libc6-dev
WORKDIR /app
COPY . ./
RUN dotnet publish "Aspose.Cells.Docker.Fonts.csproj" -c Release -o /app/publish
ENTRYPOINT ["dotnet", "publish/Aspose.Cells.Docker.Fonts.dll"]{{< /highlight >}}

- بناء صورة عامل ميناء

{{< highlight "plain" >}}
docker build -t actest .
{{< /highlight >}}

- تشغيل صورة Docker

{{< highlight "plain" >}}
docker run --mount type=bind,source=C:\Windows\Fonts,target=/Fonts  --mount type=bind,source=C:\Temp,target=/TestOut --rm actest from Docker
{{< /highlight >}}


## أنظر أيضا

- [قم بتثبيت Docker Desktop على Windows](https://docs.docker.com/docker-for-windows/install/)
- [قم بتثبيت Docker Desktop على نظام Mac](https://docs.docker.com/docker-for-mac/install/)
- [Visual Studio 2019 ، .NET Core 3.1 SDK](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=netcore31#dependencies)
- [قم بالتبديل إلى حاويات Linux](https://docs.docker.com/docker-for-windows/#switch-between-windows-and-linux-containers) اختيار
-  معلومات إضافية عن[.NET كور SDK](https://hub.docker.com/_/microsoft-dotnet-sdk)
